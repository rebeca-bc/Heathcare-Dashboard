# Healthcare Dashboard 🏥📊

## Overview

This project is an **interactive healthcare analytics dashboard** built using **Dash, Plotly, and Bootstrap**. The goal is to transform raw healthcare records (CSV data) into **meaningful insights** through data cleaning, transformation, and visualization.

The dashboard allows users to explore:

- **Patient Demographics**: Age distribution by gender.
- **Medical Conditions**: Prevalence across the dataset.
- **Insurance Comparisons**: Billing amounts by provider and condition.
- **Billing Distribution**: Filterable by patient gender and cost threshold.
- **Admissions Trends**: Line/bar charts showing condition-specific admissions over time.

This project simulates how healthcare organizations can **leverage data-driven decision making** to improve resource allocation, monitor costs, and understand patient profiles.

---

## Tools & Libraries ⚙️

- **Dash**: Web application framework for interactive Python dashboards.
- **Plotly Express**: For creating advanced, interactive charts.
- **Dash Bootstrap Components**: For clean, responsive layout and styling.
- **Pandas**: For data cleaning, preprocessing, and aggregation.
- **CSV Dataset**: Fake healthcare dataset (`healthcare.csv`) for testing.

---

## Why This Project Matters 💡

Healthcare systems generate massive amounts of data. Visualizing this information helps to:

- Detect **billing anomalies**.
- Monitor **patient demographics** and **disease prevalence**.
- Compare **insurance provider costs**.
- Track **admission trends** over time for policy and planning.

This kind of dashboard is relevant not only for healthcare, but also in any field where **data-driven insights** can improve decision-making.

---

## Features 🚀

- 📊 Interactive charts with filters (gender, conditions, billing).
- 📈 Trend analysis for hospital admissions.
- 🧩 Modular callbacks for responsive updates.
- 🎨 Bootstrap styling for a polished layout.

---

## Visualize it

---

## Dataset 📂

The dataset (`healthcare.csv`) contains **synthetic healthcare records** with fields such as:

- `Name`
- `Age`
- `Gender`
- `Blood Type`
- `Medical Condition`
- `Date of Admission`
- `Doctor`
- `Hospital`
- `Insurance`
- `Provider`
- `Billing Amount`
- `Room Number`
- `Admission Type`
- `Discharge Date`
- `Medication`
- `Test Results`

These were cleaned and transformed using **pandas** for visualization purposes.

---

## How to Run ⚡

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd healthcare-dashboard
   ```
2. Install dependencies:
   pip install dash dash-bootstrap-components plotly pandas
3. Add the dataset (healthcare.csv) into the assets/ folder.
4. Run the app:
   python app.py
5. Open your browser at:
   http://127.0.0.1:8050/
