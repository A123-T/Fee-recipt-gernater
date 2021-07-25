from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as msg
root = Tk()
root.geometry("620x450")
root.resizable(0, 0)
root.title("form for Fee Reciept creation System")
r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
r4 = StringVar()
m = IntVar()

img = Image.open("2.png")
img = img.resize((100,100))
p =ImageTk.PhotoImage(img)
l = Label(image = p)
l.place(x=500,y=15,width=100,height=100)
a = Label(root,text="Welcome to Nit Nagaland",font="comicsansms 20 bold")
a.place(x=110,y=15)

lb = Label(root,text="Registration for fee", font="Halveteica 35 bold", bg="#091e30", fg="white")
lb.place(x=50, y=75)
l1 = Label(root, text="Enter your Full name - ", font="Halveteica 12 bold", bg="#091e30", fg="white")
l1.place(x=140, y=150)
e1 = Entry(root,font=(" ", 15), textvariable=r1)
e1.place(x=320, y=150, width=180, height=28)

l2 = Label(root, text="Enter Your Year- ", font="Halveteica 12 bold", bg="#091e30", fg="white")
l2.place(x=140, y=185)
e1 = Entry(root, font=(" ", 20), textvariable=r2)
e1.place(x=320, y=185, width=180, height=28)

l2 = Label(root, text="Enter your Semester - ", font="Halveteica 12 bold", bg="#091e30", fg="white")
l2.place(x=140, y=225)
e1 = Entry(root, font=(" ", 20), textvariable=r3)
e1.place(x=320, y=225, width=180, height=28)

l1 = Label(root, text="Enter your Branch - ", font="Halveteica 12 bold", bg="#091e30", fg="white")
l1.place(x=140, y=260)
e1 = Entry(root, font=(" ", 17), textvariable=r4)
e1.place(x=320, y=260, width=180, height=28)

