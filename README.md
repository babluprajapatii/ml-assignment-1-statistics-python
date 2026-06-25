# 📘 ML Internship — Assignment 1: Statistics, Probability & Python Foundations

## Project Title
**Machine Learning Internship — Assignment 1**
**Statistics, Probability & Python Foundations**

---

## Student Information

| Field | Details |
|---|---|
| **Name** | Bablu Kumar |
| **University Roll No.** | 23052440012 |
| **College Roll No.** | 23011036 |
| **Course** | Data Analysis using Open-Source Tools |
| **Submitted To** | Mr. Basudev Mahata |
| **Department** | CSE, RTC Institute of Technology, Ranchi |
| **Session** | 2025–26 |
| **Semester** | 6th |
| **Batch** | 2023–27 |
| **Date of Submission** | 09/05/26 |

---

## Objective

This assignment covers foundational concepts of Statistics, Probability, Combinatorics, and Python Programming as applied to Machine Learning. The goal is to develop a solid mathematical and computational understanding required for ML workflows.

---

## Assignment Overview

| Task | Topic | Description |
|------|-------|-------------|
| Task 1.1 | Descriptive Statistics | Mean, Median, Mode, Range, Variance, SD |
| Task 1.2 | Probability | Coin toss, Balls in bag, Dice sum |
| Task 1.3 | Permutation & Combination | MACHINE letters, Committee selection |
| Task 1.4 | Binomial Distribution | Biased coin, P(X=3), P(X≥4) |
| Task 2 | Python + NumPy + Pandas | Statistical verification, DataFrame operations |
| Task 3.1 | Hypothesis Testing | t-test, p-value, decision |
| Task 3.2 | Confidence Interval | 95% CI, margin of error |
| Task 3.3 | Matplotlib Visualizations | Bar chart, scatter plot, histogram |

---

## Technologies Used

- **Python 3.x**
- **Jupyter Notebook**
- **NumPy** — Numerical computations
- **Pandas** — Data manipulation
- **SciPy** — Statistical tests
- **Matplotlib** — Data visualization

---

## Folder Structure

```
ml-assignment-1-statistics-python/
│
├── Student_Performance_Assignment1.ipynb   ← Main Jupyter Notebook
├── employees.csv                            ← Employee dataset
├── requirements.txt                         ← Python dependencies
├── README.md                                ← This file
│
├── bar_chart.png                            ← Department vs Avg Salary
├── scatter_plot.png                         ← Experience vs Salary
├── histogram.png                            ← Age Distribution
│
└── screenshots/                             ← Output screenshots
    ├── task1_statistics.png
    ├── task2_numpy.png
    ├── task2_dataframe.png
    ├── task3_hypothesis.png
    └── task3_visualizations.png
```

---

## Installation

### Step 1 — Clone or Download

```bash
git clone https://github.com/babluprajapatii/ml-assignment-1-statistics-python.git
cd ml-assignment-1-statistics-python
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

### Option 1 — Jupyter Notebook (Recommended)

```bash
jupyter notebook Student_Performance_Assignment1.ipynb
```

Then run all cells: **Kernel → Restart & Run All**

### Option 2 — VS Code

Open `Student_Performance_Assignment1.ipynb` in VS Code with the Jupyter extension installed.

---

## Expected Output

### Task 1 — Descriptive Statistics
```
Mean     = 79.30
Median   = 79.00
Mode     = No mode (all values unique)
Range    = 27
Variance = 82.68 (sample)
Std Dev  = 9.09  (sample)
```

### Task 2 — NumPy Verification
```
NumPy Mean     : 79.3
NumPy Median   : 79.0
NumPy Range    : 27
NumPy Variance : 82.68
NumPy Std Dev  : 9.09
```

### Task 3 — Hypothesis Test
```
t-statistic = 0.4827
p-value     = 0.6412
Decision    : Fail to Reject H₀
Conclusion  : No significant evidence that mean ≠ 8 hours
```

### Confidence Interval
```
95% CI = (7.748, 8.652)
```

---

## Conclusion

This assignment demonstrates the practical application of statistical concepts and Python programming in a machine learning context:

1. **Descriptive statistics** reveal the central tendency and spread of student marks.
2. **Probability** calculations show how to quantify uncertainty using both classical and conditional approaches.
3. **Combinatorics** provides tools for counting arrangements and selections.
4. **Binomial distribution** models discrete outcomes with a fixed probability.
5. **Hypothesis testing** allows data-driven decisions about population parameters.
6. **Confidence intervals** provide a range of plausible values for the true mean.
7. **Data visualization** with Matplotlib makes patterns and trends easy to understand.

All concepts form the mathematical backbone of modern Machine Learning algorithms.

---

## License

This project is submitted as part of the ML Internship coursework at RTC Institute of Technology, Ranchi.

© 2026 Bablu Kumar — All rights reserved.
