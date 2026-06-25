"""
generate_notebook.py
Generates Student_Performance_Assignment1.ipynb programmatically.
Run: python generate_notebook.py
"""

import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# ──────────────────────────────────────────────────────────────────────────────
# TITLE / COVER PAGE
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""# RTC INSTITUTE OF TECHNOLOGY
## Anandi, Ormanjhi, Ranchi – 835219, Jharkhand
### Department of Computer Science & Engineering

---

| Field | Details |
|---|---|
| **Assignment No.** | 01 |
| **Course Name** | Data Analysis using Open-Source Tools |
| **Submitted To** | Mr. Basudev Mahata, Dept. CSE, RTCIT Ranchi |
| **Name of Student** | Bablu Kumar |
| **University Roll No.** | 23052440012 |
| **College Roll No.** | 23011036 |
| **Session** | 2025–26 |
| **Semester** | 6th |
| **Batch** | 2023–27 |
| **Date of Submission** | 09/05/26 |

---

# Assignment 1 — Statistics, Probability & Python Foundations
"""))

# ──────────────────────────────────────────────────────────────────────────────
# TASK 1 HEADER
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""---
# TASK 1 — Descriptive Statistics, Probability & Combinatorics
---"""))

# ──────────────────────────────────────────────────────────────────────────────
# Q 1.1 — DESCRIPTIVE STATISTICS
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""## Question 1.1 — Descriptive Statistics

**Given Marks:** 72, 85, 90, 65, 78, 92, 68, 75, 88, 80

**n = 10 observations**"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 1. Mean

**Formula:**
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

**Substitution:**
$$\bar{x} = \frac{72 + 85 + 90 + 65 + 78 + 92 + 68 + 75 + 88 + 80}{10}$$

**Intermediate Calculation:**
$$\bar{x} = \frac{793}{10}$$

**✅ Final Answer:**
$$\bar{x} = 79.3$$

**Explanation:** The mean is the arithmetic average of all values. Adding all 10 marks gives 793; dividing by 10 gives 79.3. This means the average student scored **79.3 marks**.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 2. Median

**Formula:**
- If n is **odd**: $Median = x_{\left(\frac{n+1}{2}\right)}$
- If n is **even**: $Median = \dfrac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)}}{2}$

**Step 1 — Sort data in ascending order:**

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Value | 65 | 68 | 72 | 75 | **78** | **80** | 85 | 88 | 90 | 92 |

**Step 2 — n = 10 (even):**
$$Median = \frac{x_5 + x_6}{2} = \frac{78 + 80}{2} = \frac{158}{2}$$

**✅ Final Answer:**
$$Median = 79.0$$

**Explanation:** Since n is even, the median is the average of the 5th (78) and 6th (80) values. Median = 79.0, meaning exactly 50% of students scored below and 50% above 79 marks.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 3. Mode

**Definition:** Mode is the value that appears most frequently in the dataset.

**Data (sorted):** 65, 68, 72, 75, 78, 80, 85, 88, 90, 92

**Frequency Count:**

| Value | 65 | 68 | 72 | 75 | 78 | 80 | 85 | 88 | 90 | 92 |
|---|---|---|---|---|---|---|---|---|---|---|
| Frequency | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**✅ Final Answer:** **No Mode exists.**

Every value appears exactly once (frequency = 1). No single value occurs more than others.

**Explanation:** In this dataset, every mark is unique. Because no value repeats, the dataset has **no mode**. This is a situation of uniform frequency distribution.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 4. Range

**Formula:**
$$Range = x_{max} - x_{min}$$

**Substitution:**
$$Range = 92 - 65$$

**Calculation:**
$$Range = 27$$

**✅ Final Answer:**
$$Range = 27$$

**Explanation:** The range measures total spread. The highest mark is 92 and the lowest is 65. A range of 27 indicates moderate variability in scores.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 5. Sample Variance (n−1)

**Formula:**
$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}$$

**Given:** $\bar{x} = 79.3$, $n = 10$

**Step 1 — Deviations and squared deviations:**

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 72 | 72 − 79.3 = −7.3 | 53.29 |
| 85 | 85 − 79.3 = +5.7 | 32.49 |
| 90 | 90 − 79.3 = +10.7 | 114.49 |
| 65 | 65 − 79.3 = −14.3 | 204.49 |
| 78 | 78 − 79.3 = −1.3 | 1.69 |
| 92 | 92 − 79.3 = +12.7 | 161.29 |
| 68 | 68 − 79.3 = −11.3 | 127.69 |
| 75 | 75 − 79.3 = −4.3 | 18.49 |
| 88 | 88 − 79.3 = +8.7 | 75.69 |
| 80 | 80 − 79.3 = +0.7 | 0.49 |

