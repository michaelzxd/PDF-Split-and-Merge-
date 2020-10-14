import os
import PyPDF2

pdfFiles = []
for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	filename = os.path.splitext(filename)[0]
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	for pageNum in range(0, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
		pageName = filename +  'page' + '-' + str(pageNum+1) + '.pdf'
		pdfOutput = open(pageName, 'wb')
		pdfWriter.write(pdfOutput)
		pdfOutput.close()
