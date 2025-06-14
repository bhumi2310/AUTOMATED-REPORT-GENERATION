from fpdf import FPDF 
 
# assume this is the content of your file data = { 
    "Name": "John Doe", 
    "Course": "Python Internship", 
    "Performance": "Excellent", 
    "Completion Date": "31 May 2025" 
} 
 
pdf = FPDF() pdf.add_page() 
pdf.set_font("Arial", size=12) 
 
pdf.cell(200, 10, txt="Internship Report", ln=True, align='C') pdf.ln(10) 
 
for key, value in data.items(): 
    pdf.cell(200, 10, txt=f"{key}: {value}", ln=True) 
 
pdf.output("internship_report.pdf") 
 
 
