from generalFunctions import *

def voice_cmd(user_message):
    if 'set' in user_message or 'change' in user_message:
        if 'max' in user_message or 'maximum' in user_message:
            cmd = get_command('volume_set', 100)
            send_notification(f'volume is set to maximum')

        elif 'min' in user_message or 'minimum' in user_message or 'menu' in user_message or 'minimal' in user_message:
            cmd = get_command('volume_set', 0)
            send_notification(f'volume is set to minimum')
        
        else:
            volume_level = extract_int(user_message)
            cmd = get_command('volume_set', volume_level)
            send_notification(f'volume is now {volume_level}')
        
    elif 'increase' in user_message:
        by = extract_int(user_message)
        cmd = get_command('volume_up', by)
        send_notification(f'volume increased by {by}')

    elif 'decrease' in user_message:
        by = extract_int(user_message)
        cmd = get_command('volume_down', by)
        send_notification(f'volume decreased by {by}')

    elif 'on mute' in user_message or 'unmute' in user_message or "on me it's" in user_message:
        cmd = get_command('volume_unmute', None)
        send_notification('your system is now unmuted')

    elif 'mute' in user_message or 'silent' in user_message:
        cmd = get_command('volume_mute', None)
        send_notification('your system is now muted')

    return cmd