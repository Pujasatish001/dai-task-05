# Titanic Dataset - Exploratory Data Analysis (EDA)

## 📌 Objective

The goal of this project is to perform **Exploratory Data Analysis (EDA)** on the Titanic dataset to extract meaningful insights and visual patterns using statistical and graphical techniques.

---

## 📁 Dataset Information

The project uses three datasets:

- **train.csv** - contains the training set including the target variable `Survived`
- **test.csv** - the test set for model evaluation (used for comparison or future prediction)
- **gender_submission.csv** - a sample submission file showing predicted survival for test set passengers

---

## 🛠 Tools & Libraries Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🔍 Steps Performed

### 1. Data Loading & Inspection
- Read CSV files using `pandas`
- Used `.head()`, `.info()`, `.describe()`, and `.value_counts()` for basic data inspection
- Identified missing values and data types

### 2. Univariate Analysis
- Plotted distributions of individual features such as `Survived`, `Sex`, `Age`, and `Pclass`

### 3. Bivariate Analysis
- Compared survival rates across:
  - Gender (`Sex` vs `Survived`)
  - Passenger class (`Pclass` vs `Survived`)
  - Age and fare using boxplots and histograms

### 4. Correlation Analysis
- Created a heatmap of feature correlations
- Used `pairplot` to visually analyze relationships between numerical variables

### 5. Observations & Insights
- Women had significantly higher survival rates
- Passengers in higher classes survived more
- Younger passengers had better chances of survival
- Some features had missing data (e.g., Age, Cabin)

---

## 📊 Key Visualizations

- **Countplots** for gender, class, and survival
- **Histograms** for age and fare distributions
- **Boxplots** to compare age across classes
- **Heatmaps** and **pairplots** to identify feature relationships

---

## 📎 Deliverables

- ✅ `Titanic_EDA.ipynb` — Jupyter Notebook with full code and visualizations
- ✅ `Titanic_EDA.pdf` — Exported PDF version of the notebook (for reporting)

---

## ✅ How to Run

1. Clone the repo or download the files
2. Place the `train.csv`, `test.csv`, and `gender_submission.csv` in the same directory
3. Open the notebook using Jupyter
4. Run all cells to reproduce the EDA

```bash
jupyter notebook Titanic_EDA.ipynb
