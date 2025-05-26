from .generalFunctions import *


def brightness_cmd(user_message):
    if 'set' in user_message or 'change' in user_message:
        if 'max' in user_message or 'maximum' in user_message:
            cmd = get_command('brightness_set', 100)
            send_notification(f'brightness is set to maximum')

        elif 'min' in user_message or 'minimum' in user_message or 'menu' in user_message or 'minimal' in user_message:
            cmd = get_command('brightness_set', 5)
            send_notification(f'brightness is set to minimum')
        
        else:
            brightness_level = extract_int(user_message)
            cmd = get_command('brightness_set', brightness_level)
            send_notification(f'brightness is now at {brightness_level}%')
    
    elif 'increase' in user_message:
        by = extract_int(user_message)
        cmd = get_command('brightness_up', by)
        send_notification(f'brightness increased by {by}%')

    elif 'decrease' in user_message:
        by = extract_int(user_message)
        cmd = get_command('brightness_down', by)
        send_notification(f'brightness decreased by {by}%')

    return cmd