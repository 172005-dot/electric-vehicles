"""
Electric Vehicle Population - Exploratory Data Analysis
Dataset: Washington State EV Registration Data (112,634 records)
Source: https://www.kaggle.com/datasets/ratikkakkar/electric-vehicle-population-data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ─────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────
df = pd.read_csv("dataset.csv")
print(df.shape)
print(df.head())

# ─────────────────────────────────────────
# 2. DATA EXPLORATION
# ─────────────────────────────────────────
df.info()
print(df.duplicated().sum())
print(df['Model'].value_counts())
print(df['Legislative District'].describe())
print(df['Vehicle Location'].value_counts())

# ─────────────────────────────────────────
# 3. DATA CLEANING (handle missing values)
# ─────────────────────────────────────────
df['Model'] = df['Model'].fillna(df['Model'].mode()[0])
df['Legislative District'] = df['Legislative District'].fillna(df['Legislative District'].mean())
df['Vehicle Location'] = df['Vehicle Location'].fillna(df['Vehicle Location'].mode()[0])
df['Electric Utility'] = df['Electric Utility'].fillna(df['Electric Utility'].mode()[0])

print(df.isna().sum())   # should all be 0

# ─────────────────────────────────────────
# 4. UNIVARIATE ANALYSIS
# ─────────────────────────────────────────

# Distribution of Model Year
plt.figure(figsize=(6, 4))
sns.histplot(df['Model Year'], bins=20, kde=True, color='blue')
plt.title('Distribution of Model Year')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('model_year_distribution.png', dpi=150)
plt.show()

# Distribution of Electric Range
plt.figure(figsize=(6, 4))
sns.histplot(df['Electric Range'], bins=30, kde=True, color='green')
plt.title('Distribution of Electric Range')
plt.xlabel('Electric Range (Miles)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('electric_range_distribution.png', dpi=150)
plt.show()

# Distribution of Base MSRP
plt.figure(figsize=(6, 4))
sns.histplot(df['Base MSRP'], bins=30, kde=True, color='orange')
plt.title('Distribution of Base MSRP')
plt.xlabel('Base MSRP ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('base_msrp_distribution.png', dpi=150)
plt.show()

# ─────────────────────────────────────────
# 5. BIVARIATE ANALYSIS
# ─────────────────────────────────────────

# Electric Vehicle Type vs Electric Range
plt.figure(figsize=(6, 4))
sns.boxplot(x='Electric Vehicle Type', y='Electric Range', data=df)
plt.title('Electric Vehicle Type vs Electric Range')
plt.xticks(rotation=45)
plt.ylabel('Electric Range (Miles)')
plt.tight_layout()
plt.savefig('ev_type_vs_range.png', dpi=150)
plt.show()

# Top 10 Makes vs Base MSRP
plt.figure(figsize=(6, 4))
top_makes = df['Make'].value_counts().nlargest(10).index
sns.boxplot(x='Make', y='Base MSRP', data=df[df['Make'].isin(top_makes)])
plt.title('Top 10 Vehicle Makes vs Base MSRP')
plt.xticks(rotation=45)
plt.ylabel('Base MSRP ($)')
plt.tight_layout()
plt.savefig('top_makes_vs_msrp.png', dpi=150)
plt.show()

# EV Type vs Base MSRP (bar)
plt.figure(figsize=(6, 4))
sns.barplot(x='Electric Vehicle Type', y='Base MSRP', data=df)
plt.xticks(rotation=25)
plt.xlabel('Electric Vehicle Type')
plt.ylabel('Base MSRP ($)')
plt.title('Distribution of EV Type based on Base MSRP')
plt.tight_layout()
plt.savefig('ev_type_vs_msrp_bar.png', dpi=150)
plt.show()

# ─────────────────────────────────────────
# 6. TASK 2 — CHOROPLETH MAP (plotly)
# ─────────────────────────────────────────
state_data = df.groupby('State')['VIN (1-10)'].count().reset_index()
state_data.columns = ['State', 'EV Count']

fig = px.choropleth(
    state_data,
    locations='State',
    locationmode='USA-states',
    color='EV Count',
    color_continuous_scale='Blues',
    scope='usa',
    labels={'EV Count': 'Number of EV Vehicles'},
    title='Number of Electric Vehicles by State'
)
fig.show()

# ─────────────────────────────────────────
# 7. SCATTER PLOT (plotly)
# ─────────────────────────────────────────
fig = px.scatter(
    df,
    x='Base MSRP',
    y='Electric Range',
    color='Electric Vehicle Type',
    title='Scatter Plot of Electric Range vs Base MSRP',
    labels={'Base MSRP': 'Base MSRP ($)', 'Electric Range': 'Electric Range (Miles)'},
    hover_data=['Make', 'Model']
)
fig.show()

# ─────────────────────────────────────────
# 8. BOX PLOT (plotly)
# ─────────────────────────────────────────
fig = px.box(
    df,
    x='Electric Vehicle Type',
    y='Base MSRP',
    title='Box Plot of Base MSRP by Electric Vehicle Type',
    labels={'Base MSRP': 'Base MSRP ($)', 'Electric Vehicle Type': 'EV Type'},
    hover_data=['Make', 'Model']
)
fig.show()

# ─────────────────────────────────────────
# 9. PIE CHART (plotly)
# ─────────────────────────────────────────
vehicle_type_count = df.groupby('Electric Vehicle Type')['VIN (1-10)'].count().reset_index()
vehicle_type_count.columns = ['Electric Vehicle Type', 'Count']

fig = px.pie(
    vehicle_type_count,
    names='Electric Vehicle Type',
    values='Count',
    title='Distribution of Electric Vehicles by Type',
    labels={'Electric Vehicle Type': 'EV Type', 'Count': 'Number of Vehicles'}
)
fig.show()

# ─────────────────────────────────────────
# 10. TASK 3 — ANIMATED RACING BAR CHART (plotly)
# ─────────────────────────────────────────
make_year_data = df.groupby(['Model Year', 'Make'])['VIN (1-10)'].count().reset_index()
make_year_data.columns = ['Model Year', 'Make', 'Count']

fig = px.bar(
    make_year_data,
    x='Make',
    y='Count',
    color='Make',
    animation_frame='Model Year',
    animation_group='Make',
    range_y=[0, make_year_data['Count'].max() + 100],
    title='Electric Vehicle Makes Over Time',
    labels={'Count': 'Number of Vehicles', 'Make': 'EV Make'}
)
fig.show()
