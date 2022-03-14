from tkinter import *
from PIL import Image
from tkinter import filedialog
from fpdf import FPDF
from datetime import date, datetime
import webbrowser


def bestOf5(lang,lit,math,hin,phy,chem,bio,his,geo,com_eco):
    #GROUPING OF SUBJECTS
    group = [0,0,0,0,0,0]
    group[0] = (lang + lit) / 2 #english
    group[1] = (phy + chem + bio) / 3 #science
    group[2] = (his + geo)/2 # arts
    group[3] = hin
    group[4] = math
    group[5] = com_eco

    #BUBBLESORTING

    for i in range(0,len(group)-1):
        for j in range(len(group)-1):
            if(group[j]>group[j+1]):
                a
                temp = group[j]  
                group[j] = group[j+1]  
                group[j+1] = temp


    #CALCULATING PERCENTAGE
    percentage = (group[0] + group[1] + group[2] + group[3] + group[4] ) / 5

    return percentage

def addImg():
    filetypes = (
        ('PNG Images', '*.png'),
    )
    pic = filedialog.askopenfilename()
    imgOpen = Image.open(pic)

    newImg = imgOpen.resize((151,151))
    newImg.save('images/new.png')

    global photoFinal
    photoFinal = PhotoImage(file='images/new.png')
    

def submit1():
    global window2
    window2 = Tk()
    window2.geometry("500x500")
    window2.title("DNS Result Generator")

    #logo = PhotoImage(file="images/logo.png")
    #label1 = Label(window2,image=logo)
    #label1.place(y=0)

    txtHeading = "Welcome  " + str(e1.get())
    label2 = Label(window2,text=txtHeading,font=("Times New Roman",30))
    label2.place(x=100)

    label3 = Label(window2,text="Enter Marks obtained in the following subjects ",font=("Times New Roman",15)).place(x=3,y=80)
    label4 = Label(window2,text="English Language",font=("Times New Roman",13)).place(x=3,y=120)
    label5 = Label(window2,text="English Literature",font=("Times New Roman",13)).place(x=3,y=145)
    label6 = Label(window2,text="Mathematics",font=("Times New Roman",13)).place(x=3,y=170)
    label7 = Label(window2,text="Hindi",font=("Times New Roman",13)).place(x=3,y=195)
    label8 = Label(window2,text="Physics ",font=("Times New Roman",13)).place(x=3,y=220)
    label9 = Label(window2,text="Chemistry",font=("Times New Roman",13)).place(x=3,y=245)
    label10 = Label(window2,text="Biology",font=("Times New Roman",13)).place(x=3,y=270)
    label11= Label(window2,text="History & Civics",font=("Times New Roman",13)).place(x=3,y=295)
    label12 = Label(window2,text="Geography",font=("Times New Roman",13)).place(x=3,y=320)
    label13 = Label(window2,text="Computer/Economics Applications",font=("Times New Roman",13)).place(x=3,y=345)

    global e4
    global e5
    global e6
    global e7
    global e8
    global e9
    global e10
    global e11
    global e12
    global e13
    
    e4 = Entry(window2,width=10,font=("Times New Roman",13))
    e4.place(x=275,y=120)
    e5 = Entry(window2,width=10,font=("Times New Roman",13))
    e5.place(x=275,y=145)
    e6 = Entry(window2,width=10,font=("Times New Roman",13))
    e6.place(x=275,y=170)
    e7 = Entry(window2,width=10,font=("Times New Roman",13))
    e7.place(x=275,y=195)
    e8 = Entry(window2,width=10,font=("Times New Roman",13))
    e8.place(x=275,y=220)
    e9 = Entry(window2,width=10,font=("Times New Roman",13))
    e9.place(x=275,y=245)
    e10 = Entry(window2,width=10,font=("Times New Roman",13))
    e10.place(x=275,y=270)
    e11 = Entry(window2,width=10,font=("Times New Roman",13))
    e11.place(x=275,y=295)
    e12 = Entry(window2,width=10,font=("Times New Roman",13))
    e12.place(x=275,y=320)
    e13 = Entry(window2,width=10,font=("Times New Roman",13))
    e13.place(x=275,y=345)
    
    submitBtn = Button(window2,text="Submit",font=("Times New Roman",13),fg="White",bg="Black",command=submit2)
    submitBtn.place(x=250,y=390)
    
    window2.mainloop()


