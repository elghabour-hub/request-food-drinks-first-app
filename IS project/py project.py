from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Listbox

root=Tk()
root.title("Request food & Drinks")
root.configure(background="#e1d8b2")
#-----------style-----------
'''
style=ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background="#e1d8b2")
style.configure('TButton',background='#e1d8b2')
style.configure('TRadiobutton',background='#e1d8b2')
'''
ttk.Button(root,text=" The menu ").grid(row=0,column=0,columnspan=10,sticky='snew')
ttk.Button(root,text="Your order").grid(row=0,column=10,columnspan=3,rowspan=2,sticky='snew')
ttk.Label(root,text="Type").grid(row=2,column=0)
ttk.Label(root,text="Price").grid(row=2,column=1)
ttk.Button(root,text="Drinks").grid(row=1,column=6,columnspan=4,sticky='snew')
ttk.Button(root,text="Food").grid(row=1,column=0,columnspan=6,sticky='snew')
ttk.Label(root,text="Type").grid(row=2,column=6)
ttk.Label(root,text="Price").grid(row=2,column=7)
ttk.Label(root,text="Number").grid(row=2,column=3)
ttk.Label(root,text="Number").grid(row=2,column=8)

#-----------type of food-----------
ttk.Label(root,text="تشيز بررجر").grid(row=4,column=0,)
ttk.Label(root,text=" برجر شاورما").grid(row=5,column=0,)
ttk.Label(root,text="تشيز برجر ديلوكس").grid(row=6,column=0)
ttk.Label(root,text="بيف برجر").grid(row=7,column=0)
ttk.Label(root,text="شاورما دجاج").grid(row=8,column=0)
ttk.Label(root,text="شاورما لحمه").grid(row=9,column=0)
ttk.Label(root,text="فته شورما").grid(row=10,column=0)
ttk.Label(root,text="فته شورما ميكس").grid(row=11,column=0)
ttk.Label(root,text="شاورما موزريلا ومشروم").grid(row=12,column=0)
ttk.Label(root,text="شيش طاووق").grid(row=13,column=0)
ttk.Label(root,text="تشيز تشكن برجر").grid(row=14,column=0)
ttk.Label(root,text="كباب جريل").grid(row=15,column=0)
ttk.Label(root,text="بطاطس مع الجبنه").grid(row=16,column=0)
ttk.Label(root,text="فرخه مشويه").grid(row=17,column=0)
ttk.Label(root,text="نص فرخه مشويه").grid(row=18,column=0)
ttk.Label(root,text="كيلو كباب").grid(row=19,column=0)
ttk.Label(root,text="كيلو كباب شامي").grid(row=20,column=0)
ttk.Label(root,text="كيلو ميكس").grid(row=21,column=0)
ttk.Label(root,text="كيلو شيش طاوق ").grid(row=22,column=0)
ttk.Label(root,text="برجر بيض وجبنه").grid(row=23,column=0)

#---------Type of drinks---------
ttk.Label(root,text="قهوه").grid(row=4,column=6)
ttk.Label(root,text="قهوه تركي").grid(row=5,column=6)
ttk.Label(root,text="قهوه بندق").grid(row=6,column=6)
ttk.Label(root,text="قهوه فرنساوي").grid(row=7,column=6)
ttk.Label(root,text="لاتيه").grid(row=8,column=6)
ttk.Label(root,text="كابتشينو").grid(row=9,column=6)
ttk.Label(root,text="نسكافيه").grid(row=10,column=6)
ttk.Label(root,text="شاي").grid(row=11,column=6)
ttk.Label(root,text="ينسون").grid(row=12,column=6)
ttk.Label(root,text="نعناع").grid(row=13,column=6)
ttk.Label(root,text="مانجا").grid(row=14,column=6)
ttk.Label(root,text="برتقال").grid(row=15,column=6)
ttk.Label(root,text="فراوله").grid(row=16,column=6)
ttk.Label(root,text="جوافه").grid(row=17,column=6)

