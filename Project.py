import pyautogui as p	#For controlling mouse and keyboard virtually
import webbrowser as w	#For opening web.whatsapp.com
import requests	#For webscraping
from bs4 import BeautifulSoup	#For webscraping
import time
import tkinter
import random
import wikipedia as wk	#For info on a particular topic	OP
import re	#"Tel me about xyz" For extracting xyz from sent
from urllib.request import urlopen #For webscraping
import pyperclip

last_wrd = None
counterl = 0	
counter2 = 0
counter3 = 0
counter4 = 0

choce = ["God!",	#Some common prefixes
	"Mannn! I have already told you! ",
	"You forgot so easily!",
	"Come on, I already told you ",
	"Do I need to say again?"]

def send(msg):
    print(">",msg)
    p.typewrite(msg)	
    time.sleep(0.1)	
    p.press("enter")

def get_last_wrd():
    p.moveTo(462,622)
    p.dragRel(325,100,0.5)
    p.hotkey("ctrl","c")
    last_w= tkinter.Tk().clipboard_get()
    last_wrd = str(last_w.lower())

def get_reply():
    p.moveTo(462,622)
    p.dragRel(325,100,0.5)
    p.hotkey("ctrl","c")
    reply_word = tkinter.Tk().clipboard_get()
    print(reply_word)
    reply = str(reply_word.lower())
    return reply

def play_game():
    send("Are you ready ?")
    time.sleep(10)
    reply = get_reply()
    if reply == 'no':
        send("Okay")
    elif reply == 'yes':
        a = 1
        while a==1:
            reply = get_reply()
            if 'yes' in reply:
                break
            elif 'exit' in reply:
                exit()
            elif 'no' in reply:
                send("Okay")
                continue
        x = random.randrange(1,100)
        str_x = str(x)
        tries = 1
        while tries <= 5 :
            send("Give your guess " + str(tries) + " => ")
            time.sleep(10)
            guess = get_reply()
            tries += 1
            if 'exit' in guess :
                exit()
            guess_int = int(guess)
            if guess_int == x :
                string = "Congratulations!!! You won the game."
                send(string)
                last_wrd = sr(string)
                break
            elif tries <= 5 :
                if guess_int > x :
                    string = "The mystery number is smaller than your guess."
                    send(string)
                    last_wrd = str(string)
                    pass
                elif guess_int < x :
                    string = "The mystery number is bigger than your guess."
                    send(string)
                    last_word = str(string)
                    pass
        if tries >= 6 :
            string = "Sorry, You were not able to guess the number. The number was " + str_x
            send(string)
            last_wrd = str(string)

w.open("https://web.whatsapp.com/")
time.sleep(10)
p.click(100,230)
time.sleep(1)

try :
    while True:
        p.moveTo(462,622)
        p.dragRel(325,100,0.5)
        p.hotkey("ctrl","c")
        reply_word = tkinter.Tk().clipboard_get()
        reply = str(reply_word.lower())
        print(reply)
        if reply != last_wrd:
            if "hello" in reply or "hi" in reply:
                counterl += 1
                current_time = time.localtime()
                hr = current_time.tm_hour
                if hr < 12:
                    good = "morning"
                elif (hr >= 12) and (hr <= 17):
                    good = "afternoon"
                elif hr > 17:
                    good = "evening"
                string = "Good" + good
                if counterl <= 2:
                    send(string)
                    last_wrd = str(string)
                elif counter1 > 2:
                    string = "We are already talking but - " + string
                    send(string)
                    last_wrd = str(string)

            elif "how are you" in reply:
                send("Well!")
                counter2 += 1
                if (counter2 == 1):
                    string = "I am fine, thank you."
                    send(string)
                    last_wrd = str(string)
                    last = time.time()
                else:
                    current = time.time()
                    string = "Same as I was "+ str(int(current-last)) +" seconds ago. "
                    send(string)
                    last_wrd = str(string)
                
            elif "your name" in reply:
                counter3 = counter3+1
                if counter3 <=1:
                    string = "I don't have any name."
                    send(string)
                    last_wrd = str(string)
                    
                else:
                    chk = random.choice(choce)
                    string = chk + "I don't have any name."
                    send(string)
                    last_wrd = str(string)

            elif "news" in reply:
                send("Please wait while I fetch fresh news.")
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "html.parser")
                news_list = soup_page.findAll("item")
                send("Here are top 3 news")
                for news in news_list[:3]:
                    send(news.title.text)
                get_last_wrd()
                
                
            elif "tell me about" in reply:
                topic = re.search("tell me about (.+)", reply).group(1)
                send("Please wait while I gather information about " + topic)
                summry = wk.summary(topic, sentences = 2)
                send(summry)
                get_last_wrd()
                

            elif "play" and "game" in reply:
                counter4 += 1
                if counter4 == 1:
                    send("Okay,")
                    send("The rules of the game are :-")
                    send("1)I will choose a random number between 1 to 100, including both the numbers.")
                    send("2)You have to guess that number in max 5 tries.")
                    send("3)After every try you make, I will give you a hint if the the number is greater than mine or less.")
                    send("You will have 10 seconds to answer each question and 30 seconds to read these instructions")
                    send("If at any moment, you want to exit, type \"exit\".")
                    time.sleep(30)
                    play_game()
                    send("If you want to play the game again, type any sentence with \"play\" and \"game\"")
                    get_last_wrd()
                else :
                    play_game()
                    get_last_wrd()
                
            elif "exit" in reply :
                send("Ok, Nice talking to you, Bye!!!")
                exit()

            else :
                string = "This is not in my program, so ask me a different question."
                send(string)
                last_wrd = string
                
            time.sleep(5)	#Sleep for five seconds and repeat the same process!
            
        else:
            time.sleep(5)
except :
    send("An error occured")
    pass
