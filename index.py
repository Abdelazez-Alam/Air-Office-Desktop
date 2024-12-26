# import library
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# connect to database
db = sqlite3.connect('app.db')
cr = db.cursor()
cr.execute("""CREATE TABLE IF NOT EXISTS user(user_id INT(10) PRIMARY KEY, user_name VARCHAR(30),
           user_phone INT(13), user_price INT(7),user_date VARCHAR(15), ticket_name VARCHAR(20),
           ticket_date VARCHAR(15), ticket_from VARCHAR(50), ticket_to VARCHAR(50), ticket_price INT(7))""")


# class app
class Mainapp(Tk):
    def __init__(self):
        # open window
        self.root = Tk()
        self.root.geometry("1366x768+0+0")
        self.root.title('Air Office')
        
        #  variables var
        self.ver_user_id = IntVar()
        self.ver_user_id.set('')
        
        self.ver_user_name = StringVar()
        
        self.ver_user_phone = IntVar()
        self.ver_user_phone.set('')
        
        self.ver_user_price = IntVar()
        self.ver_user_price.set('')
        
        self.ver_user_date = StringVar()
        
        self.ver_ticket_name = StringVar()
        
        self.ver_ticket_date = StringVar()
        
        self.ver_ticket_from = StringVar()
        
        self.ver_ticket_to = StringVar()
        
        self.ver_ticket_price = IntVar()
        self.ver_ticket_price.set('')
        
        self.ver_search = StringVar()
        
        self.ver_select = StringVar()
        self.ver_select.set('Search by')
        
        
        # frame for user data bar
        fr_user = Frame(self.root,width=670,height=130,bg='silver')
        fr_user.place(x=0,y=0)
        Label(fr_user,width= 15,text='Customer Data',font=('Arial',16,'bold')).place(x=230,y=0)
        Label(self.root,width= 10,text='User ID',font=('Arial',13)).place(x=30,y=60)
        Label(self.root,width= 10,text='Name',font=('Arial',13)).place(x=150,y=60)
        Label(self.root,width= 10,text='Phone',font=('Arial',13)).place(x=280,y=60)
        Label(self.root,width= 10,text='Amount paid',font=('Arial',13)).place(x=410,y=60)
        Label(self.root,width= 10,text='Booking date',font=('Arial',13)).place(x=540,y=60)
        
        # entry for user data
        self.ent_user_id = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_user_id)
        self.ent_user_id.place(x=30,y=90)
        
        self.ent_user_name = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_user_name)
        self.ent_user_name.place(x=150,y=90)
        
        self.ent_user_phone = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_user_phone)
        self.ent_user_phone.place(x=280,y=90)
        
        self.ent_user_price = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_user_price)
        self.ent_user_price.place(x=410,y=90)
        
        self.ent_user_date = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_user_date)
        self.ent_user_date.place(x=540,y=90)
        
        
        # frame for ticket data bar
        fr_ticket = Frame(self.root,width=670,height=130,bg='gray')
        fr_ticket.place(x=0,y=160)
        Label(fr_ticket,width= 15,text='Ticket data',font=('Arial',16,'bold')).place(x=230,y=0)
        Label(self.root,width=10, text='Type of flight',font=('Arial',13)).place(x=30,y=210)
        Label(self.root,width=10, text='Travel date',font=('Arial',13)).place(x=150,y=210)
        Label(self.root,width=10, text='Travel from',font=('Arial',13)).place(x=280,y=210)
        Label(self.root,width=10, text='Travel to',font=('Arial',13)).place(x=410,y=210)
        Label(self.root,width=10, text='Ticket price',font=('Arial',13)).place(x=540,y=210)
        
        # entry for ticket data
        self.ent_ticket_name =  Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_ticket_name)
        self.ent_ticket_name.place(x=30,y=240)
        
        self.ent_ticket_date =  Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_ticket_date)
        self.ent_ticket_date.place(x=150,y=240)
        
        self.ent_ticket_from =  Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_ticket_from)
        self.ent_ticket_from.place(x=280,y=240)
        
        self.ent_ticket_to =    Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_ticket_to)
        self.ent_ticket_to.place(x=410,y=240)
        
        self.ent_ticket_price = Entry(self.root,width=10,justify='center',font=('Arial',13),textvariable=self.ver_ticket_price)
        self.ent_ticket_price.place(x=540,y=240)
        
        # frame for buttons bar
        Frame(self.root,width=670,height=60,bg='silver').place(x=0,y=320)
        self.btn_add = Button(self.root,text='ADD',width=10,font=('Arial',13),command=self.add)
        self.btn_add.place(x=50,y=330)
        
        self.btn_update = Button(self.root,text='UPDATE',width=10,font=('Arial',13),command=self.update_user)
        self.btn_update.place(x=200,y=330)
        
        self.btn_delete = Button(self.root,text='DELETE',width=10,font=('Arial',13),command=self.delete)
        self.btn_delete.place(x=350,y=330)
        
        self.btn_clear = Button(self.root,text='Empty fields',width=10,font=('Arial',13),command=self.clear)
        self.btn_clear.place(x=500,y=330)
        
        # frame for search bar
        fr_search = Frame(self.root,width=670,height=150,bg='silver')
        fr_search.place(x=0,y=410)
        
        # search entry
        self.ent_search = Entry(self.root,width=20,justify='center',textvariable=self.ver_search,font=('Arial',15))
        self.ent_search.place(x=200,y=420)
        # search button
        self.btn_search = Button(self.root,text='SEARCH',width=14,font=('Arial',15),command=self.search)
        self.btn_search.place(x=150,y=490)
        # show all
        self.btn_show_all = Button(self.root,text='Show all',width=14,font=('Arial',15),command=self.show)
        self.btn_show_all.place(x=350,y=490)
        # combo box
        combo = ttk.Combobox(state="readonly",values=['Name','Travel date','User id'],font=('Arial',15),textvariable=self.ver_select)
        combo.place(x=450,y=420,width=120)
        
        # frame for table
        self.fr = Frame(self.root,width=670,height=680,bg='red')
        self.fr.place(x=675,y=0)
        # columns in table
        list_columns = ['user_id','user_name','user_phone','user_price','user_date','ticket_name','ticket_date','ticket_from','ticket_to','ticket_price']
        # create table
        self.table = ttk.Treeview(self.fr,columns=list_columns,show='headings')
        self.table.place(x=0,y=0,width=670,height=690)
        self.table.heading('#0',text='Lable',anchor=W)
        self.table.heading('user_id',text='ID', anchor='center')
        self.table.heading('user_name',text='Name', anchor='center')
        self.table.heading('user_phone',text='Phone', anchor='center')
        self.table.heading('user_price',text='Amount paid', anchor='center')
        self.table.heading('user_date',text='Booking date', anchor='center')
        self.table.heading('ticket_name',text='Type of flight', anchor='center')
        self.table.heading('ticket_date',text='Travel date', anchor='center')
        self.table.heading('ticket_from',text='Travel from', anchor='center')
        self.table.heading('ticket_to',text='Travel to', anchor='center')
        self.table.heading('ticket_price',text='Ticket price', anchor='center')
        # columns table
        self.table.column('#0', width=150, minwidth=25)
        self.table.column('user_id', width=35, anchor='center')
        self.table.column('user_name', width=80, anchor='center')
        self.table.column('user_phone', width=80, anchor='center')
        self.table.column('user_price', width=65, anchor='center')
        self.table.column('user_date', width=65, anchor='center')
        self.table.column('ticket_name', width=70, anchor='center')
        self.table.column('ticket_date', width=65, anchor='center')
        self.table.column('ticket_from', width=70, anchor='center')
        self.table.column('ticket_to', width=70, anchor='center')
        self.table.column('ticket_price', width=65, anchor='center')
        self.table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
    def clear(self):
        self.ver_user_id.set('')
        self.ver_user_name.set('')
        self.ver_user_phone.set('')
        self.ver_user_price.set('')
        self.ver_user_date.set('')
        self.ver_ticket_name.set('')
        self.ver_ticket_date.set('')
        self.ver_ticket_from.set('')
        self.ver_ticket_to.set('')
        self.ver_ticket_price.set('')
        self.ver_search.set('')
        
    def add(self):
        try:
            get_user_id = self.ver_user_id.get()
            get_user_name = self.ver_user_name.get()
            get_user_phone = self.ver_user_phone.get()
            get_user_price = self.ver_user_price.get()
            get_user_date = self.ver_user_date.get()
            get_ticket_name = self.ver_ticket_name.get()
            get_ticket_date = self.ver_ticket_date.get()
            get_ticket_from = self.ver_ticket_from.get()
            get_ticket_to = self.ver_ticket_to.get()
            get_ticket_price = self.ver_ticket_price.get()
        
            cr.execute(f""" INSERT INTO user (user_id,
                                            user_name,
                                            user_phone,
                                            user_price,
                                            user_date,
                                            ticket_name,
                                            ticket_date,
                                            ticket_price,
                                            ticket_from,
                                            ticket_to) VALUES({get_user_id},'{get_user_name}',{get_user_phone},{get_user_price},'{get_user_date}',
                                            '{get_ticket_name}','{get_ticket_date}',{get_ticket_price},'{get_ticket_from}','{get_ticket_to}')""")
            db.commit()
            self.show()
            self.clear()
        except:
            messagebox.showerror('Error','Please make sure to enter the data correctly.')
        
