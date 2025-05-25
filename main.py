from time import sleep
from config import *
from notifypy import Notify
import whisper
import sounddevice
import wavio
import subprocess

def send_notification(title, message):
    notification = Notify()
    notification.title = title
    notification.message = message
    # if icon_path:
    #     notification.icon = icon_path
    notification.send()

def alert_user(message):
    send_notification("Alert", message)

def success_notification(message):
    send_notification("Success", message)

def error_notification(message):
    send_notification("Error", message)

freq = 44100
duration = 7

print('recording...')
send_notification('va', 'recording')
recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
sounddevice.wait(duration)
wavio.write("recording.mp3", recording, freq, sampwidth=2)

model = whisper.load_model(whisperModel)
user_message = model.transcribe("recording.mp3")["text"].lower()

print(user_message)

