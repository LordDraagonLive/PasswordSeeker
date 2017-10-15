import time
import string,decimal
#str.isalnum() checks if it's alphanum
def pMain():
    #userValue=input('Please select the method:\n')
  
   # if userValue=='1': #method: brute force
        #userValue=input('Please enter the password:\n')
        #userValue=MainMenu.app.entryVariable.get()
    #timeTaken,pwrdsChekd=bruteForceTimeCal(userValue)

   # timeOutputToUser(timeTaken,len(userValue))
    ##bruteForceTimeCal(userValue)

    #elif userValue=='2': #method:number search method  
    #    userValue=input('Please enter the password:\n')
    #    isPwrdDigit=userValue.isdigit()
    ##print('password is numeric: ' + str(isPwrdDigit))

    #    if isPwrdDigit:
    #        numTmeOutputToUser(numSrchMethod(userValue))
    #    else:
    #        print('Number search method will fail as the password contains non-numeric characters')
    
    #elif userValue=='3': #method: alphanumeric search method
    #    userValue=input('Please enter the password:\n')
    #    isPwrdAlphaNum=userValue.isalnum()

    #    if isPwrdAlphaNum:
    #        numTmeOutputToUser(alphaNumSrchMethd(userValue))
    #    else:
    #        print('Alpha-Numeric search method will fail as the password contains non-alpha-numeric characters')

    #elif userValue=='4': #method: dictionarry attack
    #     userValue=input('Please enter the password:\n')
    #     dictAttackTimeCal('passwords.txt', userValue)

    return

def timeForBrute(userValue):
      timeTaken,pwrdsChekd=bruteForceTimeCal(userValue)
      realTime=timeOutputToUser(timeTaken,len(userValue))
      return (pwrdsChekd,realTime)

def timeForNumSrch(userValue):
    isPwrdDigit=userValue.isdigit()
    print('password is numeric: ' + str(isPwrdDigit))

    #if isPwrdDigit:
    pwrdsChekd,timeTaken=numSrchMethod(userValue)
    realTimeTaken=numTmeOutputToUser(timeTaken,len(userValue),False)
    #else:
    #    return ('Number search method will fail as the password contains non-numeric characters')
    return (pwrdsChekd,realTimeTaken,isPwrdDigit)

def timeForAlNum(userValue):
    #userValue=input('Please enter the password:\n')

    isPwrdAlphaNum=userValue.isalnum()

    #if isPwrdAlphaNum:
    pwrdsChekd, timeTaken =alphaNumSrchMethd(userValue)
    realTimeTaken=numTmeOutputToUser(timeTaken,len(userValue),False)
    #else:
   #print('Alpha-Numeric search method will fail as the password contains non-alpha-numeric characters')

    return(pwrdsChekd,realTimeTaken,isPwrdAlphaNum)

def timeForDic(userValue):
    timeTaken,pwrdsChekd,result=dictAttackTimeCal('passwords.txt', userValue)
    realTimetaken=numTmeOutputToUser(timeTaken,len(userValue),True)
    return (realTimetaken,pwrdsChekd,result)

def bruteForceTimeCal(password):
   
    lengthOfPwrd=len(password)
    print('Password Length: '+str(lengthOfPwrd))
    pwrdsChekd=decimal.Decimal(95**(lengthOfPwrd) )#^ is a bit wise operrator and we should use ** to represent powers

    timeTaken=decimal.Decimal((pwrdsChekd)/4000000 )#(charSetLen^lengthOfPwrd)/avgKeysPerSec=timeTaken in secs
    
   # print('Time taken to crack the password: '+ str(timeTaken)+' seconds')
    #print('Time taken to crack the password: '+ str((timeTaken%531536000)/86400)+' days')
    #print('Time taken to crack the password: '+ str(((timeTaken%531536000)%86400)/3600)+' hrs')
    print("Number of passwords checked: "+str(pwrdsChekd))
    #MainMenu.app.labelVariable.set('Number of passwords checked: '+str(pwrdsChekd))

    return (timeTaken,pwrdsChekd)

def timeOutputToUser(timeTaken,lengthOfPwrd):

       inYears=timeTaken/31536000

       if lengthOfPwrd<9: #to avoid impossible division
           inDays=((timeTaken%531536000)/86400)
           inHours=(((timeTaken%531536000)%86400)/3600)
           inMins=((((timeTaken%531536000)%86400)%3600)/60)
           inSecs=((((timeTaken%531536000)%86400)%3600)%60)

       if inYears>=100:
           return calYrsAboveThous(inYears)
          # MainMenu.app.labelVariable.set(inYears)

       elif inYears>=1:
         return(str(round(inYears))+' Years')
         #MainMenu.app.labelVariable.set(str(round(inYears))+' Years')

       elif inDays>=1:
         return(str(round(inDays))+' Days')
         #MainMenu.app.labelVariable.set(str(round(inDays))+' Days')

       elif inMins>=1:
         return(str(round(inMins))+' Minutes')
         #MainMenu.app.labelVariable.set(str(round(inMins))+' Minutes')

       elif inSecs>=0:
         return(str(inSecs)+' Seconds')
         #MainMenu.app.labelVariable.set(str(inSecs)+' Seconds')