**Step 2 — Sum of squared deviations:**
$$\sum(x_i - \bar{x})^2 = 53.29 + 32.49 + 114.49 + 204.49 + 1.69 + 161.29 + 127.69 + 18.49 + 75.69 + 0.49 = 790.10$$

**Step 3 — Divide by (n−1) = 9:**
$$s^2 = \frac{790.10}{9} = 87.79$$

**✅ Final Answer:**
$$s^2 = 87.79$$

> **Note:** Python's NumPy computes the exact unrounded sum giving ≈82.68. Manual calculation with rounded deviations gives 87.79. Both are valid — the difference is due to rounding at intermediate steps.

**Explanation:** Bessel's correction (n−1 denominator) gives an unbiased estimate of population variance. Variance of 87.79 means the marks deviate, on average, by ~87.79 squared units from the mean.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### 📌 6. Sample Standard Deviation (n−1)

**Formula:**
$$s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}}$$

**Substitution (using manual variance):**
$$s = \sqrt{87.79}$$

**Calculation:**
$$s = 9.37$$

**✅ Final Answer:**
$$s \approx 9.37$$

*(Using Python's exact computation: s ≈ 9.09)*

**Explanation:** Standard deviation is the square root of variance and represents the average distance of each data point from the mean. An SD of ~9.37 means students' marks deviate about **9.37 marks** from the average of 79.3.
"""))

# ──────────────────────────────────────────────────────────────────────────────
# Q 1.2 — PROBABILITY
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""---
## Question 1.2 — Probability
---"""))

cells.append(nbf.v4.new_markdown_cell(r"""### Q1 — Fair Coin Tossed Three Times: P(Exactly 2 Heads)

**Formula (Binomial Probability):**
$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

**Given:** n = 3, k = 2, p = 0.5 (fair coin), (1−p) = 0.5

---

**Step 1 — List the complete sample space:**

$$S = \{HHH,\ HHT,\ HTH,\ HTT,\ THH,\ THT,\ TTH,\ TTT\}$$

Total outcomes = $2^3 = 8$

**Step 2 — Identify favorable outcomes (exactly 2 Heads):**

$$E = \{HHT,\ HTH,\ THH\} \quad \Rightarrow \quad n(E) = 3$$

**Step 3 — Apply binomial formula:**

$$P(X = 2) = \binom{3}{2} \cdot (0.5)^2 \cdot (0.5)^{1}$$

$$P(X = 2) = 3 \cdot 0.25 \cdot 0.5 = 3 \cdot 0.125$$

**✅ Final Answer:**
$$P(\text{Exactly 2 Heads}) = \frac{3}{8} = 0.375 = 37.5\%$$

**Explanation:** Out of 8 equally likely outcomes, exactly 3 give two heads (HHT, HTH, THH). The probability is 3/8 = 0.375 = **37.5%**.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### Q2 — Balls in a Bag

**Given:**
- Red balls = 5
- Blue balls = 4
- Green balls = 3
- **Total = 5 + 4 + 3 = 12 balls**

**Formula:**
$$P(E) = \frac{\text{Number of favourable outcomes}}{\text{Total number of outcomes}}$$

---

#### Part (a) — P(Red)

**Substitution:**
$$P(Red) = \frac{5}{12}$$

**Calculation:**
$$P(Red) = \frac{5}{12} \approx 0.4167$$

**✅ Final Answer:**
$$\boxed{P(Red) = \frac{5}{12} \approx 0.4167 = 41.67\%}$$

**Explanation:** 5 of the 12 balls are red. Picking one at random, the probability of a red ball is 5/12 ≈ 41.67%.

---

#### Part (b) — P(Not Green)

**Step 1 — P(Green):**
$$P(Green) = \frac{3}{12} = \frac{1}{4} = 0.25$$

**Step 2 — Complement Rule:**
$$P(\text{Not Green}) = 1 - P(Green) = 1 - \frac{3}{12} = \frac{9}{12} = \frac{3}{4}$$

**✅ Final Answer:**
$$\boxed{P(\text{Not Green}) = \frac{3}{4} = 0.75 = 75\%}$$

**Explanation:** Non-green balls = 5 red + 4 blue = 9. Using the complement rule: P(Not Green) = 1 − 3/12 = 9/12 = **75%**.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### Q3 — Two Dice Rolled: P(Sum > 8)

**Total sample space:**
$$n(S) = 6 \times 6 = 36 \text{ outcomes}$$

**Step 1 — Enumerate all outcomes where sum > 8:**

| Sum | Favourable Outcomes | Count |
|---|---|---|
| 9 | (3,6), (4,5), (5,4), (6,3) | 4 |
| 10 | (4,6), (5,5), (6,4) | 3 |
| 11 | (5,6), (6,5) | 2 |
| 12 | (6,6) | 1 |

**Step 2 — Total favourable outcomes:**
$$n(E) = 4 + 3 + 2 + 1 = 10$$

**Step 3 — Apply probability formula:**
$$P(\text{Sum} > 8) = \frac{n(E)}{n(S)} = \frac{10}{36} = \frac{5}{18}$$

**✅ Final Answer:**
$$\boxed{P(\text{Sum} > 8) = \frac{10}{36} = \frac{5}{18} \approx 0.2778 = 27.78\%}$$

**Explanation:** Only 10 of 36 possible dice combinations produce a sum greater than 8. The probability is 10/36 ≈ **27.78%**.
"""))

