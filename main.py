from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4") #height:297 width:210
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

#creating a pages for every topic,
#the number of pages per topic is assigned in the "pages" column.
for index, row in df.iterrows():
    for i in range(row["Pages"]): #this is a nested 'for' loop
        #Setting the header:
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=21)
        pdf.set_text_color(100,100,150) #setting color: light blue
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
        pdf.set_line_width(1)
        pdf.set_draw_color(100,100,150)
        pdf.line(10, 21, 200, 21)

        #Setting the footer:
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 230)
        pdf.cell(w=0, h=12, txt=.0row["Topic"], align="R", ln=1, border=0)




pdf.output("output.pdf")

