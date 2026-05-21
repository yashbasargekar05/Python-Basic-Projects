from pathlib import Path

from PyPDF2 import PdfMerger


script_folder = Path(__file__).parent
merger = PdfMerger()
pdfs = []

try:
    n = int(input("Enter the number of PDFs you want to merge: "))
except ValueError:
    print("Please enter a valid number.")
    raise SystemExit

for i in range(n):
    name = input(f"Enter the name of PDF {i + 1}: ").strip().strip('"')

    pdf_path = Path(name)
    if pdf_path.suffix.lower() != ".pdf":
        pdf_path = pdf_path.with_suffix(".pdf")

    if not pdf_path.is_absolute():
        pdf_path = script_folder / pdf_path

    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        print("Put the PDF in the same folder as this script or enter the full path.")
        raise SystemExit

    pdfs.append(pdf_path)

for pdf in pdfs:
    merger.append(str(pdf))

output_file = script_folder / "merged-pdf.pdf"
merger.write(str(output_file))
merger.close()

print(f"PDFs merged successfully: {output_file}")
