import speech_recognition as sr
import wit
from gtts import gTTS
from io import BytesIO
from playsound import playsound
from googletrans import Translator
import time
import RPi.GPIO as GPIO
from gpiozero import Robot
import pyttsx3
import pygame

engine = pyttsx3.init(driverName='espeak')

r = sr.Recognizer()
source = sr.Microphone()
#translator = Translator()

from Requirement import *

while True:
    f1()