#---------price of food------------
ttk.Label(root,text="21  L.E").grid(row=4,column=1)
ttk.Label(root,text="31  L.E").grid(row=5,column=1)
ttk.Label(root,text="20  L.E").grid(row=6,column=1)
ttk.Label(root,text="15  L.E").grid(row=7,column=1)
ttk.Label(root,text="30  L.E").grid(row=8,column=1)
ttk.Label(root,text="35  L.E").grid(row=9,column=1)
ttk.Label(root,text="150  L.E").grid(row=10,column=1)
ttk.Label(root,text="160  L.E").grid(row=11,column=1)
ttk.Label(root,text="24  L.E").grid(row=12,column=1)
ttk.Label(root,text="30  L.E").grid(row=13,column=1)
ttk.Label(root,text="28  L.E").grid(row=14,column=1)
ttk.Label(root,text="28  L.E").grid(row=15,column=1)
ttk.Label(root,text="13  L.E").grid(row=16,column=1)
ttk.Label(root,text="140  L.E").grid(row=17,column=1)
ttk.Label(root,text="70  L.E").grid(row=18,column=1)
ttk.Label(root,text="260  L.E").grid(row=19,column=1)
ttk.Label(root,text="200  L.E").grid(row=20,column=1)
ttk.Label(root,text="220  L.E").grid(row=21,column=1)
ttk.Label(root,text="160  L.E").grid(row=22,column=1)
ttk.Label(root,text="17  L.E").grid(row=23,column=1)

#-------------price of drinks---------
ttk.Label(root,text="10  L.E").grid(row=4,column=7)
ttk.Label(root,text="15  L.E").grid(row=5,column=7)
ttk.Label(root,text="5  L.E").grid(row=6,column=7)
ttk.Label(root,text="7  L.E").grid(row=7,column=7)
ttk.Label(root,text="18  L.E").grid(row=8,column=7)
ttk.Label(root,text="7  L.E").grid(row=9,column=7)
ttk.Label(root,text="14  L.E").grid(row=10,column=7)
ttk.Label(root,text="5  L.E").grid(row=11,column=7)
ttk.Label(root,text="8  L.E").grid(row=12,column=7)
ttk.Label(root,text="61  L.E").grid(row=13,column=7)
ttk.Label(root,text="19  L.E").grid(row=14,column=7)
ttk.Label(root,text="17  L.E").grid(row=15,column=7)
ttk.Label(root,text="99 L.E").grid(row=16,column=7)
ttk.Label(root,text="171 L.E").grid(row=17,column=7)

#----------click of food-------------
ord1=ttk.Button(root,text="click")
ord1.grid(row=4,column=4)
ord1.config(command=lambda :buclick(f"تشيز برجر-{num1.get()}"))

ord2=ttk.Button(root,text="click")
ord2.grid(row=5,column=4)
ord2.config(command=lambda :buclick(f"برجر شاورما_{num2.get()}"))

ord3=ttk.Button(root,text="click")
ord3.grid(row=6,column=4)
ord3.config(command=lambda :buclick(f"تشيز برجر ديلوكس_{num3.get()} "))

ord4=ttk.Button(root,text="click")
ord4.grid(row=7,column=4)
ord4.config(command=lambda :buclick(f"بيف برجر _{num4.get()}"))

ord5=ttk.Button(root,text="click")
ord5.grid(row=8,column=4)
ord5.config(command=lambda :buclick(f"شاورما دجاج_{num5.get()}"))

ord6=ttk.Button(root,text="click")
ord6.grid(row=9,column=4)
ord6.config(command=lambda :buclick(f"شاورما لحمه _{num6.get()}"))

ord7=ttk.Button(root,text="click")
ord7.grid(row=10,column=4)
ord7.config(command=lambda :buclick(f"فته شاورما _{num7.get()}"))

ord8=ttk.Button(root,text="click")
ord8.grid(row=11,column=4)
ord8.config(command=lambda :buclick(f"فته شاورما ميكس_{num8.get()}"))

ord9=ttk.Button(root,text="click")
ord9.grid(row=12,column=4)
ord9.config(command=lambda :buclick(f"_شاورما مودزريلا ومشروم{num9.get()}"))

ord10=ttk.Button(root,text="click")
ord10.grid(row=13,column=4)
ord10.config(command=lambda :buclick(f"شيش طاوق_{num10.get()}"))