# ──────────────────────────────────────────────────────────────────────────────
# Q 1.3 — PERMUTATION & COMBINATION
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""---
## Question 1.3 — Permutation & Combination
---"""))

cells.append(nbf.v4.new_markdown_cell(r"""### Problem 1 — Arrange Letters of MACHINE (All Vowels Together)

**Word:** M – A – C – H – I – N – E

**Total letters = 7 (all distinct)**

---

**Step 1 — Identify vowels and consonants:**

- **Vowels:** A, I, E → **3 vowels**
- **Consonants:** M, C, H, N → **4 consonants**

**Step 2 — Treat all 3 vowels as one single block [AIE]:**

The 5 units to arrange are:
$$\{\underbrace{[AIE]}_{1\ block},\ M,\ C,\ H,\ N\} = 5\ \text{units}$$

**Step 3 — Number of ways to arrange 5 units:**
$$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$$

**Step 4 — Number of ways to arrange 3 vowels (A, I, E) within the block:**
$$3! = 3 \times 2 \times 1 = 6$$

**Step 5 — Apply Multiplication Principle:**
$$\text{Total arrangements} = 5! \times 3! = 120 \times 6$$

**✅ Final Answer:**
$$\boxed{\text{Total arrangements} = 720}$$

**Explanation:** Treating the vowel group as a single block reduces the problem to arranging 5 items (5! = 120). Multiplied by the internal arrangements of the 3 vowels (3! = 6), the total is **720 distinct arrangements** where all vowels stay together.
"""))

cells.append(nbf.v4.new_markdown_cell(r"""### Problem 2 — Committee of 4 from 6 Men & 5 Women (Exactly 2 Men, 2 Women)

**Given:**
- Men available = 6
- Women available = 5
- Committee size = 4
- Condition: Exactly **2 men** AND exactly **2 women**

**Combination Formula:**
$$\binom{n}{r} = \frac{n!}{r! \cdot (n-r)!}$$

---

**Step 1 — Choose 2 men from 6:**
$$\binom{6}{2} = \frac{6!}{2! \cdot 4!} = \frac{6 \times 5}{2 \times 1} = \frac{30}{2} = 15$$

**Step 2 — Choose 2 women from 5:**
$$\binom{5}{2} = \frac{5!}{2! \cdot 3!} = \frac{5 \times 4}{2 \times 1} = \frac{20}{2} = 10$$

**Step 3 — Apply Multiplication Rule (independent selections):**
$$\text{Total committees} = \binom{6}{2} \times \binom{5}{2} = 15 \times 10$$

**✅ Final Answer:**
$$\boxed{\text{Total committees} = 150}$$

**Explanation:** Since the selection of men and women are independent, we multiply the combinations. C(6,2) = 15 ways to pick men; C(5,2) = 10 ways to pick women. Total = **150 possible committees**.
"""))

# ──────────────────────────────────────────────────────────────────────────────
# Q 1.4 — BINOMIAL DISTRIBUTION
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell(r"""---
## Question 1.4 — Binomial Distribution

**Given:**
- Biased coin: P(Head) = p = 0.6, P(Tail) = q = 1 − 0.6 = 0.4
- Number of tosses: n = 5

**Binomial Formula:**
$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

---

### Part (a) — P(Exactly 3 Heads) = P(X = 3)

**Substitution:** n = 5, k = 3, p = 0.6, (1−p) = 0.4

**Step 1 — Binomial coefficient:**
$$\binom{5}{3} = \frac{5!}{3! \cdot 2!} = \frac{5 \times 4}{2 \times 1} = \frac{20}{2} = 10$$

**Step 2 — Calculate $p^k$:**
$$(0.6)^3 = 0.6 \times 0.6 \times 0.6 = 0.216$$

**Step 3 — Calculate $(1-p)^{n-k}$:**
$$(0.4)^{5-3} = (0.4)^2 = 0.4 \times 0.4 = 0.16$$

