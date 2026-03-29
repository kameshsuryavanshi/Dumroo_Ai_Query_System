

# Dumroo AI Query System

## Overview

The **Dumroo AI Query System** is a Streamlit-based admin interface powered by **LangChain** and **Google Gemini (gemini-1.5-flash)**. It enables school administrators to query student performance data using natural language, with enforced **role-based access control (RBAC)** to restrict visibility by **grade** and **region**.

The system is designed with a modular architecture to support extensibility, maintainability, and production-grade enhancements.

---

## Purpose

This system enables administrators to:

* Query student data using natural language (e.g., “Which students have not submitted homework?”)
* Enforce scoped access based on **grade (7–10)** and **region (North, South, East, West)**
* Automatically handle missing filters through guided prompting
* View results in structured, human-readable tabular format

---

## Target Audience

* School administrators with restricted data access
* Engineers extending or maintaining the system
* Stakeholders analyzing student performance data

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

## Key Features

### Natural Language Querying

Supports flexible queries via LangChain integrated with Gemini.

### Role-Based Access Control (RBAC)

Applies strict filtering based on user-selected grade and region.

### Dynamic Input Enforcement

Prompts users for missing access constraints before executing queries.

### UI Layer

Responsive Streamlit interface with a consistent theme and structured layout.

### Data Presentation

Outputs are rendered as clean, formatted tables for readability.

### Error Handling

Graceful handling of invalid queries, missing data, and runtime issues.

---

## Prerequisites

* Python 3.9+
* Virtual environment (recommended)
* Google API Key (Gemini access via Google AI Studio)
* Dataset and branding assets in the `data/` directory

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd dumroo-ai-query-system
```

### Setup Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

**Environment Variable**

```bash
# Windows
set GOOGLE_API_KEY=your-key

# Linux/Mac
export GOOGLE_API_KEY=your-key
```

**OR update `config.py`**

```python
GOOGLE_API_KEY = "your-key"
```

---

## Dataset

**File:** `data/students.csv`

**Schema:**

* `student_id`: Unique identifier
* `student_name`: Student name
* `grade`: Integer (7–10)
* `class`: Section (A/B/C)
* `homework_status`: Completed / Incomplete / Missing
* `quiz_score`: Integer (0–100)
* `quiz_date`: DD-MM-YYYY
* `region`: North / South / East / West

---

## Running the Application

```bash
streamlit run app.py
```

Access the application at:
[http://localhost:8501](http://localhost:8501)

---

## Usage

### Step 1: Define Access Scope

Select **grade** and **region** from the sidebar.

### Step 2: Submit Query

Example queries:

* “Which students have not submitted homework?”
* “Show Grade 8 performance for last week”
* “List upcoming quizzes”

### Step 3: Review Output

Results are displayed as structured tables filtered by access scope.

---

## Example Queries

* “List Grade 9 students who missed the last quiz”
* “Show quiz scores for South region this month”
* “Which students completed their homework?”

---

## System Architecture

| Layer          | Description                               |
| -------------- | ----------------------------------------- |
| Frontend       | Streamlit UI (`app.py`)                   |
| Query Engine   | LangChain + Gemini                        |
| Access Control | RBAC logic (`rbac/rbac.py`)               |
| Data Layer     | CSV ingestion (`utils/data_loader.py`)    |
| Configuration  | API keys and runtime config (`config.py`) |

---

## UI Design

* Primary Color: `#3B82F6`
* Background: `#F8FAFC`
* Sidebar: `#E2E8F0`
* Text: `#0E1E40`
* Font: Helvetica Neue

---

## Error Handling

| Scenario               | Behavior                           |
| ---------------------- | ---------------------------------- |
| Missing dataset        | Clear error with remediation steps |
| Missing API key        | Prompt for configuration           |
| Invalid query          | Fallback response                  |
| Data processing errors | Logged for debugging               |

---

## Maintenance and Extension

* Update dataset via `data/students.csv` (schema must remain consistent)
* Extend query capabilities in `langchain_agent.py`
* Enhance RBAC logic for finer-grained control (e.g., class-level)
* Use logs for debugging and tracing execution

---

## Troubleshooting

* **Logo not visible**: Verify file path `data/dumroo_ai_logo.png`
* **Query issues**: Ensure valid scope (grade/region) and clear input
* **Gemini failures**: Validate API key and service availability

---

## Future Enhancements

* Aggregation queries (averages, trends, comparisons)
* User authentication and authorization
* Dynamic dataset uploads
* Advanced visualizations (charts, dashboards)

---

## License

MIT License