ord11=ttk.Button(root,text="click")
ord11.grid(row=14,column=4)
ord11.config(command=lambda :buclick(f"تشيز تشكن برجر_{num11.get()}"))

ord12=ttk.Button(root,text="click")
ord12.grid(row=15,column=4)
ord12.config(command=lambda :buclick(f"كباب جريل_{num12.get()}"))

ord13=ttk.Button(root,text="click")
ord13.grid(row=16,column=4)
ord13.config(command=lambda :buclick(f" بطاطس مع الجبنه_{num13.get()}"))

ord14=ttk.Button(root,text="click")
ord14.grid(row=17,column=4)
ord14.config(command=lambda :buclick(f"فرخه مشويه_{num14.get()}"))

ord15=ttk.Button(root,text="click")
ord15.grid(row=18,column=4)
ord15.config(command=lambda :buclick(f"نص فرخه مشويه_{num15.get()}"))

ord16=ttk.Button(root,text="click")
ord16.grid(row=19,column=4)
ord16.config(command=lambda :buclick(f"كيلو كباب{num16.get()}"))

ord17=ttk.Button(root,text="click")
ord17.grid(row=20,column=4)
ord17.config(command=lambda :buclick(f"كيلو كباب شامي_{num17.get()}"))

ord18=ttk.Button(root,text="click")
ord18.grid(row=21,column=4)
ord18.config(command=lambda :buclick(f"كيلو ميكس_{num18.get()}"))

ord19=ttk.Button(root,text="click")
ord19.grid(row=22,column=4)
ord19.config(command=lambda :buclick(f"كيلو شيش طاوق_{num19.get()}"))

ord20=ttk.Button(root,text="click")
ord20.grid(row=23,column=4)
ord20.config(command=lambda :buclick(f"برجر بيض وجبنه_{num20.get()}"))

#-----click of drink--------

drn1=ttk.Button(root,text="click")
drn1.grid(row=4,column=9)
drn1.config(command=lambda :buclick(f"قهوه_{num21.get()}"))

drn2=ttk.Button(root,text="click")
drn2.grid(row=5,column=9)
drn2.config(command=lambda :buclick(f"قهوه تركي_{num22.get()}"))

drn3=ttk.Button(root,text="click")
drn3.grid(row=6,column=9)
drn3.config(command=lambda :buclick(f"قهوه بندق_{num23.get()}"))

drn4=ttk.Button(root,text="click")
drn4.grid(row=7,column=9)
drn4.config(command=lambda :buclick(f"قهوه فرنساوي_{num24.get()}"))

drn5=ttk.Button(root,text="click")
drn5.grid(row=8,column=9)
drn5.config(command=lambda :buclick(f"لاتيه-{num25.get()}"))

drn6=ttk.Button(root,text="click")
drn6.grid(row=9,column=9)
drn6.config(command=lambda :buclick(f"كابتشينو_{num26.get()}"))

drn7=ttk.Button(root,text="click")
drn7.grid(row=10,column=9)
drn7.config(command=lambda :buclick(f"نسكافيه_{num27.get()}"))

drn8=ttk.Button(root,text="click")
drn8.grid(row=11,column=9)
drn8.config(command=lambda :buclick(f"شاي_{num28.get()}"))

drn9=ttk.Button(root,text="click")
drn9.grid(row=12,column=9)
drn9.config(command=lambda :buclick(f"ينسون_{num29.get()}"))

drn10=ttk.Button(root,text="click")
drn10.grid(row=13,column=9)
drn10.config(command=lambda :buclick(f"نعناع_{num30.get()}"))

drn11=ttk.Button(root,text="click")
drn11.grid(row=14,column=9)
drn11.config(command=lambda :buclick(f"مانجا_{num31.get()}"))

drn12=ttk.Button(root,text="click")
drn12.grid(row=15,column=9)
drn12.config(command=lambda :buclick(f"برتقال_{num32.get()}"))

drn13=ttk.Button(root,text="click")
drn13.grid(row=16,column=9)
drn13.config(command=lambda :buclick(f"فراوله_{num33.get()}"))