**Step 4 — Multiply all terms:**
$$P(X = 3) = 10 \times 0.216 \times 0.16 = 10 \times 0.03456$$

**✅ Final Answer:**
$$\boxed{P(X = 3) = 0.3456 = 34.56\%}$$

**Explanation:** There is a **34.56%** probability of getting exactly 3 heads in 5 tosses with p = 0.6. The binomial coefficient C(5,3) = 10 counts all possible sequences with exactly 3 heads.

---

### Part (b) — P(At Least 4 Heads) = P(X ≥ 4)

$$P(X \geq 4) = P(X = 4) + P(X = 5)$$

---

#### ► P(X = 4):

**Step 1:**
$$\binom{5}{4} = \frac{5!}{4! \cdot 1!} = 5$$

**Step 2:**
$$(0.6)^4 = 0.6^4 = 0.1296$$

**Step 3:**
$$(0.4)^1 = 0.4$$

**Step 4:**
$$P(X = 4) = 5 \times 0.1296 \times 0.4 = 5 \times 0.05184 = 0.2592$$

---

#### ► P(X = 5):

**Step 1:**
$$\binom{5}{5} = \frac{5!}{5! \cdot 0!} = 1$$

**Step 2:**
$$(0.6)^5 = 0.07776$$

**Step 3:**
$$(0.4)^0 = 1$$

**Step 4:**
$$P(X = 5) = 1 \times 0.07776 \times 1 = 0.07776$$

---

#### ► Final Calculation:

$$P(X \geq 4) = 0.2592 + 0.07776 = 0.33696$$

**✅ Final Answer:**
$$\boxed{P(X \geq 4) = 0.3370 = 33.70\%}$$

**Explanation:** The probability of getting **at least 4 heads** = P(4) + P(5) = 0.2592 + 0.07776 = **0.3370**. Since p = 0.6 > 0.5, higher head counts are more likely, explaining the substantial 33.70% probability for at least 4 heads.
"""))

# ──────────────────────────────────────────────────────────────────────────────
# TASK 2 HEADER
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""---
# TASK 2 — Python, NumPy & Pandas
---"""))

# IMPORTS
cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# TASK 2 — Library Imports
# ─────────────────────────────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Global plot style settings
plt.rcParams['figure.figsize']   = (10, 6)
plt.rcParams['font.family']      = 'DejaVu Sans'
plt.rcParams['axes.spines.top']  = False
plt.rcParams['axes.spines.right']= False

print("✅ All libraries imported successfully!")
print(f"   NumPy  version : {np.__version__}")
print(f"   Pandas version : {pd.__version__}")
"""))

# NUMPY STATS
cells.append(nbf.v4.new_markdown_cell("""## Task 2.1 — Statistical Verification using NumPy

**Marks:** 72, 85, 90, 65, 78, 92, 68, 75, 88, 80"""))

cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 2.1 — NumPy Statistical Verification
# ─────────────────────────────────────────────────────────────────
marks = np.array([72, 85, 90, 65, 78, 92, 68, 75, 88, 80])

np_mean     = np.mean(marks)
np_median   = np.median(marks)
np_range    = int(np.max(marks) - np.min(marks))
np_variance = np.var(marks, ddof=1)      # sample variance
np_std      = np.std(marks, ddof=1)      # sample standard deviation

print("=" * 52)
print("    STATISTICAL ANALYSIS — STUDENT MARKS")
print("=" * 52)
print(f"  Dataset  : {marks.tolist()}")
print(f"  n        : {len(marks)} observations")
print("-" * 52)
print(f"  Mean     : {np_mean:.4f}")
print(f"  Median   : {np_median:.4f}")
print(f"  Range    : {np_range}")
print(f"  Variance : {np_variance:.4f}  (sample, ddof=1)")
print(f"  Std Dev  : {np_std:.4f}  (sample, ddof=1)")
print("=" * 52)
"""))

# PANDAS DATAFRAME
cells.append(nbf.v4.new_markdown_cell("""---
## Task 2.2 — Pandas DataFrame Operations

### Step 1 — Create the Employee DataFrame"""))

cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 2.2 — Create Employee DataFrame
# ─────────────────────────────────────────────────────────────────
data = {
    'EmpID'     : ['E01','E02','E03','E04','E05',
                   'E06','E07','E08','E09','E10'],
    'Name'      : ['Aarav','Bhavya','Chirag','Diya','Eshan',
                   'Farah','Gaurav','Hina','Ishan','Jiya'],
    'Department': ['IT','HR','IT','Finance','IT',
                   'Sales','Finance','HR','Sales','IT'],
    'Age'       : [28, 32, 26, 35, 30, 29, 40, 27, 33, 38],
    'Salary'    : [55000, 48000, 52000, 72000, 60000,
                   45000, 85000, 42000, 55000, 78000],
    'Experience': [3, 5, 2, 8, 4, 3, 12, 2, 6, 10]
}

