import pandas as pd
import os

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '../data/students.csv')
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at: {data_path}. Please ensure 'students.csv' exists in the 'data' directory.")
    df = pd.read_csv(data_path)
    df['quiz_date'] = pd.to_datetime(df['quiz_date'], format='%d-%m-%Y')
    return df