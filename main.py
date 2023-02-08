# from date import datetime
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
activationWord = 'vamsi'


def speak(text,rate=120):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for command')

    with sr.Microphone() as source:
        listener.pause_threshold=2
        input_speech = listener.listen(source)


    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech,language='en-db')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'

    return query

if __name__=='__main__':
    speak("yes all systems nominal.")

    while True:
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] =='say' or query[0]=='fuck' or query[0]=='dingutha' or query[0]=='venukuth' or query[0]=='dingu tha':
                if 'hello' in query:
                    speak('yes Hello everyone.')
                if 'fuck' in query:
                    speak('yes fuck you asshole')
                if 'dingutha' in query or 'venkutha' in query or 'dingu tha' in query:
                    speak(' yes gudhaaa paagaalu denguuthaa')
                    speak(' yes yeerriipukaa')
                else:
                    query.pop(0)
                    speech=' '.join(query)
                    speak(speech)

