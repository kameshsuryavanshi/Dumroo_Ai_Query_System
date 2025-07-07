from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from datetime import datetime, timedelta
import pandas as pd
import re

def create_query_chain():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    prompt_template = PromptTemplate(
        input_variables=["query", "context", "today", "next_week_start", "next_week_end"],
        template="""
        You are an AI assistant for an admin panel. Based on the user query and dataset context, generate a **single-line** Pandas query string for use with DataFrame.query(). The dataset has columns: student_id, student_name, grade, class, homework_status, quiz_score, quiz_date, region. The homework_status column has values: 'Completed', 'Incomplete', or 'Missing'. For queries about unsubmitted homework, use `homework_status.isin(['Incomplete', 'Missing'])`. For submitted homework, use `homework_status == 'Completed'`. For date-based queries, use 'quiz_date' (format DD-MM-YYYY, e.g., `quiz_date >= 'DD-MM-YYYY' and quiz_date <= 'DD-MM-YYYY'`). Return **only** a single-line query string with no 'df' prefix, no indexing (e.g., df['column']), no newlines, no comments, and no extra text. If the query is unclear or requires grade/region, return 'PROMPT_GRADE_REGION'. Do not include grade/region in the query unless specified in the context.

        Examples:
        - Query: "Which students have submitted their homework?" -> `homework_status == 'Completed'`
        - Query: "Which students haven’t submitted their homework?" -> `homework_status.isin(['Incomplete', 'Missing'])`
        - Query: "Show quizzes from 01-07-2025 to 07-07-2025" -> `quiz_date >= '01-07-2025' and quiz_date <= '07-07-2025'`

        Query: {query}
        Context: {context}

        Pandas Query:
        """
    )
    return prompt_template | llm

def process_query(query, df, admin_role, chain):

    # Debug inputs
    print(f"Process Query: admin_role={admin_role}, df is None={df is None}")
    
    if df is None or admin_role is None or not all(k in admin_role for k in ['grade', 'region']):
        print("Process Query: Prompting for grade/region due to invalid inputs")
        return "Please provide specific details of assigned grade and region."

    # Prepare context and date variables for LangChain
    today = datetime.now().strftime('%d-%m-%Y')
    next_week_start = (datetime.now() + timedelta(days=7 - datetime.now().weekday())).strftime('%d-%m-%Y')
    next_week_end = (datetime.now() + timedelta(days=13 - datetime.now().weekday())).strftime('%d-%m-%Y')
    context = f"Dataset columns: {', '.join(df.columns)}. Admin role: grade={admin_role.get('grade', 'unspecified')}, region={admin_role.get('region', 'unspecified')}. Today's date: {today}."

    # Generate Pandas query using invoke
    try:
        response = chain.invoke({
            "query": query,
            "context": context,
            "today": today,
            "next_week_start": next_week_start,
            "next_week_end": next_week_end
        })
        pandas_query = response.content.strip() if hasattr(response, 'content') else response.strip()
        # Sanitize query: remove newlines, comments, and 'df' references
        pandas_query = re.sub(r'\n.*$', '', pandas_query)  # Remove newlines and subsequent text
        pandas_query = re.sub(r'#.*$', '', pandas_query)   # Remove comments
        pandas_query = re.sub(r'df\[(.*?)\]', r'\1', pandas_query)  # Remove df[...] references
        pandas_query = re.sub(r'df\.', '', pandas_query)  # Remove df. references
        pandas_query = pandas_query.strip()
        # Log queries for debugging
        print(f"Raw response: {response.content if hasattr(response, 'content') else response}")
        print(f"Sanitized Pandas query: {pandas_query}")
    except Exception as e:
        print(f"Process Query: Error generating query: {str(e)}")
        return f"Error generating query: {str(e)}"

    if pandas_query == 'PROMPT_GRADE_REGION':
        print("Process Query: Received PROMPT_GRADE_REGION from chain")
        return "Please provide specific details of assigned grade and region."

    if not pandas_query:
        print("Process Query: Empty query generated")
        return "Sorry, I couldn't understand the query. Please try rephrasing."

    try:
        result = df.query(pandas_query)
        if result.empty:
            print("Process Query: No data found for query")
            return "No data found for the query."
        print(f"Process Query: Query successful, {len(result)} rows returned")
        return result.to_markdown(index=False)
    except Exception as e:
        print(f"Process Query: Error processing query: {str(e)}")
        return f"Error processing query: {str(e)}"