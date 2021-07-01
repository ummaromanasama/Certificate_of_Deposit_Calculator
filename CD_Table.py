from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

# Generate invoice
fileName = ('CD_Table.pdf')

pdf = SimpleDocTemplate(
    fileName,
    pagesize = (700, 500)
    
)

#Lists of lists
data = [
    ['CD Term', 'APY', 'Total Earnings'],
    ['6 Month CD', '0.10%', '$0',],
    ['9 Month CD', '0.10%', '$0',],
    ['12 Month CD', '0.20%', '$1',],
    ['18 Month CD', '0.25%', '$3',],
    ['24 Month CD', '0.25%', '$5',],
    ['30 Month CD', '0.25%', '$6',],
    ['36 Month CD', '0.30%', '$9',],
    ['48 Month CD', '0.35%', '$14',],
    ['60 Month CD', '0.40%', '$20',],
]

table = Table(data)

#Add style
style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.green),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige)
])
table.setStyle(style)

#Alternate background colors
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 ==0:
        bc = colors.burlywood
    else:
        bc = colors.beige
    ts = TableStyle(
        [('BACKGROUND', (0,i), (-1,i), bc)]
    )
    table.setStyle(ts)

#Add borders
ts = TableStyle(
        [
            ('BOX', (0,0), (-1,-1), 2, colors.black),
            ('GRID', (0,1), (-1,-1), 2, colors.black)
        ]
    )
table.setStyle(ts)


elems = []
elems.append(table)

pdf.build(elems)