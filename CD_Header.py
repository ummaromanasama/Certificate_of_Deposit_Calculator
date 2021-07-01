from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

pdf = canvas.Canvas("CD_Header.pdf")
pdf.setTitle('CD Header')
pdf.setPageSize((700, 500))

pdf.setFont("Helvetica", 12)
pdf.drawString(100, 450, 'Jane Doe')
pdf.drawString(100, 438, 'jane.doe@gmail.com')
pdf.drawString(100, 425, '121-11 103 Ave, Maple street, NY 12124')

pdf.drawString(400, 450, 'Capital One')
pdf.drawString(400, 438, 'Capital.One@gmail.com')
pdf.drawString(400, 425, '341-01 45 Ave, Sky street, NJ 16933')

# pdf.translate(600, 690)
pdf.rect(.5*inch,5.8*inch,8.8*inch,.005*inch, fill=1)

pdf.save()