from tkinter import *
from pytube import YouTube
import time

#Make the program window for everyone to see
root = Tk()
root.geometry = ("800x600")
root.title("Youtube Downloader")

#Code to grab video links and download them as mp4/3

def splitURL(string):
    print (string)
    return list(string.split('~'))

def Video_links():
    #This is imput from the user after they press a button
    INPUT = inputtxt.get("1.0", "end-1c")
    url = splitURL(INPUT)
    for i in url:
        try:
        #Name of the youtube title to download being saved as Good_apple
            good_apple = YouTube(i)
            #Video Information
            Output.insert(END,f"\nDownloading:\n {good_apple.title}")
            time.sleep(2)
            good_apple.streams.get_highest_resolution().download("C:/Users/danka/Downloads",f"{good_apple.title}.mp4")
            Output.insert(END,"\nDone loading\n")
        except: 
            Output.insert(END, "\nError raised\n")
            print("Goodapple isnt so good. But the files load in DL folder somehow who cares")
        inputtxt.delete("1.0", "end-1c")

def Audio_links():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        good_apple = YouTube(INPUT)

        #Video Information
        Output.insert(END,f"Downloading:\n {good_apple.title}")
        good_apple.streams.get_audio_only().download("C:/Users/danka/Downloads",f"{good_apple.title}.mp3")
        Output.insert(END,"\nDone loading")
    except:
        Output.insert(END, "\nError raised\n")
        print("Hi error its ya boy")
    inputtxt.delete("1.0", "end-1c")



l = Label(text = "Youtube links go here ")
inputtxt = Text(root, height = 10,
                width = 45,
                bg = "light yellow")

Output = Text(root, height = 5,
              width = 45,
              bg = "light cyan")
 
Display1 = Button(root, height = 1,
                 width = 20,
                 text ="Download Vids",
                 command = lambda:Video_links())
Display2 = Button(root, height = 1,
                 width = 20,
                 text ="Download Music",
                 command = lambda:Audio_links())


l.pack()
inputtxt.pack()
Display1.pack()
Display2.pack()
Output.pack()
mainloop()