# show data in table
    def show(self):
        cr.execute("SELECT * FROM user")
        result = cr.fetchall()
        if len(result) != 0:
            self.table.delete(*self.table.get_children())
            for i in result:
                self.table.insert('',END,values=i)
        else:
            self.table.delete(*self.table.get_children())

# select data from table to entry inputs
    def get_data(self,eve):
        self.bo = self.table.focus()
        self.dt = self.table.item(self.bo)
        self.va = self.dt.get('values')
        self.ver_user_id.set(self.va[0])
        self.ver_user_name.set(self.va[1])
        self.ver_user_phone.set(self.va[2])
        self.ver_user_price.set(self.va[3])
        self.ver_user_date.set(self.va[4])
        self.ver_ticket_name.set(self.va[5])
        self.ver_ticket_date.set(self.va[6])
        self.ver_ticket_from.set(self.va[7])
        self.ver_ticket_to.set(self.va[8])
        self.ver_ticket_price.set(self.va[9])
        
        
        
    def delete(self):
        try:
            cr.execute(f"DELETE FROM user WHERE user_id = {self.ver_user_id.get()}")
            db.commit()
            self.show()
            self.clear()
        except:
            messagebox.showerror('Error','Please make sure of the user id you want to delete.')
        
        
        
    def update_user(self):
        try:
            cr.execute(f"""UPDATE user 
                    SET user_name = '{self.ver_user_name.get()}',user_phone = {self.ver_user_phone.get()}, user_price = {self.ver_user_price.get()}, user_date = '{self.ver_user_date.get()}',
                    ticket_name = '{self.ver_ticket_name.get()}', ticket_date = '{self.ver_ticket_date.get()}', ticket_from = '{self.ver_ticket_from.get()}', ticket_to = '{self.ver_ticket_to.get()}', ticket_price = {self.ver_ticket_price.get()}
                    WHERE user_id = {self.ver_user_id.get()}""")
            
            db.commit()
            self.clear()
            self.show()
        except:
            messagebox.showerror('Error','Please make sure of the user id you want to update.')
    
    
    def search(self):
        if self.ver_select.get() == 'Name':
            try:
                cr.execute(f"""SELECT * FROM user WHERE user_name LIKE "%{self.ver_search.get()}%" """)
                data = cr.fetchall()
                if len(data) != 0:
                    self.table.delete(*self.table.get_children())
                    for x in data:
                        self.table.insert('',END,values=x)
                else:
                    messagebox.showinfo('Sorry','The name you are looking for does not exist.')
            except:
                messagebox.showerror('Error','Please enter the name correctly.')
                
        elif self.ver_select.get() == 'User id':
            try:
                cr.execute(f"""SELECT * FROM user WHERE user_id = {self.ver_search.get()} """)
                data = cr.fetchall()
                if len(data) != 0:
                    self.table.delete(*self.table.get_children())
                    for i in data:
                        self.table.insert('',END,values=i)
                else:
                    messagebox.showinfo('Sorry','The number you are looking for does not exist.')
            except:
                messagebox.showerror('Error','Please enter the user id correctly.')
                
                
        elif self.ver_select.get() == 'Travel date':
            try:
                cr.execute(f"""SELECT * FROM user WHERE ticket_date LIKE '%{self.ver_search.get()}%' """)
                data = cr.fetchall()
                if len(data) != 0:
                    self.table.delete(*self.table.get_children())
                    for o in data:
                        self.table.insert('',END,values=o)
                else:
                    messagebox.showinfo('Sorry','The date you are looking for does not exist.')
            except:
                messagebox.showerror('Error','Please enter the date correctly.')
        
        else:
            messagebox.showerror('Error','Please select the type of search.')
    
    
    
        
if __name__ == '__main__':
    app = Mainapp()
    
    app.root.mainloop()