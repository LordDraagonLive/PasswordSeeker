import time,array,re
from itertools import product


def numHack(password):

    passOrFail=False
    result='NOT FOUND'
    timetaken=0
    attempts=0

    if re.match("^[0-9 ]+$", password):
        passOrFail=True
        start = time.time()
        breaker=False
        chars = '0123456789 ' # chars to look for
        for length in range(1, 26): # only do lengths of 1 + 25
           for  passCombines in product(chars, repeat=length): #custom for each loop
               passCombines=''.join(passCombines)
               #print('password is {}. '.format(to_attempt))
               attempts =attempts+1
               if passCombines ==password:#checks if password is equal to user password
                 result=passCombines
                # print('password is {}. '.format(passCombines))
                 end = time.time()
                 timetaken = end - start
                # print('Time taken in {} seconds\nAttempts {} '.format(timetaken,attempts))
                 breaker=True
                 break

           if breaker:
                break
    else:
        passOrFail=False
    #    print('This checks only for Numeric passwords')
    #print('program ended')
    return passOrFail,attempts,timetaken,result

def alphaNumHack(password):

    passOrFail=False
    result='NOT FOUND'
    timetaken=0
    attempts=0

    if re.match("^[0-9a-zA-Z ]+$", password):
        passOrFail=True
        start = time.time()
        breaker=False
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  ' # chars to look for
        for length in range(1, 26): # only do lengths of 1 + 25
           for  passCombines in product(chars, repeat=length): #custom for each loop
               passCombines=''.join(passCombines)
               #print('password is {}. '.format(to_attempt))
               attempts =attempts+1
               if passCombines ==password:#checks if password is equal to user password
                 result=passCombines
                 #print('password is {}. '.format(passCombines))
                 end = time.time()
                 timetaken = end - start
                 #print('Time taken in {} seconds\nAttempts {} '.format(timetaken,attempts))
                 breaker=True
                 break

           if breaker:
               break
    else:
        passOrFail=False
    #    print('This checks only for alphanumeric passwords')
    #print('program ended')
    return passOrFail,attempts,timetaken,result

def bruteForceHack(password):

    start = time.time()
    timetaken=0
    attempts=0
    breaker=False
    result='ERROR'
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()_+=-[]\|}{;:\'",<.>/?`~' # chars to look for
    for length in range(1, 26): # only do lengths of 1 + 25
       for  passCombines in product(chars, repeat=length):
           passCombines=''.join(passCombines)
           #print('password is {}. '.format(to_attempt))
           attempts =attempts+1
           if passCombines ==password:
             result=passCombines
             #print('password is {}. '.format(passCombines))
             end = time.time()
             timetaken = end - start
             #print('Time taken in {} seconds\nAttempts {} '.format(timetaken,attempts))
             breaker=True
             break

       if breaker:
            break

    #print('program ended')
    return attempts,timetaken,result

def dictAttackTimeCal(file_name,password):

    totalguesses=0
    result = False
    thePassword='NOT FOUND'

    # Starts reading the list of words to another list
    f = open(file_name)
    words = f.readlines()
    f.close
    # We need to know the number of words there are
    number_of_words = len(words)
    print("Using a dictionary attack with "+str(number_of_words)+" in the list")
    
    
	
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each line as the password and check the result
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next

    while still_searching:
        ourguess_pass = words[word1count]
        #print("Guess: "+ourguess_pass)   
        
		
        if (password == ourguess_pass):
            print ("Success! Password is " + ourguess_pass)
            thePassword=ourguess_pass
            still_searching = False   # we can stop now - we found it!
            result = True
        #else:
            #print ("Shit. " + ourguess_pass + " is not the password.")
        tests = tests + 1
        totalguesses = totalguesses + 1

        # Trying with first letter caps
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
            #print("Guessing: "+ourguess_pass)
            if (password== ourguess_pass):
                thePassword=ourguess_pass
                print ("Success! Password is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            #else:
            #    print ("Darn. " + ourguess_pass + " is NOT the password.")
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >= number_of_words):
             still_searching = False


    seconds = time.time()-starttime
    #report_search_time(tests, seconds)
    return result,tests,seconds,thePassword

## formats and cleans the formatting
def cleanup (s):
    s = s.strip()
    return s

## caps the first letter of the word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s

def timeOutputToUser(timeTaken):

       inYears=timeTaken/31536000
       inDays=((timeTaken%531536000)/86400)
       inHours=(((timeTaken%531536000)%86400)/3600)
       inMins=((((timeTaken%531536000)%86400)%3600)/60)
       inSecs=((((timeTaken%531536000)%86400)%3600)%60)

       if inYears>=1:
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

def timeForDic(userValue):
    passOrFail,pwrdsChekd,timeTaken,result=dictAttackTimeCal('passwords.txt', userValue)
    realTimetaken=timeOutputToUser(timeTaken)
    return (passOrFail,pwrdsChekd,realTimetaken,result)

def timeForBrute(userValue):
    pwrdsChekd,timeTaken,result=bruteForceHack(userValue)
    realTimeTaken=timeOutputToUser(timeTaken)
    return(pwrdsChekd,realTimeTaken,result)

def timeForAlphaNum(userValue):
    passOrFail,pwrdsChekd,timeTaken,result=alphaNumHack(userValue)
    realTimeTaken=timeOutputToUser(timeTaken)
    return(passOrFail,pwrdsChekd,realTimeTaken,result)

def timeForNum(userValue):
     passOrFail,pwrdsChekd,timeTaken,result=numHack(userValue)
     realTimeTaken=timeOutputToUser(timeTaken)
     return(passOrFail,pwrdsChekd,realTimeTaken,result)

#userPassword=input("What is your password?\n")
#realTimetaken,pwrdsChekd,result=timeForDic(userPassword)
#print('time {} passwords checked {} result is true if found {}'.format(realTimetaken,pwrdsChekd,result))
#bruteForceHack(userPassword)
#alphaNumHack(userPassword)
#numHack(userPassword)