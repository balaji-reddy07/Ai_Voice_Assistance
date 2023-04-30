from datetime import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
#import openai

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
activationWord = 'prime'

chrome_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

appId ='WYERTK-AHRAEY592A'
wolframClient = wolframalpha.Client(appId)

def speak(text,rate=120):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)


    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'

    return query

def search_wikipedia(query= ''):
    searchResult = wikipedia.search(query)
    if not searchResult:
        print('No wikipedia result')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResult[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']

def search_wolframAlpha(query=''):
    response = wolframClient.query(query)

    if response['@success'] == 'false':
        return 'Could not compute'
    else:
        result= ''
        pod0 = response['pod'][0]
        pod1 = response['pod'][1]
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary','false')):
            result = listOrDict(pod1['subpod'])
            return result.split('(')[0]
        else:
            question = listOrDict(pod0['subpod'])
            return question.split('(')[0]

            speak('Computation failed. Querying universal databank.')
            return search_wikipedia(question)


if __name__=='__main__':
    speak("yes all systems nominal.")
    speak("lets start")
    speak("  listening for command")
    while True:
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            if query[0] =='say' or query[0]=='se' or query[0]=='fuck' or query[0]=='dingutha' or query[0]=='venukuth' or query[0]=='dingu tha':
                if 'hello' in query:
                    speak('yes Hello everyone.')
                    speak('Nice meeting you all')
                if 'fuck' in query:
                    speak('yes fuck you asshole')
                if 'dingutha' in query or 'venkutha' in query or 'dingu tha' in query:
                    speak(' yes gudhaaa paagaalu denguuthaa')
                    speak(' yes yeerriipukaa')
                else:
                    query.pop(0)
                    speech=' '.join(query)
                    speak(speech)

            if query[0]=='go' and query[1] =='to':
                speak('Opening...')
                query=' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)
                if 'Balaji' or 'balaji' in query:
                    webbrowser.get('chrome').open_new('balajireddy.netlify.app')

            if query[0] =='wikipedia':
                query =' '.join(query[1:])
                speak('Querying the universal databank.')
                speak(search_wikipedia(query))

            if query[0] == 'computer' or query[0] == 'compute':
                query = ' '.join(query[1:])
                speak('Computing')
                try:
                    result = search_wolframAlpha(query)
                    speak(result)
                except:
                    speak('Unable to compute')

            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%s.txt % now', 'w') as newFile:
                    newFile.write(now)
                    newFile.write(' ')
                    newFile.write(newNote)
                speak('Note written')

            if query[0] == 'exit':
                speak('Goodbye')
                break