def calYrsAboveThous(years):

    thousand =    1000
    million =     1000000
    billion =     1000000000
    trillion =    1000000000000
    quadrillion = 1000000000000000
    quintillion = 1000000000000000000
    sextillion =  1000000000000000000000
    septillion =  1000000000000000000000000
    octillion =	  1000000000000000000000000000
    nonillion =   1000000000000000000000000000000
    decillion =   1000000000000000000000000000000000

    if years < million:
        years = round(years / thousand)
        return ( str(years) + ' thousand years')
        #MainMenu.app.labelVariable.set(str(years) + ' thousand years')

    elif years < billion:
        years = round(years / million)
        return(str(years) + ' million years')
        #MainMenu.app.labelVariable.set(str(years) + ' million years')

    elif years < trillion :
        years = round(years / billion)
        return(str(years) + ' billion years')

    elif years < quadrillion :
        years = round(years / trillion)
        return(str(years) + ' trillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' trillion years')

    elif years < quintillion :
        years = round(years / quadrillion)
        return(str(years) + ' quadrillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' quadrillion years')

    elif years < sextillion :
        years = round(years / quintillion)
        return(str(years) + '  quintillion years')
        #MainMenu.app.labelVariable.set(str(years) + '  quintillion years')

    elif years < septillion :
        years = round(years / sextillion)
        return( str(years) + ' sextillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' sextillion years')

    elif  years < octillion :
        years = round(years / septillion)
        return(str(years) + ' septillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' septillion years')

    elif years < nonillion :
        years = round(years / octillion)
        return(str(years) + ' octillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' octillion years')

    elif years < decillion :
        years = round(years / nonillion)
        return(str(years) + ' nonillion years')
        #MainMenu.app.labelVariable.set(str(years) + ' nonillion years')

    else :
        return('Infinite')
        #MainMenu.app.labelVariable.set('It will take forever')


def numSrchMethod(password):

    lengthOfPwrd=len(password)
    print('Password Length: '+str(lengthOfPwrd))
    pwrdsChekd=decimal.Decimal(10**(lengthOfPwrd) )#^ is a bit wise operrator and we should use ** to represent powers

    timeTaken=decimal.Decimal((pwrdsChekd)/4000000 )#(charSetLen^lengthOfPwrd)/avgKeysPerSec=timeTaken in secs
    
   # print('Time taken to crack the password: '+ str(timeTaken)+' seconds')
    #print('Time taken to crack the password: '+ str((timeTaken%531536000)/86400)+' days')
    #print('Time taken to crack the password: '+ str(((timeTaken%531536000)%86400)/3600)+' hrs')
    print("Number of passwords checked: "+str(pwrdsChekd))


    return (pwrdsChekd,timeTaken)

def numTmeOutputToUser(timeTaken,lengthOfPwrd,chkIfDic):

     
       inYears=(timeTaken/31536000)
       
       if lengthOfPwrd<25: #to avoid impossible division
           inDays=((timeTaken%531536000)/86400)
           inHours=(((timeTaken%531536000)%86400)/3600)
           inMins=((((timeTaken%531536000)%86400)%3600)/60)
           inSecs=((((timeTaken%531536000)%86400)%3600)%60)

       if chkIfDic: #to avoid impossible division
           inDays=((timeTaken%531536000)/86400)
           inHours=(((timeTaken%531536000)%86400)/3600)
           inMins=((((timeTaken%531536000)%86400)%3600)/60)
           inSecs=((((timeTaken%531536000)%86400)%3600)%60)

       if inYears>=1000:
           return calYrsAboveThous(inYears)

       elif inYears>=1:
         return(str(round(inYears))+' Years')

       elif inDays>=1:
         return(str(round(inDays))+' Days')

       elif inMins>=1:
         return(str(round(inMins))+' Minutes')

       elif inSecs>=0:
         return(str(inSecs)+' Seconds')



def alphaNumSrchMethd(password):

    lengthOfPwrd=len(password)
    print('Password Length: '+str(lengthOfPwrd))
    pwrdsChekd=decimal.Decimal(62**(lengthOfPwrd) )#^ is a bit wise operrator and we should use ** to represent powers

    timeTaken=decimal.Decimal((pwrdsChekd)/4000000 )#(charSetLen^lengthOfPwrd)/avgKeysPerSec=timeTaken in secs
    
   # print('Time taken to crack the password: '+ str(timeTaken)+' seconds')
    #print('Time taken to crack the password: '+ str((timeTaken%531536000)/86400)+' days')
    #print('Time taken to crack the password: '+ str(((timeTaken%531536000)%86400)/3600)+' hrs')
    print("Number of passwords checked: "+str(pwrdsChekd))


    return (pwrdsChekd, timeTaken)

def dictAttackTimeCal(file_name,password):
    totalguesses=0
    result = False
    
    # Start by reading the list of words into a Python list
    f = open(file_name)
    words = f.readlines()
    f.close
    # We need to know how many there are
    number_of_words = len(words)
    print("Using a dictionary attack with "+str(number_of_words)+" in the list")
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next

    while still_searching:
        ourguess_pass = words[word1count]
        #print("Guessing: "+ourguess_pass)   
        # Try it the way it is in the word list
        if (password == ourguess_pass):
            print ("Success! Password is " + ourguess_pass)
            
            still_searching = False   # stops, we found it!
            result = True
        #else:
            #print ("Shit. " + ourguess_pass + " is not the password.")
        tests = tests + 1
        totalguesses = totalguesses + 1

        #Trying with the first letter capitalized
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
            #print("Guessing: "+ourguess_pass)
            if (password== ourguess_pass):
                print ("Success! Password is " + ourguess_pass)
                still_searching = False   # stops, we found it!
                result = True
            #else:
            #    print ("Shit. " + ourguess_pass + " is not the password.")
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >= number_of_words):
             still_searching = False


    seconds = time.time()-starttime
    
    return seconds,tests,result


def cleanup (s):
    s = s.strip()
    return s


def Cap (s):
    s = s.upper()[0]+s[1:]
    return s




#main()