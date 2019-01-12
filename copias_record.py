#! python3
# copias_record.py - convierte una carpeta de PDFs en un archivo PDF con la marca de agua de la CR

import PyPDF2, os, sys

#cambio CWD para usar las carpetas helper que vienen en el paquete
os.chdir(os.path.dirname(sys.argv[0]))
formato = input('Introduzca formato (A1, A3, A4): ')
pdfWatermarkReader = PyPDF2.PdfFileReader(open('.\\watermark\\watermark_%s.pdf' % (formato), 'rb'))

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.\\pdfs'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    print(filename)
    pdfFileObj = open('.\\pdfs\\' + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages and add them with the watermark.
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pageObj.mergePage(pdfWatermarkReader.getPage(0))
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
name_file = '.\\copia_record\\' + str(input('Nombre del archivo: ')) + '.pdf'
pdfOutput = open(name_file, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
