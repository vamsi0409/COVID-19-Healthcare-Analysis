import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('covid_clean.csv')
df['date'] = pd.to_datetime(df['date'])

# Create database
conn = sqlite3.connect('covid.db')
df.to_sql('covid_data', conn, if_exists='replace', index=False)
print("Database created!")

queries = {
    "1. National Summary": """
        SELECT COUNT(DISTINCT state) as total_states,
               ROUND(MAX(positive)/1000000.0, 2) as total_cases_millions,
               ROUND(MAX(death)/1000.0, 1) as total_deaths_thousands,
               ROUND(MAX(death)/MAX(positive)*100, 2) as case_fatality_rate
        FROM covid_data
        WHERE date = (SELECT MAX(date) FROM covid_data)
        GROUP BY date
        LIMIT 1
    """,
    "2. Top 10 States by Cases": """
        SELECT state,
               CAST(positive AS INT) as total_cases,
               CAST(death AS INT) as total_deaths,
               ROUND(death/positive*100, 2) as fatality_rate
        FROM covid_data
        WHERE date = (SELECT MAX(date) FROM covid_data)
        AND positive > 0
        ORDER BY total_cases DESC
        LIMIT 10
    """,
    "3. Top 10 States by Deaths": """
        SELECT state,
               CAST(death AS INT) as total_deaths,
               CAST(positive AS INT) as total_cases,
               ROUND(death/positive*100, 2) as fatality_rate
        FROM covid_data
        WHERE date = (SELECT MAX(date) FROM covid_data)
        AND death > 0
        ORDER BY total_deaths DESC
        LIMIT 10
    """,
    "4. States with Highest Fatality Rate": """
        SELECT state,
               CAST(positive AS INT) as total_cases,
               CAST(death AS INT) as total_deaths,
               ROUND(death/positive*100, 2) as fatality_rate
        FROM covid_data
        WHERE date = (SELECT MAX(date) FROM covid_data)
        AND positive > 10000
        ORDER BY fatality_rate DESC
        LIMIT 10
    """,
    "5. Peak Hospitalization by State": """
        SELECT state,
               CAST(MAX(hospitalizedCurrently) AS INT) as peak_hospitalized,
               CAST(MAX(inIcuCurrently) AS INT) as peak_icu,
               CAST(MAX(onVentilatorCurrently) AS INT) as peak_ventilator
        FROM covid_data
        GROUP BY state
        ORDER BY peak_hospitalized DESC
        LIMIT 10
    """,
    "6. Monthly New Cases Trend": """
        SELECT strftime('%Y-%m', date) as month,
               CAST(SUM(positiveIncrease) AS INT) as new_cases,
               CAST(SUM(deathIncrease) AS INT) as new_deaths
        FROM covid_data
        GROUP BY month
        ORDER BY month
    """,
    "7. Testing vs Positivity Analysis": """
        SELECT state,
               CAST(MAX(totalTestResults) AS INT) as total_tests,
               CAST(MAX(positive) AS INT) as total_cases,
               ROUND(MAX(positive)/MAX(totalTestResults)*100, 1) as positivity_rate
        FROM covid_data
        WHERE totalTestResults > 0
        GROUP BY state
        ORDER BY positivity_rate DESC
        LIMIT 10
    """,
    "8. Daily Average New Cases by State": """
        SELECT state,
               ROUND(AVG(positiveIncrease), 0) as avg_daily_cases,
               ROUND(AVG(deathIncrease), 1) as avg_daily_deaths,
               ROUND(AVG(hospitalizedIncrease), 1) as avg_daily_hospitalized
        FROM covid_data
        WHERE positiveIncrease > 0
        GROUP BY state
        ORDER BY avg_daily_cases DESC
        LIMIT 10
    """
}

for name, query in queries.items():
    print(f"\n{'='*50}")
    print(f"{name}")
    print('='*50)
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

conn.close()
print("\n\nAll SQL queries executed successfully!")