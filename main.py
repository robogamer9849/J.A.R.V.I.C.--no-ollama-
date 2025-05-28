from pathlib import Path
from config import *
import os
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
send_notification('recording...')
logging.info('Started recording audio')
recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
sounddevice.wait(duration)
wavio.write(f"{Path(__file__).parent.resolve()}/recording.mp3", recording, freq, sampwidth=2)
logging.info('Audio recording completed')

model = whisper.load_model(whisperModel)
logging.info(f'Loaded Whisper model: {whisperModel}')
user_message = model.transcribe(f"{Path(__file__).parent.resolve()}/recording.mp3")["text"].lower().replace('.', '').replace('%', '')
logging.info(f'Transcribed message: {user_message}')

if ('volume' or 'audio' or 'sound' or 'mute' or 'unmute') in user_message:
    logging.info('Processing sound-related command')    
    command = voice_cmd(user_message = user_message)

if ('brightness' or 'brightest' or 'light' or 'backlight') in user_message:
    logging.info('Processing brightness-related command')
    command = brightness_cmd(user_message = user_message)

if ('open' or 'run' or 'lunch' or 'show') in user_message:
    for word in user_message.split():
        try:
            print(word)
            command = apps[word]
            send_notification(f'opening {word}')
            break
        except:
            continue
if ('take' or 'shoot' or 'capture') and ('screen' or 'display' or 'screenshot') in user_message :
    command = screenshot_cmd + '&' + screenshot_open_path

try:
    run_cmd(command)
except:
    if ('clear' or 'delete') in user_message and ('logs' or 'log') in user_message:
        log_file = f'{Path(__file__).parent.resolve()}/pengu_speak.log'
        if os.path.exists(log_file):
            os.remove(log_file)
            send_notification('Log file cleared')
    else:
        logging.warning(f'Unrecognized command: {user_message}')
        send_notification(f"I din't understand that, please try again\n'{user_message}'")