Here’s your cleaned README with all emojis removed and formatting kept intact:

---

# Dumroo AI Query System

## Overview

The **Dumroo AI Query System** is an intelligent admin panel built with **Streamlit**, **LangChain**, and **Google's Gemini (gemini-1.5-flash)**. It enables school administrators to query student performance data using simple natural language commands, with **role-based access control (RBAC)** that ensures users only see data relevant to their assigned **grade** and **region**.

Clean UI •
Gemini-powered NLP •
Fine-grained RBAC •
Modular, extendable design

---

## Purpose

This tool is designed for school administrators to:

* Ask questions like “Which students haven’t submitted their homework yet?” in plain English.
* Filter student data by **grade (7–10)** and **region (North, South, East, West)**.
* Automatically prompt for missing grade/region filters to ensure access restrictions.
* Visualize responses in an intuitive, styled table format.

---

## Target Audience

* School administrators with limited data access scope
* Developers extending or maintaining the system
* Education stakeholders seeking insights from student data

---

## Project Structure

```
dumroo-ai-query-system/
├── .streamlit/
│   └── config.toml
├── agents/
│   └── langchain_agent.py
├── data/
│   ├── students.csv
│   └── dumroo_ai_logo.png
├── rbac/
│   └── rbac.py
├── utils/
│   └── data_loader.py
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Features

* **Natural Language Querying**
  Process queries like *"Which students haven’t submitted their homework yet?"* via LangChain + Gemini.

* **Role-Based Access Control (RBAC)**
  Filter data based on the admin’s selected **grade** and **region**.

* **Dynamic Prompting**
  Prompts user to specify grade/region if not selected.

* **Modern UI Design**
  Custom blue-gray theme, responsive layout, and Dumroo branding.

* **Styled Data Tables**
  Results are displayed using markdown-style tables with enhanced styling.

* **Robust Error Handling**
  Invalid queries, file issues, and parsing problems are gracefully managed.

---

## Prerequisites

* **Python**: Version 3.9 or higher
* **Virtual Environment**: Recommended
* **Google API Key**: Required to access Gemini (from Google AI Studio)
* **Logo File**: Place `dumroo_ai_logo.png` in `data/` directory

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd dumroo-ai-query-system
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Google API Key

**Option A: Environment Variable**

```bash
# Windows
set GOOGLE_API_KEY=your-google-api-key

# Linux/Mac
export GOOGLE_API_KEY=your-google-api-key
```

**Option B: Update config.py**

```python
GOOGLE_API_KEY = "your-google-api-key"
```

---

## Dataset

* **File**: `data/students.csv`
* **Fields**:

  * `student_id`: Unique ID (e.g., S001)
  * `student_name`: Indian-origin names (e.g., Ayesha Fernandes)
  * `grade`: Integer (7–10)
  * `class`: A, B, or C
  * `homework_status`: "Completed", "Incomplete", "Missing"
  * `quiz_score`: Integer (0–100)
  * `quiz_date`: `DD-MM-YYYY` format
  * `region`: North, South, East, West

220 student entries across 4 grades and 4 regions

---

## Running the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Usage Guide

### 1. Select Role Scope

Choose a **grade** and **region** from the sidebar.
If missing, the system will prompt for it before processing queries.

### 2. Type a Natural Query

Examples:

* *“Which students haven’t submitted their homework yet?”*
* *“Show me performance data for Grade 8 from last week”*
* *“List all upcoming quizzes scheduled for next week”*

### 3. View the Results

Styled tables will show only the relevant, scoped data.

---

## Example Queries

* *"Which students have submitted their homework?"*
* *"List Grade 9 students who missed the last quiz"*
* *"Show quiz scores of South region for this month"*

---

## Architecture

| Layer           | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| **Frontend**    | Streamlit (`app.py`) + custom theme (`.streamlit/config.toml`) |
| **Query Agent** | LangChain + Gemini in `agents/langchain_agent.py`              |
| **RBAC Logic**  | Grade + Region filter in `rbac/rbac.py`                        |
| **Data Loader** | Reads and parses CSV in `utils/data_loader.py`                 |
| **Config**      | API keys and settings in `config.py`                           |

---

## UI Design

* **Primary Color**: Blue `#3B82F6`
* **Background**: Light Gray `#F8FAFC`
* **Sidebar**: `#E2E8F0`
* **Text**: Navy `#0E1E40`
* **Font**: Helvetica Neue
* **Logo**: `data/dumroo_ai_logo.png`

---

## Error Handling

| Scenario                 | Behavior                                     |
| ------------------------ | -------------------------------------------- |
| Missing `students.csv`   | Error message with troubleshooting steps     |
| Missing `GOOGLE_API_KEY` | Prompt to set environment or edit config.py  |
| Unrecognized query       | User-friendly fallback message               |
| Pandas error             | Logs sanitized query + terminal debug output |

---

## Maintenance & Extension

* **Update Dataset**: Modify `data/students.csv` — schema must match original
* **Add New Query Types**: Extend `langchain_agent.py` logic
* **Role Enhancements**: Adjust filters in `rbac.py`
* **Debugging**: Use logs printed in terminal

---

## Troubleshooting

* **Logo not displaying?**
  Check file exists at `data/dumroo_ai_logo.png`

* **Query not understood?**
  Ensure proper grade/region is selected and query is specific

* **Gemini not responding?**
  Check API key, rate limits, or service availability

---

## Future Enhancements

* Support aggregate queries like averages and comparisons
* Add user authentication for secure access
* Allow uploading new datasets dynamically
* Enhance visuals with charts and analytics

---

## License

MIT License