def submit2():
    name = str(e1.get())
    roll = str(e2.get())
    ID = str(e3.get())
    studentClass = int(a.get())
    section = str(sec.get())

    window1.destroy()


    lang = int(e4.get())
    lit = int(e5.get())
    math = int(e6.get())
    hin = int(e7.get())
    phy = int(e8.get())
    chem = int(e9.get())
    bio = int(e10.get())
    his = int(e11.get())
    geo = int(e12.get())
    com_eco = int(e13.get())

    window2.destroy()
    
    percentage = bestOf5(lang,lit,math,hin,phy,chem,bio,his,geo,com_eco)

    if(percentage>=90):msg = "You are a sincere and hard working child ! Keep up your good work "
    elif(percentage<90 and percentage>=80): msg="You are a Go Getter ! Keep it up and wish you good luck to achieve more"
    elif(percentage<80 and percentage>=70): msg="Promoted"
    else: msg = "Study Well !"
    
    #CREATING PDF FROM HERE
    pdf = FPDF()
    pdf.add_page()
    img1 = pdf.image('images/logo.png',10,10)
    pdf.set_text_color(250,0,80)
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(250,20,txt="Report Card 2022",ln=1,align="C")
    pdf.set_font("Times",size = 12)

    pdf.set_text_color(0,0,0)
    pdf_w=210
    pdf_h=297
    pdf.set_line_width(0.0)

    pdf.rect(5.0, 5.0, 200.0,287.0)

    #pdf.rect(8.0, 8.0, 194.0,282.0)

    pdf.set_fill_color(170,225,230)
    pdf.rect(12,40,186,63,'DF')
    img2 = pdf.image('images/new.png',140,45)

    txt1 = "NAME : " + name
    txt2 = "ROLL NO : " + roll
    txt3 = "ID NO : " + ID
    txt4 = "CLASS : " + str(studentClass)
    txt5 = "SECTION : " + str(section)

    pdf.rect(50,110,80,110)
    pdf.rect(130,110,30,110)

    pdf.set_fill_color(163,98,170)
    pdf.rect(50,110,80,10,'DF')
    pdf.rect(130,110,30,10,'DF')

    cell_h = 10

    pdf.set_fill_color(48,172,220)
    pdf.rect(50,120,80,100,'DF')
    pdf.rect(130,120,30,100,'DF')


    pdf.rect(50,110,110,10)

    pdf.rect(50,120,110,10,)
    pdf.rect(50,130,110,10)
    pdf.rect(50,140,110,10)
    pdf.rect(50,150,110,10)
    pdf.rect(50,160,110,10)
    pdf.rect(50,170,110,10)
    pdf.rect(50,180,110,10)
    pdf.rect(50,190,110,10)
    pdf.rect(50,200,110,10)
    pdf.rect(50,210,110,10)



    # RECTANGLE (5,40) (205,40) (5,82) (205,82)
    pdf.set_font("Times",size = 12)
    img2 = pdf.image('images/new.png',265,40)
    pdf.cell(200,20,txt="",ln=2)
    pdf.cell(75,8,txt=txt1,align='C',ln=3)
    pdf.cell(47,8,txt=txt2,align='C',ln=4)
    pdf.cell(51,8,txt=txt3,align='C',ln=5)
    pdf.cell(43,8,txt=txt4,align='C',ln=6)
    pdf.cell(47,8,txt=txt5,align='C',ln=7)

    pdf.cell(200,20,txt="",ln=8)

    txt16 = "Subject                                            Marks"
    txt6 = "English Language " +"                                       " + str(lang)
    txt7 = "English Literature " +"                                       " + str(lit)
    txt8 = "   Mathematics" +"                                             " + str(math)
    txt9 = "        Hindi" +"                                                   " + str(hin)
    txt10 = "  Physics         " +"                                            " + str(phy)
    txt11 = "  Chemistry      " +"                                          " + str(chem)
    txt12 = "   Biology      " +"                                            " + str(bio)
    txt13 = "History & Civics " +"                                      " + str(his)
    txt14 = "Geography  " + "                                             " + str(geo)
    txt15 = "Computer/Eco Applications          "+"          " + str(com_eco)

    pdf.cell(200,10,txt=txt16,align="C",ln=8)
    pdf.cell(200,10,txt=txt6,align ="C",ln=9)
    pdf.cell(200,10,txt=txt7,align ="C",ln=10)
    pdf.cell(200,10,txt=txt8,align ="C",ln=11)
    pdf.cell(200,10,txt=txt9,align ="C",ln=12)
    pdf.cell(200,10,txt=txt10,align ="C",ln=13)
    pdf.cell(200,10,txt=txt11,align ="C",ln=14)
    pdf.cell(200,10,txt=txt12,align ="C",ln=15)
    pdf.cell(200,10,txt=txt13,align ="C",ln=16)
    pdf.cell(200,10,txt=txt14,align ="C",ln=17)
    pdf.cell(200,10,txt=txt15,align ="C",ln=18)

    pdf.cell(200,10,txt="",ln=19)

    pdf.set_fill_color(130,210,120)
    pdf.rect(15,230,180,20,'DF')

    msg = "You are a sincere and hard working child ! Keep up your good work "
    remarks = "REMARKS :  " + msg

    txtPer = "PERCENTAGE : " + str(percentage)
    pdf.cell(200,10,txt=txtPer,align="C",ln=20)
    pdf.cell(200,10,txt=remarks,align="C",ln=21)

    now = datetime.now()
    date = now.strftime("%d.%m.%Y")

    pdf.cell(200,10,txt="",ln=22)
    txtPrint = "Date : " + date + "                                                 Class Teacher                                                            Principal"
    pdf.cell(25,4,txt = txtPrint,ln=23)


    pdf.output("report card.pdf")


