from pathlib import Path
from config import *
import os
import whisper
import sounddevice
import wavio
import logging
import spacy
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

print('Starting audio recording...')
send_notification('listening...')
logging.info('Initiating audio recording session')
recording = sounddevice.rec(int(duration * freq), samplerate=freq, channels=2)
sounddevice.wait(duration)
wavio.write(f"{Path(__file__).parent.resolve()}/recording.mp3", recording, freq, sampwidth=2)
logging.info('Successfully completed audio recording')

model = whisper.load_model(whisperModel)
logging.info(f'Successfully loaded Whisper model: {whisperModel}')
user_message = model.transcribe(f"{Path(__file__).parent.resolve()}/recording.mp3")["text"].lower().replace('.', '').replace('%', '')
logging.info(f'Successfully transcribed voice command: "{user_message}"')

if ('volume' or 'audio' or 'sound' or 'mute' or 'unmute') in user_message:
    logging.info('Processing sound-related command: adjusting system audio')    
    command = voice_cmd(user_message = user_message)

if ('brightness' or 'brightest' or 'light' or 'backlight') in user_message:
    logging.info('Processing brightness-related command: adjusting display settings')
    command = brightness_cmd(user_message = user_message)

if ('open' or 'run' or 'lunch' or 'show') in user_message:
    for word in user_message.split():
        try:
            print(word)
            command = apps[word]
            logging.info(f'Attempting to open application: {word}')
            send_notification(f'Opening application: {word}')
            break
        except:
            logging.debug(f'Application not found: {word}')
            continue

if ('take' or 'shoot' or 'capture') and ('screen' or 'display' or 'screenshot') in user_message :
    command = screenshot_cmd + '&' + screenshot_open_path
    send_notification('Capturing screenshot of your display')
    logging.info('Successfully captured and saved screenshot')

if ('search' or 'find' or 'google') in user_message:
    user_message = user_message.replace('search', '').replace('find', '').replace('google', '').strip()
    logging.info('Processing web search command')

    try:
        nlp = spacy.load(spacyModel)
    except OSError:
        run_cmd(f'python3 -m spacy download {spacyModel} --break-system-packages')
        nlp = spacy.load(spacyModel)

    doc = nlp(user_message)
    search_term = search_term = "".join(chunk.text for chunk in doc.noun_chunks)
    logging.info(f'Initiating web search for query: "{search_term}"')
    print(search_term)
    command = search_cmd(search_term)

if ('shutdown' or 'power off') in user_message:
    logging.info('Processing shutdown command')
    command = 'systemctl poweroff'
if ('restart' or 'reboot') in user_message:
    logging.info('Processing restart command')
    command = 'reboot'
if 'lock' in user_message:
    logging.info('Processing lock command')
    command = 'loginctl lock-session'




try:
    run_cmd(command)
except:
    if ('clear' or 'delete') in user_message and ('logs' or 'log') in user_message:
        log_file = f'{Path(__file__).parent.resolve()}/pengu_speak.log'
        if os.path.exists(log_file):
            os.remove(log_file)
            send_notification('Successfully cleared system log file')
    else:
        logging.warning(f'Unable to process unrecognized command: "{user_message}"')
        send_notification(f"Sorry, I couldn't understand that command. Please try rephrasing:\n'{user_message}'")