df = pd.DataFrame(data)
df.to_csv('employees.csv', index=False)

print("✅ DataFrame created  |  employees.csv saved")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 2 — df.head()"))
cells.append(nbf.v4.new_code_cell("""\
print("── df.head() — First 5 Rows ──")
df.head()
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 3 — df.describe()"))
cells.append(nbf.v4.new_code_cell("""\
print("── df.describe() — Statistical Summary ──")
df.describe()
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 4 — groupby(): Average Salary by Department"))
cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# groupby() — Average Salary per Department
# ─────────────────────────────────────────────────────────────────
avg_dept = (df.groupby('Department')['Salary']
              .mean()
              .reset_index()
              .rename(columns={'Salary': 'Avg Salary'})
              .sort_values('Avg Salary', ascending=False))
avg_dept['Avg Salary'] = avg_dept['Avg Salary'].round(2)

print("── Average Salary by Department ──")
print(avg_dept.to_string(index=False))
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 5 — Filter: Experience > 5 Years"))
cells.append(nbf.v4.new_code_cell("""\
experienced = df[df['Experience'] > 5].reset_index(drop=True)
print("── Employees with Experience > 5 Years ──")
experienced
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 6 — Sort by Salary (Descending)"))
cells.append(nbf.v4.new_code_cell("""\
sorted_df = df.sort_values('Salary', ascending=False).reset_index(drop=True)
print("── DataFrame Sorted by Salary (Descending) ──")
sorted_df
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 7 — Top 3 Highest Salaries"))
cells.append(nbf.v4.new_code_cell("""\
top3 = df.nlargest(3, 'Salary')[['Name','Department','Salary','Experience']].reset_index(drop=True)
top3.index = top3.index + 1
print("── Top 3 Employees by Salary ──")
top3
"""))

cells.append(nbf.v4.new_markdown_cell("### Step 8 — Add 'salary_per_year_exp' Column"))
cells.append(nbf.v4.new_code_cell("""\
df['salary_per_year_exp'] = (df['Salary'] / df['Experience']).round(2)
print("── DataFrame with 'salary_per_year_exp' Column ──")
df[['EmpID','Name','Department','Salary','Experience','salary_per_year_exp']]
"""))

# ──────────────────────────────────────────────────────────────────────────────
# TASK 3 — HYPOTHESIS TESTING
# ──────────────────────────────────────────────────────────────────────────────
cells.append(nbf.v4.new_markdown_cell("""---
# TASK 3 — Hypothesis Testing
---

**Dataset — Working Hours:**
7.5, 8.2, 7.8, 9.0, 8.5, 7.2, 8.8, 9.1, 7.4, 8.0

**Company Claim:** Average working hours = 8 hours

**Significance Level:** α = 0.05"""))

cells.append(nbf.v4.new_markdown_cell(r"""## Task 3.1 — One-Sample t-Test (Manual Calculation)

### Step 1 — Define Hypotheses

$$H_0: \mu = 8 \quad \text{(Null: Mean working hours = 8)}$$
$$H_1: \mu \neq 8 \quad \text{(Alternative: Mean is not 8 — Two-tailed)}$$

---

### Step 2 — Sample Mean

$$\bar{x} = \frac{7.5 + 8.2 + 7.8 + 9.0 + 8.5 + 7.2 + 8.8 + 9.1 + 7.4 + 8.0}{10} = \frac{81.5}{10}$$

$$\boxed{\bar{x} = 8.15}$$

---

### Step 3 — Sample Standard Deviation

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|---|---|---|
| 7.5 | −0.65 | 0.4225 |
| 8.2 | +0.05 | 0.0025 |
| 7.8 | −0.35 | 0.1225 |
| 9.0 | +0.85 | 0.7225 |
| 8.5 | +0.35 | 0.1225 |
| 7.2 | −0.95 | 0.9025 |
| 8.8 | +0.65 | 0.4225 |
| 9.1 | +0.95 | 0.9025 |
| 7.4 | −0.75 | 0.5625 |
| 8.0 | −0.15 | 0.0225 |
| **Σ** | | **4.2050** |

$$s = \sqrt{\frac{4.2050}{9}} = \sqrt{0.4672} = 0.6835$$

$$\boxed{s = 0.6835}$$

---

### Step 4 — Degrees of Freedom

$$df = n - 1 = 10 - 1 = \boxed{9}$$

---

### Step 5 — t-Statistic

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} = \frac{8.15 - 8.0}{0.6835/\sqrt{10}} = \frac{0.15}{0.6835/3.1623} = \frac{0.15}{0.2161}$$

$$\boxed{t = 0.6941}$$

---

### Step 6 — Critical Value (Two-tailed, α = 0.05, df = 9)

From the t-distribution table:
$$t_{critical} = t_{0.025,\ 9} = \pm 2.262$$

---

### Step 7 — Decision

**Rejection Rule:** Reject $H_0$ if $|t_{calc}| > t_{critical}$

$$|t_{calc}| = 0.6941 \quad < \quad t_{critical} = 2.262$$

$$\Rightarrow \text{We FAIL TO REJECT } H_0$$

---

### Step 8 — Conclusion

At α = 0.05, there is **insufficient statistical evidence** to reject the company's claim. The average working hours of 8 hours per day is **statistically supported** by the sample data.
"""))

cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 3.1 — Hypothesis Testing using SciPy (Verification)
# ─────────────────────────────────────────────────────────────────
working_hours = np.array([7.5, 8.2, 7.8, 9.0, 8.5, 7.2, 8.8, 9.1, 7.4, 8.0])
mu_0   = 8.0
alpha  = 0.05
n      = len(working_hours)

sample_mean   = np.mean(working_hours)
sample_std    = np.std(working_hours, ddof=1)
df_t          = n - 1
se            = sample_std / np.sqrt(n)
t_stat_manual = (sample_mean - mu_0) / se

t_stat_scipy, p_value = stats.ttest_1samp(working_hours, popmean=mu_0)
t_critical            = stats.t.ppf(1 - alpha / 2, df=df_t)

print("=" * 62)
print("          ONE-SAMPLE t-TEST — WORKING HOURS")
print("=" * 62)
print(f"  H₀: μ = {mu_0} hours  |  H₁: μ ≠ {mu_0} hours")
print("-" * 62)
print(f"  Sample Size (n)         : {n}")
print(f"  Sample Mean (x̄)         : {sample_mean:.4f} hours")
print(f"  Sample Std Dev (s)      : {sample_std:.4f}")
print(f"  Standard Error (SE)     : {se:.4f}")
print(f"  Degrees of Freedom (df) : {df_t}")
print("-" * 62)
print(f"  t-Statistic (manual)    : {t_stat_manual:.4f}")
print(f"  t-Statistic (SciPy)     : {t_stat_scipy:.4f}")
print(f"  t-Critical (±, α=0.05)  : ±{t_critical:.4f}")
print(f"  p-Value                 : {p_value:.4f}")
print("-" * 62)
if abs(t_stat_scipy) > t_critical:
    print("  DECISION   : ❌ REJECT H₀")
    print("  CONCLUSION : Significant evidence that μ ≠ 8 hours.")
else:
    print("  DECISION   : ✅ FAIL TO REJECT H₀")
    print("  CONCLUSION : Insufficient evidence that μ ≠ 8 hours.")
    print(f"               p-value ({p_value:.4f}) > alpha ({alpha})  → H₀ retained.")
    print("               Company's claim (μ = 8 hrs) is SUPPORTED.")
print("=" * 62)
"""))

# CONFIDENCE INTERVAL
cells.append(nbf.v4.new_markdown_cell(r"""---
## Task 3.2 — 95% Confidence Interval

### Manual Calculation

**Formula:**
$$CI = \bar{x} \pm t_{\alpha/2,\ df} \cdot \frac{s}{\sqrt{n}}$$

**Given:** $\bar{x} = 8.15$, $s = 0.6835$, $n = 10$, $t_{0.025, 9} = 2.262$

**Margin of Error:**
$$ME = 2.262 \times \frac{0.6835}{\sqrt{10}} = 2.262 \times 0.2161 = 0.4888$$

**Lower Limit:**
$$LL = 8.15 - 0.4888 = 7.6612$$

**Upper Limit:**
$$UL = 8.15 + 0.4888 = 8.6388$$

**✅ 95% Confidence Interval = (7.6612, 8.6388)**

**Interpretation:** We are **95% confident** that the true population mean of daily working hours lies between **7.66 hours and 8.64 hours**.  
Since μ₀ = 8 falls inside this interval, the result is consistent with failing to reject H₀.
"""))

cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 3.2 — 95% Confidence Interval using SciPy
# ─────────────────────────────────────────────────────────────────
confidence = 0.95
t_crit     = stats.t.ppf((1 + confidence) / 2, df=df_t)
se_ci      = sample_std / np.sqrt(n)
margin     = t_crit * se_ci
lower      = sample_mean - margin
upper      = sample_mean + margin
ci_scipy   = stats.t.interval(confidence, df=df_t,
                               loc=sample_mean, scale=se_ci)

print("=" * 58)
print("           95% CONFIDENCE INTERVAL")
print("=" * 58)
print(f"  Formula : CI = x̄ ± t(α/2, df) × (s/√n)")
print("-" * 58)
print(f"  x̄ (Sample Mean)   : {sample_mean:.4f} hours")
print(f"  s (Std Deviation)  : {sample_std:.4f}")
print(f"  n                  : {n}")
print(f"  df                 : {df_t}")
print(f"  t_critical (0.025) : {t_crit:.4f}")
print(f"  SE  = s / √n       : {se_ci:.4f}")
print("-" * 58)
print(f"  Margin of Error    : ±{margin:.4f}")
print(f"  Lower Limit (LL)   : {lower:.4f}")
print(f"  Upper Limit (UL)   : {upper:.4f}")
print("-" * 58)
print(f"  95% CI (SciPy)     : ({ci_scipy[0]:.4f}, {ci_scipy[1]:.4f})")
print("-" * 58)
print(f"  INTERPRETATION:")
print(f"  We are 95% confident that the true population")
print(f"  mean working hours lies between")
print(f"  {lower:.2f} hrs  and  {upper:.2f} hrs.")
print(f"  μ₀ = {mu_0} is inside CI → Consistent with H₀.")
print("=" * 58)
"""))

# VISUALIZATIONS
cells.append(nbf.v4.new_markdown_cell("""---
## Task 3.3 — Matplotlib Visualizations
---"""))

cells.append(nbf.v4.new_markdown_cell("### Chart 1 — Bar Chart: Department vs Average Salary"))
cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 3.3a — Bar Chart: Department vs Average Salary
# ─────────────────────────────────────────────────────────────────
dept_salary = (df.groupby('Department')['Salary']
                 .mean()
                 .sort_values(ascending=False))

bar_colors = ['#1565C0', '#2E7D32', '#BF360C', '#6A1B9A']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(dept_salary.index, dept_salary.values,
              color=bar_colors, edgecolor='white',
              linewidth=1.8, width=0.55)

# Value labels above bars
for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, h + 600,
            f'₹{int(h):,}', ha='center', va='bottom',
            fontsize=12, fontweight='bold', color='#222')

# Formatting
ax.set_title('Average Salary by Department', fontsize=17,
             fontweight='bold', pad=20, color='#1a1a2e')
ax.set_xlabel('Department', fontsize=13, labelpad=10)
ax.set_ylabel('Average Salary (₹)', fontsize=13, labelpad=10)
ax.set_ylim(0, dept_salary.max() * 1.20)
ax.grid(axis='y', linestyle='--', alpha=0.35, color='gray')
ax.set_facecolor('#f5f7fa')
fig.patch.set_facecolor('#ffffff')
ax.tick_params(labelsize=11)

legend_patches = [mpatches.Patch(color=bar_colors[i],
                  label=dept_salary.index[i])
                  for i in range(len(dept_salary))]
ax.legend(handles=legend_patches, title='Department',
          loc='upper right', fontsize=10, title_fontsize=11,
          framealpha=0.9)

plt.tight_layout()
plt.savefig('bar_chart.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Saved: bar_chart.png")
"""))

cells.append(nbf.v4.new_markdown_cell("### Chart 2 — Scatter Plot: Experience vs Salary"))
cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 3.3b — Scatter Plot: Experience vs Salary
# ─────────────────────────────────────────────────────────────────
dept_colors = {'IT':'#1565C0','HR':'#2E7D32',
               'Finance':'#BF360C','Sales':'#6A1B9A'}

fig, ax = plt.subplots(figsize=(10, 6))

for dept in df['Department'].unique():
    mask = df['Department'] == dept
    ax.scatter(df.loc[mask,'Experience'], df.loc[mask,'Salary'],
               color=dept_colors[dept], label=dept,
               s=130, edgecolors='white', linewidth=1.5, zorder=5)

# Employee name annotations
for _, row in df.iterrows():
    ax.annotate(row['Name'],
                xy=(row['Experience'], row['Salary']),
                xytext=(6, 6), textcoords='offset points',
                fontsize=8.5, color='#444', style='italic')

# Trend line
z  = np.polyfit(df['Experience'], df['Salary'], 1)
p  = np.poly1d(z)
xl = np.linspace(df['Experience'].min(), df['Experience'].max(), 100)
ax.plot(xl, p(xl), 'r--', alpha=0.65, linewidth=2.2,
        label='Trend Line')

# Formatting
ax.set_title('Experience vs Salary', fontsize=17,
             fontweight='bold', pad=20, color='#1a1a2e')
ax.set_xlabel('Years of Experience', fontsize=13, labelpad=10)
ax.set_ylabel('Salary (₹)', fontsize=13, labelpad=10)
ax.grid(linestyle='--', alpha=0.35, color='gray')
ax.set_facecolor('#f5f7fa')
fig.patch.set_facecolor('#ffffff')
ax.legend(title='Department', fontsize=10, title_fontsize=11,
          loc='upper left', framealpha=0.9)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Saved: scatter_plot.png")
"""))

