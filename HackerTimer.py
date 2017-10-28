import tkinter.ttk
import PasswordTimeCracker
import tkinter.messagebox
import PasswordHacker
import sys,os


class mainMenu(tkinter.Tk): #inheriting tkinter class (like jFrame in java)
    def __init__(self,parent): #python constructors are names as __init__
        tkinter.Tk. __init__(self,parent)
        self.parent= parent
        self.initialise()
        

    def initialise(self):
       # pass #pass statement does nothing particular but can act as a placeholder (a null)
       self.grid()
      

       #new tkinter special variable for the entry field
       self.entryVariable=tkinter.StringVar()

       #new entry form
       self.entry=tkinter.Entry(self,textvariable=self.entryVariable) #assign the new tkinter special entry field var
       self.entry.grid(column=0,row=1,sticky='EW')
       self.entry.bind('<Return>',self.onPressEnter)
       self.entryVariable.set(u'Enter password here')

     
       #space label
       spceLbl=tkinter.Label(self,text='   ',anchor='w')
       spceLbl.grid(column=0, row=10,sticky='WE')
       spceLbl.config(font=('comic sans ms',18))

       #open window button
       button1=tkinter.Button(self,text=u'Main Menu',command=self.createWindow,height=2,width=10)
       button1.grid(column=0,row=11,sticky='W')


       #new button
       button=tkinter.Button(self,text=u'click',command=self.onButtonClick)
       button.grid(column=1,row=1)

       
       ##new tkinter special var for dictAtRsLbl
       #self.failsLblVar=tkinter.StringVar()
       #new label for fails
       self.fails=tkinter.Label(self,text=u'Failed',anchor='w',fg='#F0F0F0',bg='#F0F0F0') #assign new tkinter special label var
       self.fails.grid(column=1,row=5,sticky='EW')
       self.fails.config(font=('Comic sans ms',12))
       self.fails.bind('<Button-1>',self.onButton1Click)
       

       self.fails1=tkinter.Label(self,text=u'Failed',anchor='w',fg='#F0F0F0',bg='#F0F0F0') #assign new tkinter special label var
       self.fails1.grid(column=1,row=7,sticky='EW')
       self.fails1.config(font=('Comic sans ms',12))
       self.fails1.bind('<Button-1>',self.onButton2Click)

       self.fails2=tkinter.Label(self,text=u'Failed',anchor='w',fg='#F0F0F0',bg='#F0F0F0') #assign new tkinter special label var
       self.fails2.grid(column=1,row=9,sticky='EW')
       self.fails2.config(font=('Comic sans ms',12))
       self.fails2.bind('<Button-1>',self.onButton3Click)

        #new tkinter special variable
       self.labelVariable=tkinter.StringVar()
       #new tkinter special var 2
       self.labelVariable2=tkinter.StringVar()
       #new tkinter special var for bfNamLbl
       self.bfNamLblVar=tkinter.StringVar()
        #new tkinter special var for numSrchLbl
       self.numSrchLblVar=tkinter.StringVar()
        #new tkinter special var for numSrchRsLbl
       self.numSrchRsLblVar=tkinter.StringVar()
       #new tkinter special var for alNumSrchLbl
       self.alNumLblVar=tkinter.StringVar()
       #new tkinter special var for alNumSrchRsLbl
       self.alNumRsLblVar=tkinter.StringVar()
         #new tkinter special var for dictAtNamLbl
       self.dictAtNamLblVar=tkinter.StringVar()
       #new tkinter special var for dictAtRsLbl
       self.dictAtRsLblVar=tkinter.StringVar()

       #bruteForce result label
       label=tkinter.Label(self,textvariable=self.labelVariable,anchor='w',fg='white',bg='blue') #assign new tkinter special label var
       label.grid(column=0,row=3,sticky='EW')
       label.config(font=('comic sans ms',12))
       #self.labelVariable.set(u'Hello !')
       #bruteForce name label
       bfNamLbl=tkinter.Label(self,textvariable=self.bfNamLblVar,anchor='w',fg='black')
       bfNamLbl.grid(column=0, row=2,sticky='WE')
       bfNamLbl.config(font=('comic sans ms',12))
       self.bfNamLblVar.set('Using a brute force attack to hack the password :')
       # Title Label
       label1=tkinter.Label(self,textvariable=self.labelVariable2,anchor='center',fg='black')
       label1.grid(column=0, row=0,sticky='WE')
       label1.config(font=('Impact',24))
       self.labelVariable2.set(' Hacking Time Calculator ')
       #number search method name label
       numSrchNamLbl=tkinter.Label(self,textvariable=self.numSrchLblVar,anchor='w',fg='black')
       numSrchNamLbl.grid(column=0, row=4,sticky='WE')
       numSrchNamLbl.config(font=('comic sans ms',12))
       self.numSrchLblVar.set('Using a number search method to hack the password :')
        #number search method result label
       numSrchResultLbl=tkinter.Label(self,textvariable=self.numSrchRsLblVar,anchor='w',fg='white',bg='blue') #assign new tkinter special label var
       numSrchResultLbl.grid(column=0,row=5,sticky='EW')
       numSrchResultLbl.config(font=('comic sans ms',12))
       #self.numSrchRsLblVar.set(u'hi')
        #alpha numeric search method name label
       alNumSrchNamLbl=tkinter.Label(self,textvariable=self.alNumLblVar,anchor='w',fg='black')
       alNumSrchNamLbl.grid(column=0, row=6,sticky='WE')
       alNumSrchNamLbl.config(font=('comic sans ms',12))
       self.alNumLblVar.set('Using a Alphanumeric search method to hack the password :')
        #alpha numeric search method result label
       alNumSrchRsLbl=tkinter.Label(self,textvariable=self.alNumRsLblVar,anchor='w',fg='white',bg='blue') #assign new tkinter special label var
       alNumSrchRsLbl.grid(column=0,row=7,sticky='EW')
       alNumSrchRsLbl.config(font=('comic sans ms',12))
       #self.numSrchRsLblVar.set(u'Hello !')
       #Dictionary attack name label
       dictAtNamLbl=tkinter.Label(self,textvariable=self.dictAtNamLblVar,anchor='w',fg='black')
       dictAtNamLbl.grid(column=0, row=8,sticky='WE')
       dictAtNamLbl.config(font=('comic sans ms',12))
       self.dictAtNamLblVar.set('Using a dictionary attack to hack the password :')
        #alpha numeric search method result label
       dictAtRsLbl=tkinter.Label(self,textvariable=self.dictAtRsLblVar,anchor='w',fg='white',bg='blue') #assign new tkinter special label var
       dictAtRsLbl.grid(column=0,row=9,sticky='EW')
       dictAtRsLbl.config(font=('comic sans ms',12))
       #self.numSrchRsLblVar.set(u'Hello !')

       self.grid_columnconfigure(0,weight=1)
       #self.resizable(True,False)
       self.update()        #(And we perform an update() to make sure Tkinter has finished rendering all widgets and evaluating their size.) 
       #self.geometry(self.geometry())   #This way, Tkinter will stop trying to accomodate window size all the time.
       self.geometry('1024x450+1+1')

       self.entry.focus_set() #set focus to the test field
       self.entry.selection_range(0,tkinter.END)

    def onButtonClick(self):
        print('You clicked the button!!')
        self.labelVariable.set(self.entryVariable.get()+ ' [You pressed the button!!]')
        pwrdsChekd,timeTaken=PasswordTimeCracker.timeForBrute(self.entryVariable.get())
        self.labelVariable.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))

        pwrdsChekd,timeTaken,isPwrdDigit=PasswordTimeCracker.timeForNumSrch(self.entryVariable.get())
        if isPwrdDigit:
           #self.numSrchRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.numSrchRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails.config(bg='#F0F0F0')

        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.numSrchRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails.config(bg='red')

         
        pwrdsChekd,timeTaken,isPwrdAlphaNum=PasswordTimeCracker.timeForAlNum(self.entryVariable.get())
        if isPwrdAlphaNum:
           self.alNumRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails1.config(bg='#F0F0F0')
        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.alNumRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails1.config(bg='red')

        timeTaken,pwrdsChekd,result=PasswordTimeCracker.timeForDic(self.entryVariable.get())
        if result:
           self.dictAtRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails2.config(bg='#F0F0F0')
        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.dictAtRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails2.config(bg='red')

        self.entry.focus_set() #set focus to the test field
        self.entry.selection_range(0,tkinter.END)

    def onPressEnter(self,event):
        print('You pressed Enter!!')
        self.labelVariable.set(self.entryVariable.get()+' [You pressed the Enter key !!]')
        pwrdsChekd,timeTaken=PasswordTimeCracker.timeForBrute(self.entryVariable.get())
        self.labelVariable.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))

        pwrdsChekd,timeTaken,isPwrdDigit=PasswordTimeCracker.timeForNumSrch(self.entryVariable.get())
        if isPwrdDigit:
           self.numSrchRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails.config(bg='#F0F0F0')

        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.numSrchRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails.config(bg='red')

        pwrdsChekd,timeTaken,isPwrdAlphaNum=PasswordTimeCracker.timeForAlNum(self.entryVariable.get())
        if isPwrdAlphaNum:
           self.alNumRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails1.config(bg='#F0F0F0')
        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.alNumRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails1.config(bg='red')

        timeTaken,pwrdsChekd,result=PasswordTimeCracker.timeForDic(self.entryVariable.get())
        if result:
           self.dictAtRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
           self.fails2.config(bg='#F0F0F0')
        else:
            #self.numSrchRsLblVar.set('Number search method will fail as the password contains non-numeric characters')
            self.dictAtRsLblVar.set('Passwords checked: '+str(pwrdsChekd)+' Time Taken: '+str(timeTaken))
            self.fails2.config(bg='red')

        self.entry.focus_set() #set focus to the test field
        self.entry.selection_range(0,tkinter.END)

    def onButton1Click(self,event):
        tkinter.messagebox.showinfo('Information','Number search method will fail as the password contains non-numeric characters')
    def onButton2Click(self,event):
        tkinter.messagebox.showinfo('Information','Alphanumeric search method will fail as the password contains non-alphanumeric characters')
    def onButton3Click(self,event):
        tkinter.messagebox.showinfo('Information','Dictionary attack failed as the password was unable to be found in the list provided')

    def createWindow(self):
        #new=PasswordHacker.HackerMenu(None)
        #new.title('hack 2')
        self.destroy()
        os.system('MainMenu.py')

if __name__=='__main__':
    app=mainMenu(None)
    app.title('Password Hacker')
    #mainMenu(parent).pack
    app.mainloop()
    
    

    
