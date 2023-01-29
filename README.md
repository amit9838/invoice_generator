# Automate your invoice with python

Automatically generate print friendly invoices/bills using python. [Sample pdf](https://github.com/amit9838/invoice_generator/blob/master/sample_invoice.pdf)

<img title="" src="https://github.com/amit9838/invoice_generator/blob/master/Screenshot/sample_invoice.png" alt="" width="724" style = "border-radius:5px;">

# 

---

### Directions to use

-----

Step 1 - Clone the repo or download the archive to you local system. Now head to "invoice_genarator"  directory.

Step 2 - Install "reportlab" and "pillow" with following commands:

Run these commands in your terminal -

`pip install reportlab`

`pip install pillow`

or simply run

`pip install requirements.txt`

Step 3 - Now feed the data into the pdf.py file in array format.

That's it

### Working

--------

Data is converted into objects for simplicity.

```python
# Sample Data 
item = ['Dell Keboard Wireless', 'Samsung RAM 4GB','Samsung SSD 480GB']
warrenty=[12,24,36]  # in months
unit_price = [700, 2400,4860]
qty = [1,2,1]
tax = [0,.18,.18]

objects = []
class Product:
    def __init__(self,item,warrenty,unit_price,tax,quantity):
        self.item = item
        self.unit_price = unit_price
        self.warrenty = warrenty
        self.tax = tax
        self.quantity = quantity
        self.t_price = unit_price*quantity
```

Some useful offsets for repositioning of elements.

```python
# Y offsets - Global
y_offset = 0   # Header section (above Invoice,company) 
cust_offset = 50 #Customer section
table_offset = 0   #Table section
sub_total_y_offset = -5  # Subtotal/total section offset

# x-offsets in the table
unit_price_x_pos = 370  #Default 370
warrenty_x_pos = 280  #Default 280
qty_x_pos = 470  #Default 470
price_x_pos = 550  #Default 550

# y-offset for new entries is dynamically calculated.
```

### Reference

-------------

For in-depth usage visit  [Documentation](https://docs.reportlab.com/reportlab/userguide/ch1_intro/)  or for some extra recipies visit [More](https://www.reportlab.com/dev/docs/).
