#!/usr/bin/env python

"""
For more inforamtion read doc here -
http://docs.wand-py.org/en/0.4.2/
"""
from wand.image import Image

with Image(filename='17d_attrition.pdf', resolution=400) as img:
	img.compression_quality = 99
	img.save(filename="op1.jpg")

#resizing this image 
with Image(filename="op1.jpg") as img:
	img.resize(200, 150)
	img.save(filename="op_thumb.jpg")


# response = PDFTemplateResponse(request, template='reports/report_email.html', filename='17d_attrition.pdf', context=render_data, cmd_options={"load-error-handling":"ignore"})