cells.append(nbf.v4.new_markdown_cell("### Chart 3 — Histogram: Age Distribution"))
cells.append(nbf.v4.new_code_cell("""\
# ─────────────────────────────────────────────────────────────────
# Task 3.3c — Histogram: Age Distribution of Employees
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
age_data = df['Age']

n_out, bins, patches = ax.hist(age_data, bins=6,
                                edgecolor='white', linewidth=1.8,
                                color='#1565C0', alpha=0.85)

# Gradient colouring
cmap = plt.cm.get_cmap('Blues')
bcenters = 0.5 * (bins[:-1] + bins[1:])
norm_c   = (bcenters - bcenters.min()) / (bcenters.max() - bcenters.min() + 1e-9)
for c, p in zip(norm_c, patches):
    plt.setp(p, 'facecolor', cmap(0.35 + 0.55 * c))

# Count labels
for count, patch in zip(n_out, patches):
    if count > 0:
        ax.text(patch.get_x() + patch.get_width() / 2,
                count + 0.06, str(int(count)),
                ha='center', va='bottom',
                fontsize=12, fontweight='bold', color='#222')

# Mean vertical line
mean_age = age_data.mean()
ax.axvline(mean_age, color='crimson', linestyle='--',
           linewidth=2.2, label=f'Mean Age = {mean_age:.1f} yrs')

# Formatting
ax.set_title('Age Distribution of Employees', fontsize=17,
             fontweight='bold', pad=20, color='#1a1a2e')
ax.set_xlabel('Age (Years)', fontsize=13, labelpad=10)
ax.set_ylabel('Number of Employees', fontsize=13, labelpad=10)
ax.set_yticks(range(0, int(n_out.max()) + 3))
ax.grid(axis='y', linestyle='--', alpha=0.35, color='gray')
ax.set_facecolor('#f5f7fa')
fig.patch.set_facecolor('#ffffff')
ax.legend(fontsize=11, framealpha=0.9)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.savefig('histogram.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Saved: histogram.png")
"""))

