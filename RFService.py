import sys
import speech_recognition as sr

def write_speech_from_mic(recognizer, microphone):
    print('Speak->')
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            output = recognizer.recognize_google(audio)
            print(output)
            if('exit' in output):
                sys.exit()
        except sr.RequestError:
            print("API unavailable")
        except sr.UnknownValueError:
            print("Unable to recognize speech")
    return


print("\n_SPEECH RECOGNITION_  (Say (Exit) to quit)\n")

recognizer = sr.Recognizer()
microphone = sr.Microphone()

recognizer.energy_threshold = 600

while True:
    write_speech_from_mic(recognizer, microphone)
        

    
    