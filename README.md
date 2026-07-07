<div align="center">

# 📊 Machine Learning Internship — Assignment 1

### Statistics, Probability & Python Foundations

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)
[![SciPy](https://img.shields.io/badge/SciPy-1.10+-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org)

[![License: MIT](https://img.shields.io/badge/License-Academic-green?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)]()
[![Assignment](https://img.shields.io/badge/Assignment-01-blue?style=flat-square)]()
[![Session](https://img.shields.io/badge/Session-2025--26-orange?style=flat-square)]()

</div>

---

## 📋 Project Overview

This repository contains **Assignment 1** of the **Machine Learning Internship** program, submitted as part of the course *Data Analysis using Open-Source Tools* at **RTC Institute of Technology, Ranchi**.

The assignment demonstrates a thorough understanding of the mathematical and computational foundations of Machine Learning, covering:

> 📐 **Descriptive Statistics** · 🎲 **Probability Theory** · 🔢 **Combinatorics** · 📉 **Binomial Distribution** · 🐍 **Python Programming** · 🔬 **Hypothesis Testing** · 📊 **Data Visualization**

All mathematical solutions include **Formula → Substitution → Calculation → Final Answer → Explanation** — no shortcuts, no placeholders.

---

## 🎯 Objectives

| # | Objective |
|---|---|
| 1 | Apply descriptive statistics to analyze real-world student marks data |
| 2 | Solve classical probability and combinatorics problems mathematically |
| 3 | Verify all manual calculations programmatically using **NumPy** |
| 4 | Perform comprehensive data analysis using **Pandas** DataFrames |
| 5 | Conduct one-sample **t-test** and interpret p-values and critical values |
| 6 | Calculate and interpret **95% Confidence Intervals** |
| 7 | Create professional, publication-quality charts using **Matplotlib** |

---

## 📁 Repository Structure

```text
ml-assignment-1-statistics-python/
│
├── 📓 Student_Performance_Assignment1.ipynb   ← Main Jupyter Notebook (50 cells)
├── 📄 Assignment_1_Solution.pdf               ← PDF with embedded charts & formulas
├── 📝 Assignment_1_Solution.docx              ← Word document with full solution
├── 📊 employees.csv                           ← Employee dataset (10 records)
│
├── 🖼️  bar_chart.png                          ← Department vs Average Salary
├── 🖼️  scatter_plot.png                       ← Experience vs Salary (with trend)
├── 🖼️  histogram.png                          ← Age Distribution of Employees
│
├── 📂 screenshots/                            ← Output screenshots folder
│   ├── task3_bar_chart.png
│   ├── task3_scatter_plot.png
│   └── task3_histogram.png
│
├── 📋 requirements.txt                        ← Python dependencies
└── 📖 README.md                              ← This file
```

---

## 📚 Tasks Covered

<details open>
<summary><b>🔢 Task 1 — Descriptive Statistics, Probability &amp; Combinatorics</b></summary>

<br>

### 📌 Task 1.1 — Descriptive Statistics

Given marks: `72, 85, 90, 65, 78, 92, 68, 75, 88, 80`

| Measure | Formula | Result |
|---|---|---|
| **Mean** | `Σxᵢ / n` | **79.30** |
| **Median** | Middle value (sorted) | **79.00** |
| **Mode** | Most frequent value | **No Mode** (all unique) |
| **Range** | `x_max − x_min` | **27** |
| **Sample Variance** | `Σ(xᵢ−x̄)² / (n−1)` | **87.79** |
| **Sample Std Dev** | `√Variance` | **9.37** |

---

### 🎲 Task 1.2 — Probability

| Problem | Setup | Answer |
|---|---|---|
| **Q1** — Fair coin, 3 tosses | P(exactly 2 heads) | **3/8 = 0.375** |
| **Q2a** — Bag: 5R, 4B, 3G | P(Red) | **5/12 ≈ 0.4167** |
| **Q2b** — Same bag | P(Not Green) | **3/4 = 0.75** |
| **Q3** — Two dice rolled | P(Sum > 8) | **10/36 = 5/18 ≈ 0.2778** |

---

### 🔡 Task 1.3 — Permutation & Combination

**Problem 1 — MACHINE (vowels together)**
```
Vowels: A, I, E (3) | Consonants: M, C, H, N (4)
Treat [AIE] as 1 block → 5 units
Total = 5! × 3! = 120 × 6 = 720 arrangements
```

**Problem 2 — Committee: 2 men from 6, 2 women from 5**
```
C(6,2) × C(5,2) = 15 × 10 = 150 committees
```

---

### 📉 Task 1.4 — Binomial Distribution

Biased coin: `P(Head) = 0.6`, `n = 5` tosses

```
P(X = k) = C(n,k) × pᵏ × (1−p)ⁿ⁻ᵏ

P(X = 3) = C(5,3) × (0.6)³ × (0.4)²
         = 10 × 0.216 × 0.16 = 0.3456  ✅

P(X ≥ 4) = P(X=4) + P(X=5)
          = 0.2592 + 0.07776 = 0.3370  ✅
```

</details>

---

<details open>
<summary><b>🐍 Task 2 — Python, NumPy &amp; Pandas</b></summary>

<br>

### 📦 Task 2.1 — NumPy Statistical Verification

```python
import numpy as np
marks = np.array([72, 85, 90, 65, 78, 92, 68, 75, 88, 80])

print(f"Mean     : {np.mean(marks):.4f}")      # 79.3000
print(f"Median   : {np.median(marks):.4f}")    # 79.0000
print(f"Range    : {int(np.ptp(marks))}")      # 27
print(f"Variance : {np.var(marks, ddof=1):.4f}")  # 87.7889
print(f"Std Dev  : {np.std(marks, ddof=1):.4f}")  # 9.3696
```

---

### 🗄️ Task 2.2 — Pandas DataFrame Operations

**Employee Dataset (10 records):**

| EmpID | Name | Department | Age | Salary | Experience |
|---|---|---|---|---|---|
| E01 | Aarav | IT | 28 | ₹55,000 | 3 yrs |
| E02 | Bhavya | HR | 32 | ₹48,000 | 5 yrs |
| E03 | Chirag | IT | 26 | ₹52,000 | 2 yrs |
| E04 | Diya | Finance | 35 | ₹72,000 | 8 yrs |
| E05 | Eshan | IT | 30 | ₹60,000 | 4 yrs |
| E06 | Farah | Sales | 29 | ₹45,000 | 3 yrs |
| E07 | Gaurav | Finance | 40 | ₹85,000 | 12 yrs |
| E08 | Hina | HR | 27 | ₹42,000 | 2 yrs |
| E09 | Ishan | Sales | 33 | ₹55,000 | 6 yrs |
| E10 | Jiya | IT | 38 | ₹78,000 | 10 yrs |

**Operations performed:**

- ✅ `df.head()` — Preview first 5 rows
- ✅ `df.describe()` — Statistical summary
- ✅ `df.groupby('Department')['Salary'].mean()` — Average salary per department
- ✅ `df[df['Experience'] > 5]` — Filter experienced employees
- ✅ `df.sort_values('Salary', ascending=False)` — Sort by salary
- ✅ `df.nlargest(3, 'Salary')` — Top 3 earners
- ✅ `df['salary_per_year_exp'] = Salary / Experience` — Feature engineering

**Average Salary by Department:**

| Department | Average Salary |
|---|---|
| 🥇 Finance | ₹78,500 |
| 🥈 IT | ₹61,250 |
| 🥉 Sales | ₹50,000 |
| 4th HR | ₹45,000 |

</details>

---

<details open>
<summary><b>🧪 Task 3 — Hypothesis Testing, CI &amp; Visualizations</b></summary>

<br>

### 📐 Task 3.1 — One-Sample t-Test

**Working Hours Data:** `7.5, 8.2, 7.8, 9.0, 8.5, 7.2, 8.8, 9.1, 7.4, 8.0`

| Step | Item | Value |
|---|---|---|
| H₀ | Null Hypothesis | μ = 8 hours |
| H₁ | Alternative | μ ≠ 8 hours (two-tailed) |
| x̄ | Sample Mean | **8.15** |
| s | Sample Std Dev | **0.6835** |
| df | Degrees of Freedom | **9** |
| t | t-Statistic | **0.6941** |
| t_crit | Critical Value (±) | **±2.262** |
| p | p-Value | **0.5052** |
| 🔴 Decision | \|t\| = 0.6941 < 2.262 | **FAIL TO REJECT H₀** |

> **Conclusion:** At α = 0.05, there is insufficient evidence to reject the company's claim. The average working hours of 8 hours per day is **statistically supported**.

---

### 📏 Task 3.2 — 95% Confidence Interval

```
CI = x̄ ± t(α/2, df) × (s/√n)

Margin of Error = 2.262 × (0.6835/√10) = ±0.4888

Lower Limit = 8.15 − 0.4888 = 7.6612
Upper Limit = 8.15 + 0.4888 = 8.6388
```

> **95% CI = (7.66, 8.64) hours**
> We are 95% confident the true mean lies between **7.66** and **8.64** hours.

---

### 📊 Task 3.3 — Matplotlib Visualizations

| Chart | File | Description |
|---|---|---|
| 📊 Bar Chart | `bar_chart.png` | Department vs Average Salary |
| 🔵 Scatter Plot | `scatter_plot.png` | Experience vs Salary (+ trend line) |
| 📈 Histogram | `histogram.png` | Age Distribution with mean line |

</details>

---

## 🛠️ Technologies Used

<div align="center">

| Tool | Version | Purpose |
|---|---|---|
| 🐍 Python | 3.x | Core programming language |
| 📓 Jupyter Notebook | Latest | Interactive development environment |
| 🔢 NumPy | ≥ 1.24 | Numerical computations & array operations |
| 🐼 Pandas | ≥ 2.0 | Data manipulation & DataFrame analysis |
| 🔬 SciPy | ≥ 1.10 | Statistical tests (t-test, CI) |
| 📊 Matplotlib | ≥ 3.7 | Data visualization & chart generation |
| 📝 MS Word (python-docx) | Latest | Assignment document generation |
| 📄 ReportLab | Latest | PDF generation with embedded charts |

</div>

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** and **pip** installed.

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/babluprajapatii/ml-assignment-1-statistics-python.git

# 2. Navigate into the project directory
cd ml-assignment-1-statistics-python

# 3. Install all required dependencies
pip install -r requirements.txt
```

### Running the Notebook

```bash
# Launch Jupyter Notebook
jupyter notebook Student_Performance_Assignment1.ipynb
```

Then select **Kernel → Restart & Run All** to execute all cells and regenerate all outputs.

### Regenerate Charts & Documents

```bash
# Regenerate all 3 charts (bar, scatter, histogram)
python -c "
import matplotlib
matplotlib.use('Agg')
exec(open('generate_notebook.py').read())
"

# Regenerate Word document (with embedded charts)
python generate_docx.py

# Regenerate PDF
python generate_pdf.py
```

---

## 📈 Key Results Summary

```
╔══════════════════════════════════════════════════════════╗
║           ASSIGNMENT 1 — RESULTS AT A GLANCE            ║
╠══════════════════════════════════════════════════════════╣
║  Task 1.1  │ Mean=79.3 │ Median=79 │ SD≈9.37            ║
║  Task 1.2  │ P(2H)=0.375 │ P(R)=0.4167 │ P(>8)=0.2778  ║
║  Task 1.3  │ MACHINE=720 arrangements │ Committee=150   ║
║  Task 1.4  │ P(X=3)=0.3456 │ P(X≥4)=0.3370             ║
║  Task 2    │ 8 Pandas operations ✅ │ NumPy verified ✅  ║
║  Task 3.1  │ t=0.6941 │ p=0.5052 │ Fail to Reject H₀   ║
║  Task 3.2  │ 95% CI = (7.66, 8.64) hours                ║
║  Task 3.3  │ 3 professional charts generated ✅          ║
╚══════════════════════════════════════════════════════════╝
```

---

## 👨‍🎓 Internship Information

| Field | Details |
|-------|---------|
| Name | Bablu Kumar |
| University Roll No. | 23052440012 |
| College Roll No. | 23011036 |
| Internship | Machine Learning Internship |
| Organization | Internship Studio (iStudio) |
| Department | Computer Science & Engineering |
| College | RTC Institute of Technology, Ranchi |
| Session | 2025–26 |
| Semester | 6th |
| Batch | 2023–27 |
| Date of Submission | 18/06/2026 |

---

## 🙏 Acknowledgement

This project was successfully completed as part of the **Machine Learning Internship** conducted by **Internship Studio (iStudio)**. I sincerely thank Internship Studio (iStudio) for providing the opportunity to gain practical experience in machine learning and data analysis.

---

## 📄 License

© 2026 Bablu Kumar. All rights reserved.

This repository contains a project developed during the **Machine Learning Internship** conducted by **Internship Studio (iStudio)**. It is intended for internship evaluation, educational purposes, and portfolio demonstration.

<div align="center">

**⭐ If this repository helped you, please consider giving it a star!**

Made with ❤️ using Python, NumPy, Pandas, SciPy & Matplotlib

</div>
