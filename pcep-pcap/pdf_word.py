from pypdf import PdfReader
import docx

# Load the PDF file
pdf_path = "C:\\Users\\r.fermanelli\\Desktop\\pcep\\pcep..exam.simulation\\R. Karamagi.pdf"
pdf_reader = PdfReader(pdf_path)

# Create a new Word document
doc = docx.Document()

# Read each page from the PDF and add to the Word document
for page in pdf_reader.pages:
    text = page.extract_text()
    doc.add_paragraph(text)

# Save the Word document
word_path = "C:\\Users\\r.fermanelli\\Downloads\\R. Karamagi.docx"
doc.save(word_path)

print(word_path)
