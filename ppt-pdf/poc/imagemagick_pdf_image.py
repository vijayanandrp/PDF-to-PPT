#!/usr/bin/env python

"""
Source: http://www.xavierdupre.fr/blog/2014-03-12_nojs.html
"""

from PythonMagick import Image
import PythonMagick
import os

# os.environ["MAGICK_HOME"] = r'path_to_ImageMagick'

pdf_file = '17d_attrition.pdf'
to = pdf_file.replace('pdf', 'jpg')

p = PythonMagick.Image()
p.density('400')
p.read(os.path.abspath(pdf_file))
p.write(os.path.abspath(to))


# We also can convert image file into pdf
