# E-Commerce Sales Analysis & Customer Satisfaction Prediction

A complete Data Analytics and Machine Learning pipeline analyzing real e-commerce data from Olist (Brazil). This project covers everything from data ingestion and cleaning to exploratory data analysis (EDA) and predictive modeling.

---

## Project Overview
The goal of this project is to extract actionable business insights from raw e-commerce data and build a Machine Learning model to predict customer satisfaction based on logistics performance.

### 🛠️ Technologies Used
*   **Language:** Python
*   **Data Manipulation:** Pandas
*   **Data Visualization:** Matplotlib, Seaborn
*   **Machine Learning:** Scikit-Learn (Random Forest)

---

## Project Structure

### 1. Exploratory Data Analysis (`1_exploracion.ipynb`)
*   **Data Cleaning:** Handled dates and filtered out canceled orders.
*   **Data Integration:** Merged multiple datasets (Orders, Customers, Items) to create a comprehensive source of truth.
*   **Business Insights:** Grouped and aggregated revenue data to identify the top-performing regions.
*   **Visualization:** Created elegant bar charts to display the **Top 5 Revenue Generating States**.

### 2. Machine Learning Pipeline (`2_machine_learning.ipynb`)
*   **Feature Engineering:** Calculated `shipping_days` by finding the difference between purchase and delivery dates.
*   **Target Variable:** Created a binary `happy_customer` metric based on raw review scores.
*   **Predictive Modeling:** Trained a **Random Forest Classifier** to predict if a customer will leave a positive review based strictly on how many days the shipping took.
*   **Evaluation:** Measured model performance using Accuracy Score and Confusion Matrix.

---

## How to Run the Project
1. Clone this repository.
2. Ensure you have the required libraries installed (`pip install pandas matplotlib seaborn scikit-learn`).
3. Run the Jupyter Notebooks in sequence.

> **Note:** The raw `.csv` data files are not included in this repository to keep it lightweight, but the complete code to process them is fully functional.
