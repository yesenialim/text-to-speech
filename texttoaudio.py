from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

def textToSpeech():
  text=entry.get()
  language='zh-cn'
  output=gTTS(text=text,lang=language,slow=False)
  output.save('output.mp3')
  os.system("afplay output.mp3")



entry = Entry(root)
canvas.create_window(200,180,window=entry)

button=Button(text='Start',command=textToSpeech)
canvas.create_window(200,230,window=button)
root.mainloop()

'''
text=open('demo.txt','r').read()
language='en'
output= gTTS(text=text,lang='en',slow=False)
output.save('fileoutput.mp3')
os.system("afplay fileoutput.mp3")

'''
'''
text="this is really funny"
output= gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system("afplay output.mp3")

'''
