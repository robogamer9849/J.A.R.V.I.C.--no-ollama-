from time import sleep
from config import *
from notifypy import Notify
import whisper
import sounddevice
import wavio
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename='pengu_speak.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_notification(message):
    notification = Notify()
    notification.title = 'PenguSpeak'
    notification.message = message
    notification.icon = 'logo.png'
    notification.send()
    logging.info(f'Notification sent: {message}')

def run_cmd(cmd):
    try:
        subprocess.Popen(cmd, shell = True)
        logging.info(f'Command executed: {cmd}')
    except Exception as e:
        logging.error(f'Command execution failed: {cmd}, Error: {str(e)}')
        pass


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
    print('sound related')
    if 'set' in user_message or 'change' in user_message:
        volume_level = None
        for word in user_message.split():
            try:
                volume_level = int(word)
                break
            except ValueError:
                continue
        print(volume_level)
        cmd = get_command('volume_set', volume_level)
        run_cmd(cmd)
        send_notification(f'volume is now {volume_level}')
    
    elif 'increase' in user_message:
        by = None
        for word in user_message.split():
            try:
                by = int(word)
                break
            except ValueError:
                continue
        print(by)
        cmd = get_command('volume_up', by)
        run_cmd(cmd)
        send_notification(f'volume increased by {by}')

    elif 'decrease' in user_message:
        by = None
        for word in user_message.split():
            try:
                by = int(word)
                break
            except ValueError:
                continue
        print(by)
        cmd = get_command('volume_down', by)
        run_cmd(cmd)
        send_notification(f'volume decreased by {by}')

    elif 'on mute' in user_message or 'unmute' in user_message or "on me it's" in user_message:
        cmd = get_command('volume_unmute', None)
        run_cmd(cmd)
        send_notification('your system is now unmuted')

    elif 'mute' in user_message or 'silent' in user_message:
        cmd = get_command('volume_mute', None)
        run_cmd(cmd)
        send_notification('your system is now muted')

if 'brightness' in user_message or 'brightest' in user_message or 'light' in user_message or 'backlight' in user_message:
    logging.info('Processing brightness-related command')
    print('brightness related')
    if 'set' in user_message or 'change' in user_message:
        if 'max' in user_message or 'maximum' in user_message:
            cmd = get_command('brightness_set', 100)
            run_cmd(cmd)
            send_notification(f'brightness is set to maximum')

        elif 'min' in user_message or 'minimum' in user_message or 'menu' in user_message or 'minimal' in user_message:
            cmd = get_command('brightness_set', 5)
            run_cmd(cmd)
            send_notification(f'brightness is set to minimum')
        
        else:
            brightness_level = None
            for word in user_message.split():
                try:
                    brightness_level = int(word)
                    break
                except ValueError:
                    continue
            print(brightness_level)
            cmd = get_command('brightness_set', brightness_level)
            run_cmd(cmd)
            send_notification(f'brightness is now at {brightness_level}%')
    
    elif 'increase' in user_message:
        by = None
        for word in user_message.split():
            try:
                by = int(word)
                break
            except ValueError:
                continue
        print(by)
        cmd = get_command('brightness_up', by)
        run_cmd(cmd)
        send_notification(f'brightness increased by {by}%')

    elif 'decrease' in user_message:
        by = None
        for word in user_message.split():
            try:
                by = int(word)
                break
            except ValueError:
                continue
        print(by)
        cmd = get_command('brightness_down', by)
        run_cmd(cmd)
        send_notification(f'brightness decreased by {by}%')

else:
    logging.warning(f'Unrecognized command: {user_message}')
    send_notification("I din't understand that, please try again")