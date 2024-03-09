import pyttsx3, speech_recognition as sr, random, os, webbrowser, datetime, wikipedia, pyjokes, subprocess, winshell, ctypes, time, ascii_magic
from ecapture import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 120)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    output=ascii_magic.from_image_file("2023-02-21 20 12 34.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    output=ascii_magic.from_image_file("laptop-with-voice-assistant-icon-vector-24351514.jpg",columns=175,char='@')
    ascii_magic.to_terminal(output)
    print()    
        

assname = "Jarvis 1 point O"
def UserName():
    speak("Hi I am"+assname+", What should i call you sir")
    uname = TakeCommand()
    speak("Hello"+uname+", welcome to jarvis 1 point O and now please tell me how may I help you")


def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Unable to Recognize your voice, can you please Say that again _/\_")
        print()
        return "None"

    return query

ANS='s'
while ANS.lower()=='s':
 print()
 WishMe()
 UserName()
 ans = True
 while ans:
    query = TakeCommand().lower()

    if 'wikipedia' in query:        
        speak("Searching wikipedia")
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'google' in query:
        speak("Searching in google")
        query = query.replace('google', '')
        webbrowser.open(query)
        speak("According to google")

    elif 'youtube' in query:
        speak("Opening youtube")
        webbrowser.open("youtube.com")

    elif 'spotify.com' in query or 'spotify website' in query:
        speak("Opening spotify website")
        webbrowser.open('https://open.spotify.com/?')

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print('Sir, the time is: ', strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'play music' in query:
        music_dir = 'D:\\Python Projects\\Voice Assistant\\songs'
        songs = os.listdir(music_dir)
        # print(songs)
        a = random.choice(songs)
        print(a)
        os.startfile(os.path.join(music_dir, a))

    elif 'linkedin.com' in query or 'linkedin website' in query:
        speak("Opening linkedin")
        webbrowser.open("linkedin.com")

    elif 'hackerrank.com' in query or 'hackerrank website' in query:
        speak("Opening hackerrank")
        webbrowser.open("hackerrank.com")

    elif 'geeks.org' in query or 'geeks website' in query:
        speak("Opening geeksforgeeks")
        webbrowser.open("geeksforgeeks.org")

    elif 'java point.com' in query or 'java point website' in query or 'javat point website' in query:
        speak("Opening javatpoint")
        webbrowser.open("javatpoint.com")

    elif 'programming.com' in query or 'programming website' in query:
        speak("Opening programiz")
        webbrowser.open("programiz.com")

    elif 'w3schools.com' in query or 'w3schools website' in query:
        speak("Opening w3schools")
        webbrowser.open("w3schools.com")

    elif 'godaddy.com' in query or 'godaddy website' in query:
        speak("Opening GoDaddy")
        webbrowser.open("GoDaddy.com")

    elif 'flipkart.com' in query or 'flipkart website' in query:
        speak("Opening flipkart")
        webbrowser.open("flipkart.com")

    elif 'amazon.in' in query or 'amazon website' in query:
        speak("Opening amazon.in")
        webbrowser.open("amazon.in")

    elif 'makemytrip.com' in query or 'makemytrip website' in query:
        speak("Opening makemytrip")
        webbrowser.open("makemytrip.com")

    elif 'trivago.com' in query or 'trivago website' in query:
        speak("Opening trivago")
        webbrowser.open("trivago.com")

    elif 'yatra.com' in query or 'yatra website' in query:
        speak("Opening yatra")
        webbrowser.open("yatra.com")

    elif 'goibibo.com' in query or 'goibibo website' in query:
        speak("Opening goibibo")
        webbrowser.open("goibibo.com")

    elif 'booking.com' in query or 'booking website' in query:
        speak("Opening booking.com")
        webbrowser.open("booking.com")

    elif 'greatlearning.com' in query or 'greatlearning website' in query:
        speak("Opening mygreatlearning")
        webbrowser.open("mygreatlearning.com")

    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")
        
    elif "good morning" in query or "good afternoon" in query or "good evening" in query:
        speak("A warm"+query+", how are you Mister")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")

    elif "change your name to" in query:
        query = query.replace("change your name to", "")
        assname = query

    elif "change name" in query:
        speak("What would you like to call me, Sir ")
        assname = TakeCommand()
        speak("Thanks for naming me")

    elif "what's your name" in query or "What is your name" in query:
        speak("My friends call me")
        print("My friends call me",assname)
        speak(assname)
        print()

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by soham maity")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "who i am" in query:
        speak("If you talk then definitely you are human")

    elif "why you came to world" in query:
        speak("Thanks to Gaurav. further It's a secret")

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who am i" in query:
        speak("you are programmer, who created mee")

    elif 'reason for you' in query:
        speak("I was created as a Major project by Mister soham maity")

    elif 'open bluestack' in query:
        speak("Opening bluestack app")
        app = r"C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
        os.startfile(app)

    elif 'open spotify' in query:
        speak("Opening spotify app")
        app = r"C:\\Users\\SOHAM MAITY\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(app)

    elif 'open canvas student' in query or 'open canvas' in query:
        speak("Opening canvas student app")
        app = r"C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
        os.startfile(app)

    elif 'open visual studio code' in query or 'open vs code' in query:
        speak("Opening visual studio code")
        app = r"C:\\Users\\SOHAM MAITY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(app)

    elif 'open whatsapp' in query:
        speak("Opening whatsapp")
        app = r"C:\\Users\\SOHAM MAITY\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(app)

    elif 'open anydesk' in query:
        speak("Opening anydesk app")
        app = r"C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"
        os.startfile(app)

    elif 'open zoom' in query:
        speak("Opening zoom app")
        app = r"C:\\Users\\SOHAM MAITY\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(app)

    elif 'open pic pic' in query:
        speak("Opening picpick app")
        app = r"C:\\Program Files (x86)\\PicPick\\picpick.exe"
        os.startfile(app)

    elif 'open microsoft edge' in query:
        speak("Opening microsoft edge")
        app = r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(app)

    elif 'open google chrome' in query:
        speak("Opening google chrome")
        app = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(app)

    elif 'open microsoft word' in query or 'open ms word' in query:
        speak("Opening microsoft word")
        app = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(app)

    elif 'open microsoft powerpoint' in query or 'open ppt' in query:
        speak("Opening microsoft powerpoint")
        app = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(app)

    elif 'open microsoft excel' in query or 'open ms excel' in query:
        speak("Opening microsoft excel")
        app = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(app)

    elif 'open python idle' in query or 'open python app' in query:
        speak("Opening python app")
        app = r"C:\\Python310\\Lib\\idlelib\\idle.pyw"
        os.startfile(app)

    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif 'empty recycle bin' in query:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin Recycled")

    elif "don't listen" in query or "stop listening" in query:
        speak("for how much time you want to stop jarvis from listening commands")
        a = int(TakeCommand())
        time.sleep(a)
        print(a)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("User asked to Locate")
        speak(location)
        webbrowser.open("https://www.google.nl/maps/place/"+location+"")

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "Jarvis Camera ", "img.jpg")

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif "write a note" in query:
        speak("What should i write, sir")
        note = TakeCommand()
        file = open('jarvis.txt', 'w')
        snfm = TakeCommand()
        file.write(note)
        file.close()

    elif "so note" in query or 'show note' in query or "show my note" in query:
        speak("Showing Notes")
        file = open("jarvis.txt", "r")
        note=file.read()
        print(note)
        speak(note)
        print()
        file.close()
                    
    elif "jarvis" in query:
        WishMe()
        speak("Jarvis 1 point o in your service Mister")
        
    elif "will you be my gf" in query or "will you be my bf" in query:  
        speak("I'm not sure about, may be you should give me some time")
 
    elif "how are you" in query:
        speak("I'm fine, glad you me that")
 
    elif "i love you" in query:
        speak("Sorry my friend, It's hard to understand")

    elif 'exit' in query:
        speak("Thank you for using jarvis voice assistant")
        print()
        output=ascii_magic.from_image_file("how-to-respond-to-thank-you.webp",columns=150,char='@')
        ascii_magic.to_terminal(output)
        print()
        ans = False
 print()
 ANS=input("Press 's' or 'S' to start the voice assistant again or else press any key to exit: ")
 print()