drn14=ttk.Button(root,text="click")
drn14.grid(row=17,column=9)
drn14.config(command=lambda :buclick(f"جوافه_{num34.get()}"))


#--------the number of menu-----
varnum1=IntVar()
varnum2=IntVar()
varnum3=IntVar()
varnum4=IntVar()
varnum5=IntVar()
varnum6=IntVar()
varnum7=IntVar()
varnum8=IntVar()
varnum9=IntVar()
varnum10=IntVar()
varnum11=IntVar()
varnum12=IntVar()
varnum13=IntVar()
varnum14=IntVar()
varnum15=IntVar()
varnum16=IntVar()
varnum17=IntVar()
varnum18=IntVar()
varnum19=IntVar()
varnum20=IntVar()
varnum21=IntVar()
varnum22=IntVar()
varnum23=IntVar()
varnum24=IntVar()
varnum25=IntVar()
varnum26=IntVar()
varnum27=IntVar()
varnum28=IntVar()
varnum29=IntVar()
varnum30=IntVar()
varnum31=IntVar()
varnum32=IntVar()
varnum33=IntVar()
varnum34=IntVar()


varnum1.set("0")
varnum2.set("0")
varnum3.set("0")
varnum4.set("0")
varnum5.set("0")
varnum5.set("0")
varnum6.set("0")
varnum7.set("0")
varnum8.set("0")
varnum9.set("0")
varnum10.set("0")
varnum11.set("0")
varnum12.set("0")
varnum13.set("0")
varnum14.set("0")
varnum15.set("0")
varnum16.set("0")
varnum17.set("0")
varnum18.set("0")
varnum19.set("0")
varnum20.set("0")
varnum21.set("0")
varnum22.set("0")
varnum23.set("0")
varnum24.set("0")
varnum25.set("0")
varnum26.set("0")
varnum27.set("0")
varnum28.set("0")
varnum29.set("0")
varnum30.set("0")
varnum31.set("0")
varnum32.set("0")
varnum33.set("0")
varnum34.set("0")



num1=ttk.Entry(root,textvariable=varnum1)
num1.grid(row=4,column=3)

num2=ttk.Entry(root,textvariable=varnum2)
num2.grid(row=5,column=3)

num3=ttk.Entry(root,textvariable=varnum3)
num3.grid(row=6,column=3)

num4=ttk.Entry(root,textvariable=varnum4)
num4.grid(row=7,column=3)

num5=ttk.Entry(root,textvariable=varnum5)
num5.grid(row=8,column=3)

num6=ttk.Entry(root,textvariable=varnum6)
num6.grid(row=9,column=3)

num7=ttk.Entry(root,textvariable=varnum7)
num7.grid(row=10,column=3)

num8=ttk.Entry(root,textvariable=varnum8)
num8.grid(row=11,column=3)

num9=ttk.Entry(root,textvariable=varnum9)
num9.grid(row=12,column=3)

num10=ttk.Entry(root,textvariable=varnum10)
num10.grid(row=13,column=3)

num11=ttk.Entry(root,textvariable=varnum11)
num11.grid(row=14,column=3)

num12=ttk.Entry(root,textvariable=varnum12)
num12.grid(row=15,column=3)

num13=ttk.Entry(root,textvariable=varnum13)
num13.grid(row=16,column=3)

num14=ttk.Entry(root,textvariable=varnum14)
num14.grid(row=17,column=3)

num15=ttk.Entry(root,textvariable=varnum15)
num15.grid(row=18,column=3)

num16=ttk.Entry(root,textvariable=varnum16)
num16.grid(row=19,column=3)

num17=ttk.Entry(root,textvariable=varnum17)
num17.grid(row=20,column=3)

num18=ttk.Entry(root,textvariable=varnum18)
num18.grid(row=21,column=3)

num19=ttk.Entry(root,textvariable=varnum19)
num19.grid(row=22,column=3)

num20=ttk.Entry(root,textvariable=varnum20)
num20.grid(row=23,column=3)

#--------the number of drinks-----
num21=ttk.Entry(root,textvariable=varnum21)
num21.grid(row=4,column=8)

