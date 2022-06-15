from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry = ("500x400")
root.title("Youtube Downloader")

def Video_links():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        good_apple = YouTube(INPUT)

        #Video Information
        Output.insert(END,f"Downloading:\n {good_apple.title}")
        good_apple.streams.get_highest_resolution().download("C:/Users/danka/Downloads",f"{good_apple.title}.mp4")
        Output.insert(END,"\nDone loading")
    except:
        Output.insert(END, "\nError raised\n")
        print("Hi error its ya boy")
def Audio_links():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        good_apple = YouTube(INPUT)

        #Video Information
        Output.insert(END,f"Downloading:\n {good_apple.title}")
        good_apple.streams.get_audio_only().download("C:/Users/danka/Downloads",f"{good_apple.title}.mp3")
        Output.insert(END,"\nDone loading")
    except:
        print("Hi error its ya boy")
    return;

l = Label(text = "Youtube links go here ")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 
Output = Text(root, height = 5,
              width = 25,
              bg = "light cyan")
 
Display1 = Button(root, height = 2,
                 width = 20,
                 text ="Download Vids",
                 command = lambda:Video_links())
Display2 = Button(root, height = 2,
                 width = 20,
                 text ="Download Music",
                 command = lambda:Audio_links())


l.pack()
inputtxt.pack()
Display1.pack()
Display2.pack()
Output.pack()
mainloop()
