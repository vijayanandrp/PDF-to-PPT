#!/usr/bin/env python


import glob
from PyPDF2 import PdfFileWriter, PdfFileReader


input_pdf = PdfFileReader(file('merged.pdf', 'rb'))

for i in range(input_pdf.numPages):
	output = PdfFileWriter()
	output.addPage(input_pdf.getPage(i))
	
	# new filename
	new_name = str(i)+'_new.pdf'
	file_stream = file(new_name, 'wb')
	output.write(file_stream)
	file_stream.close()
	