num22=ttk.Entry(root,textvariable=varnum22)
num22.grid(row=5,column=8)

num23=ttk.Entry(root,textvariable=varnum23)
num23.grid(row=6,column=8)

num24=ttk.Entry(root,textvariable=varnum24)
num24.grid(row=7,column=8)

num25=ttk.Entry(root,textvariable=varnum25)
num25.grid(row=8,column=8)

num26=ttk.Entry(root,textvariable=varnum26)
num26.grid(row=9,column=8)

num27=ttk.Entry(root,textvariable=varnum27)
num27.grid(row=10,column=8)

num28=ttk.Entry(root,textvariable=varnum28)
num28.grid(row=11,column=8)

num29=ttk.Entry(root,textvariable=varnum29)
num29.grid(row=12,column=8)

num30=ttk.Entry(root,textvariable=varnum30)
num30.grid(row=13,column=8)

num31=ttk.Entry(root,textvariable=varnum31)
num31.grid(row=14,column=8)

num32=ttk.Entry(root,textvariable=varnum32)
num32.grid(row=15,column=8)

num33=ttk.Entry(root,textvariable=varnum33)
num33.grid(row=16,column=8)

num34=ttk.Entry(root,textvariable=varnum34)
num34.grid(row=17,column=8)


#----------bill of the order----------

def calculate():
    mil1    =(varnum1.get()*21)
    mil2    =(varnum2.get()*31)
    mil3    =(varnum3.get()*20)
    mil4    =(varnum4.get()*15)
    mil5    =(varnum5.get()*30)
    mil6    =(varnum6.get()*35)
    mil7    =(varnum7.get()*150)
    mil8    =(varnum8.get()*160)
    mil9    =(varnum9.get()*24)
    mil10   =(varnum10.get()*30)
    mil11   =(varnum11.get()*28)
    mil12   =(varnum12.get()*28)
    mil13   =(varnum13.get()*13)
    mil14   =(varnum14.get()*140)
    mil15   =(varnum15.get()*70)
    mil16   =(varnum16.get()*260)
    mil17   =(varnum17.get()*200)
    mil18   =(varnum18.get()*220)
    mil19   =(varnum19.get()*160)
    mil20   =(varnum20.get()*17)
    mil21   =(varnum21.get()*10)
    mil22   =(varnum22.get()*15)
    mil23   =(varnum23.get()*5)
    mil24   =(varnum24.get()*7)
    mil25   =(varnum25.get()*18)
    mil26   =(varnum26.get()*7)
    mil27   =(varnum27.get()*14)
    mil28   =(varnum28.get()*5)
    mil29   =(varnum29.get()*8)
    mil30   =(varnum30.get()*61)
    mil31   =(varnum31.get()*19)
    mil32   =(varnum32.get()*17)
    mil33   =(varnum33.get()*99)
    mil34   =(varnum34.get()*171)

    total=(mil1 + mil2 + mil3 + mil4 + mil5 + mil6 + mil7 + mil8 + mil9 + mil10
           + mil11 + mil12 + mil13 + mil14 + mil15 + mil16 + mil17 + mil18 + mil19
           + mil20 + mil21 + mil22 + mil23 + mil24 + mil25 + mil26 + mil27 + mil28 + mil29 + mil30
           + mil31 + mil32 + mil33 + mil34)
    bill = Button(root,text = f" =  {total }    L.E")
    bill.grid(row=14, column=11)

