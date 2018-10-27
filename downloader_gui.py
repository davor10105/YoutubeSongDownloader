import youtube_api
from Tkinter import *
import youtube_api
import tkFont

class Application(Frame):
    def start(self):
        videoNames=self.text.get("1.0",'end-1c').splitlines()
	youtube_api.downloadVideos(videoNames)

    def createWidgets(self):
	helvetica=tkFont.Font(family='Helvetica', size=36, weight='bold')
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
	self.QUIT["font"]=helvetica

        self.QUIT.pack({"side": "right"})

        self.START = Button(self)
        self.START["text"] = "START"
	self.START["fg"]   = "green"
        self.START["command"] = self.start
	self.START["font"]=helvetica

        self.START.pack({"side": "left"})

    def __init__(self, text,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
	self.text=text

root = Tk()

text=Text(root,height=30,width=60, font = ('Arial',20))
app = Application(text,master=root)

app.pack(side=BOTTOM)
text.pack(side=TOP)
app.mainloop()
root.destroy()
