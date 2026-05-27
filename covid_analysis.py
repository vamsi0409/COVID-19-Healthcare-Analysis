import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the state-level COVID-19 dataset
print("Loading data...")
df = pd.read_csv('us_states_covid19_daily.csv')
print(f"Shape: {df.shape}")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
# STEP 2: DATA CLEANING & KEY METRICS
print("\nCleaning data...")
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df = df.sort_values(['state', 'date'])

# Focus on key columns
key_cols = ['date', 'state', 'positive', 'death', 'hospitalizedCurrently',
            'positiveIncrease', 'deathIncrease', 'totalTestResults',
            'hospitalizedIncrease', 'inIcuCurrently', 'onVentilatorCurrently']
df = df[key_cols].copy()

# Fill nulls with 0
df = df.fillna(0)

# Get latest date snapshot
latest_date = df['date'].max()
latest = df[df['date'] == latest_date]

print(f"Date range: {df['date'].min()} to {latest_date}")
print(f"Total states: {df['state'].nunique()}")
print(f"\nNational Totals (Latest):")
print(f"  Total Cases: {latest['positive'].sum():,.0f}")
print(f"  Total Deaths: {latest['death'].sum():,.0f}")
print(f"  Currently Hospitalized: {latest['hospitalizedCurrently'].sum():,.0f}")
print(f"  Currently in ICU: {latest['inIcuCurrently'].sum():,.0f}")
print(f"  On Ventilator: {latest['onVentilatorCurrently'].sum():,.0f}")

# Death rate
total_cases = latest['positive'].sum()
total_deaths = latest['death'].sum()
death_rate = (total_deaths / total_cases) * 100
print(f"  Case Fatality Rate: {death_rate:.2f}%")

print(f"\nTop 10 States by Cases:")
top_states = latest.nlargest(10, 'positive')[['state', 'positive', 'death']]
print(top_states.to_string(index=False))
# STEP 3: VISUALIZATIONS
print("\nCreating charts...")

# Chart 1: Top 10 States by Cases
fig, ax = plt.subplots(figsize=(10, 6))
top10 = latest.nlargest(10, 'positive').sort_values('positive')
ax.barh(top10['state'], top10['positive']/1000, color='#F44336')
ax.set_title('Top 10 States by COVID-19 Cases', fontsize=14, fontweight='bold')
ax.set_xlabel('Total Cases (Thousands)')
for i, v in enumerate(top10['positive']/1000):
    ax.text(v + 5, i, f'{v:.0f}K', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('top_states_cases.png', dpi=150)
print("Saved: top_states_cases.png")

# Chart 2: Top 10 States by Deaths
fig, ax = plt.subplots(figsize=(10, 6))
top10_deaths = latest.nlargest(10, 'death').sort_values('death')
ax.barh(top10_deaths['state'], top10_deaths['death']/1000, color='#9C27B0')
ax.set_title('Top 10 States by COVID-19 Deaths', fontsize=14, fontweight='bold')
ax.set_xlabel('Total Deaths (Thousands)')
for i, v in enumerate(top10_deaths['death']/1000):
    ax.text(v + 0.1, i, f'{v:.1f}K', va='center', fontsize=9)
plt.tight_layout()
plt.savefig('top_states_deaths.png', dpi=150)
print("Saved: top_states_deaths.png")

# Chart 3: National Daily New Cases Trend
national = df.groupby('date')['positiveIncrease'].sum().reset_index()
national = national[national['positiveIncrease'] > 0]
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(national['date'], national['positiveIncrease'], color='#F44336', linewidth=1.5)
ax.fill_between(national['date'], national['positiveIncrease'], alpha=0.3, color='#F44336')
ax.set_title('National Daily New COVID-19 Cases', fontsize=14, fontweight='bold')
ax.set_ylabel('Daily New Cases')
ax.set_xlabel('Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_cases_trend.png', dpi=150)
print("Saved: daily_cases_trend.png")

# Chart 4: Hospitalization Trend
national_hosp = df.groupby('date')['hospitalizedCurrently'].sum().reset_index()
national_hosp = national_hosp[national_hosp['hospitalizedCurrently'] > 0]
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(national_hosp['date'], national_hosp['hospitalizedCurrently'], color='#2196F3', linewidth=2)
ax.fill_between(national_hosp['date'], national_hosp['hospitalizedCurrently'], alpha=0.3, color='#2196F3')
ax.set_title('National COVID-19 Hospitalizations Over Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Currently Hospitalized')
ax.set_xlabel('Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('hospitalization_trend.png', dpi=150)
print("Saved: hospitalization_trend.png")

# Export clean data
df.to_csv('covid_clean.csv', index=False)
print("Saved: covid_clean.csv")
print("\nAnalysis Complete!")