#Hello friends!

#Today, I will show you how to make python talk or text-to-speech in Windows

#Well! For that there are many modules. But, I will show the two easiest of them.

#First module - pyttsx3

#Step1: Install it using - 'pip install pyttsx3'
#step2: Run the code -

'''import pyttsx3
engine = pyttsx3.init()
engine.say('Hello world!')
engine.runAndWait()
'''

#Module 2 - win32com

#Step1: Install win32com using - 'pip install win32com'
#Step2: Run the code -

import win32com.client as winc1
speak = winc1.Dispatch('SAPI.spVoice')
speak.Speak('Hello world')

#Sorry! I forgot to exclude the previous code. Now let's run it and test it.
#I have posted the code on Github. The link is in the description below.

#Thanks for watching!! BYE!!
