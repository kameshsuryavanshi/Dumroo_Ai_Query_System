import streamlit as st
import os
import base64
from rbac.rbac import apply_role_filter
from agents.langchain_agent import create_query_chain, process_query
from utils.data_loader import load_data
from config import GOOGLE_API_KEY

# Set up Google API key
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "AIzaSyCktS9cpbZW1CcTNMj_bBf8xBl4dL5p2F0")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "AIzaSyA3yK4xhtGyDvQ33qhh06b-8QZ7B8qQv1I")

@st.cache_data
def cached_load_data():
    return load_data()

# Function to encode logo as base64
@st.cache_resource
def get_base64_of_bin_file(png_file):
    try:
        with open(png_file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.error(f"Logo file not found at: {png_file}")
        return ""

# Function to add logo to sidebar and header
def add_logo(png_file):
    binary_string = get_base64_of_bin_file(png_file)
    if binary_string:
        logo_markup = f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{binary_string}");
                background-repeat: no-repeat;
                background-position: 20px 20px;
                background-size: 60% auto;
                padding-top: 100px;
            }}
            .header-logo {{
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }}
            .header-logo img {{
                width: 150px;
                height: auto;
            }}
        </style>
        <div class="header-logo">
            <img src="data:image/png;base64,{binary_string}">
        </div>
        """
        st.markdown(logo_markup, unsafe_allow_html=True)

def main():
    # Set page config for title and favicon
    st.set_page_config(page_title="Dumroo AI Admin Panel", page_icon=":books:", layout="wide")

    # Add logo to sidebar and header
    logo_path = os.path.join(os.path.dirname(__file__), 'data/dumroo_ai_logo.png')
    add_logo(logo_path)

    # Custom CSS for styling
    st.markdown("""
        <style>
            .stApp {{
                background-color: #F8FAFC;
            }}
            h1 {{
                color: #1E3A8A;
                text-align: center;
                font-family: 'Helvetica Neue', sans-serif;
            }}
            .stTextInput > div > div > input {{
                border: 2px solid #3B82F6;
                border-radius: 5px;
                padding: 10px;
            }}
            .stSelectbox > div > div > div {{
                border: 2px solid #3B82F6;
                border-radius: 5px;
                padding: 5px;
            }}
            .stSpinner > div {{
                color: #3B82F6;
            }}
            .sidebar .sidebar-content {{
                background-color: #E2E8F0;
            }}
            .stMarkdown table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }}
            .stMarkdown th, .stMarkdown td {{
                border: 1px solid #CBD5E1;
                padding: 8px;
                text-align: left;
            }}
            .stMarkdown th {{
                background-color: #3B82F6;
                color: white;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Main content in a container
    with st.container():
        st.title("Dumroo AI Admin Panel")
        
        # Admin role selection in sidebar
        st.sidebar.header("Admin Login")
        valid_grades = [7, 8, 9, 10]
        valid_regions = ["North", "South", "East", "West"]
        grade = st.sidebar.selectbox("Assigned Grade", ["Select Grade"] + valid_grades)
        region = st.sidebar.selectbox("Assigned Region", ["Select Region"] + valid_regions)

        # Validate role inputs
        admin_role = None
        if grade != "Select Grade" and region != "Select Region":
            admin_role = {"grade": int(grade), "region": region}

        # Load data and apply role filter
        df = cached_load_data()
        filtered_df = apply_role_filter(df, admin_role) if admin_role else None

        # Initialize LangChain
        chain = create_query_chain()

        # Query input
        st.markdown("### Ask a Question")
        query = st.text_input("Enter your query (e.g., 'Which students haven’t submitted their homework yet?')", 
                             placeholder="Type your query here...")

        if query:
            with st.spinner("Processing query..."):
                result = process_query(query, filtered_df, admin_role, chain)
                st.markdown("**Result:**")
                st.markdown(result)

        # Example queries in sidebar
        st.sidebar.header("Example Queries")
        st.sidebar.markdown("""
            - Which students have submitted their homework yet?
           
        """)

if __name__ == "__main__":
    main()

