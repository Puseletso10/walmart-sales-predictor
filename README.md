# Walmart Sales Prediction

## Project Overview
This project focuses on predicting Walmart weekly sales using machine learning techniques.  
The notebook includes data loading, exploratory data analysis (EDA), preprocessing, model training, and evaluation.

---

## Dataset
The dataset used in this project is:

- `Walmart_Sales.csv`

The dataset contains historical Walmart sales information used to train predictive models.
Source: Kaggle.com

---

## Objectives
- Analyze Walmart sales trends
- Perform exploratory data analysis
- Prepare and preprocess the dataset
- Train machine learning models
- Evaluate model performance using regression metrics

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Random Forest Regressor

---

## Machine Learning Workflow

### 1. Data Loading
The dataset is loaded using Pandas.

```python
df = pd.read_csv("Walmart_Sales.csv", sep=';')
```

### 2. Exploratory Data Analysis (EDA)
The notebook includes:
- Dataset inspection
- Summary statistics
- Duplicate checks
- Feature understanding

### 3. Data Preprocessing
Preprocessing steps include:
- Model evaluation using MAE
- Model evaluation using R² Score
- Train-test split

### 4. Model Training
Models used:
- Random Forest Regressor

### 5. Model Evaluation
Evaluation metrics include:
- Mean Absolute Error (MAE)
- R² Score

Example result:
```python
R2_Score = 0.9319579236898834
```

An R² score of approximately 0.93 indicates strong predictive performance.

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone <repository-url>
```

### 2. Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib
```

### 3. Run the Notebook
Open the notebook using Jupyter Notebook or VS Code:

```bash
jupyter notebook walmart_sales_prediction.ipynb
```

---

## Project Structure

```text
.
├── walmart_sales_prediction.ipynb
├── Walmart_Sales.csv
└── README.md
```

---



## Deployment

This project is deployed using:

- Streamlit
- GitHub

### Live Application
https://sales-prediction-walmart.streamlit.app/

The deployed application allows users to interact with the machine learning model and generate Walmart sales predictions through a web interface.


## Author
Machine Learning Project – Walmart Sales Prediction
