"""Builds Yue_Liu_CV.pdf (the one-page CV linked from the site). Needs: pip install reportlab
Run from anywhere: python3 tools/make_cv.py
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import black, HexColor
from reportlab.platypus.flowables import HRFlowable

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Yue_Liu_CV.pdf")
F, FB = "Times-Roman", "Times-Bold"
base = ParagraphStyle("b", fontName=F, fontSize=10, leading=11.8)
name = ParagraphStyle("n", fontName=FB, fontSize=18, leading=21, alignment=TA_CENTER)
contact = ParagraphStyle("c", parent=base, alignment=TA_CENTER)
sec = ParagraphStyle("s", fontName=FB, fontSize=11.5, leading=13, spaceBefore=5)
bullet = ParagraphStyle("bl", parent=base, leftIndent=10, firstLineIndent=-7)
right = ParagraphStyle("r", parent=base, alignment=2)
TODO = HexColor("#C00000")

story = []
def S(t):
    story.append(Paragraph(t, sec))
    story.append(HRFlowable(width="100%", thickness=0.6, color=black, spaceBefore=1, spaceAfter=2))
def row(left, r):
    t = Table([[Paragraph(left, base), Paragraph(r, right)]], colWidths=[6.0*72, 1.5*72])
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                           ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    story.append(t)
def P(t): story.append(Paragraph(t, base))
def B(t): story.append(Paragraph("• " + t, bullet))
def todo(t): return f'<font color="#C00000">[{t}]</font>'

story.append(Paragraph("Yue LIU", name))
story.append(Paragraph("abacixzs@gmail.com | github.com/Youngwing-0314 | youngwing-0314.github.io", contact))

S("SUMMARY")
P("Computer Engineering master's student at NYU Tandon seeking a research position in robot perception and robot learning. "
  "Hands-on experience integrating real-time perception with control on a Raspberry Pi mobile robot and a 6-DoF manipulator, "
  "OCR text detection research under class imbalance, and embedded systems under tight compute constraints. "
  "Interested in perception-driven robot learning and vision-language-action models for embodied navigation and manipulation.")

S("EDUCATION")
row("<b>New York University, Tandon School of Engineering</b>", "Brooklyn, NY")
row("Master of Science in Computer Engineering", "Expected May 2028")
P("<b>Current Coursework:</b> Machine Learning, Computing Systems Architecture, Data Structures and Algorithms.")
row("<b>Northern Kentucky University / Hubei Polytechnic University</b>", "Aug 2022 - May 2026")
P("Bachelor of Electrical and Electronics Engineering Technology | 2+2 Joint Program | GPA: 3.52/4.0")
P("Cum Laude; Dean's Scholarship (top 5%, 2024); Scholar's List (2025)")

S("RESEARCH AND ROBOTICS PROJECTS")
row("<b>Raspberry Pi Obstacle-Avoidance Car</b> | NKU Capstone | Advisor: Dr. Gang Sun", "Nov 2025 - May 2026")
B("Closed the loop from perception to control on a Raspberry Pi 5; mitigated latency and reduced false positives on reflective surfaces.")
B("Profiled the pipeline, removed redundant image copies, switched to a lighter detector, and synchronized processing with actuation.")
B("Added runtime health checks (FPS, queue length, control latency) and tuned actuation to avoid low-speed oscillation; completed a short outdoor route without intervention, with fewer false stops across lighting changes. Added voice control for spoken commands.")
row("<b>6-DoF Robotic Arm Pick-and-Place Automation</b> | NKU | Advisor: Prof. Shin", "Jan 2026 - May 2026")
B("Programmed a Hiwonder 6-DoF arm to pick objects and place them at predefined coordinates to form a multi-piece arrangement.")
B("Tuned servo sequences, gripper opening, arm height, rotation, and timing; demonstrated repeated automated pick-and-place cycles on video.")
row("<b>OCR Text Detection for Less-Common Languages</b> | Jinan University | Advisor: Prof. Longxin Lin", "Aug 2025 - Nov 2025")
B("Tackled irreproducible results and weak tail classes caused by class imbalance and limited data; standardized preprocessing and training configs, then built a clean baseline and a controlled second architecture.")
B("Added targeted sampling and augmentation with per-class metrics; tracked F1 on low-frequency symbols and stress-tested distribution shift (noisy scans, varied resolution).")
B("Achieved consistent reruns and improved rare-class performance while keeping on-device latency feasible.")

S("PUBLICATIONS")
P("<b>Multitask Attention-Based Approach for Efficient Offloading and Resource Allocation in Wireless Powered MEC Networks</b>")
P("Third author | Manuscript submitted to IEEE Sensors Journal, Sep 2025")
B("Worked on an attention-enhanced multitask network with a shared encoder, task-specific heads, and adaptive masking to jointly learn offloading and resource allocation; achieved near-optimal rates with low inference latency.")
P("<b>Coupled Physical Field Simulation based on COMSOL</b> | First author, Proceedings of ICMEEA 2024")
B("Built COMSOL and MATLAB models of silicon under bending, elongation, and torsion to analyze coupled mechanical-electrical responses.")

S("PROFESSIONAL EXPERIENCE")
row("<b>Super Telecom Co., Ltd</b> | Embedded System Engineer | Shenzhen, China", "Jun 2025 - Aug 2025")
B("Built BMS device-to-cloud telemetry and cloud-to-device command paths over cellular under CPU/RAM constraints and intermittent connectivity.")
B("Modularized I/O, MQTT messaging, and command execution; created a one-command build/deploy workflow with developer documentation.")

S("TECHNICAL SKILLS")
P("<b>Programming:</b> Python, C, MATLAB, NumPy, pandas, scikit-learn")
P("<b>Machine Learning / Vision:</b> YOLO / Mamba-YOLO, CRNN-CTC, attention recognizers, TensorFlow Lite, quantization, pruning")
P("<b>Robotics and Embedded:</b> Raspberry Pi, servo-actuated manipulators, MSP430 (register-level C), Code Composer Studio, MQTT, COMSOL")

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.5*72, rightMargin=0.5*72, topMargin=0.45*72, bottomMargin=0.4*72)
doc.build(story)
print(OUT)
