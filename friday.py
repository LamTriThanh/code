import pyttsx3
import datetime
import webbrowser as wb 
import os 
n = pyttsx3.init()
voice=n.getProperty('voices')
n.setProperty('voice', voice[1].id)




def noi(audio):
    print("Cmon :" + audio) 
    n.say(audio)
    n.runAndWait()


time=datetime.datetime.now().strftime("%I:%M:%p")


def wc():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<=12:
        noi("good moring sir")
    elif hour >=12 and hour<=18:
        noi("good afternoon sir")
    elif hour >=18 and hour<=24:
        noi("good night sir")
    noi("what do you want ")



def main():
    while True:
        tin = input("cmon listen :")

        if  "hi" in tin:
            rb = "hi tin"
        elif "thoat" in tin :
            break
        elif "what is your name" in tin:
            rb = "my name is Cmon"
        elif "time" in tin:
            rb = ("now is "+ time)
        elif "pygame" in tin:
            os.system('click_circle.py')
            rb = "open now"
        else:
            rb = "ok"
            continue

        print(noi(rb))

if __name__  =="__main__":
    wc()
    main()