l1 = Label(root, text="Family income less than 1 Lack - ", font="Halveteica 12 bold", bg="#091e30", fg="white")
l1.place(x=85, y=295)
g1 = Checkbutton(root,text="Yes",variable=m)
g1.place(x=350,y=300)
def fee():
    ch = m.get()
    ch = str(ch)
    rln = r1.get()
    r = r2.get()
    rls = r3.get()
    rl = r4.get().lower()
    if  r == '1' or r=='2' or r == '3' or r == '4' and rls < '9':
        #l == 'cse'or rl == 'computer science 'or rl == 'computer science and engineering':
        f = Frame()
        f.place(x=0, y=0, width=620, height=450)
        l = "Fee Recipt "+ rl
        f1 = Label(f,text=l,bg='#091e30',fg="white",font="Halveteica 15 bold")
        f1.place(x=90,y=20,width="480",height=50)
        f1 = Label(f,text='Name    - ', bg='#091e30', fg="white", font="Halveteica 15 bold")
        f1.place(x=90, y=90, width=150, height=50)
        f1 = Label(f,text=rln, bg='#091e30', fg="white", font="Halveteica 15 bold")
        f1.place(x=250, y=90, width="150", height=50)
        f2 = Label(f,text='Tution fee    - ', bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=90, y=150, width=150, height=50)
        f2 = Label(f, text='Hostel fee    - ', bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=90, y=270, width=150, height=50)
        f0 =10000
        f2 = Label(f, text=f0, bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=250, y=270, width="150", height=50)
        f2 = Label(f, text='Mess Fee     - ', bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=90, y=330, width=150, height=50)
        fc1 = 1000
        f2 = Label(f, text=fc1, bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=250, y=330, width="150", height=50)
        f2 = Label(f, text='Computer fee', bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=90, y=390, width=150, height=50)
        fc2 = 5000
        f2 = Label(f, text=fc2, bg='#091e30', fg="white", font="Halveteica 15 bold")
        f2.place(x=250, y=390, width="150", height=50)
        if ch == '0':
            fc = 100000
            f2 = Label(f,text=fc, bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=250, y=150, width="150", height=50)

            f2 = Label(f,text="Semister - ", bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=90, y=210, width="150", height=50)
            f2 = Label(f,text=rls, bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=250, y=210, width="150", height=50)
            def pr1():
                from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
                from reportlab.lib.pagesizes import A4
                from reportlab.lib import colors
                from reportlab.lib.styles import getSampleStyleSheet
                DATA = [['          ', '                             ', '        '],
                        ['          ', '                             ', '        '],
                        ["NAME", "Tution fee", "Semester", "Hostel - fee", 'Messh-fee', 'Computer fee'],
                        ]
                DATA1 = [
                    ['        ', '           '],
                ]
                # data which we are going to Insert Pdf function  as tables
                l1 = r1.get()
                l2 = fc
                l3 = r3.get()
                l4 = f0
                l5 = fc1
                l6 = fc2
                D = [l1, l2, l3, l4, l5, l6]
                DATA.append(D)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                DATA1.append(a)
                a = ['          ', '                             ', '        ']
                DATA1.append(a)
                a = ['          ', '                             ', '        ']
                DATA1.append(a)

                # creating a Base Document Template of page size A4
                pdf = SimpleDocTemplate("Fee.pdf", pagesize=A4)

                # standard stylesheet defined within reportlab itself
                styles = getSampleStyleSheet()

                # fetching the style of Top level heading (Heading1)
                title_style = styles["Heading1"]

                title_style1 = styles["Heading1"]
                title_style2 = styles["Heading1"]
                title_style3 = styles["Heading1"]
                # 0: left, 1: center, 2: right
                title_style.alignment = 1

                title_style1.alignment = 1

                title_style2.alignment = 1

                title_style3.alignment = 1
                # creating the paragraph with
                # the heading text and passing the styles of it
                title = Paragraph('NIT NAGALAND Fee 2021-23', title_style)
                style = TableStyle(
                    [
                        ("BOX", (0, 5), (5, 0), 1, colors.black),
                        ("BACKGROUND", (0, 5), (5, 0), colors.beige),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ]
                )
                tp2 = "Total Fees  : " + l1 + "  " + rl
                title1 = Paragraph(tp2, title_style1)
                title3 = Paragraph(total, title_style3)
                title2 = Paragraph("| | |---------------THANK YOU----------------| | |", title_style2)
                # creates a table object and passes the style to it
                table = Table(DATA, style=style)
                table1 = Table(DATA1)
                # final step which builds the
                # actual pdf putting together all the elements
                pdf.build([title, table, title1, title3, table1, title2])
                exit()
            s = Button(f,text="Print", font="Halveteica 14 bold", bg="grey", border="8",command=pr1)
            s.place(x=404, y=140, width=160, height=45)
            def log():
                exit()
            s = Button(f,text="logout", font="Halveteica 14 bold", bg="grey", border="8",command=log)
            s.place(x=404, y=85, width=160, height=45)
            total =fc + fc1 + fc2 + f0
            total = str(total)
            total = " Total = " + total
            s = Label(f, text=total, font="Halveteica 14 bold", bg="#00ffff", border="8")
            s.place(x=404, y=200, width=190, height=45)
        else:
            fc = 14000
            print(fc)
            f2 = Label(f, text=fc, bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=250, y=150, width="150", height=50)
            f2 = Label(f, text="Semister - ", bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=90, y=210, width="150", height=50)
            f2 = Label(f, text=rls, bg='#091e30', fg="white", font="Halveteica 15 bold")
            f2.place(x=250, y=210, width="150", height=50)
            def pr1():
                from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
                from reportlab.lib.pagesizes import A4
                from reportlab.lib import colors
                from reportlab.lib.styles import getSampleStyleSheet
                DATA = [['          ', '                             ', '        '],
                        ['          ', '                             ', '        '],
                        ["NAME", "Tution fee", "Semester", "Hostel - fee", 'Messh-fee', 'Computer fee'],
                        ]
                DATA1 = [
                    ['        ', '           '],
                ]
                # data which we are going to Insert Pdf function  as tables
                l1 = r1.get()
                l2 = fc
                l3 = r3.get()
                l4 = f0
                l5 = fc1
                l6 = fc2
                D = [l1, l2, l3, l4, l5, l6]
                DATA.append(D)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                a = ['          ', '                             ', '        ']
                DATA.append(a)
                DATA1.append(a)
                a = ['          ', '                             ', '        ']
                DATA1.append(a)
                a = ['          ', '                             ', '        ']
                DATA1.append(a)

                # creating a Base Document Template of page size A4
                pdf = SimpleDocTemplate("Fee.pdf", pagesize=A4)

                # standard stylesheet defined within reportlab itself
                styles = getSampleStyleSheet()

                # fetching the style of Top level heading (Heading1)
                title_style = styles["Heading1"]

                title_style1 = styles["Heading1"]
                title_style2 = styles["Heading1"]
                title_style3 = styles["Heading1"]
                # 0: left, 1: center, 2: right
                title_style.alignment = 1

                title_style1.alignment = 1

                title_style2.alignment = 1

                title_style3.alignment = 1
                # creating the paragraph with
                # the heading text and passing the styles of it
                title = Paragraph('NIT NAGALAND Fee 2021-23', title_style)
                style = TableStyle(
                    [
                        ("BOX", (0, 5), (5, 0), 1, colors.black),
                        ("BACKGROUND", (0, 5), (5, 0), colors.beige),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ]
                )
                tp2 = "Total Fees  : " + l1 + "  " + rl
                title1 = Paragraph(tp2, title_style1)
                title3 = Paragraph(total, title_style3)
                title2 = Paragraph("| | |---------------THANK YOU----------------| | |", title_style2)
                # creates a table object and passes the style to it
                table = Table(DATA, style=style)
                table1 = Table(DATA1)
                # final step which builds the
                # actual pdf putting together all the elements
                pdf.build([title, table, title1, title3, table1, title2])
                exit()

            s = Button(f, text="Print", font="Halveteica 14 bold", bg="grey", border="8", command=pr1)
            s.place(x=404, y=140, width=160, height=45)

            def log():
                exit()
            s = Button(f, text="logout", font="Halveteica 14 bold", bg="grey", border="8", command=log)
            s.place(x=404, y=85, width=160, height=45)
            total = fc + fc1 + fc2 + f0
            total = str(total)
            total = " Total = "+total
            s = Label(f, text=total, font="Halveteica 14 bold", bg="#00ffff", border="8")
            s.place(x=404, y=200, width=190, height=45)
    else:
        msg.showinfo('title',"Please provide some information       \n        THANK  YOU          ")

s = Button(text="Submit", font="Halveteica 14 bold", bg="grey", border="8", command=fee)
s.place(x=284, y=375, width=220, height=45)
root.mainloop()