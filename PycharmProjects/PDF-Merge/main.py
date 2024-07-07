# import PyPDF2
#
# pdfile = ['1.pdf.pdf','2.pdf.pdf']
#
# merger = PyPDF2.PdfMerger()
# for filename in pdfile:
#     pdfFile = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfReader(pdfFile)
#     merger.append(pdfReader)
#
# pdfFile.close()
# merger.write('merged.pdf')



import PyPDF2

pdfile = ['1.pdf.pdf','2.pdf.pdf']

merger = PyPDF2.PdfMerger()
for filename in pdfile:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')
