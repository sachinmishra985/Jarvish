import pyttsx3
import pyaudio
import pywhatkit as kit
import os
import subprocess as sp
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 150)
paths = {
    'notepad': "C:\\Windows\\SysWOW64\\notepad.exe",
    'visualcode': "C:\\Users\\Sachin Mishra\\OneDrive\\Desktop\\Visual Studio Code.lnk" ,
    'eclipse': "C:\\Users\\Sachin Mishra\\OneDrive\\Documents\\Eclipse IDE for Java Developers- 2021-06.Ink",
    'personal_documents': "E:\\my personal document",
    'my_music': "C:\\Users\\Sachin Mishra\\OneDrive\\Desktop\\Songs",
    'whatsapp': "C:\\Users\\Sachin Mishra\\OneDrive\\Desktop\\WhatsApp.lnk",
    'word': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word",
    'powerpoint': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint",
    'excel': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"


\

}
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening !")
    speak("I am jarvis  sir how may help you")

def takecommand ():
        r = sr.Recognizer()
        with sr.Microphone() as source :
            print("listening.............")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing............")
            query= r.recognize_google(audio,language="en-In")
            print(f" user said :{query}\n")
        except Exception as e:
            print("Say that again please ......")
            return "None"
        return query
def open_cmd():
    os.system('start cmd')
def open_calculator():
    sp.Popen(paths['calculator'])
def open_notepad():
    os.startfile(paths['notepad'])
def open_visualcode():
    os.startfile(paths['visualcode'])
def open_personal_documents():
    os.startfile(paths['personal_documents'])
def open_my_music():
    os.startfile(paths['my_music'])
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
def search_on_google(query):
    kit.search(query)
def open_eclipse():
    os.startfile(paths['eclipse'])
def open_whatsapp():
    os.startfile(paths['whatsapp'])
def open_word():
    os.startfile(paths['word'])
def open_powerpoint():
    os.startfile(paths['powerpoint'])
def open_excel():
    os.startfile(paths['excel'])
def open_gmail():
    webbrowser.open("https://mail.google.com//mail//u//1//#inbox")




if __name__ =="__main__" :
    wishMe()
    # speak("I take decisions and give output according to teh command")
    query = takecommand().lower()
    if'wikipedia' in query :
        speak('Searching wikipedia.......')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=3)
        speak("according to wikipedia")
        speak(results)
        print(results)
    elif'open youtube'in query:
        webbrowser.open("youtube.com")
        speak("ok sir ! now it was opened....... ")
    elif'open google'in query :
        webbrowser.open("google.com")
        speak("ok sir ! now it was opened....... ")

    elif'what is the time now'in query or 'whats time now'in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strtime}")
        print("the time is " + strtime)
    elif' can you open Gmail'in query or 'open Gmail..' in query:
        open_gmail()
        speak("ok sir ! now it was opened....... ")
    elif'open visual code ' in query:
        open_visualcode()
        speak("ok sir ! now it was opened....... ")
    elif'open Eclipse' in query:
        open_eclipse()
        speak("ok sir ! now it was opened....... ")
    elif 'who are you ' in query or 'whats your name' in query:
        speak("I am jarvis sir your Virtual assistant...")

    elif 'how are you' in query or 'what about you jarvis ' in query:
        speak("I am fine sir Thank you for asking")
        speak("How are you, Sir...")

    elif 'fine' in query or 'good' in query:
        speak("It's good to know that your fine")
    elif 'who made you' in query or 'who created you' in query:
        speak("I have been created by Amit ...")
    elif'introduce yourself' in query or 'who are you'in query:
        speak("Sir i am a virtual assistant.")
    elif'open cmd' in query:
        open_cmd()
        speak(" ok Sir! Now it was opened .....")
    elif'open calculator'in query:
        open_calculator()
        speak(" ok sir ! Now it was opened.....")
    elif 'open notepad' in query:
        open_notepad()
        speak(" ok sir ! Now it was opened.....")
    elif 'open personal documents' in query:
        open_personal_documents()
        speak(" ok sir ! Now it was opened.....")
    elif'open my music ' in query:
        open_my_music()
        speak("ok sir! Now it was opened....")
    elif'open camera' in query:
        open_camera()
        speak("ok sir! Now it was opened....")
    elif 'google' in query:
        speak('ok sir wait for a moment I am searching on Google, sir?')
        query = query.replace("google"," ")
        search_on_google(query)
    elif'open whatsapp' in query or 'jarvis I want to see my Whatsapp  ' in query:
        open_whatsapp()
        speak(" ok sir wait for a moment I am trying to open whatsapp")
    elif'open word'in query:
        open_word()
        speak(" ok sir wait for a moment I am trying to open Word")
    elif 'open PowerPoint' in query:
        open_powerpoint()
        speak(" ok sir wait for a moment I am trying to open PowerPoint")
    elif'open excel' in query:
        open_excel()
        speak(" ok sir wait for a moment I am trying to open excel")
    elif 'about Techno collage' in query:
        webbrowser.open("https://technocratsgroup.edu.in/")
        speak("ok sir ! now it was opened....... ")




