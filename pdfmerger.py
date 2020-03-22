import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_lists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lists:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('tilted.pdf', 'wb') as new_file:
        writer.write(new_file)