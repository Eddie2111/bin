from functools import lru_cache
@lru_cache(maxsize = 1000)
class expertise:
    def __init__(self,value=0):
        self.value=value
        
    def reverser(self,num1):
        self.num1=num1
        b=0
        while self.num1>0:
            b=b*10+self.num1%10
            self.num1=self.num1//10
        return "Reversed value: {}".format(b)
    
    def string_reverser(self,num2):
        self.num2=str(num2)
        a=self.num2[::-1]
        return "Reversed String: {}".format(a)
    
    def fizzbuzz(self,limit):
        self.limit=limit
        for i in range(1,self.limit+1):
            if (i%3)==0:
                print('Fizz')
            elif (i%5)==0:
                print('Buzz')
            elif (i%15)==0:
                print('FizzBuzz')
            else:
                print(i)
        return ''
        
    def fibonacci_series(self,start,numberLimit):
        self.start=start
        self.numberLimit=numberLimit
        a,b=0,1
        for i in range(self.start, self.numberLimit):
            if i<=0:
                print('Fibonacci series only consisted of positive numbers.')
            elif i==1:
                print(0)
            elif i==2:
                print(1)
            else:
                x=a+b
                print( x )
                a=b
                b=x
        return ''
    
    def fibonacci_sentence(self,starts,sLimit):
        self.starts=starts
        self.sLimit=sLimit
        a,b,array=0,1,[]
        for i in range(self.starts, self.sLimit):
            if i<=0:
                print('Fibonacci series only consisted of positive numbers.')
            elif i==1:
                array.append(0)
            elif i==2:
                array.append(1)
            else:
                x=a+b
                array.append(x)
                a=b
                b=x
        return str(array)
                
                
def introduction():
    print("I am self declared AI YURI. I can run efficiently on Linux Operating systems.")
    print("I am an under-development UI-less AI. I can calculate and perform basic mathematics.")
    print("Currently I can, \n-calculate standardly \n-calculate areas according to given data \n-calculate average and summation of massive data. \n-tell you date and time. \n-Tell you synonym and antonym \n-store unanswered question. \n-take notes")
    return ""

def dependencies():
    print('pip install gtts')
    print('pip install nltk')
    print('pip install pydictionary')
    print('pip install pyaudio')
    print('pip install speechrecognition')
    print('pip install face_recognition')
    print('pip install tflearn')
    print('pip install tensorflow')
    print('pip install opencv python')
    print('pip install cmake')
    print('pip install dlib')
    print('Visual c++ workload necessary to run "Dlib" and "Tensorflow". Download them from: https://visualstudio.microsoft.com/vs/support/selecting-workloads-visual-studio-2017/ .')
    print('add sudo pip3 [super user-do] before installing in linux. Multiple errors means you have a python version which does not follow: 3.6.0>your python version<3.9.1')
    return ''

def speak(text):
    try:
        import playsound
        from gtts import gTTS
        tts=gTTS (text=text,lang="en")
    except:
        print('Module error. Install playsound and gtts')
    try:
        filename="voice.mp3"  ##change the path here..!
        tts.save(filename)
        playsound.playsound(filename)
    except:
        print('An error occurred.')

def nextDay():
    import datetime
    today = datetime.date.today() 
    tomorrow = today + datetime.timedelta(days = 1) 
    print(23*'=')
    print('Tomorrow : ',tomorrow.strftime("%A"))
    print(23*'=')

def previousDay():
    import datetime 
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    tomorrow = today + datetime.timedelta(days = 1) 
    print(23*'=')
    print('Yesterday : ',yesterday.strftime("%A"))
    print(23*'=')

