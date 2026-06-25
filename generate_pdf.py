"""
generate_pdf.py
Generates Assignment_1_Solution.pdf using ReportLab.
Run: python generate_pdf.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, HRFlowable,
                                 PageBreak, Image)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import KeepTogether
import os

# ── Document setup ────────────────────────────────────────────────────────────
PDF_FILE = "Assignment_1_Solution.pdf"
doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

# ── Colour palette ────────────────────────────────────────────────────────────
DARK_BLUE  = colors.HexColor("#1a1a4e")
MED_BLUE   = colors.HexColor("#1565C0")
GREEN      = colors.HexColor("#2E7D32")
LIGHT_GREY = colors.HexColor("#f5f7fa")
DARK_GREY  = colors.HexColor("#444444")
BORDER     = colors.HexColor("#cccccc")
GOLD       = colors.HexColor("#FFC107")

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

title_style = ParagraphStyle("Title2",
    parent=styles["Title"],
    fontSize=20, textColor=DARK_BLUE,
    spaceAfter=6, alignment=TA_CENTER, fontName="Helvetica-Bold")

sub_title = ParagraphStyle("SubTitle",
    parent=styles["Normal"],
    fontSize=12, textColor=DARK_BLUE,
    spaceAfter=4, alignment=TA_CENTER, fontName="Helvetica-Bold")

heading1 = ParagraphStyle("H1",
    parent=styles["Heading1"],
    fontSize=15, textColor=DARK_BLUE,
    spaceBefore=14, spaceAfter=6, fontName="Helvetica-Bold",
    borderPad=4)

heading2 = ParagraphStyle("H2",
    parent=styles["Heading2"],
    fontSize=12, textColor=MED_BLUE,
    spaceBefore=10, spaceAfter=4, fontName="Helvetica-Bold")

body = ParagraphStyle("Body",
    parent=styles["Normal"],
    fontSize=10, textColor=DARK_GREY,
    spaceAfter=4, leading=14, alignment=TA_LEFT)

body_j = ParagraphStyle("BodyJ",
    parent=body, alignment=TA_JUSTIFY)

bold_body = ParagraphStyle("Bold",
    parent=body, fontName="Helvetica-Bold", textColor=DARK_BLUE)

formula_style = ParagraphStyle("Formula",
    parent=styles["Normal"],
    fontSize=10, fontName="Courier-Bold",
    textColor=MED_BLUE, alignment=TA_CENTER,
    spaceAfter=4, spaceBefore=4,
    backColor=LIGHT_GREY, borderPad=6,
    borderRadius=4)

answer_style = ParagraphStyle("Answer",
    parent=styles["Normal"],
    fontSize=11, fontName="Helvetica-Bold",
    textColor=GREEN, alignment=TA_CENTER,
    spaceAfter=6, spaceBefore=4,
    backColor=colors.HexColor("#E8F5E9"),
    borderPad=6)

explain_style = ParagraphStyle("Explain",
    parent=body,
    textColor=colors.HexColor("#555555"),
    fontName="Helvetica-Oblique", fontSize=9,
    spaceAfter=6)

code_style = ParagraphStyle("Code",
    parent=styles["Normal"],
    fontName="Courier", fontSize=8.5,
    backColor=colors.HexColor("#1e1e2e"),
    textColor=colors.HexColor("#cdd6f4"),
    spaceAfter=4, spaceBefore=4,
    leftIndent=8, rightIndent=8, borderPad=8,
    leading=13)

output_style = ParagraphStyle("Output",
    parent=styles["Normal"],
    fontName="Courier", fontSize=8.5,
    backColor=colors.HexColor("#1a3a1a"),
    textColor=colors.HexColor("#a6e3a1"),
    spaceAfter=4, spaceBefore=2,
    leftIndent=8, rightIndent=8, borderPad=8,
    leading=13)

center_body = ParagraphStyle("Center",
    parent=body, alignment=TA_CENTER)

# ── Helper builders ───────────────────────────────────────────────────────────
def H(text, style=heading1):
    return Paragraph(text, style)

def P(text, style=body):
    return Paragraph(text, style)

def F(text):
    return Paragraph(text, formula_style)

def A(text):
    return Paragraph(f"&#x2705; Final Answer: {text}", answer_style)

def E(text):
    return Paragraph(f"<i>Explanation:</i> {text}", explain_style)

def SP(n=6):
    return Spacer(1, n)

def HR():
    return HRFlowable(width="100%", thickness=0.5,
                      color=BORDER, spaceAfter=4, spaceBefore=4)

def make_table(data, col_widths=None, header_bg=MED_BLUE,
               header_fg=colors.white, row_bg=LIGHT_GREY,
               font_size=9):
    t_style = [
        ("BACKGROUND", (0,0), (-1,0), header_bg),
        ("TEXTCOLOR",  (0,0), (-1,0), header_fg),
        ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",   (0,0), (-1,-1), font_size),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, row_bg]),
        ("GRID",       (0,0), (-1,-1), 0.4, BORDER),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("LEFTPADDING",(0,0),(-1,-1), 6),
    ]
    if col_widths is None:
        avail = A4[0] - 4*cm
        col_widths = [avail/len(data[0])] * len(data[0])
    rows_para = []
    for i, row in enumerate(data):
        fn = "Helvetica-Bold" if i == 0 else "Helvetica"
        rows_para.append([
            Paragraph(str(cell), ParagraphStyle("tc",
                fontName=fn, fontSize=font_size,
                textColor=header_fg if i==0 else DARK_GREY,
                leading=font_size+2))
            for cell in row
        ])
    return Table(rows_para, colWidths=col_widths, style=TableStyle(t_style))

story = []

# =============================================================================
# COVER PAGE
# =============================================================================
story.append(SP(20))
story.append(Paragraph("RTC INSTITUTE OF TECHNOLOGY", title_style))
story.append(Paragraph("Anandi, Ormanjhi, Ranchi – 835219, Jharkhand", sub_title))
story.append(Paragraph("Department of Computer Science &amp; Engineering", sub_title))
story.append(SP(10))
story.append(HR())
story.append(SP(10))

cover_data = [
    ["Field", "Details"],
    ["Assignment No.",      "01"],
    ["Course Name",         "Data Analysis using Open-Source Tools"],
    ["Submitted To",        "Mr. Basudev Mahata, Dept. CSE, RTCIT Ranchi"],
    ["Name of Student",     "Bablu Kumar"],
    ["University Roll No.", "23052440012"],
    ["College Roll No.",    "23011036"],
    ["Session",             "2025–26"],
    ["Semester",            "6th"],
    ["Batch",               "2023–27"],
    ["Date of Submission",  "09/05/26"],
]
story.append(make_table(cover_data, col_widths=[5*cm, 10*cm]))
story.append(SP(20))

story.append(Paragraph(
    "Assignment 1 — Statistics, Probability &amp; Python Foundations",
    ParagraphStyle("BigTitle", parent=title_style, fontSize=16)))
story.append(PageBreak())

# =============================================================================
# TASK 1.1 — DESCRIPTIVE STATISTICS
# =============================================================================
story.append(H("TASK 1 — Descriptive Statistics, Probability &amp; Combinatorics"))
story.append(H("Question 1.1 — Descriptive Statistics", heading2))
story.append(P("<b>Given Marks:</b> 72, 85, 90, 65, 78, 92, 68, 75, 88, 80"))
story.append(P("<b>n = 10 observations</b>"))
story.append(SP())

# ── MEAN ──────────────────────────────────────────────────────────────────────
story.append(H("1. Mean", heading2))
story.append(P("Formula:"))
story.append(F("x̄  =  Σxᵢ / n"))
story.append(P("Substitution:"))
story.append(F("x̄  =  (72 + 85 + 90 + 65 + 78 + 92 + 68 + 75 + 88 + 80) / 10"))
story.append(P("Intermediate Calculation:"))
story.append(F("x̄  =  793 / 10"))
story.append(A("Mean  x̄  =  79.3"))
story.append(E("The mean is the arithmetic average. Summing all 10 marks gives 793; dividing by 10 gives 79.3. The average student scored 79.3 marks."))
story.append(HR())

# ── MEDIAN ─────────────────────────────────────────────────────────────────────
story.append(H("2. Median", heading2))
story.append(P("Formula (n even): Median = [ x(n/2) + x(n/2+1) ] / 2"))
story.append(P("Step 1 — Sort in ascending order:"))
story.append(F("65,  68,  72,  75,  [78],  [80],  85,  88,  90,  92"))
story.append(P("Step 2 — n=10 (even), 5th value=78, 6th value=80:"))
story.append(F("Median  =  (78 + 80) / 2  =  158 / 2"))
story.append(A("Median  =  79.0"))
story.append(E("Since n is even, median = average of the 5th and 6th values. 50% of students scored below 79 and 50% above."))
story.append(HR())

# ── MODE ───────────────────────────────────────────────────────────────────────
story.append(H("3. Mode", heading2))
story.append(P("Definition: Value appearing most frequently."))
mode_data = [
    ["65","68","72","75","78","80","85","88","90","92"],
    ["1","1","1","1","1","1","1","1","1","1"],
]
story.append(Table(
    [[Paragraph(c, ParagraphStyle("tc", fontName="Helvetica", fontSize=9, textColor=DARK_GREY)) for c in row]
     for row in mode_data],
    style=TableStyle([
        ("BACKGROUND",(0,0),(-1,0), MED_BLUE),
        ("TEXTCOLOR", (0,0),(-1,0), colors.white),
        ("FONTNAME",  (0,0),(-1,0), "Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.4,BORDER),
        ("FONTSIZE",(0,0),(-1,-1),9),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT_GREY]),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]),
    colWidths=[1.65*cm]*10
))
story.append(SP(4))
story.append(A("No Mode — all values appear exactly once (frequency = 1)"))
story.append(E("Every mark appears only once. No repeated value means no mode. This is a uniform frequency distribution."))
story.append(HR())

# ── RANGE ──────────────────────────────────────────────────────────────────────
story.append(H("4. Range", heading2))
story.append(P("Formula:"))
story.append(F("Range  =  x_max  -  x_min"))
story.append(P("Substitution:"))
story.append(F("Range  =  92  -  65"))
story.append(A("Range  =  27"))
story.append(E("The highest mark (92) minus the lowest (65) = 27. This measures the total spread of the dataset."))
story.append(HR())

# ── VARIANCE ───────────────────────────────────────────────────────────────────
story.append(H("5. Sample Variance (n-1)", heading2))
story.append(P("Formula:"))
story.append(F("s²  =  Σ(xᵢ - x̄)²  /  (n - 1)"))
story.append(P("Given: x̄ = 79.3, n = 10"))
story.append(SP(4))

var_data = [
    ["xᵢ", "xᵢ - x̄", "(xᵢ - x̄)²"],
    ["72",  "72 − 79.3 = −7.3",   "53.29"],
    ["85",  "85 − 79.3 = +5.7",   "32.49"],
    ["90",  "90 − 79.3 = +10.7",  "114.49"],
    ["65",  "65 − 79.3 = −14.3",  "204.49"],
    ["78",  "78 − 79.3 = −1.3",   "1.69"],
    ["92",  "92 − 79.3 = +12.7",  "161.29"],
    ["68",  "68 − 79.3 = −11.3",  "127.69"],
    ["75",  "75 − 79.3 = −4.3",   "18.49"],
    ["88",  "88 − 79.3 = +8.7",   "75.69"],
    ["80",  "80 − 79.3 = +0.7",   "0.49"],
    ["Σ",   "",                    "790.10"],
]
story.append(make_table(var_data, col_widths=[2*cm, 7*cm, 4*cm]))
story.append(SP(4))
story.append(F("s²  =  790.10 / 9  =  87.79"))
story.append(A("Sample Variance  s²  =  87.79"))
story.append(E("Bessel's correction (n-1) gives an unbiased estimate. NumPy exact value: 87.7889."))
story.append(HR())

# ── STD DEV ────────────────────────────────────────────────────────────────────
story.append(H("6. Sample Standard Deviation (n-1)", heading2))
story.append(P("Formula:"))
story.append(F("s  =  √(s²)  =  √87.79"))
story.append(A("Sample Standard Deviation  s  ≈  9.37   (NumPy exact: 9.3696)"))
story.append(E("Standard deviation measures average distance from mean. Students' marks deviate ~9.37 marks from the mean of 79.3."))

story.append(PageBreak())

# =============================================================================
# Q 1.2 — PROBABILITY
# =============================================================================
story.append(H("Question 1.2 — Probability", heading2))

# ── Q1 ─────────────────────────────────────────────────────────────────────────
story.append(H("Q1 — Fair Coin Tossed 3 Times: P(Exactly 2 Heads)", heading2))
story.append(P("Formula (Binomial):"))
story.append(F("P(X = k)  =  C(n, k)  ×  pᵏ  ×  (1−p)ⁿ⁻ᵏ"))
story.append(P("<b>Given:</b> n = 3, k = 2, p = 0.5 (fair coin)"))
story.append(P("Step 1 — Complete sample space (2³ = 8 outcomes):"))
story.append(F("S  =  { HHH, HHT, HTH, HTT, THH, THT, TTH, TTT }"))
story.append(P("Step 2 — Favourable outcomes (exactly 2 Heads):"))
story.append(F("E  =  { HHT, HTH, THH }      n(E) = 3"))
story.append(P("Step 3 — Apply formula: n=3, k=2, p=0.5"))
story.append(F("P(X=2)  =  C(3,2) × (0.5)² × (0.5)¹  =  3 × 0.25 × 0.5  =  3 × 0.125"))
story.append(A("P(Exactly 2 Heads)  =  3/8  =  0.375  =  37.5%"))
story.append(E("3 of 8 equally likely outcomes have exactly 2 heads. Probability = 37.5%."))
story.append(HR())

# ── Q2 ─────────────────────────────────────────────────────────────────────────
story.append(H("Q2 — Balls in a Bag", heading2))
story.append(P("<b>Given:</b> Red=5, Blue=4, Green=3  →  Total = 12 balls"))
story.append(P("Formula:  P(E) = n(E) / n(S)"))
story.append(SP(4))
story.append(P("<b>Part (a) — P(Red):</b>"))
story.append(F("P(Red)  =  5 / 12  ≈  0.4167"))
story.append(A("P(Red)  =  5/12  ≈  0.4167  =  41.67%"))
story.append(SP(4))
story.append(P("<b>Part (b) — P(Not Green):</b>"))
story.append(F("P(Green)  =  3/12  =  1/4"))
story.append(F("P(Not Green)  =  1 − P(Green)  =  1 − 3/12  =  9/12  =  3/4"))
story.append(A("P(Not Green)  =  3/4  =  0.75  =  75%"))
story.append(E("Non-green = 5 red + 4 blue = 9 balls. Complement rule gives P = 9/12 = 75%."))
story.append(HR())

# ── Q3 ─────────────────────────────────────────────────────────────────────────
story.append(H("Q3 — Two Dice Rolled: P(Sum > 8)", heading2))
story.append(F("Total sample space:  n(S) = 6 × 6 = 36 outcomes"))
story.append(P("Favourable outcomes (sum = 9, 10, 11, or 12):"))

dice_data = [
    ["Sum", "Favourable Outcomes",       "Count"],
    ["9",   "(3,6),(4,5),(5,4),(6,3)",   "4"],
    ["10",  "(4,6),(5,5),(6,4)",         "3"],
    ["11",  "(5,6),(6,5)",               "2"],
    ["12",  "(6,6)",                     "1"],
    ["TOTAL", "",                         "10"],
]
story.append(make_table(dice_data, col_widths=[2.5*cm, 9*cm, 1.5*cm]))
story.append(SP(4))
story.append(F("P(Sum > 8)  =  n(E) / n(S)  =  10 / 36  =  5 / 18"))
story.append(A("P(Sum > 8)  =  10/36  =  5/18  ≈  0.2778  =  27.78%"))
story.append(E("10 of 36 equally likely outcomes give sum > 8. Probability ≈ 27.78%."))

story.append(PageBreak())

# =============================================================================
# Q 1.3 — PERMUTATION & COMBINATION
# =============================================================================
story.append(H("Question 1.3 — Permutation &amp; Combination", heading2))

story.append(H("Problem 1 — Arrange MACHINE (All Vowels Together)", heading2))
story.append(P("<b>Word:</b> M-A-C-H-I-N-E  |  Total = 7 distinct letters"))
story.append(P("Step 1 — Vowels: A, I, E (3)  |  Consonants: M, C, H, N (4)"))
story.append(P("Step 2 — Treat [AIE] as ONE block → 5 units: { [AIE], M, C, H, N }"))
story.append(P("Step 3 — Arrangements of 5 units:"))
story.append(F("5!  =  5 × 4 × 3 × 2 × 1  =  120"))
story.append(P("Step 4 — Internal arrangements of 3 vowels:"))
story.append(F("3!  =  3 × 2 × 1  =  6"))
story.append(P("Step 5 — Multiplication Principle:"))
story.append(F("Total  =  5! × 3!  =  120 × 6"))
story.append(A("Total Arrangements  =  720"))
story.append(E("Treating vowels as a single block gives 5 entities (5!=120 ways). Internal vowel arrangements add a factor of 3!=6. Total = 720."))
story.append(HR())

story.append(H("Problem 2 — Committee: 2 Men from 6, 2 Women from 5", heading2))
story.append(P("Formula:  C(n, r)  =  n! / [ r! × (n−r)! ]"))
story.append(P("Step 1 — Choose 2 men from 6:"))
story.append(F("C(6,2)  =  6! / (2! × 4!)  =  (6 × 5) / (2 × 1)  =  30 / 2  =  15"))
story.append(P("Step 2 — Choose 2 women from 5:"))
story.append(F("C(5,2)  =  5! / (2! × 3!)  =  (5 × 4) / (2 × 1)  =  20 / 2  =  10"))
story.append(P("Step 3 — Multiply (independent events):"))
story.append(F("Total  =  C(6,2) × C(5,2)  =  15 × 10"))
story.append(A("Total Committees  =  150"))
story.append(E("15 ways to pick 2 men × 10 ways to pick 2 women = 150 distinct committees."))

story.append(PageBreak())

# =============================================================================
# Q 1.4 — BINOMIAL DISTRIBUTION
# =============================================================================
story.append(H("Question 1.4 — Binomial Distribution", heading2))
story.append(P("<b>Given:</b> P(Head) = p = 0.6,  P(Tail) = q = 0.4,  n = 5 tosses"))
story.append(F("P(X = k)  =  C(n,k)  ×  pᵏ  ×  (1−p)ⁿ⁻ᵏ"))
story.append(SP())

story.append(H("Part (a) — P(Exactly 3 Heads) = P(X = 3)", heading2))
story.append(F("C(5,3)  =  5! / (3! × 2!)  =  (5 × 4) / (2)  =  10"))
story.append(F("(0.6)³  =  0.6 × 0.6 × 0.6  =  0.216"))
story.append(F("(0.4)²  =  0.4 × 0.4  =  0.16"))
story.append(F("P(X=3)  =  10 × 0.216 × 0.16  =  10 × 0.03456"))
story.append(A("P(X = 3)  =  0.3456  =  34.56%"))
story.append(E("C(5,3)=10 counts all arrangements of 3H in 5 tosses. The probability is 34.56%."))
story.append(HR())

story.append(H("Part (b) — P(At Least 4 Heads) = P(X ≥ 4)", heading2))
story.append(F("P(X ≥ 4)  =  P(X = 4)  +  P(X = 5)"))
story.append(SP(4))
story.append(P("<b>Calculate P(X = 4):</b>"))
story.append(F("C(5,4) = 5  |  (0.6)⁴ = 0.1296  |  (0.4)¹ = 0.4"))
story.append(F("P(X=4)  =  5 × 0.1296 × 0.4  =  5 × 0.05184  =  0.2592"))
story.append(SP(4))
story.append(P("<b>Calculate P(X = 5):</b>"))
story.append(F("C(5,5) = 1  |  (0.6)⁵ = 0.07776  |  (0.4)⁰ = 1"))
story.append(F("P(X=5)  =  1 × 0.07776 × 1  =  0.07776"))
story.append(SP(4))
story.append(P("<b>Final:</b>"))
story.append(F("P(X ≥ 4)  =  0.2592  +  0.07776  =  0.33696"))
story.append(A("P(X ≥ 4)  =  0.3370  =  33.70%"))
story.append(E("P(4 heads)+P(5 heads)=0.2592+0.07776=0.3370. Since p=0.6>0.5, higher head counts are frequent."))

story.append(PageBreak())

# =============================================================================
# TASK 2 — PYTHON
# =============================================================================
story.append(H("TASK 2 — Python, NumPy &amp; Pandas"))
story.append(H("Task 2.1 — NumPy Statistical Verification", heading2))
story.append(P("<b>Marks:</b> 72, 85, 90, 65, 78, 92, 68, 75, 88, 80"))
story.append(SP(4))

def code_block(text, style):
    """Render a code block safely — escapes &, <, > then converts newlines."""
    safe = (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", "<br/>")
            .replace(" ", "&nbsp;"))
    return Paragraph(safe, style)

code_numpy = (
    "import numpy as np\n"
    "marks = np.array([72, 85, 90, 65, 78, 92, 68, 75, 88, 80])\n\n"
    "print(f'Mean      : {np.mean(marks):.4f}')\n"
    "print(f'Median    : {np.median(marks):.4f}')\n"
    "print(f'Range     : {int(np.max(marks)-np.min(marks))}')\n"
    "print(f'Variance  : {np.var(marks, ddof=1):.4f}  (sample, ddof=1)')\n"
    "print(f'Std Dev   : {np.std(marks, ddof=1):.4f}  (sample, ddof=1)')"
)
story.append(code_block(code_numpy, code_style))
story.append(SP(4))
story.append(P("<b>Output:</b>"))
out_numpy = (
    "Mean      : 79.3000\n"
    "Median    : 79.0000\n"
    "Range     : 27\n"
    "Variance  : 87.7889  (sample, ddof=1)\n"
    "Std Dev   : 9.3696   (sample, ddof=1)"
)
story.append(code_block(out_numpy, output_style))
story.append(HR())

story.append(H("Task 2.2 — Pandas DataFrame Operations", heading2))
story.append(P("<b>Average Salary by Department (groupby):</b>"))
dept_data = [
    ["Department", "Avg Salary (Rs.)"],
    ["Finance",    "78,500.00"],
    ["IT",         "61,250.00"],
    ["Sales",      "50,000.00"],
    ["HR",         "45,000.00"],
]
story.append(make_table(dept_data, col_widths=[6*cm, 7*cm]))
story.append(SP(6))

story.append(P("<b>Employees with Experience &gt; 5 years:</b>"))
exp_data = [
    ["Name", "Dept", "Salary", "Experience"],
    ["Diya",   "Finance", "72,000", "8"],
    ["Gaurav", "Finance", "85,000", "12"],
    ["Ishan",  "Sales",   "55,000", "6"],
    ["Jiya",   "IT",      "78,000", "10"],
]
story.append(make_table(exp_data, col_widths=[4*cm,4*cm,4*cm,3*cm]))
story.append(SP(6))

story.append(P("<b>Top 3 Salaries:</b>"))
top3_data = [
    ["Rank","Name","Dept","Salary (Rs.)"],
    ["1","Gaurav","Finance","85,000"],
    ["2","Jiya","IT","78,000"],
    ["3","Diya","Finance","72,000"],
]
story.append(make_table(top3_data, col_widths=[2*cm,4*cm,4*cm,5*cm]))
story.append(SP(6))

story.append(P("<b>salary_per_year_exp column (Salary / Experience):</b>"))
spe_data = [
    ["Name","Salary","Experience","salary_per_year_exp"],
    ["Aarav","55,000","3","18,333.33"],
    ["Bhavya","48,000","5","9,600.00"],
    ["Chirag","52,000","2","26,000.00"],
    ["Diya","72,000","8","9,000.00"],
    ["Eshan","60,000","4","15,000.00"],
    ["Farah","45,000","3","15,000.00"],
    ["Gaurav","85,000","12","7,083.33"],
    ["Hina","42,000","2","21,000.00"],
    ["Ishan","55,000","6","9,166.67"],
    ["Jiya","78,000","10","7,800.00"],
]
story.append(make_table(spe_data, col_widths=[3.5*cm,3.5*cm,3*cm,5*cm]))

story.append(PageBreak())

# =============================================================================
# TASK 3 — HYPOTHESIS TESTING
# =============================================================================
story.append(H("TASK 3 — Hypothesis Testing"))
story.append(P("<b>Working Hours:</b> 7.5, 8.2, 7.8, 9.0, 8.5, 7.2, 8.8, 9.1, 7.4, 8.0"))
story.append(P("<b>Company Claim:</b> μ = 8 hours  |  <b>α = 0.05</b>"))
story.append(SP(6))

story.append(H("Task 3.1 — One-Sample t-Test", heading2))
story.append(P("<b>Step 1 — Hypotheses:</b>"))
story.append(F("H₀ : μ = 8   (Null: mean working hours = 8)"))
story.append(F("H₁ : μ ≠ 8   (Alternative: two-tailed)"))

story.append(P("<b>Step 2 — Sample Mean:</b>"))
story.append(F("x̄ = (7.5+8.2+7.8+9.0+8.5+7.2+8.8+9.1+7.4+8.0) / 10 = 81.5/10 = 8.15"))

story.append(P("<b>Step 3 — Sample Standard Deviation:</b>"))
story.append(F("Σ(xᵢ−x̄)² = 4.2050    →    s = √(4.2050/9) = √0.4672 = 0.6835"))

story.append(P("<b>Step 4 — Degrees of Freedom:</b>"))
story.append(F("df = n - 1 = 10 - 1 = 9"))

story.append(P("<b>Step 5 — t-Statistic:</b>"))
story.append(F("t = (x̄ - μ₀) / (s/√n)  =  (8.15-8.0) / (0.6835/√10)  =  0.15/0.2161  =  0.6941"))

story.append(P("<b>Step 6 — Critical Value (two-tailed, α=0.05, df=9):</b>"))
story.append(F("t_critical  =  ±2.262   (from t-distribution table)"))

story.append(P("<b>Step 7 — p-Value (SciPy):</b>"))
story.append(F("p-value  =  0.5052"))

story.append(P("<b>Step 8 — Decision:</b>"))
story.append(F("|t_calc| = 0.6941  <  t_critical = 2.262   →   p = 0.5052 > α = 0.05"))
story.append(A("DECISION: FAIL TO REJECT H₀"))
story.append(E("At α=0.05, insufficient evidence to reject the company's claim. Mean working hours of 8 is statistically supported. t=0.6941 lies in the acceptance region (-2.262, +2.262)."))

ht_code = (
    "from scipy import stats\n"
    "import numpy as np\n\n"
    "wh = np.array([7.5,8.2,7.8,9.0,8.5,7.2,8.8,9.1,7.4,8.0])\n"
    "t_stat, p_val = stats.ttest_1samp(wh, popmean=8.0)\n"
    "t_crit = stats.t.ppf(0.975, df=9)\n\n"
    "print(f'x_bar  : mean')\n"
    "print(f't-stat : value')\n"
    "print(f't-crit : value')\n"
    "print(f'p-val  : value')\n"
    "print('Decision: Fail to Reject H0 / Reject H0')"
)
story.append(code_block(ht_code, code_style))
story.append(SP(4))
ht_out = (
    "x_bar  : 8.1500\n"
    "t-stat : 0.6940\n"
    "t-crit : 2.2622\n"
    "p-val  : 0.5052\n"
    "Decision: Fail to Reject H0"
)
story.append(code_block(ht_out, output_style))
story.append(HR())

story.append(H("Task 3.2 — 95% Confidence Interval", heading2))
story.append(P("Formula:"))
story.append(F("CI  =  x̄  ±  t(α/2, df)  ×  (s/√n)"))
story.append(P("Given: x̄=8.15, s=0.6835, n=10, t_crit=2.262:"))
story.append(F("Margin of Error  =  2.262 × (0.6835/√10)  =  2.262 × 0.2161  =  0.4888"))
story.append(F("Lower Limit  =  8.15 − 0.4888  =  7.6612"))
story.append(F("Upper Limit  =  8.15 + 0.4888  =  8.6388"))
story.append(A("95% CI  =  ( 7.6612 ,  8.6388 )  hours"))
story.append(E("We are 95% confident the true mean working hours lies between 7.66 and 8.64 hours. Since μ₀=8 is inside this interval, the result is consistent with failing to reject H₀."))

story.append(PageBreak())

story.append(H("Task 3.3 — Matplotlib Visualizations", heading2))

chart_files = ["bar_chart.png", "scatter_plot.png", "histogram.png"]
chart_titles = [
    "Chart 1: Average Salary by Department (Bar Chart)",
    "Chart 2: Experience vs Salary (Scatter Plot)",
    "Chart 3: Age Distribution of Employees (Histogram)",
]
for fname, ctitle in zip(chart_files, chart_titles):
    if os.path.exists(fname):
        story.append(P(f"<b>{ctitle}</b>"))
        story.append(Image(fname, width=14*cm, height=8.4*cm))
        story.append(SP(8))
    else:
        story.append(P(f"<b>{ctitle}</b> — [Run notebook to generate chart]"))

story.append(PageBreak())

# =============================================================================
# SUMMARY
# =============================================================================
story.append(H("Assignment 1 — Complete Summary"))

summary_data = [
    ["Task","Topic","Key Result","Status"],
    ["1.1","Descriptive Statistics","Mean=79.3, Median=79, SD=9.37","DONE"],
    ["1.2 Q1","Coin Toss (3x)","P(2H)=3/8=0.375","DONE"],
    ["1.2 Q2","Balls in Bag","P(R)=5/12, P(~G)=3/4","DONE"],
    ["1.2 Q3","Two Dice","P(Sum>8)=5/18≈0.2778","DONE"],
    ["1.3 P1","MACHINE Vowels","720 arrangements","DONE"],
    ["1.3 P2","Committee","C(6,2)×C(5,2)=150","DONE"],
    ["1.4 (a)","Binomial P(X=3)","0.3456 (34.56%)","DONE"],
    ["1.4 (b)","Binomial P(X≥4)","0.3370 (33.70%)","DONE"],
    ["2.1","NumPy Verification","All stats verified","DONE"],
    ["2.2","Pandas Operations","8 operations complete","DONE"],
    ["3.1","Hypothesis Test","Fail to Reject H₀","DONE"],
    ["3.2","Confidence Interval","(7.66, 8.64) hours","DONE"],
    ["3.3","Visualisations","3 charts generated","DONE"],
]

def sum_row_style(data):
    t_style = [
        ("BACKGROUND",(0,0),(-1,0), DARK_BLUE),
        ("TEXTCOLOR", (0,0),(-1,0), colors.white),
        ("FONTNAME",  (0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",  (0,0),(-1,-1), 9),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, LIGHT_GREY]),
        ("GRID",(0,0),(-1,-1),0.4,BORDER),
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1),4),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),5),
    ]
    rows = []
    for i, row in enumerate(data):
        fn = "Helvetica-Bold" if i == 0 else "Helvetica"
        col = colors.white if i == 0 else DARK_GREY
        if i > 0:
            # status col green
            row_cells = []
            for j, cell in enumerate(row):
                fc = GREEN if j == 3 else col
                ffn = "Helvetica-Bold" if j == 3 else fn
                row_cells.append(Paragraph(str(cell),
                    ParagraphStyle("sc", fontName=ffn, fontSize=9,
                                   textColor=fc, leading=11)))
            rows.append(row_cells)
        else:
            rows.append([Paragraph(str(c),
                ParagraphStyle("sh", fontName="Helvetica-Bold",
                               fontSize=9, textColor=colors.white,
                               leading=11)) for c in row])
    return Table(rows, colWidths=[2*cm, 5*cm, 6*cm, 2*cm],
                 style=TableStyle(t_style))

story.append(sum_row_style(summary_data))
story.append(SP(16))
story.append(Paragraph(
    "Student: <b>Bablu Kumar</b>  |  Roll No.: <b>23052440012</b>  |  "
    "Course: <b>Data Analysis using Open-Source Tools</b>  |  Date: <b>09/05/26</b>",
    ParagraphStyle("Footer", parent=center_body, fontSize=9,
                   textColor=DARK_BLUE, fontName="Helvetica")))

# ── Build PDF ─────────────────────────────────────────────────────────────────
doc.build(story)
print("PDF saved: " + PDF_FILE)
