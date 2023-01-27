from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

#NOTE:  Canvas methods only support UTF-8 characters therefore each data must be converted to string while passing to function/method. 

# Sample Data 
item = ['Dell Keboard Wireless', 'Samsung RAM 4GB','Samsung SSD 480GB']
warrenty=[12,24,36]  # in months
unit_price = [700, 2400,4860]
qty = [1,2,1]
tax = [0,.18,.18]


discount = 100  # If no disount is applicabe,  put 'discount = 0'
service_charge = 500   # If no service charge is applicabe,  put 'discount = 0'

# Store data in object for simplicity
objects = []
class Product:
    def __init__(self,item,warrenty,unit_price,tax,quantity):
        self.item = item
        self.unit_price = unit_price
        self.warrenty = warrenty
        self.tax = tax
        self.quantity = quantity
        self.t_price = unit_price*quantity
        
# Append object containing data into objects array
for x in range(len(item)):
    obj = Product(item[x],warrenty[x],unit_price[x],tax[x],qty[x])
    objects.append(obj);


# Y offsets
y_offset = 0   # Header section (above Invoice,company)
cust_offset = 50 #Customer section offset
table_offset = 0   #Table section offset


# initializing variables with values
fileName = 'sample_invoice.pdf'
documentTitle = 'Sample Invoice'
title = 'Technology'
subTitle = 'The largest thing now!!'

# Create pdf canvas 
pdf = canvas.Canvas(fileName)
pdf.setTitle(title)

# Start font-formating  
pdf.setFont("Helvetica-Bold", 36)
pdf.setFillColorRGB(.3,.3,.3)  # Start Font Color 
pdf.drawString(40,(735-y_offset), "INVOICE")
pdf.setFont("Helvetica", 13)   # Now Resume Default Font-Formatting
pdf.setFillColorRGB(0,0,0)  # Resume font color (black, zero-illumination) 

pdf.drawRightString(550,(750-y_offset), "The New Square")
pdf.drawRightString(550,(730-y_offset), "Delhi,India")
pdf.drawRightString(550,(710-y_offset), "support@square.in")
pdf.drawRightString(550,(690-y_offset), "+9180xxxxxxxx")

# Offset between complany and customer section
y_offset = y_offset + cust_offset

# Customer Section - left
pdf.setFont("Helvetica-Bold", 13)
pdf.drawString(40,(680-y_offset), "Billed To:")
pdf.setFont("Helvetica", 13)
pdf.drawString(40,(660-y_offset), "James Bond")
# pdf.drawString(40,(640-y_offset), "amitchaudhary0539@gmail.com")
pdf.drawString(40,(640-y_offset), "+9197xxxxxxxx")
pdf.drawString(40,(620-y_offset), "Bansi,Siddharthnagar")

# Customer Section - right
pdf.drawRightString(550,(660-y_offset), "Invoice : #123")
pdf.drawRightString(550,(640-y_offset), "Issued on : Jan 1, 2020")
pdf.drawRightString(550,(620-y_offset), "Status : Repaired")

y_offset = y_offset + table_offset
# Items list header

unit_price_x_pos = 370  #Default 325
warrenty_x_pos = 280  #Default 325
qty_x_pos = 470  #Default 450
price_x_pos = 550  #Default 550

pdf.setFont("Helvetica-Bold", 12)
pdf.setLineWidth(.2)
pdf.line(40,(600-y_offset),550,(600-y_offset))
pdf.drawString(40,585-y_offset, "Item")
pdf.drawString(warrenty_x_pos,585-y_offset, "Warrenty")
pdf.line(40,(580-y_offset),550,(580-y_offset))
# pdf.drawString(100,585, "Description")
pdf.drawString(unit_price_x_pos,(585-y_offset), "Unit Price")
pdf.drawCentredString(qty_x_pos,(585-y_offset), "Qty")
pdf.drawRightString(price_x_pos,(585-y_offset), "Price")
pdf.setFont("Helvetica", 13)
# text = pdf.beginText(40, 680)


# Calculate total cost of a product -> Unit_price * quantity * tax_amt  


i=0;
for i in range(len(objects)):
    pdf.drawString(40,(565-y_offset-20*i), objects[i].item)
    if objects[i].warrenty: # If there is any warrenty of the product
        pdf.drawString(warrenty_x_pos,(565-y_offset-20*i), str(objects[i].warrenty))
        pdf.setFont("Helvetica", 10)
        pdf.drawString(warrenty_x_pos+18,(565-y_offset-20*i), "Months")
        pdf.setFont("Helvetica", 13)
  
    pdf.drawRightString(unit_price_x_pos+40,(565-y_offset-20*i), str(objects[i].unit_price)+".0")
    if(objects[i].tax):
        pdf.setFont("Helvetica", 10)
        pdf.drawString(unit_price_x_pos+45,(565-y_offset-20*i), "+Tax")
        pdf.setFont("Helvetica", 13)
    pdf.drawString(qty_x_pos,(565-y_offset-20*i), str(objects[i].quantity))
    pdf.drawRightString(price_x_pos,(565-y_offset-20*i), str(objects[i].t_price * objects[i].quantity)+".0")


# Calculate total tax
total_tax=0;
for i in range(len(objects)):
    if(objects[i].tax):
        total_tax += objects[i].t_price*objects[i].tax

# Calculate Sub total
sub_total = 0
for i in range(len(objects)):
    sub_total += objects[i].t_price
    


# Calculate Gross Total
labels_x_pos = 480

pdf.line(40,(565-y_offset-20*i-5),556,(565-y_offset-20*i-5))
y_offset = y_offset-5 #  Gross total offset
pdf.drawRightString(labels_x_pos,(565-y_offset-20*i-25),  "Sub Total : ")
pdf.drawRightString(550,(565-y_offset-20*i-25),str(sub_total)+".0")

pdf.drawRightString(labels_x_pos,(565-y_offset-20*i-40), "Tax : ")
pdf.drawRightString(550,(565-y_offset-20*i-40),"+ "+str(total_tax))


if(service_charge):  # If service charge is applicable
    y_offset = y_offset+10 # Service Charge offset
    pdf.drawRightString(labels_x_pos,(565-y_offset-20*i-45), "Service Charge : ")
    pdf.drawRightString(550,(565-y_offset-20*i-45), "+ "+str(service_charge)+".0")
    y_offset = y_offset+5 # Service Charge offset


if(discount):  # I any discount is applicable 
    y_offset = y_offset+10 # discount Charge offset
    pdf.drawRightString(labels_x_pos,(565-y_offset-20*i-45), "Discount : ")
    pdf.drawRightString(550,(565-y_offset-20*i-45), "- "+str(discount)+".0")
    y_offset = y_offset+5 # Service Charge offset


pdf.line(380,(565-y_offset-20*i-45),556,(565-y_offset-20*i-45))
pdf.setFont("Helvetica-Bold", 15)
pdf.drawRightString(labels_x_pos,(565-y_offset-20*i-63), "Total : ")
pdf.drawRightString(550,(565-y_offset-20*i-63), str(sub_total+total_tax+service_charge-discount))
pdf.line(380,(565-y_offset-20*i-70),556,(565-y_offset-20*i-70))
pdf.setFont("Helvetica", 13)

pdf.drawString(40,(505-y_offset-20*i), "Thanks for visiting")

pdf.save()