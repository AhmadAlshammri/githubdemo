import re
import mysql.connector as mys
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


class Visualization():

    def _init_(self):
        self.Price = np.array([2, 6, 30, 25, 55, 20, 40, 35, 60, 27])
        self.Prodects = np.array(
            ['water', 'soda', 'burger', 'pizza', 'meet', 'chicken', 'burger meal', 'pizza meal', 'meet meal',
             'chicken meal'])
        #print(self.Price+self.Prodects)
        self.colers = np.array([10, 20, 30, 40, 50, 60, 65, 70, 80, 90])
        plt.subplot(1, 2, 1)
        plt.scatter(self.Price, self.Prodects, c=self.colers)
        plt.colorbar()
        plt.title("Menu")
        plt.xlabel("Price")
        plt.ylabel("Prodects")
        plt.subplot(1, 2, 2)
        self.myexpolt = [0.2, 0, 0, 0, 0, 0, 0, 0, 0.1, 0]
        plt.pie(self.Price, labels=self.Prodects, explode=self.myexpolt, autopct='%1.2f%%')
        plt.legend()
        plt.title("best seller")
        plt.suptitle("productive families")
        plt.grid()
        plt.show()

    def array(self):
        return np.hstack((self.Price, self.Prodects))


class thread():
    def VAT(self):
        dbobj = sqlDatabase()
        z=dbobj.count_price(coulumn='price')
        self.x = (float(z) * 0.15)

    def profet_count(self, cost):
        dbobj = sqlDatabase()
        z = dbobj.count_price(coulumn='price')
        #time.sleep(2)
        self.y= z - cost

    def CallThread(self):
        t=threading.Thread(target=self.VAT)
        r=threading.Thread(target=self.profet_count, args=(30,))
        t.start()
        t.join()
        r.start()
        r.join()

class UnAvailablNumber(Exception):
    def _init_(self,message):
        self.message=message

class person ():
    def _init_(self='',name='',number=0,location='',email=''):
        self.name=name
        self.number=number
        self.location=location
        self.email=email

    def valid(self='',number=''):
        if (len(number) != 10):
            return False

        for i in range(len(number)):
            if number[i] < '0' or number[i] > '9':
                return False
        return True


    #def _str_(self):
        #return "name:{}, number:{}, location:{}, email:{}".format(name, number, location, email)


class family(person):
    def _init_(self,name,number,location,email):
        person._init_(name,number,location,email)

    #def _str_(self):
        #return "name: {}, number: {}, location: {}, email: {}, Type_Of_Product: {}".format(name, number, location, email, Type_Of_Product)


class costumer(person):
    def _init_(self,name=0,number=0,location='',email='',reading=''):
        person._init_(name,number,location,email)
        self.reading=reading

    #def _str_(self):
        #return "name: {}, number: {}, location: {}, email: {}".format(name,number,location,email)


class delivery(person):
    def _init_(self, name, number, email):
        person._init_(name, number, email)

    #def _str_(self):
        #return "name: {}, number: {}, email: {}, CarInformation: {}".format(name, number, email, CarInformation)

class Order():
    def _init_(self,id=0, cust='', deliv='', prod=''):
        self.id=id
        self.cust=cust
        self.deliv=deliv
        self.prod=prod

    def read_deteils(self):
        with open('details.txt','r') as rd:
            data = rd.read()
        return data

class products ():
    def _init_(self,ID_Number=0,type_of_product='',name='',price=0,details=''):
        self.ID_Number=ID_Number
        self.type_of_product=type_of_product
        self.name=name
        self.price=price
        self.details=details

    def details_write(self,dt):
        with open('details.txt','w') as write_details:
            write_details.write(dt)

    def _str_(self):
        return "ID_Number: {}, type_of_product: {}, name: {} ,price: {} ,details: {}".format(ID_Number, type_of_product , name, price, details)


