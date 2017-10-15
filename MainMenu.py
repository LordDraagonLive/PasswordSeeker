
import tkinter.ttk
import PasswordTimeCracker
import sys,os
import tkinter.messagebox

class Menu(tkinter.Tk): #inheriting tkinter class (like jFrame in java)
    def __init__(self,parent): #python constructors are names as __init__
        tkinter.Tk. __init__(self,parent)
        self.parent= parent
        self.initialise()
        

    def initialise(self):
        self.grid()

        #main title label
        label1=tkinter.Label(self,text='Password Seeker',anchor='center',fg='black')
        label1.grid(column=0, row=0,sticky='WE')
        label1.config(font=('Impact',24))

        #columnspan
        label2=tkinter.Label(self,anchor='center',fg='black')
        label2.grid(column=0, row=1,sticky='WE')

        #Button hacking timer
        button1=tkinter.Button(self,text=u'Hacking Time Calculator',anchor='center',width=20,height=2,command=self.openHackerTimer)
        button1.grid(column=0,row=3)

        #columnspan
        label3=tkinter.Label(self,anchor='center',fg='black')
        label3.grid(column=0, row=4,sticky='WE')
      

         #Button hack your passoword
        button2=tkinter.Button(self,text=u'Hack a Password',anchor='center',width=15,height=2,command=self.openHacker)
        button2.grid(column=0,row=5)

         #columnspan
        label4=tkinter.Label(self,anchor='center',fg='black')
        label4.grid(column=0, row=6,sticky='WE')


         #Button exit
        button3=tkinter.Button(self,text=u'Exit',anchor='center',width=15,height=2,command=self.exitProgram)
        button3.grid(column=0,row=7)

        self.grid_columnconfigure(0,weight=1)
        
        self.resizable(False,False)
        self.update()        #(And we perform an update() to make sure Tkinter has finished rendering all widgets and evaluating their size.) 
       #self.geometry(self.geometry())   #This way, Tkinter will stop trying to accomodate window size all the time.
        self.geometry('360x500+500+20')

    
    def openHackerTimer(self):
       self.destroy()
       os.system('HackerTimer.py')

    def openHacker(self):
       self.destroy()
       os.system('PasswordHacker.py')

    def exitProgram(self):
        self.quit()
        sys,exit()
    

if __name__=='__main__':
    app=Menu(None)
    app.title('Main Menu')
    #mainMenu(parent).pack
    app.mainloop()