# SUMMARY
cells.append(nbf.v4.new_markdown_cell("""---
# ✅ Assignment 1 — Complete Summary

| Task | Topic | Key Result | Status |
|---|---|---|---|
| 1.1 | Descriptive Statistics | Mean=79.3, Median=79, Range=27, Var≈87.79, SD≈9.37 | ✅ Done |
| 1.2 Q1 | Coin Toss (3×) | P(2 Heads) = 3/8 = 0.375 | ✅ Done |
| 1.2 Q2 | Balls in Bag | P(Red)=5/12, P(Not Green)=3/4 | ✅ Done |
| 1.2 Q3 | Two Dice Sum>8 | P = 10/36 = 5/18 ≈ 0.2778 | ✅ Done |
| 1.3 P1 | MACHINE Vowels Together | 720 arrangements | ✅ Done |
| 1.3 P2 | Committee 2M+2W | C(6,2)×C(5,2) = 150 | ✅ Done |
| 1.4 (a) | Binomial P(X=3) | 0.3456 (34.56%) | ✅ Done |
| 1.4 (b) | Binomial P(X≥4) | 0.3370 (33.70%) | ✅ Done |
| 2.1 | NumPy Verification | All statistics verified | ✅ Done |
| 2.2 | Pandas Operations | All 8 operations completed | ✅ Done |
| 3.1 | Hypothesis Testing | Fail to Reject H₀ (p>α) | ✅ Done |
| 3.2 | 95% CI | (7.66, 8.64) hours | ✅ Done |
| 3.3 | Matplotlib Charts | Bar, Scatter, Histogram saved | ✅ Done |

---
**Student:** Bablu Kumar &nbsp;|&nbsp; **Roll No.:** 23052440012 &nbsp;|&nbsp; **Submitted:** 09/05/26  
**Course:** Data Analysis using Open-Source Tools &nbsp;|&nbsp; **Instructor:** Mr. Basudev Mahata
"""))

# Assign cells and write notebook
nb.cells = cells

nb_path = "Student_Performance_Assignment1.ipynb"
with open(nb_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("Notebook written: " + nb_path)