class sqlDatabase():
    def _init_(self):
        self.mycon = mys.connect(host='localhost', user='root', passwd='1234', database='produser_family')
        self.mycursor = self.mycon.cursor()

    def user_number_get(self,email):
        query = "SELECT phone_number FROM person where email='{}'".format(email)
        self.mycursor.execute(query)
        mydata= self.mycursor.fetchall()
        return mydata[0][0]

    def user_email_get(self,phone_number):
        query = "SELECT email FROM person where phone_number={}".format(phone_number)
        self.mycursor.execute(query)
        mydata= self.mycursor.fetchall()
        return mydata[0][0]

    def insertDataPerson(self,v1,v2,v3,v4):
        query = "insert into person values ({},'{}','{}','{}')".format(v1,v2,v3,v4)
        self.mycursor.execute(query)
        self.mycon.commit()
        x=('## data saved ##')
        return x

    def insertDataProduct(self,v1,v2,v3,v4,v5):
        query = "insert into product values ({},'{}','{}',{},'{}')".format(v1,v2,v3,v4,v5)
        self.mycursor.execute(query)
        self.mycon.commit()
        x=('## data saved ##')
        return x

    def insertDataOrders(self,v1,v2,v3,v4):
        query = "insert into orders values ({},'{}','{}','{}')".format(v1,v2,v3,v4)
        self.mycursor.execute(query)
        self.mycon.commit()
        x=('## data saved ##')
        return x

    def count_price(self,coulumn):
        query = 'select sum({}) from product'.format(coulumn)
        self.mycursor.execute(query)
        mydata = self.mycursor.fetchall()
        return mydata[0][0]


