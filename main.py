from pathlib import Path
from config import *
import whisper
import sounddevice
import wavio
import logging
from functionss.generalFunctions import *
from functionss.sound import *
from functionss.brightness import *

# Configure logging
logging.basicConfig(
    filename=f'{Path(__file__).parent.resolve()}/pengu_speak.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


freq = 44100
duration = 7

print('recording...')
send_notification('recording')
logging.info('Started recording audio')
recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
sounddevice.wait(duration)
wavio.write("recording.mp3", recording, freq, sampwidth=2)
logging.info('Audio recording completed')

model = whisper.load_model(whisperModel)
logging.info(f'Loaded Whisper model: {whisperModel}')
user_message = model.transcribe("recording.mp3")["text"].lower().replace('.', '').replace('%', '')
logging.info(f'Transcribed message: {user_message}')

if 'volume' in user_message or 'audio' in user_message or 'sound' in user_message or 'mute' in user_message or 'unmute' in user_message:
    logging.info('Processing sound-related command')    
    command = voice_cmd(user_message = user_message)

if 'brightness' in user_message or 'brightest' in user_message or 'light' in user_message or 'backlight' in user_message:
    logging.info('Processing brightness-related command')
    command = brightness_cmd(user_message = user_message)

if 'open' in user_message or 'run' in user_message or 'lunch' in user_message or 'show' in user_message:
    for word in user_message.split():
        try:
            print(word)
            command = apps[word]
            send_notification(f'opening {word}')
            break
        except:
            continue

try:
    run_cmd(command)
except:
    logging.warning(f'Unrecognized command: {user_message}')
    send_notification("I din't understand that, please try again")