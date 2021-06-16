from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table

#----------------------------------CD Information--------------------------------------
# # Input the deposit amount
# year = int(input('Enter the intial year of the CD account: '))

# # Input the deposit amount
# amount = int(input('Enter the deposit amount: '))

# # Input the annual interest rate.
# annual_interest_rate = float(input('Enter the annual interest rate (%): '))
# annual_interest_rate /= 100

# # Input number of years account will earn interest.
# time = int(input('Enter how many years the account will accrue interest: '))
# year += time

# # The compund rate is monthly.
# compound = 12

# # # Calculate the total amount
# total_amount = (amount * (1 + annual_interest_rate/ compound) ** (compound * time))
# total_intrest = total_amount - amount

# # Display the total amount.
# print('At the end of', year,'you will have $',format(total_amount, '.2f'))
# print('The total amount of interest accumulated is $',format(total_intrest, '.2f'))

# Generate invoice
pdf = canvas.Canvas("CD_Invoice_2021.pdf")
pdf.setTitle('Certificate Deposit')
pdf.setPageSize((700, 500))

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')    

drawMyRuler(pdf)

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
