import PyPDF2

pdf_file = PyPDF2.PdfFileReader('super.pdf', 'rb')
watermark = PyPDF2.PdfFileReader('wtr.pdf', 'rb')
output = PyPDF2.PdfFileWriter()

for i in range(pdf_file.getNumPages()):
    page = pdf_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('edited.pdf', 'wb') as file1:
        output.write(file1)

       # with open('edited.pdf', 'wb') as new_pdf:
            ##writer = PyPDF2.PdfFileWriter()
           # writer.addPage(merged)
