from tkinter import *


# Functionality Part
def employee_form():
    global back_image
    employee_frame = Frame(window, width=1070, height=567, bg='white')
    employee_frame.place(x=200, y=100)
    headingLabel = Label(employee_frame, text='Manage Employee Details ', font=('times new roman', 16, 'bold'),
                         bg='#0f4d7d', fg='white')
    headingLabel.place(x=0, y=0, relwidth=1)
    back_image = PhotoImage(file='Back_image.png')
    back_button = Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                         command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    topFrame = Frame(employee_frame, bg='white')
    topFrame.place(x=0, y=60, relwidth=1, height=235)
    search_frame = Frame(topFrame)
    search_frame.pack()


'''GUI part  '''
# Object of TK class
window = Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0, 0)
window.config(bg='white')

''' Inventory Management System ( Main Heading or Title ) '''
# For Title ( Heading Title )
bg_image = PhotoImage(file='inventory.png')
tittleLabel = Label(window, image=bg_image, compound=LEFT, text=' Inventory Management System',
                    font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
tittleLabel.place(x=0, y=0, relwidth=1)
# Creating laGout Button
logoutButton = Button(window, text='Logout', font=('times new roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

''' Subtitle of the Inventory Management System '''
# Subtitle Label
subtitleLabel = Label(window, text='Welcome Admin\t\t Date : 18-03-2025\t\t Time : 1.32 pm',
                      font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)


'''==> For Left Side Bar Create a frame <===='''
# For Left Frame
leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=555)

# For Left Frame Image
LogoImage = PhotoImage(file='logo.png')
# Creating an Image Label --> for placing this into Left Frame or [ Putting this Image into Left Frame ]
imageLabel = Label(leftFrame, image=LogoImage)
# Pack method ---> I use Pack Method to place thw thing one below one
imageLabel.pack()

# For Menu
manuLabel = Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
manuLabel.pack(fill=X)

'''==> For Employees <===== ## This is Something I am placing a PNG image under the Employees Button ##'''
# Employee Image ==> this is PNG image attaching way
employee_image = PhotoImage(file='emloyee.png')
# for Employee Button
employee_button = Button(leftFrame, image=employee_image, compound=LEFT, text=' Employees',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10, command=employee_form)
employee_button.pack(fill=X)


'''==> For Suppliers <===== ## This is Something I am placing a PNG image under the Employees Button ##'''
# Supply Image ==> this is PNG image attaching way
supply_image = PhotoImage(file='supplier.png')
# For Supplier Button
suppler_button = Button(leftFrame, image=supply_image, compound=LEFT, text=' Suppliers',
                        font=('times new roman', 20, 'bold'), anchor='w', padx=10)
suppler_button.pack(fill=X)

'''==> For Category  <===== ## This is Something I am placing a PNG image under the Employees Button ##'''
# Category==> this is PNG image attaching way
category_image = PhotoImage(file='catagories.png')
# For Categories Button
categories_button = Button(leftFrame, image=category_image, compound=LEFT, text=' Categories',
                           font=('times new roman', 20, 'bold'), anchor='w', padx=10)
categories_button.pack(fill=X)

'''==> For Products <===== ## This is Something I am placing a PNG image under the Employees Button ##'''
# products ==> this is PNG image attaching way
product_image = PhotoImage(file='product.png')
# For product Button
product_button = Button(leftFrame, image=product_image, compound=LEFT, text=' Products',
                        font=('times new roman', 20, 'bold'), anchor='w', padx=10)
product_button.pack(fill=X)

'''==> For Sales <===== ## This is Something I am placing a PNG image under the Employees Button ##'''
# Sales==> this is PNG image attaching way
Sales_image = PhotoImage(file='sales.png')
# For Sales Button
sales_button = Button(leftFrame, image=Sales_image, compound=LEFT, text=' Sales', font=('times new roman', 20, 'bold'),
                      anchor='w', padx=10)
sales_button.pack(fill=X)

# Exit==> this is PNG image attach way
Exit_image = PhotoImage(file='exit.png')
# For Exit Button
exit_button = Button(leftFrame, image=Exit_image, compound=LEFT, text=' Exit', font=('times new roman', 20, 'bold'),
                     anchor='w', padx=10)
exit_button.pack(fill=X)


'''===>  For Total Employees  <========= '''
emp_frame = Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, height=170, width=280)
total_emp_image = PhotoImage(file='totalemployees.png')
total_emp_label = Label(emp_frame, image=total_emp_image, bg='#2C3E50')
total_emp_label.pack(pady=10)

# For Total Employees text
total_emp_label_text = Label(emp_frame, text='Total Employees', bg='#2C3E50', fg='white',
                             font=('times new roman', 15, 'bold'))
total_emp_label_text.pack()

# For Showing the Total Employees is Zero Initially
total_emp_count_label = Label(emp_frame, text='0', bg='#2C3E50', fg='white', font=('times new roman', 30, 'bold'))
total_emp_count_label.pack()

'''===>  For Total Suppliers <===========  '''
sup_frame = Frame(window, bg='#8E44AD', bd=3, relief=RIDGE)
sup_frame.place(x=800, y=125, height=170, width=280)
total_sup_image = PhotoImage(file='totalsuppliers.png')
total_sup_label = Label(sup_frame, image=total_sup_image, bg='#8E44AD')
total_sup_label.pack(pady=10)

# for total Employees Test
total_sup_label_text = Label(sup_frame, text='Total Employees', bg='#8E44AD', fg='white',
                             font=('times new roman', 15, 'bold'))
total_sup_label_text.pack()

# For Showing total Employees is Zero Initially
total_sup_count_label = Label(sup_frame, text='0', bg='#8E44AD', fg='white', font=('times new roman', 30, 'bold'))
total_sup_count_label.pack()

'''====>  For Total Categories <=========  '''
cat_frame = Frame(window, bg='#27AE60', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, height=170, width=280)
total_cat_image = PhotoImage(file='totalcategories.png')
total_cat_label = Label(cat_frame, image=total_cat_image, bg='#27AE60')
total_cat_label.pack(pady=10)

# For Total Category Test
total_cat_label_text = Label(cat_frame, text='Total Categories', bg='#27AE60', fg='white',
                             font=('times new roman', 15, 'bold'))
total_cat_label_text.pack()

# For Showing total Category is Zero initially
total_cat_count_label = Label(cat_frame, text='0', bg='#27AE60', fg='white', font=('times new roman', 30, 'bold'))
total_cat_count_label.pack()

'''====> For Total products <=====  '''
prod_frame = Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
prod_frame.place(x=800, y=310, height=170, width=280)
total_prod_image = PhotoImage(file='totalproducts.png')
total_prod_label = Label(prod_frame, image=total_prod_image, bg='#2C3E50')
total_prod_label.pack(pady=10)

# For Total Product Text
total_prod_label_text = Label(prod_frame, text='Total Products', bg='#2C3E50', fg='white',
                              font=('times new roman', 15, 'bold'))
total_prod_label_text.pack()

# For Showing Total Products is Zero Initially
total_prod_count_label = Label(prod_frame, text='0', bg='#2C3E50', fg='white', font=('times new roman', 30, 'bold'))
total_prod_count_label.pack()

''' ===> For Total Sales <======  '''
sales_frame = Frame(window, bg='#E74C3C', bd=3, relief=RIDGE)
sales_frame.place(x=600, y=495, height=170, width=280)
total_sales_image = PhotoImage(file='totalSales.png')
total_sales_label = Label(sales_frame, image=total_sales_image, bg='#E74C3C')
total_sales_label.pack(pady=10)

# For Total Sales Text
total_sales_label_text = Label(sales_frame, text='Total Sales', bg='#E74C3C', fg='white',
                               font=('times new roman', 15, 'bold'))
total_sales_label_text.pack()

# For showing Total Sales is zero initially
total_sales_count_label = Label(sales_frame, text='0', bg='#E74C3C', fg='white', font=('times new roman', 30, 'bold'))
total_sales_count_label.pack()

# I have to keep everything under this loop
window.mainloop()
