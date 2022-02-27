from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage  import resizeimage


class Qr_generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR code generator")
        self.root.resizable(False, False)

        title = Label(self.root, text="    Q-R code generator", font=("times new roman", 40), bg='#053246', fg='white',
                      anchor='w').place(x=0, y=0, relwidth=1)
        # employe detail window

        # variable
        self.var_name = StringVar()
        self.var_father_name = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_address = StringVar()
        p_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        p_frame.place(x=50, y=100, width=500, height=380)
        p_title = Label(p_frame, text=" User Detail", font=("goudy old style", 20), bg='#043256',
                          fg='white', ).place(x=0, y=0, relwidth=1)
        lbl_name = Label(p_frame, text="Name", font=("times new roman", 15, 'bold'), bg='white', ).place(
            x=20, y=100, )
        lbl_father_name = Label(p_frame, text="Father's Name", font=("times new roman", 15, 'bold'), bg='white', ).place(x=20,
                                                                                                           y=140, )
        lbl_date_of_birth = Label(p_frame, text="Date of Birth", font=("times new roman", 15, 'bold'), bg='white', ).place(
            x=20, y=180, )
        lbl_address = Label(p_frame, text="Address", font=("times new roman", 15, 'bold'),
                                bg='white', ).place(x=20, y=220, )

        txt_name = Entry(p_frame, font=("times new roman", 15,), textvariable=self.var_name,
                             bg='lightyellow', ).place(x=200, y=100, )
        txt_father_name = Entry(p_frame, font=("times new roman", 15,), textvariable=self.var_father_name,
                         bg='lightyellow', ).place(x=200, y=140, )
        txt_date_of_birth = Entry(p_frame, font=("times new roman", 15,), textvariable=self.var_date_of_birth,
                               bg='lightyellow', ).place(x=200, y=180, )
        txt_address = Entry(p_frame, font=("times new roman", 15,), textvariable=self.var_address,
                                bg='lightyellow', ).place(x=200, y=220, )

        btn_generate = Button(p_frame, text="Generate Qr code", command=self.generate,
                              font=("times new roman", 15, 'bold'), bg='#2196f3', fg='white').place(x=90, y=280,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_clear = Button(p_frame, text="Clear", command=self.clear, font=("times new roman", 15, 'bold'), bg='#607d8b',
                           fg='white').place(x=280, y=280, width=180, height=30)

        self.msg = ''
        self.lbl_msg = Label(p_frame, text=self.msg, font=("times new roman", 20,), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=320, relwidth=1)

        # Qr detail window
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_frame.place(x=600, y=100, width=250, height=380)
        qr_title = Label(qr_frame, text="    Q-R code", font=("goudy old style", 20), bg='#043256', fg='white', ).place(
            x=0, y=0, relwidth=1)
        self.qr_code = Label(qr_frame, text="QR code not Available", font=("times new roman", 15,), bg='#3f51b5',
                             fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)
    def clear(self):
        self.var_name.set('')
        self.var_father_name.set('')
        self.var_date_of_birth.set('')
        self.var_address.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg, )

    def generate(self):
        if self.var_name.get() == '' or self.var_father_name.get() == '' or self.var_date_of_birth.get() == '' or self.var_address.get() == '':
            self.msg = "All fields are Required"
            self.lbl_msg.config(text=self.msg, fg='red')
        else:
            qr=(f"Name : {self.var_name.get()}\nFather's Name : {self.var_father_name.get() }\nDate of birth : {self.var_date_of_birth.get() }\nAddress : {self.var_address.get()}")
            qr_code=qrcode.make(qr)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            name=self.var_name.get()
            qr_code.save('{}.png'.format(name))
            self.im= ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg = "Qr code generated sucessfully"
            self.lbl_msg.config(text=self.msg, fg='green')


root = Tk()
obj = Qr_generator(root)
root.mainloop()
