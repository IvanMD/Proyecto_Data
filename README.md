# E-commerce Data Analysis & Machine Learning Project

This repository contains a comprehensive data analysis pipeline for the Olist E-commerce dataset. The project demonstrates modular software engineering practices and end-to-end data science workflows.

## Project Structure
- `src/`: Contains custom Python modules for data cleaning and preparation.
- `tests/`: Automated unit tests using `pytest` to ensure data integrity.
- `1_exploracion.ipynb`: Exploratory Data Analysis (EDA), featuring relational database merging and data visualization.
- `2_machine_learning.ipynb`: Machine Learning pipeline including feature engineering, model training (Random Forest), and rigorous performance evaluation.

## Technical Highlights
- **Software Engineering**: Modularized code and automated testing.
- **Data Wrangling**: Relational joins across multiple datasets.
- **Machine Learning**: Binary classification to predict customer satisfaction, evaluated with precision, recall, and confusion matrices.

## How to Run
1. Install dependencies: `pip install pandas matplotlib seaborn scikit-learn pytest`
2. Run tests: `python -m pytest`
3. Execute the notebooks in order: `1_exploracion.ipynb` followed by `2_machine_learning.ipynb`.
