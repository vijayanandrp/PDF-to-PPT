#!/usr/bin/env python

import os
from PyPDF2 import PdfFileMerger, PdfFileReader

file_names = [ fn for fn in os.listdir(".") if ".pdf" in fn and 'merged' not in fn]

merger = PdfFileMerger()
for fn in file_names:
	merger.append(PdfFileReader(open(fn, 'rb')))
merger.write("merged.pdf")

