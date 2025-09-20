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
<img width="1440" height="900" alt="Screen Shot 2025-09-19 at 18 39 04" src="https://github.com/user-attachments/assets/10e4bee4-9cc0-4df6-9d17-1aa33e17f333" />

<img width="1440" height="900" alt="Screen Shot 2025-09-19 at 18 39 17" src="https://github.com/user-attachments/assets/1863bcdb-0636-4cac-a791-b7936dcd22a1" />

<img width="1440" height="900" alt="Screen Shot 2025-09-19 at 18 39 29" src="https://github.com/user-attachments/assets/7b791b30-4e94-4540-8053-7608a5426a31" />

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
