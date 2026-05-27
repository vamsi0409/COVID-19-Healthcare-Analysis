# COVID-19 Healthcare Analysis

I built this project because COVID-19 data tells one of the most 
important public health stories of our time. I wanted to analyze 
the spread, impact, and healthcare burden across US states using 
real data from The COVID Tracking Project.

## What I Did
I analyzed 15,633 state-level daily records across 56 US states 
and territories. My goal was to understand which states were hit 
hardest, how healthcare systems were strained, and what the data 
reveals about case fatality rates across different regions.

The most striking finding was the difference between case volume 
and fatality rate. California had the most cases (1.34M) but New 
York had the highest deaths (27,149) — and New York's fatality 
rate of 3.85% was double the national average of 1.88%. That tells 
a story about healthcare capacity being overwhelmed early in the 
pandemic before treatments improved.

## Live Dashboard
[View Interactive HTML Dashboard](https://vamsi0409.github.io/COVID-19-Healthcare-Analysis/index.html)

## Key Findings
- **Total Cases: 15.7M+** across all US states and territories
- **Total Deaths: 282,000+** | Case Fatality Rate: **1.88%**
- **California** had most cases: 1,341,700
- **New York** had most deaths: 27,149 with 3.85% fatality rate
- **Daily cases peaked in December 2020** at 210,000+ per day
- States with early outbreaks (NY, NJ, MA) had highest fatality rates

## National Metrics
| Metric | Value |
|--------|-------|
| Total Cases | 15.7M+ |
| Total Deaths | 282K+ |
| Case Fatality Rate | 1.88% |
| States Analyzed | 56 |
| Date Range | Jan 2020 – Dec 2020 |

## Top 5 States by Cases
| State | Cases | Deaths | Fatality Rate |
|-------|-------|--------|---------------|
| CA | 1,341,700 | 19,876 | 1.48% |
| TX | 1,249,323 | 22,594 | 1.81% |
| FL | 1,040,727 | 19,423 | 1.87% |
| IL | 787,573 | 14,116 | 1.79% |
| NY | 705,827 | 27,149 | 3.85% |

## SQL Analysis
I wrote 8 SQL queries to extract healthcare insights:
- National Summary
- Top 10 States by Cases
- Top 10 States by Deaths
- Highest Fatality Rate
- Peak Hospitalization
- Monthly Trend
- Testing vs Positivity
- Daily Average New Cases

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- SQL
- HTML/JavaScript (Chart.js)

## Files
- `covid_analysis.py` — Complete Python analysis
- `covid_queries.sql` — 8 SQL healthcare queries
- `run_covid_sql.py` — SQL execution script
- `covid_dashboard.html` — Interactive HTML dashboard
- `index.html` — GitHub Pages entry point
- `top_states_cases.png` — Cases by state chart
- `top_states_deaths.png` — Deaths by state chart
- `daily_cases_trend.png` — Daily trend chart
- `hospitalization_trend.png` — Hospitalization trend
- `covid_clean.csv` — Cleaned dataset

## What I Learned
This project showed me how important it is to look beyond raw 
numbers. New York had fewer total cases than California but far 
more deaths — because the outbreak hit early before treatments 
were established and healthcare capacity was overwhelmed. Data 
without context can be very misleading.
