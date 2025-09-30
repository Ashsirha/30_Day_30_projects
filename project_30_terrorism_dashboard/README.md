# Project 30: Dashboard for Global Terrorism Analysis

## Objective
The objective of this project is to create an interactive dashboard that visualizes global terrorism data, providing insights into trends, patterns, and geographical distribution of terrorist activities worldwide. The dashboard will enable users to explore the data through various filters and visualizations.

## Dataset
This project uses the **Global Terrorism Database (GTD)**, which is one of the most comprehensive databases on terrorist attacks worldwide.

- **Source**: [Global Terrorism Database](https://www.start.umd.edu/gtd/)
- **Data File**: `globalterrorismdb.csv` (to be downloaded due to size)
- **Coverage**: 1970-2020 (or latest available)
- **Records**: 200,000+ terrorist attacks worldwide

### Dataset Features:
- **Date and Location**: Year, month, day, country, region, city
- **Attack Information**: Attack type, weapon type, target type
- **Perpetrator Information**: Group name, motive
- **Casualties**: Number killed, wounded
- **Success**: Whether the attack was successful
- **And many more detailed attributes**

## Project Plan
1. **Data Loading and Initial Exploration**:
   - Download and load the Global Terrorism Database.
   - Perform initial data exploration to understand the structure and quality.
   - Handle missing values and data quality issues.

2. **Data Cleaning and Preprocessing**:
   - Clean and standardize location data for mapping.
   - Handle missing values in key columns.
   - Create derived features like decade, casualty severity levels.

3. **Exploratory Data Analysis (EDA)**:
   - Analyze trends over time (yearly, monthly patterns).
   - Explore geographical distribution of attacks.
   - Investigate attack types, weapons used, and target types.
   - Analyze casualty patterns and attack success rates.

4. **Dashboard Development**:
   - Design interactive visualizations using Plotly and Dash (or Streamlit).
   - Create geographical maps showing attack locations and intensity.
   - Build time series charts for temporal analysis.
   - Develop filtering capabilities by country, year, attack type, etc.

5. **Dashboard Features**:
   - **World Map**: Interactive map showing attack locations with clustering.
   - **Time Series**: Trends in attack frequency and casualties over time.
   - **Regional Analysis**: Bar charts and pie charts for regional comparisons.
   - **Attack Characteristics**: Analysis of attack types, weapons, and targets.
   - **Filters**: Interactive filters for country, year range, group, etc.

6. **Deployment and Documentation**:
   - Deploy the dashboard locally or on a web platform.
   - Create user documentation and usage instructions.
   - Summarize key insights discovered through the analysis.

## Technologies
- Python
- Pandas
- NumPy
- Plotly
- Dash (or Streamlit)
- Matplotlib
- Seaborn
- Folium (for mapping)
- Jupyter Notebook

## Key Insights to Explore
- Temporal trends in global terrorism
- Most affected regions and countries
- Evolution of attack methods over time
- Relationship between political events and terrorist activities
- Seasonal patterns in terrorist attacks
- Impact of counter-terrorism efforts on attack patterns

## Ethical Considerations
This project is intended for educational and research purposes only. The analysis should be conducted with sensitivity to the human impact of terrorism and should not glorify or promote violent activities. The goal is to understand patterns that might help in prevention and policy-making.