# Electric Vehicle Population - Data Analysis

Exploratory Data Analysis (EDA) on Washington State Electric Vehicle registration data covering **112,634 EV records** across 17 features, using Python, Seaborn, Matplotlib, and Plotly.

---

## Dataset

- **Source:** [Kaggle - Electric Vehicle Population Data](https://www.kaggle.com/datasets/ratikkakkar/electric-vehicle-population-data)
- **Records:** 112,634 rows × 17 columns
- **Coverage:** Washington State EV registrations (BEV & PHEV)

---

## Key Features Analysed

| Feature | Description |
|---|---|
| Make / Model | Vehicle manufacturer and model |
| Model Year | Year of manufacture (1997–2023) |
| Electric Vehicle Type | BEV (Battery) vs PHEV (Plug-in Hybrid) |
| Electric Range | Range in miles on electric charge |
| Base MSRP | Manufacturer suggested retail price |
| State / County / City | Geographic location of registration |

---

## Tasks Completed

### Task 1 — Univariate & Bivariate EDA
- Distribution of Model Year, Electric Range, Base MSRP
- EV Type vs Electric Range (boxplot)
- Top 10 Makes vs Base MSRP
- EV Type vs Base MSRP (barplot)

### Task 2 — Interactive Plotly Visualisations
- **Choropleth map** — number of EVs by US state
- **Scatter plot** — Electric Range vs Base MSRP coloured by EV type
- **Box plot** — Base MSRP by EV type
- **Pie chart** — Distribution of BEV vs PHEV

### Task 3 — Animated Racing Bar Chart
- Animated bar chart showing EV Make count growth year by year (2000–2023)

---

## Key Findings

- **Tesla MODEL3** is the most registered EV with 23,135 units, followed by MODEL Y (17,142) and Nissan LEAF (12,880)
- **Battery Electric Vehicles (BEV)** have significantly higher electric range than PHEVs
- EV registrations grew **exponentially post-2015**, with the sharpest spike in 2022
- **Washington State** dominates registrations; Tesla commands the highest Base MSRP among top manufacturers
- After cleaning, all 17 columns had **zero missing values**

---

## Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Plotly Express

---

## How to Run

```bash
pip install pandas matplotlib seaborn plotly
python ev_analysis.py
```

Place `dataset.csv` in the same folder before running. Dataset available on [Kaggle](https://www.kaggle.com/datasets/ratikkakkar/electric-vehicle-population-data).