class GUI(tk.Tk):
    def _init_(self, *args, **kwargs):
        tk.Tk._init_(self, *args, **kwargs)

        self.title('Producer Families')
        self.config(background='black')

        self.frame1=Frame(self, width=300,height=500)
        self.frame1.grid(row=0,column=0 ,padx=20 ,pady=20)

        self.frame2=Frame(self, width=700,height=500)
        self.frame2.grid(row=0,column=1 ,padx=20,pady=20)

        self.image=PhotoImage(file='oo.png')
        self.original_image=self.image.subsample (1,1)
        self.PhLabel=Label(self.frame2,image=self.original_image).grid(row=0,column=0,padx=5, pady=5)

        self.lable1=Label(self.frame1,text='Login Window')
        self.lable1.grid(row=0,column=2,padx=2,pady=2)

        self.Name_var = tk.StringVar()
        self.Passw_var = tk.StringVar()

        self.user=Entry(self.frame1,width=20,textvariable=self.Name_var)
        self.user.grid(row=1,column=3,padx=5,pady=2)

        self.lable2 = Label(self.frame1, text='user')
        self.lable2.grid(row=1, column=0)

        self.password = Entry(self.frame1, width=20,textvariable=self.Passw_var,show='*')
        self.password.grid(row=2, column=3,padx=5)

        self.lable3 = Label(self.frame1, text='password')
        self.lable3.grid(row=2, column=0)

        self.Botton1 =Button(self.frame1,text='login',command=lambda:self.CheckLogin())
        self.Botton1.grid(row=3,column=0)

        self.Botton2 = Button(self.frame1, text='Exit', command=lambda:self.quit())
        self.Botton2.grid(row=3, column=1)

        self.register=Button(self.frame1, text='Register', command=lambda:self.registerW())
        self.register.grid(row=4, column=1)

    def registerW(self):
        self.wm_attributes("-disabled", True)
        ##################### Creating the Register dialog #######################
        self.Registerwind = tk.Toplevel(self)
        self.Registerwind.geometry("400x350")
        self.Registerwind.transient(self)
        self.Registerwind.protocol("WM_DELETE_WINDOW", self.CloseRegisterWind)

        self.NameVar = StringVar()
        self.NumberVar = StringVar()
        self.Emailvar = StringVar()
        self.LocationVar = StringVar()

        self.Tryframe = Frame(self.Registerwind, width=500, height=500)
        self.Tryframe.grid(row=0, column=0, padx=20, pady=20)

        self.namela = Label(self.Tryframe, text='Name')
        self.namela.grid(row=1, column=0,padx=5,pady=5)

        self.nameE = Entry(self.Tryframe, width=20,textvariable=self.NameVar)
        self.nameE.grid(row=1,column=1,padx=5,pady=5)

        self.numberla = Label(self.Tryframe, text='Number')
        self.numberla.grid(row=2, column=0,padx=5,pady=5)

        self.numberE = Entry(self.Tryframe, width=20,textvariable=self.NumberVar)
        self.numberE.grid(row=2, column=1,padx=5,pady=5)

        self.emailla = Label(self.Tryframe, text='Email')
        self.emailla.grid(row=3, column=0,padx=5,pady=5)

        self.emailE = Entry(self.Tryframe, width=20,textvariable=self.Emailvar)
        self.emailE.grid(row=3, column=1,padx=5,pady=5)

        self.locationla = Label(self.Tryframe, text='Location')
        self.locationla.grid(row=4, column=0,padx=5,pady=5)

        self.locationE = Entry(self.Tryframe, width=20,textvariable=self.LocationVar)
        self.locationE.grid(row=4, column=1,padx=5,pady=5)

        self.submetB=Button(self.Tryframe, text='Create Account',command=lambda:self.checkinfo())
        self.submetB.grid(row=5,column=1,padx=5,pady=5)

        self.text=Text(self.Tryframe,height=10,width=25)
        self.text.grid(row=5,column=0,padx=5,pady=5)

    def checkinfo(self):
        p = person()
        self.name = self.NameVar.get()
        self.number = self.NumberVar.get()
        self.email = self.Emailvar.get()
        self.location = self.LocationVar.get()

        if self.number == '' or self.number == '' or self.email == '' or self.location == '':
            messagebox.showerror("Error", 'Pleas fill all requirements')
        else:
            try:
                if p.valid(number=self.number) != True:
                    raise UnAvailablNumber('')
            except UnAvailablNumber:
                messagebox.showerror("Error", 'Please enter 10 numbers !')
            else:
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if bool((re.fullmatch(regex, self.email))) == False:
                    messagebox.showerror("Error", 'Please enter Valid email !')
                else:
                    db = sqlDatabase()
                    db.insertDataPerson(v1=self.number, v2=self.name, v3=self.location, v4=self.email)
                    messagebox.showinfo("Done", 'saved')

    def CloseRegisterWind(self):
        self.wm_attributes("-disabled", False) # IMPORTANT!
        self.Registerwind.destroy()

    def loginW(self):
        self.wm_attributes("-disabled", True)
        ##################### Creating the Login dialog #######################
        self.Loginwind = tk.Toplevel(self)
        self.Loginwind.transient(self)
        self.Loginwind.protocol("WM_DELETE_WINDOW", self.CloseLoginWind)

        self.idProduct_var = StringVar()
        self.priceProduct_var = StringVar()
        self.typeProduct_var = StringVar()
        self.nameProduct_var = StringVar()
        self.detailsProduct_var = StringVar()

        self.frameM = Frame(self.Loginwind, width=500, height=500)
        self.frameM.grid(row=0, column=0, padx=5, pady=5)
        self.frame3 = Frame(self.frameM, width=500, height=500)
        self.frame3.grid(row=0, column=0, padx=5, pady=5)
        self.frame4 = Frame(self.frameM, width=500, height=500)
        self.frame4.grid(row=1, column=0, padx=5, pady=5)
        self.frame5 = Frame(self.frameM, width=500, height=500)
        self.frame5.grid(row=2, column=0, padx=5, pady=5)
        self.frame6 = Frame(self.frameM, width=500, height=500)
        self.frame6.grid(row=0, column=1, padx=5, pady=5)
        self.frame7 = Frame(self.frameM, width=500, height=500)
        self.frame7.grid(row=1, column=1, padx=5, pady=5)
        self.frame8 = Frame(self.frameM, width=500, height=500)
        self.frame8.grid(row=2, column=1, padx=5, pady=5)
        self.text1 = Text(self.frame5, height=10, width=25)
        self.text1.grid(row=1, column=0, padx=5, pady=5)
        self.getPrice = Button(self.frame5, text='get total price', command=lambda: self.sq())
        self.getPrice.grid(row=2, column=0, padx=5, pady=5)
        self.inso = Button(self.frame4, text='insert order', command=lambda: self.InsOrder())
        self.inso.grid(row=5, column=1, padx=5, pady=5)
        self.insp = Button(self.frame3, text='insert product', command=lambda: self.InsProduct())
        self.insp.grid(row=6, column=1, padx=5, pady=5)
        self.th = Button(self.frame5, text='Get VAT and Profit ', command=lambda: self.threa())
        self.th.grid(row=3, column=0, padx=5, pady=5)
        self.text4 = Text(self.frame8, height=10, width=25)
        self.text4.grid(row=0, column=0, padx=5, pady=5)
        self.menuB = Button(self.frame8, text='Get Menu and Statics ', command=lambda: self.menuGet())
        self.menuB.grid(row=1, column=0, padx=10, pady=20)

        # insert product
        self.PrID = Entry(self.frame3, width=20, textvariable=self.idProduct_var)
        self.PrID.grid(row=1, column=2, padx=5, pady=2)
        self.PrIDL = Label(self.frame3, text='Product ID')
        self.PrIDL.grid(row=1, column=0, padx=5, pady=5)
        self.TOP = Entry(self.frame3, width=20, textvariable=self.typeProduct_var)
        self.TOP.grid(row=2, column=2, padx=5, pady=2)
        self.TOPL = Label(self.frame3, text='Type of Product')
        self.TOPL.grid(row=2, column=0, padx=5, pady=5)
        self.NOP = Entry(self.frame3, width=20, textvariable=self.nameProduct_var)
        self.NOP.grid(row=3, column=2, padx=5, pady=2)
        self.NOPL = Label(self.frame3, text='Name of Product')
        self.NOPL.grid(row=3, column=0, padx=5, pady=5)
        self.Price = Entry(self.frame3, width=20, textvariable=self.priceProduct_var)
        self.Price.grid(row=4, column=2, padx=5, pady=2)
        self.PriceL = Label(self.frame3, text='Price')
        self.PriceL.grid(row=4, column=0, padx=5, pady=5)
        self.Details = Entry(self.frame3, width=20, textvariable=self.detailsProduct_var)
        self.Details.grid(row=5, column=2, padx=5, pady=2)
        self.DetailsL = Label(self.frame3, text='Details')
        self.DetailsL.grid(row=5, column=0, padx=5, pady=5)

        # insert order

        self.idOrder_var = StringVar()
        self.custmerOrder_var = StringVar()
        self.delivOrder_var = StringVar()
        self.ProductOrder_var = StringVar()

        self.OrID = Entry(self.frame4, width=20, textvariable=self.idOrder_var)
        self.OrID.grid(row=1, column=2, padx=5, pady=2)
        self.OrIDL = Label(self.frame4, text='Order ID')
        self.OrIDL.grid(row=1, column=0, padx=5, pady=5)
        self.Cust = Entry(self.frame4, width=20, textvariable=self.custmerOrder_var)
        self.Cust.grid(row=2, column=2, padx=5, pady=2)
        self.CustL = Label(self.frame4, text='Customer')
        self.CustL.grid(row=2, column=0, padx=5, pady=5)
        self.Del = Entry(self.frame4, width=20, textvariable=self.delivOrder_var)
        self.Del.grid(row=3, column=2, padx=5, pady=2)
        self.DelL = Label(self.frame4, text='Delivery')
        self.DelL.grid(row=3, column=0, padx=5, pady=5)
        self.Prod = Entry(self.frame4, width=20, textvariable=self.ProductOrder_var)
        self.Prod.grid(row=4, column=2, padx=5, pady=2)
        self.ProdL = Label(self.frame4, text='Product')
        self.ProdL.grid(row=4, column=0, padx=5, pady=5)

        # write file

        self.write_var = StringVar()

        self.writeD = Label(self.frame6, text='Enter Details for Product')
        self.writeD.grid(row=0, column=0, padx=10, pady=5)
        self.text2 = Entry(self.frame6, width=25, textvariable=self.write_var)
        self.text2.grid(row=1, column=0, padx=10, pady=5)
        self.writeBot = Button(self.frame6, text='Insert Details', command=lambda: self.writeDetails())
        self.writeBot.grid(row=2, column=0, padx=10, pady=5)

        # read details
        self.readD = Label(self.frame7, text='Read Details of Product')
        self.readD.grid(row=0, column=0, padx=10, pady=5)
        self.text3 = Text(self.frame7, height=10, width=25)
        self.text3.grid(row=1, column=0, padx=10, pady=5)
        self.readBot = Button(self.frame7, text='Read Details', command=lambda: self.readDetails())
        self.readBot.grid(row=2, column=0, padx=10, pady=5)

        # menu bar
        menubar = Menu(self.Loginwind)

        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file)
        file.add_command(label='new file', command=None)
        file.add_command(label='OPEN...', command=None)
        file.add_command(label='Save', command=None)
        file.add_separator()
        file.add_command(label='Exit', command=self.Loginwind.destroy)

        edit = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='edit', menu=edit)
        edit.add_command(label='cut', command=None)
        edit.add_command(label='copy', command=None)
        edit.add_command(label='paste', command=None)
        edit.add_command(label='select All', command=None)
        edit.add_separator()
        edit.add_command(label='find ...', command=None)
        edit.add_command(label='find again', command=None)

        help = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help)
        help.add_command(label='tk help', command=None)
        help.add_command(label='demo', command=None)
        help.add_command(label='cut', command=None)
        help.add_separator()
        help.add_command(label='about tk', command=None)

        self.Loginwind.config(menu=menubar)

    def CloseLoginWind(self):
        self.wm_attributes("-disabled", False)  # IMPORTANT!
        self.Loginwind.destroy()

    def CheckLogin(self):
        self.username = self.Name_var.get()
        self.password = self.Passw_var.get()
        try:
            self.password !=str(self.user_number_get_check()) and self.username !=str(self.user_email_get_check())
        except Exception:
            messagebox.showinfo("Message", "Incorrect password ... Try again ...!")
        else:
            self.loginW()

    def writeDetails(self):
        if self.write_var.get() == '':
            messagebox.showerror("Error", 'Pleas Enter Details !')
        else:
            x=products()
            x.details_write(dt=self.write_var.get())
            messagebox.showinfo("Done", 'Details Saved')

    def readDetails(self):
        x=Order()
        self.text3.insert(END, str(x.read_deteils()))

    def sq(self):
        dbobj = sqlDatabase()
        self.text1.insert(END,'The Total Price : ' + str(dbobj.count_price(coulumn='price'))+'\n')

    def user_number_get_check(self):
        sqlPass=sqlDatabase()
        return sqlPass.user_number_get(email=self.username)

    def user_email_get_check(self):
        sqlPass=sqlDatabase()
        return sqlPass.user_email_get(phone_number=self.password)

    def threa(self):
        mythread=thread()
        mythread.CallThread()
        self.text1.insert(END,'The VAT Is : ' + str(mythread.x)+'\n')
        self.text1.insert(END,'The Total Profit : ' +str(mythread.y)+'\n')

    def InsProduct(self):
        sql = sqlDatabase()
        self.idProduct = self.idProduct_var.get()
        self.priceProduct = self.priceProduct_var.get()
        self.nameProduct = self.nameProduct_var.get()
        self.typeProduct = self.typeProduct_var.get()
        self.detailsProduct = self.detailsProduct_var.get()

        try:
            self.idProduct=='' and self.typeProduct=='' and self.nameProduct=='' and self.priceProduct =='' and self.detailsProduct==''
            sql.insertDataProduct(v1=self.idProduct, v2=self.typeProduct, v3=self.nameProduct, v4=self.priceProduct,
                                  v5=self.detailsProduct)
            messagebox.showinfo("Done", 'Product Saved')
        except Exception:
            messagebox.showerror("Error", 'fill all data')

    def InsOrder(self):
        sql = sqlDatabase()
        self.idOrder = self.idOrder_var.get()
        self.custmerOrder = self.custmerOrder_var.get()
        self.delivOrder = self.delivOrder_var.get()
        self.ProductOrder = self.ProductOrder_var.get()

        try:
            self.idOrder=='' and self.custmerOrder=='' and self.delivOrder=='' and self.ProductOrder ==''
            sql.insertDataOrders(v1=self.idOrder, v2=self.custmerOrder, v3=self.delivOrder, v4=self.ProductOrder)
            messagebox.showinfo("Done", 'Product Saved')
        except Exception:
            messagebox.showerror("Error", 'fill all data')

    def menuGet(self):
        vis=Visualization()
        self.text4.insert(END, 'This is the Menu\n'+str(vis.array()))



if _name_ == "_main_":

    x=GUI()
    x.mainloop()