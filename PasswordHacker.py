import tkinter.ttk
import time,os
import PasswordHackerCon
import tkinter.messagebox
from tkinter import ttk  
import threading

class HackerMenu(tkinter.Tk): #inheriting tkinter class (like jFrame in java)
    def __init__(self,parent): #python constructors are names as __init__
        tkinter.Tk. __init__(self,parent)
        self.parent= parent
        self.initialise()
        

    def initialise(self):
        self.grid()


      # Title Label
        titleLbl=tkinter.Label(self,text=' Hack a Password ',fg='black',anchor='center')
        titleLbl.grid(column=1, row=0,columnspan=2)
        titleLbl.config(font=('Impact',28))

      #space label   
        spc1Lbl=tkinter.Label(self,text='blank',fg='#F0F0F0')
        spc1Lbl.grid(column=0, row=1)
        spc1Lbl.config(font=('arial',20))

      #userValue label      
        userValLbl=tkinter.Label(self,text='Password :',fg='black',anchor='w')
        userValLbl.grid(column=0, row=2,sticky='WE')
        userValLbl.config(font=('arial',12))

      #new tkinter special variable for the entry field
        self.entryVariable=tkinter.StringVar()
       
      #new tkinter special variable for the time result
        self.timeResVar=tkinter.StringVar()

      #new tkinter special variable for the password checks
        self.passChksVar=tkinter.StringVar() 

      #new tkinter special variable for the password
        self.passwordVar=tkinter.StringVar() 

      #new entry form
        self.entry=tkinter.Entry(self,textvariable=self.entryVariable,width=100) #assign the new tkinter special entry field var
        self.entry.grid(column=1,row=2,columnspan=3)
        self.entryVariable.set(u'Enter password here')

     #space label   1   
        spcLbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spcLbl.grid(column=0, row=3,sticky='WE')
        spcLbl.config(font=('arial',18))
        
      #Execute label      
        executeLbl=tkinter.Label(self,text='Execute : ',fg='black',anchor='w')
        executeLbl.grid(column=0, row=4,sticky='WE')
        executeLbl.config(font=('arial',12))

      #space label   3
        spc3Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc3Lbl.grid(column=1, row=5)
        spc3Lbl.config(font=('arial',4))

        #new button
        bruteForceBtn=tkinter.Button(self,text=u'Brute Force Attack',anchor='w', command=self.onBruteBtnClick)
        bruteForceBtn.grid(column=0,row=6)

         #new button
        numSrchBtn=tkinter.Button(self,text=u'Number Search Attack',anchor='w',command=self.onNumClick)
        numSrchBtn.grid(column=1,row=6)


         #new button
        alphaNumSrchBtn=tkinter.Button(self,text=u'Alpha-Num Search Attack',anchor='w',command=self.onAlphaNumClick)
        alphaNumSrchBtn.grid(column=2,row=6)

         #new button
        dictAtckBtn=tkinter.Button(self,text=u' Dictionary Attack  ',anchor='w',command=self.onDictClick)
        dictAtckBtn.grid(column=3,row=6,sticky='E')

        ##progress bar label
        #progBarLbl=tkinter.Label(self,text='Progress : ',fg='black',anchor='w')
        #progBarLbl.grid(column=0, row=7,sticky='WE')
        #progBarLbl.config(font=('arial',12))

        ##progress bar
        #self.progressbar=ttk.Progressbar(self,orient='horizontal',mode='indeterminate',length=600)
        #self.progressbar.grid(column=0,row=7,columnspan=4)
        ##self.progressbar.grid_forget()
       

        ##progress bar
        #progressBar=ttk.Progressbar(self,orient='horizontal',mode='indeterminate',length=600,maximum=2)
        #progressBar.grid(column=0,row=7,columnspan=4)

         #space label   2 
        spc2Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc2Lbl.grid(column=1, row=7)
        spc2Lbl.config(font=('arial',72))

         #Result label      
        resultLbl=tkinter.Label(self,text='Result : ',fg='black',anchor='w')
        resultLbl.grid(column=0, row=8,sticky='WE')
        resultLbl.config(font=('arial',12))

           #space label   3
        spc3Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc3Lbl.grid(column=0, row=9)
        spc3Lbl.config(font=('arial',4))

          #Time Taken label      
        timeLbl=tkinter.Label(self,text='Time Taken : ',fg='black',anchor='w')
        timeLbl.grid(column=1, row=10,sticky='W')
        timeLbl.config(font=('arial',12))

          #Time Taken Result label      
        timeResLbl=tkinter.Label(self,textvariable=self.timeResVar,fg='black',anchor='w')
        timeResLbl.grid(column=2, row=10,sticky='WE')
        timeResLbl.config(font=('arial',12))

            #space label   4
        spc4Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc4Lbl.grid(column=0, row=11)
        spc4Lbl.config(font=('arial',4))

          #Passwords Checked label      
        passChksLbl=tkinter.Label(self,text='Checks : ',fg='black',anchor='w')
        passChksLbl.grid(column=1, row=12,sticky='W')
        passChksLbl.config(font=('arial',12))

          #Psswords Checked label      
        passChksResLbl=tkinter.Label(self,textvariable=self.passChksVar,fg='black',anchor='w')
        passChksResLbl.grid(column=2, row=12,sticky='WE')
        passChksResLbl.config(font=('arial',12))

          #space label   5
        spc5Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc5Lbl.grid(column=0, row=13)
        spc5Lbl.config(font=('arial',4))

          #Password label      
        passwordLbl=tkinter.Label(self,text='Password : ',fg='black',anchor='w')
        passwordLbl.grid(column=1, row=14,sticky='W')
        passwordLbl.config(font=('arial',12))

          #Paswords Checked label      
        passwordResLbl=tkinter.Label(self,textvariable=self.passwordVar,fg='black',anchor='w')
        passwordResLbl.grid(column=2, row=14,sticky='WE')
        passwordResLbl.config(font=('arial',12))

        
          #space label   6
        spc6Lbl=tkinter.Label(self,text='blank',anchor='w',fg='#F0F0F0')
        spc6Lbl.grid(column=0, row=15)
        spc6Lbl.config(font=('arial',18))

        #open window button
        mainMenuBtn=tkinter.Button(self,text=u'Main Menu',height=2,width=10,command=self.openMainMenu)
        mainMenuBtn.grid(column=0,row=16,sticky='W')

    
        #self.grid_columnconfigure(1,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()        #(And we perform an update() to make sure Tkinter has finished rendering all widgets and evaluating their size.) 
       #self.geometry(self.geometry())   #This way, Tkinter will stop trying to accomodate window size all the time.
        self.geometry('800x540+0+0')
        self.entry.focus_set() #set focus to the test field
        self.entry.selection_range(0,tkinter.END)
        
    def onBruteBtnClick(self):
     
       pwrdsChekd,realTimeTaken,result=PasswordHackerCon.timeForBrute(self.entryVariable.get())
       self.timeResVar.set(realTimeTaken)
       self.passChksVar.set(pwrdsChekd)
       self.passwordVar.set(result)

    def onAlphaNumClick(self):
        passOrFail,pwrdsChekd,realTimeTaken,result=PasswordHackerCon.timeForAlphaNum(self.entryVariable.get())
        if passOrFail == False:
             tkinter.messagebox.showerror('Error','Alphanumeric search method failed as the password contains non-alphanumeric characters')

        self.timeResVar.set(realTimeTaken)
        self.passChksVar.set(pwrdsChekd)
        self.passwordVar.set(result)

    def onNumClick(self):
      
        passOrFail,pwrdsChekd,realTimeTaken,result=PasswordHackerCon.timeForNum(self.entryVariable.get())
        if passOrFail == False:
            tkinter.messagebox.showerror('Error','Numeric search method failed as the password contains non-numeric characters')
        self.timeResVar.set(realTimeTaken)
        self.passChksVar.set(pwrdsChekd)
        self.passwordVar.set(result)        
      
       
    def onDictClick(self):
         passOrFail,pwrdsChekd,realTimeTaken,result = PasswordHackerCon.timeForDic(self.entryVariable.get())
         if passOrFail == False:
           tkinter.messagebox.showerror('Error','The password is not available in the provided password list')

         self.timeResVar.set(realTimeTaken)
         self.passChksVar.set(pwrdsChekd)
         self.passwordVar.set(result)

    def openMainMenu(self):
        self.destroy()
        os.system('MainMenu.py')
    
if __name__=='__main__':
    app=HackerMenu(None)
    app.title(' Hack a Password ')
    #mainMenu(parent).pack
    #thread.start_new_thread(startFunc, (self))    
    app.mainloop()