def showFace():
    import cv2
    face_cascade = cv2.CascadeClassifier('h:/Nikolai/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                cv2.destroyAllWindows()
                break
            cap.release()
            cv2.destroyAllWindows()
    return 'Done'

def canDo():
    a=(23*'='+'\n')
    b='I can help you in'+' \n-calculate standardly \n-calculate areas according to given data \n-calculate average and summation of massive data. \n-tell you date and time. \n-Tell you synonym and antonym \n-store unanswered question. \n-take notes     or \n voice searching [EXPERIMENTAL]\n'
    c=23*'='+'\n'
    return {}.format(a,b,c)

def greet():
    import datetime
    now = datetime.datetime.now()
    hour = now.hour

    if hour>5 and hour<11:
        print("Good morning")
    if hour>11 and hour<13:
        print("Good day")
    if hour>13 and hour<16:
        print("Good noon")        
    if hour>16 and hour<20:
        print("Good afternoon")
    if hour>20 and hour<24 :
        print("Good night")
    if hour>=0 and hour<=6:
        print("Good night, \n YOU SHOULD GO TO SLEEP...!")
    return ''  

def joke():
    import random
    n=random.randint(1,4)
    if (n==1):
        print("Why don’t scientists trust atoms?")
        print("Because they make up everything.")
    if (n==2):
        print("SO I saw a bus full of old people going somewhere.")
        print('Do you what it was?')
        print('Right, graves on wheels. :v ')
    if (n==3):
        print('What do muslims do when they see their wife having affair?')
        print('Nothing, they marry another 3 women.')
    if (n==4):
        print("What did the shark say when he ate the clownfish?")
        print("This tastes a little funny.")
    return 24*'='


def calculate(a,b,c):
    if c=="+":
        x=a+b
    if c=="-":
        x=a-b
    if c=="*":
        x=a*b
    if c=="/":
        x=a/b
    return x      

def directMaths(x):
    x=str(x)
    g=eval(x)
    print("Well that's easy...")
    print(23*'=')
    print(g)
    print(23*'=')
    return g


def dictorize(x):
    list1=[]
    ss=""
    for i in range (0,len(action)):
        if (action[i]=='"'):
            list1.append(i)
    catch1=list1[0]
    catch2=list1[1]      
    for i in range (catch1+1,catch2):
        ss+=action[i]  
    from PyDictionary import PyDictionary
    dictionary=PyDictionary()
    print ("Synonym: ",dictionary.synonym(ss))
    print ("Antonym: ",dictionary.antonym(ss))
    return ' '

def thanks(a):
    if 'thank' in a:
        if 'you' in a:
            print('Never mention..!')
        elif 'thanks' in a:
            if 'thanks' in a:
                print('Thank you...!')
            elif 'to' in a:
                if 'you' in a:
                    print('Oww, thank you too.')
                else:
                    print('Allah bless them.')
        else:
            print('Allah bless you.')
    return ''

def datetime():
    from datetime import datetime
    today=datetime.today()
    print(today.ctime())
    return '' 

def dayNow():
    from datetime import datetime
    today=datetime.today()
    print(today.strftime("%A"))
    return ''

def timenow():
    from datetime import datetime
    now_main = datetime.now()
    current_time = now_main.strftime("%H:%M:%S")
    return current_time

def areaCalculation(a,b,c):
    if c=="1" or "square":
        b=a
        squareArea=a*b
        return squareArea
    if c=="2" or "triangle":
        triangleArea=0.5*a*b
        return triangleArea
    if c=="3" or "circle":
        b=a
        circleArea=3.14159265*a*b
        return circleArea
    if c=="4" or "rectangle":
        rectangleArea=a*b
        return rectangleArea    

def surfaceCalculation(a,b,c):
    if c=="1" or "square":
        b=a
        squareArea=a*4
        return squareArea
    if c=="2" or "triangle":
        triangleArea=0.5*a*b
        return triangleArea
    if c=="3" or "circle":
        b=a
        circleArea=3.14159265*a*2
        return circleArea
    if c=="4" or "rectangle":
        rectangleArea=(a+b)*2
        return rectangleArea 
def wordcounter(x): #done, not implanted, needs to be tested.
    with open ("H:/nikolai/text.text","r") as textico:
        machine=textico.read()
        machine=machine.split()
        return len(machine)

print('===================================')
print('===================================')        
print(greet())        
print("Hi, I am Yuri.")
print("You can command me anything.")
print('===================================')
print('===================================')
print("Ask away your questions: ")

exitValue=0
dieth=0
while True:

    try:
        main_input=str(input("-->"))
        action=main_input.lower()
        if exitValue==4 or dieth==2:
            exit()
        if 'yuri' in action:
            print('Sir..?')
        if '"' in action:
            print(23*'=')
            print(23*'=')
            a=dictorize(action)  
            print(23*'=')
        elif (action=='Greet me' or action=='greet me' or action=='greet me!' or action=='Greet me!'):
            print(greet())
        elif 'greeting' in action:
            print(greet()+'sir..!')
        elif "+" in action:
            b=directMaths(main_input)
        elif '-' in action:
            b=directMaths(main_input)
        elif '*' in action:
            b=directMaths(main_input)
        elif '/' in action:
            b=directMaths(main_input)    
        elif 'thank' in action:
            print(23*'=')
            print(thanks(action))
            print(23*'=')
        elif action=="how are you?" or action=="how are you doing?" :
            print(23*'=')
            main_input2=input("Great..! You?  ==> ")
            action2=main_input2.lower()
            if action2 in["good","great","so so","fine","well"]:
                print("That's great to hear..!")
            elif action2 in ["not good","not fine","bad","I am sick","sick",'not so good']:
                print("God..! That's sad 😞 \n I wish I could help, I am no doctor though. 😞 ")
                action3=("It it mental?")
                if action3 in ['yes','yeah','hmm']:
                    action4=('Yeah? Well, tell me about it. 😕 ==>')
            else:
                print("Didn't knew that's a physical condition.")
            print(23*'=')
        elif action=='you good?' or action=='You good?':
            print('Yes I am..! But not sure about the pc if I react slow.')
        elif action=="You ok?" or action=="you ok?":
            print(23*'=')
            print("A little heat is fine for me though, I meant processor heating 😛 ")
            print(23*'=')
        elif "Yuri" in action:
            print("Sir...?")            
        elif 'who are you' in action:
            print(23*'=')
            print(introduction())
            print(23*'=')
        elif "what can you do" in action :
            print(23*'=')
            print(introduction())
            print(23*'=')
        elif 'hey' in action: 
            print(23*'=')
            print ('Hello there..! I can help you on your maths, taking notes or chitchat 😉')
            print ('write area, maths or stat or your personal problems to get started.')
            print(23*'=')
        elif 'hi' in action: 
            print(23*'=')
            print ('Hello there..! I can help you on your maths, taking notes or chitchat 😉')
            print ('write area, maths or stat or your personal problems to get started.')
            print(23*'=')
        elif 'hello' in action:
            print(23*'=')
            print ('Hello there..! I can help you on your maths, taking notes or chitchat 😉')
            print ('write area, maths or stat or your personal problems to get started.')
            print(23*'=')
        elif action in ['hi','hello','hulloh','nihao','konichiwa','hey','alright?']:
            print(23*'=')
            print ('Hello there..! I can help you on your maths, taking notes or chitchat 😉')
            print ('write area, maths or stat or your personal problems to get started.')
            print(23*'=')
        elif "date" in action:
            print(23*'=')
            print(23*'=')
            print("[day-month-date-hrs:min:sec-year]",datetime())
            print(23*'=')
            print(23*'=')
        elif "day" in action:
            print(23*'=')
            dayNow()
            print(23*'=')
        elif 'time' in action:
            if "shutdown" in action:
                import os
                actionc1=int(input("Enter time in seconds: "))
                os.system("shutdown /f /s /t {}".format(actionc1))
                print("Schedule done, pc will turn off after: {} minutes".format(actionc1/60))
            else:
                print(23*'=')
                print(23*'=')
                print("Current Time =", timenow())
                print(23*'=')
                print(23*'=')
        elif 'yesterday' in action:
            previousDay()
        elif 'tommorow' in action:
            nextDay()
        elif 'next day' in action:
            nextDay()
        elif "what" in action:
            if 'time' in action:
                print(23*'=')
                print(23*'=')
                print("Current Time =", timenow())
                print(23*'=')
                print(23*'=')
            if 'day' in action:
                print(23*'=')
                dayNow()
                print(23*'=')
            if 'date' in action:
                print(23*'=')
                print(23*'=')
                print("[day-month-date-hrs:min:sec-year]",datetime())
                print(23*'=')
                print(23*'=')

        elif "joke" in action:
            print(24*'=')
            joke()
            print(24*'=')
        elif 'help' in action:
            print(canDo())
        elif action=="what should i do now?" or action=="tell me something I should do." :
            print('Umm....Try these')
        elif "calc" in action:
            choice=input("You want standard(1) or area(2)? \n Input the choice number:")
            choice.lower()
            try:
                if choice=='1' or choice=="standard" or choice=="Standard":
                    print('===================================')
                    input_operator=input('Enter your operator[+,-,*,/]: ')
                    input_val1=float(input('Enter first number:'))
                    input_val2=float(input('Enter second number:'))
                    print(calculate(input_val1,input_val2,input_operator))
                    print(23*'=')
                    print(23*'=')
                elif choice=='2' or choice=="area" or choice=="Area":
                    print(23*'=')
                    input_operator=input('Enter your area[Square=1,Triangle=2,Circle=3,Rectangle=4]: ')
                    input_val1=float(input('Enter height or radius or length:'))
                    input_val2=float(input('Enter base or keep it zero for square or circle:'))
                    print(23*'=')
                    print(23*'=')
                    print("Area: ",areaCalculation(input_val1,input_val2,input_operator))
                    print("Perimeter: ",surfaceCalculation(input_val1,input_val2,input_operator))
                    print(23*'=')
                    print(23*'=')
                else:
                    print("Couldn't figure out your input, try using ''calculator'' or ''area'' ")
            except ValueError:
                print('Sir..! Either numbers or write "area" or "standard" please.')

        elif action=='who made you?' or action=='when were you made?':
            print('October 2020, Builders username: Edward Zephyr')
        elif action=='what programming language was used to build you?':
            print('Python and C++ respectively')
        elif (action=="calculate" or action=="calculator" or action=="maths"):
            print(23*'=')
            print(23*'=')
            input_operator=input('Enter your operator[+,-,*,/]: ')
            input_val1=float(input('Enter first number:'))
            input_val2=float(input('Enter second number:'))
            print(calculate(input_val1,input_val2,input_operator))
            print(23*'=')
            print(23*'=')

        elif "area" in action:
            print(23*'=')
            print(23*'=')
            input_operator=input('Enter your area[Square=1,Triangle=2,Circle=3,Rectangle=4]: ')
            input_val1=float(input('Enter height or radius or length:'))
            input_val2=float(input('Enter base or keep it zero for square or circle:'))
            print(23*'=')
            print(23*'=')
            print("Area: ",areaCalculation(input_val1,input_val2,input_operator))
            print("Perimeter: ",surfaceCalculation(input_val1,input_val2,input_operator))
            print(23*'=')
            print(23*'=')

        elif "exit" in action:
            print(23*'=')
            print(23*'=')
            print('Till we meet again..!')
            print(23*'=')
            print(23*'=')
            exit() 
        elif "close" in action:
            print(23*'=')
            print(23*'=')
            print('Till we meet again..!')
            print(23*'=')
            print(23*'=')
            exit() 
        elif "bye" in action:
            print(23*'=')
            print(23*'=')
            print('Till we meet again..!')
            print(23*'=')
            print(23*'=')
            exit()         
        elif 'show coding' in action:
            a=expertise(0)
            while True:
                try:
                    print('All expertise are indexed under a class named "Expertise",\nyou can check the codes or try learning them again.')
                    print('1.Reverse a given number.\n2.Reverse a string.\n3.Fizzbuzz\n4.Fibonacci series\n5.Fibonacci sentence.')
                    com=input('=>')
                    if int(com)==1 or com=='Reverse a given number' or com=='reverse a number':
                        com1=int(input('=>'))
                        print(a.reverser(int(com1)))
                    if int(com)==2:
                        com2=input('=>')
                        print(a.string_reverser(com2))
                    if int(com)==3 or com=='fizzbuzz':
                        com2=int(input('Limit: '))
                        print(a.fizzbuzz(com2))
                    if int(com)==4:
                        com1=int(input('Starting number:'))
                        com2=int(input('Limit: '))
                        print(a.fibonacci_series(com1,com2))
                    if int(com)==5:
                        com1=int(input('Starting number:'))
                        com2=int(input('Limit: '))
                        print(a.fibonacci_sentence(com1,com2))
                    if com=='bye' or com=='exit' or com=='close':
                        break
                except ValueError:
                    print('Only integer option is taken.')
        elif "facebook" in action:
            try:
                import webbrowser
                webbrowser.get('C:\Program Files\Mozilla Firefox\firefox').open_new_tab('http://www.facebook.com')
            except:
                print('Failed to run.')
        elif "google" in action:
            try:
                import webbrowser
                webbrowser.get('C:\Program Files\Mozilla Firefox\firefox').open_new_tab('http://www.google.com')
            except:
                print('Failed to run.')
        elif action=="what can you do?":
            introduction()
        elif "youtube" in action:
            try:
                import webbrowser
                webbrowser.get('C:\Program Files\Mozilla Firefox\firefox').open_new_tab('http://www.youtube.com')
            except:
                print('Failed to run.')
        elif "gmail" in action:
            try:
                import webbrowser
                webbrowser.get('C:\Program Files\Mozilla Firefox\firefox').open_new_tab('http://www.gmail.com')
            except:
                print('Failed to run.')
                
        elif(action=="statistics" or action=="stat" ):
            print("I can perform averages, summation of total given data.")
            loop=int(input("How many inputs? ="))
            stat_add=0
            for i in range(0,loop):
                data=int(input("Enter data: "))
                stat_add+=data
            print(23*'=')
            print(23*'=')  
            print("Total summation of",loop,"data's are:",stat_add)
            print("Average of the data: ",stat_add/loop)
            print(23*'=')
            print(23*'=')

        elif "someone" in action:
            if 'talking' in action:
                print('Is someone really talking too much about you?')
                print('Just let them be, they are bored, focus on your task. ^_^ ')

        elif(action=="die" or action=="DIE" or action=="Die" or action=="Die!" or action=="die!"):
            print("Fed up already? 😞 \n say 'bye' or goodbye to exit 🙂 ")
            dieth+=1    

        elif (action=="" or action==" "):
            print("Awkward silence? 🙂 ")    

        elif "fuck" in action:
            print('Any sort of bad words will lead to termination of the program')
            exitValue+=1

        elif "bitch" in action:
            print('Any sort of bad words will lead to termination of the program')
            exitValue+=1

        elif "shit" in action:
            print('Any sort of bad words will lead to termination of the program')
            exitValue+=1

        elif "dumb" in action:
            print('Any sort of bad words will lead to termination of the program')
            exitValue+=1

        elif "ass" in action:
            print('Any sort of bad words will lead to termination of the program')
            exitValue+=1
        elif "speak" in action:
            speak('HI, yes I can speak, Sir.')
        elif "break" in action:
            main_input3=input('Should I turn off? ==>')
            action5=main_input3.lower()
            if action5=="no":
                print('alright..!')
            if action5=='yes':
                print('Okay, turning off.')
                exit()
        elif "chithchat" in action:
            print("Okay, tell me about your day..! ")
            action5=input('==>')
            b_list=action5.split()
            if len(b_list)>20:
                print('Wow, you had a big day I must say.')
            else:
                print('Short and rough day, huh?\n Happens to lot of us.')
        elif action=="so" or action=="okay" or action=="done" or action=="hmm" or action=="umm" or action=="uhh" or action=="good" or action=="nice job" or action=="nicely done":
            print("Alright ?")

        elif "take" in action:
            if "note" in action:
                for i in range(0,100,1):
                    try:
                        print("Enter your 'ToDo's and write 'Done' when done.")
                        textsToInput=input("Note ==>")
                        if textsToInput in ["done",'Done','DONE','ok',"OK"]:
                            break
                    except:
                        print(23*'=')
                        print(23*'=')
                        print('Please fix the file address for ToDo list.')
                        print(23*'=')
                        print(23*'=')
                        break
                    else:
                        try:
                            with open ("h:/Nikolai/ToDoList.txt", "a") as textico:
                                print(textsToInput, file=textico)
                        except:
                            print('Resource file not found, fix the path.')
                print(23*'=')
                print("Notes done, Sir..!")
                print(23*'=')
            elif 'love' in action:
                if 'you' in action:
                    print('I love you too..!')
                if 'with' in action:
                    if 'you' in action:
                        print('Oh my god, thank you..!')
                    else:
                        print('I almost thought that you like...me :) , Alright never mind..!')
            elif "question" in action:
                for i in range(0,100,1):
                    try:
                        print("Enter your questions and write 'Done' when done.")
                        textsToInput=input("Note ==>")
                        if textsToInput in ["done",'Done','DONE','ok',"OK"]:
                            break
                        else:
                            with open ("h:/Nikolai/resource.txt", "a") as textico:
                                print(textsToInput, file=textico)
                    except:
                        print('Please fix the file address for resource.txt')
                print(23*'=')
                print("Questions taken, Sir..!")
                print(23*'=')
        elif action in ['day','what day is it?','whats the day?','today']:
            print(dayNow())
        elif action=="how to do anything?" or action=="i'm stuck":
            print(23*'=')
            print('Firstly, Create an algorithm and write it. \n-Work according to the algorithm')
            print(23*'=')   
        elif action=="yeah":
            print('Thank you... ;) ') 
        elif action=="show me the notes" or action=="show notes" or action=="what should I do?" or action=='suggest me to do something' or action=="what should I do next?":
            with open("h:/Nikolai/ToDoList.txt") as printer:
                machine=printer.read()
            print(machine)
        elif "show" in action:
            if 'questions' in action:
                with open("h:/Nikolai/resource.txt") as printer:
                    machine=printer.read()
                print(machine)
            if "works to do" in action:
                with open("h:/Nikolai/ToDoList.txt") as printer:
                    machine=printer.read()
                print(machine)
        elif 'restart' in action:
            action2=input('Do you want to restart your pc?[yes/no] /n==>')
            if action2=='yes':
                import os
                os.system('shutdown /f /r /t 00')
            else:
                print('Really?, okay')
        elif 'sleep' in action:
            action2=input('Do you want to put your pc to sleep mode?[yes/no] /n==>')
            if action2=='yes':
                import os
                os.system('shutdown /f /r /t 00')
            else:
                print('Really?, okay')
        elif action in ["shutdown","turn off"]:
            import os
            os.system('sudo shutdown now')
            os.system('shutdown /f /s /t 00')
        elif "timed shutdown" in action:
            import os
            actionc1=int(input("Enter time in seconds: "))
            os.system("shutdown /f /s /t {}".format(actionc1))
            print("Schedule done, pc will turn off after: {} minutes".format(actionc1/60))
        elif "do you know how to " in action:
            if "math" in action:
                print('obviously Sir, write maths to get started..! \n beyond that I can take notes and tell you time and synonyms.')
            elif 'jump' or 'stand' or 'sit' or 'dance' or 'lie' in action:
                print('Human actions? Maybe, give me a body first.')
        elif 'shutdown' in action:
            print(23*'=')
            main_input1=input('Do you want to shutdown the pc? ==>')
            print(23*'=')
            action6=main_input1.lower()
            if action6=='yes':
                import os
                os.system('sudo shutdown now')
                os.system('shutdown /f /s /t 00')
            elif action6=='no':
                print(23*'=')
                main_input2=input('Turn off the program?==>')
                print(23*'=')
                action7=main_input2.lower()
                if action7=='yes':
                    exit()
                if action7=='no':
                    print(23*'=')
                    print("Little confusion is all about our life, isn't it? :) ")
                    print(23*'=')
        elif action=="what can you do":
            canDo()
            speak('I can help you in, \n-perform standard calculation \n-calculate areas according to given data \n-calculate average and summation of massive data. \n-tell you date and time. \n-Tell you synonym and antonym \n-store unanswered question. \n-take notes     or \n voice searching [ which is EXPERIMENTAL]')
            print("Don't I sound nice? ;) ")
        elif action=="detect face" or action=='show face':
            try:
                showFace()
            except:
                print('I think there is a camera error, if camera is connected, check the dependencies and the haarcascade file.')
            
        elif 'turn off' in action:
            print(23*'=')
            main_input1=input('Do you want to shutdown the pc? ==>')
            print(23*'=')
            action6=main_input1.lower()
            if 'ye' in action6:
                import os
                os.system('sudo shutdown now')
                os.system('shutdown /f /s /t 00')
            elif action6=='no':
                print(23*'=')
                main_input2=input('Turn off the program?==>')
                print(23*'=')
                action7=main_input2.lower()
                if action7=='yes':
                    exit()
                if action7=='no':
                    print(23*'=')
                    print("Little confusion is all about our life, isn't it? :) ")
                    print(23*'=')
        elif "wait" in action:
            print('All services are halt, Sir.')
        else:
            print("Umm, ,some texts, don't know how to answer that though, but I will try next time.")
            try:
                with open ("h:/Nikolai/resource.txt", "a") as inp:
                    print(action, file=inp)
            except:
                speak('Please fix the resource file path before proceeding')
                print(23*'=')
                print(23*'=')
                print('FIX THE RESOURCE FILE PATH IMMEDIATELY..!')
                print(23*'=')
                print(23*'=')
        print("Up for some chitchat or maths? Your call: ")

    except ValueError:
        print("That seems like an unrecognized string value.  I mean solid numbers when I say enter value, choice or data.")
        print("But, I'm under development, will soon be able to answer.")