def openTwitter():
    webbrowser.open('https://www.twitter.com/imbinit17')

def openGithub():
    webbrowser.open('https://www.github.com/imbinit17')
    
def function():
    #global logo
    global window1
    
    window1 = Tk()
    window1.geometry("550x700")
    window1.title("Student Result Dashboard")


    logo = PhotoImage(file='images\logo.png')
    global label1
    label1 = Label(window1,image=logo).place(x=0,y=0)

    label2 = Label(window1,text="Welcome",font=("Cambria",35)).place(x=250)

    label3 = Label(window1,text="Enter the name of the student ",font=("Times New Roman",13)).place(y=80)
    label4 = Label(window1,text="Enter the roll number of the student ",font=("Times New Roman",13)).place(y=110)
    label5 = Label(window1,text="Enter the ID No. of the student ",font=("Times New Roman",13)).place(y=140)
    label6 = Label(window1,text="Select the class of the student ",font=("Times New Roman",13)).place(y=170)

    global e1
    global e2
    global e3
    
    e1 = Entry(window1,width=30,font=("Times New Roman",13))
    e1.place(x=270,y=80)
    e2 = Entry(window1,width=30,font=("Times New Roman",13))
    e2.place(x=270,y=110)
    e3 = Entry(window1,width=30,font=("Times New Roman",13))
    e3.place(x=270,y=140)

    global a
    global sec
        
    a = IntVar()
    btn1 = Radiobutton(window1,text="CLASS 1 ",variable=a,value=1,font=("Times New Roman",13)).place(y=200)
    btn2 = Radiobutton(window1,text="CLASS 2 ",variable=a,value=2,font=("Times New Roman",13)).place(y=220)
    btn3 = Radiobutton(window1,text="CLASS 3 ",variable=a,value=3,font=("Times New Roman",13)).place(y=240)
    btn4 = Radiobutton(window1,text="CLASS 4 ",variable=a,value=4,font=("Times New Roman",13)).place(y=260)
    btn5 = Radiobutton(window1,text="CLASS 5 ",variable=a,value=5,font=("Times New Roman",13)).place(y=280)
    btn6 = Radiobutton(window1,text="CLASS 6 ",variable=a,value=6,font=("Times New Roman",13)).place(y=300)
    btn7 = Radiobutton(window1,text="CLASS 7 ",variable=a,value=7,font=("Times New Roman",13)).place(y=320)
    btn8 = Radiobutton(window1,text="CLASS 8 ",variable=a,value=8,font=("Times New Roman",13)).place(y=340)
    btn9 = Radiobutton(window1,text="CLASS 9 ",variable=a,value=9,font=("Times New Roman",13)).place(y=360)
    btn10 = Radiobutton(window1,text="CLASS 10 ",variable=a,value=10,font=("Times New Roman",13)).place(y=380)
    btn11 = Radiobutton(window1,text="CLASS 11 ",variable=a,value=11,font=("Times New Roman",13)).place(y=400)
    btn12 = Radiobutton(window1,text="CLASS 12 ",variable=a,value=12,font=("Times New Roman",13)).place(y=420)

    sec = StringVar()
    label7 = Label(window1,text="Select the section of the student ",font=("Times New Roman",13)).place(y=450)
    btn1 = Radiobutton(window1,text="A ",variable=sec,value='A',font=("Times New Roman",13)).place(y=470)
    btn1 = Radiobutton(window1,text="B ",variable=sec,value='B',font=("Times New Roman",13)).place(y=490)
    btn1 = Radiobutton(window1,text="C ",variable=sec,value='C',font=("Times New Roman",13)).place(y=510)

    
    label8 = Label(window1,text="Upload an image of the student ",font=("Times New Roman",13)).place(y=540)
    imageBtn = Button(window1,text="Upload Image",font=("Times New Roman",13),fg="White",bg="Blue",command=addImg)
    imageBtn.place(x=15,y=560)

    submitBtn = Button(window1,text="Submit",font=("Times New Roman",13),fg="White",bg="Black",command=submit1)
    submitBtn.place(x=250,y=600)

    twitterIcon = PhotoImage(file='images/twitter.png')
    tBtn = Button(window1,image=twitterIcon,command = openTwitter)
    tBtn.place(x=350,y =400)

    githubIcon = PhotoImage(file='images/github.png')
    gBtn = Button(window1,image=githubIcon,command = openGithub)
    gBtn.place(x=410,y=400)
        
    window1.mainloop()
function()