'''

#-----------time of the order--------
def time_calculate():
    time1=varnum1.get()
    time2 = varnum2.get()
    time3 = varnum3.get()
    time4 = varnum4.get()
    time5 = varnum5.get()
    time6 = varnum6.get()
    time7 = varnum7.get()
    time8 = varnum8.get()
    time9 = varnum9.get()
    time10 = varnum10.get()
    time11 = varnum11.get()
    time12 = varnum12.get()
    time13 = varnum13.get()
    time14 = varnum14.get()
    time15 = varnum15.get()
    time16 = varnum16.get()
    time17 = varnum17.get()
    time18 = varnum18.get()
    time19 = varnum19.get()
    time20 = varnum20.get()
    time21 = varnum21.get()
    time22 = varnum22.get()
    time23 = varnum23.get()
    time24 = varnum24.get()
    time25 = varnum25.get()
    time26 = varnum26.get()
    time27 = varnum27.get()
    time28 = varnum28.get()   
    time29 = varnum29.get()
    time30 = varnum30.get()
    time31 = varnum31.get()
    time32 = varnum32.get()
    time33 = varnum33.get()
    time34 = varnum34.get() 


    total_time = (time1+time2+time3+time4+time5+time6+time7+time8+time9
                  +time10+time11+time12+time13+time14+time15+time16+time17
                  +time18+time19+time20+time21+time22+time23+time24+time25+time26+time27
                  +time28+time29+time30+time31+time32+time33+time34 )
    time = Button(root, text=f"{total_time} minute")
    time.grid(row=23, column=11)

'''
#------------listbox-------------
lbx=Listbox(root)
lbx.grid(row=4,column=10,columnspan=3,rowspan=10,ipadx=30,ipady=120)

#----------bill of the order----------
ttk.Button(root, text="bill", command=calculate).grid(row=14, column=10)
'''
#---------time of the order--------
ttk.Button(root,text=" time ",command=time_calculate).grid(row=15,column=10)
'''

#------------ try again  -----------

delete=ttk.Button(root,text=" try again")
delete.grid(row=20,column=9)
delete.config(command=lambda :tryagain("delete all"))
#------------ Exit ---------------
Ex=ttk.Button(root,text="Exit")
Ex.grid(row=20,column=8)
Ex.config(command=lambda :iExit())

def iExit():
    qExit=messagebox.askyesno("fast food","Do you want to  Exit ?")
    if qExit > 0:
        root.destroy()
        return

def buclick(one):
    lbx.insert("end",one)

    
    #print("1:{}".format(one))
def tryagain(two):

    lbx.delete(0,'end')
    num1.delete(0,"end")
    num2.delete(0,'end')
    num3.delete(0, 'end')
    num4.delete(0, 'end')
    num5.delete(0, 'end')
    num6.delete(0, 'end')
    num7.delete(0, 'end')
    num8.delete(0, 'end')
    num9.delete(0, 'end')
    num10.delete(0, 'end')
    num11.delete(0, 'end')
    num12.delete(0, 'end')
    num13.delete(0, 'end')
    num14.delete(0, 'end')
    num15.delete(0, 'end')
    num16.delete(0, 'end')
    num17.delete(0, 'end')
    num18.delete(0, 'end')
    num19.delete(0, 'end')
    num20.delete(0, 'end')
    num21.delete(0, 'end')
    num22.delete(0, 'end')
    num23.delete(0, 'end')
    num24.delete(0, 'end')
    num25.delete(0, 'end')
    num26.delete(0, 'end')
    num27.delete(0, 'end')
    num28.delete(0, 'end')
    num29.delete(0, 'end')
    num30.delete(0, 'end')
    num31.delete(0, 'end')
    num32.delete(0, 'end')
    num33.delete(0, 'end')
    num34.delete(0, 'end')

    varnum1.set("0")
    varnum2.set("0")
    varnum3.set("0")
    varnum4.set("0")
    varnum5.set("0")
    varnum5.set("0")
    varnum6.set("0")
    varnum7.set("0")
    varnum8.set("0")
    varnum9.set("0")
    varnum10.set("0")
    varnum11.set("0")
    varnum12.set("0")
    varnum13.set("0")
    varnum14.set("0")
    varnum15.set("0")
    varnum16.set("0")
    varnum17.set("0")
    varnum18.set("0")
    varnum19.set("0")
    varnum20.set("0")
    varnum21.set("0")
    varnum22.set("0")
    varnum23.set("0")
    varnum24.set("0")
    varnum25.set("0")
    varnum26.set("0")
    varnum27.set("0")
    varnum28.set("0")
    varnum29.set("0")
    varnum30.set("0")
    varnum31.set("0")
    varnum32.set("0")
    varnum33.set("0")
    varnum34.set("0")


def busavedata():

    print("your order is :{}".format(lbx.get()))


#print("no any think here")
root.mainloop()
