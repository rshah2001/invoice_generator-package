import os

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, company_logo, column1, column2, column3, column4, column5):
    # glob.glob will return all file paths that match a specific pattern
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        # excels have multiple sheets in one document so having the sheet name is mandatory
        df = pd.read_excel(filepath, sheet_name="Sheet 1")

        # P stands for portrait
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_nr, invoice_date = filename.split("-")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=50, h=8, txt=f"Date: {invoice_date}", ln=1)

        # Header
        columns = df.columns
        columns = [item.replace("_", " ").title() for item in columns]
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=30, h=8, txt=columns[0], border=1)
        pdf.cell(w=70, h=8, txt=columns[1], border=1)
        pdf.cell(w=30, h=8, txt=columns[2], border=1)
        pdf.cell(w=30, h=8, txt=columns[3], border=1)
        pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

        # Adding rows to the table
        for index, row in df.iterrows():
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[column1]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[column2]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[column3]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[column4]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[column5]), border=1, ln=1)

        total_sum = df["total_price"].sum()
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

        # add total sum sentence
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=30, h=8, txt=f"The total Price is {total_sum}", ln=1)

        # Add company name and logo
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=30, h=8, txt=f"Rishil Shah")
        pdf.image(company_logo, w=10)

        # Output file
        os.makedirs((pdfs_path))
        pdf.output(f"{pdfs_path}/{filename}.pdf")
