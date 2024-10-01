import keyboard._keyboard_event
from langchain_community.llms import Ollama
import pyttsx3
from pynput import keyboard
engine=pyttsx3.init()
engine.setProperty("rate",150)
llm=Ollama(model="llama3.2:1b")
talk=1
try:
    while talk:
        print("Type \'bye\' to quit\n CTRL+C to stop Voice")
        me=input("me:")
        if me=='bye':
            talk=0
        response=llm.invoke(me)
        print(f'A.L.F.R.E.D:{response}')
        engine.say(response)
        engine.runAndWait()
except KeyboardInterrupt:
        engine.stop()
    

        
