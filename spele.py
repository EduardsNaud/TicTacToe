from tkinter import*
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk()
mansLogs.title('TicTacToe')

speletajsX=True #Tas kurš liks krustiņus
count=0 #aizpildīto rūtiņu skaits

def resets():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)

    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""

    global winner, count, speletajsX
    winner=False
    count=0
    speletajsX=True
    return 0


def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title('Info par programmu')
    jaunsLogs.geometry("412x300")
    apraksts=Label(jaunsLogs,text="Spēles noteikumi")
    apraksts.grid(row=0,column=0)
    apraksts=Label(jaunsLogs,text="1. Spēle tiek spēlēta 3x3 režģī")
    apraksts.grid(row=1,column=0)
    apraksts=Label(jaunsLogs,text="2. Pirmais sāk spēlēt X spēlētājs")
    apraksts.grid(row=2,column=0)
    apraksts=Label(jaunsLogs,text="3. Uzvar spelētājs kurš iegūst trīs lauciņus horizontāli,vertikāli vai pa diagonāli")
    apraksts.grid(row=3,column=0)
    return 0



def disableButtons():
 btn1.config(state=DISABLED) #DISABLED = [poga izslēgta]
 btn2.config(state=DISABLED)
 btn3.config(state=DISABLED)
 btn4.config(state=DISABLED)
 btn5.config(state=DISABLED)
 btn6.config(state=DISABLED)
 btn7.config(state=DISABLED)
 btn8.config(state=DISABLED)
 btn9.config(state=DISABLED)


def btnClick(button): #tukša poga tiek padota
    global speletajsX,count #mainīgie kuri tiks izmantoti
    if button ["text"]=="" and speletajsX==True: #Spēlē X speletājs
        button["text"]="X" #maina lauciņu uz X
        speletajsX=False
        count+=1 #Aizpilda rūtiņu kurā vairs nevarēs likt
        checkWinner()
    elif button["text"]=="" and speletajsX==False:
        button["text"]="O" #maina lauciņu uz O
        speletajsX=True
        count+=1 #Aizpilda rūtiņu kurā vairs nevarēs likt
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šis lauciņš jau ir izmantots!")
    
def checkWinner():
    global winner
    if (btn1["text"]=="X" and btn2["text"]=="X"and btn3["text"]=="X"or
    btn4["text"]=="X"and btn5["text"]=="X"and btn6["text"]=="X"or
    btn7["text"]=="X"and btn8["text"]=="X"and btn9["text"]=="X"or
    btn1["text"]=="X"and btn5["text"]=="X"and btn7["text"]=="X"or
    btn2["text"]=="X"and btn5["text"]=="X"and btn8["text"]=="X"or
    btn3["text"]=="X"and btn6["text"]=="X"and btn9["text"]=="X"or
    btn1["text"]=="X"and btn5["text"]=="X"and btn9["text"]=="X"or
    btn3["text"]=="X"and btn5["text"]=="X"and btn7["text"]=="X"):
     winner=True
     disableButtons()
     messagebox.showinfo("TicTacToe", "Speletajs X ir uzvarētājs")
    elif (btn1["text"]=="O" and btn2["text"]=="O"and btn3["text"]=="O"or
    btn4["text"]=="O"and btn5["text"]=="O"and btn6["text"]=="O"or
    btn7["text"]=="O"and btn8["text"]=="O"and btn9["text"]=="O"or
    btn1["text"]=="O"and btn4["text"]=="O"and btn7["text"]=="O"or
    btn2["text"]=="O"and btn5["text"]=="O"and btn8["text"]=="O"or
    btn3["text"]=="O"and btn6["text"]=="O"and btn9["text"]=="O"or
    btn1["text"]=="O"and btn5["text"]=="O"and btn9["text"]=="O"or
    btn3["text"]=="O"and btn5["text"]=="O"and btn7["text"]=="O"):
     winner=True
     disableButtons()
     messagebox.showinfo("TicTacToe", "Speletajs O ir uzvarētājs")
    elif count==9:
     messagebox.showinfo("TicTacToe", "Neviens nav uzvarējis")
     disableButtons()

btn1=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn1))
btn2=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn2))
btn3=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn3))
btn4=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn4))
btn5=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn5))
btn6=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn6))
btn7=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn7))
btn8=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn8))
btn9=Button(mansLogs,text="",width=7,height=3,font=('Helvica',23),bg="black", fg="white", activebackground="#2B2D2F", command=lambda: btnClick(btn9))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)

btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)

#IZVELNES VEIDOŠANA----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
galvenaIzvelne=Menu(mansLogs)#Izveido galveno izvelni
mansLogs.config(menu=galvenaIzvelne)#pievieno galveno logu
#MAZĀ IZVELNE----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvēlne
galvenaIzvelne.add_cascade(label="Iestatijumi",menu=opcijas)#lejupkrītošais saraksts
#KOMANDAS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
opcijas.add_command(label="Jauna spēle",command=resets)
opcijas.add_command(label="Iziet",command=mansLogs.quit)
#PAPILDUS POGA IZVEIDE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
galvenaIzvelne.add_command(label="Par programmu",command=infoLogs) # pievieno mazajai izvēlnei


mansLogs.mainloop()