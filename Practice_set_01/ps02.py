###### P-2: install an external module and use it to perform an operation of your interest
# install pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("""Johny, Johny!
Yes papa?
Eating sugar?
No papa.
Telling lies?
No papa.
Open your mouth!
Ha ha ha! """)
engine.runAndWait()