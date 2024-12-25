from tkinter import*
mw=Tk()
def siva():
    name=input.get()
    nametext="Thank You For Entering Your Name Dear"+"!"
    my="Hello My Dear "+name+"!"+"\n"+"One friend can change everything in life, bringing endless happiness. For me, that friend is you."+"\n"+"You have filled my life with joy and made it so much brighter."+"\n"+" Without you, I can’t imagine my B.Tech journey. You are not just the best person but also the most special person in my life."+"\n"+"Over these four years, we have grown so close, and I deeply cherish our bond."+"\n"+" I truly admire and love your friendship."+"\n"+"Sometimes, I feel like you are my good luck charm because being with you makes everything better."+"\n"+" At other times, I feel like the luckiest person because I have a friend like you."+"\n"+"Thank you for coming into my life and being such a wonderful part of it."+"\n"+"......Finally!"+"\n"+"I want to say—I love you, my dear friend......!"
    if(name=="manju"):
        text.config(text=nametext+"\n"+my,font=("italic",15))
        input.delete(0,END)
    elif (name == ""):
        text.config(text="Please Enter Your Good Name!")
    elif (name == "siva"):
        text.config(text="Your friend is siva")
    elif(name!="manju"):
        text.config(text="This Page Only Belongs To My Bestie Not For You,So Please You Can Close It")

    elif(name==""):
        text.config(text="nter your name")
text=Label(mw,text="Hello My_dear friend!",font=("bold",25))
text.pack()
input=Entry(mw,width=20)
input.pack(pady=5)
text=Label(mw,text="Please Enter Your Good Name!",font=("bold",25))
text.pack()
btn=Button(mw,text="Press Me!",padx=10,pady=10,font=("bold",10),command=siva)
btn.pack(pady=5)
cre=Label(mw,text="Created By SIVA NARAYANA",font=("bold",12))
cre.pack(side=BOTTOM)
mw.mainloop()