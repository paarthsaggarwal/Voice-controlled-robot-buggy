import speech_recognition as sr
import wit
import time
import RPi.GPIO as GPIO
from gpiozero import Robot
import pyttsx3
import beepy


engine = pyttsx3.init(driverName='espeak')

robot = Robot(left = (20, 21), right = (19, 26))

def f1():
    while True:
        robot.forward(0.5)
        time.sleep(0.5)
        #print("F")
        hear()

def hear():
    while True:
        try:
            r = sr.Recognizer()
            source = sr.Microphone()
            with source as source:
                print("I'm listening...")
                r.adjust_for_ambient_noise(source)
                beepy.beep(sound="ping")
                audio = r.listen(source, phrase_time_limit = 2)
                print("Recognizing...")
                words = r.recognize_google(audio, language="en-GB")
                #words = r.recognize_wit(audio, key = "FD5G2CHDOG4ET3APAROEZ7RRLL3ETO6C")
                print(words)
                #print("You said using Wit: " + recog1)
                if "right" in words:
                    r1()
                elif "left" in words:
                    l1()
                    #print("left")
                elif "forward" in words:
                    engine.say("Moving forward")
                    engine.runAndWait()
                    f1()
                elif "stop" in words:
                    s1()
                else:
                    words = "I am moving"
                    engine.say(words)
                    engine.runAndWait()
                    f1()

        except:
            words = "I am moving"
            engine.say(words)
            engine.runAndWait()
            f1()

def r1():
    engine.say("Moving right, Your Highness")
    engine.runAndWait()
    robot.right()
    time.sleep(0.5) # 0.7
    print("R")
    #while True:
    robot.forward(0.5)
    time.sleep(0.5)
    print("F")
    hear()

def l1():
    engine.say("Moving left, Your Highness")
    engine.runAndWait()
    robot.left()
    time.sleep(0.5) # 0.7
    print("L")
    #while True:
    robot.forward(0.5)
    time.sleep(0.5)
    print("F")
    hear()



def s1():
    engine.say("Stopping, Your Highness, I am tired too")
    engine.runAndWait()
    print("S")
    while True:
        robot.stop()
