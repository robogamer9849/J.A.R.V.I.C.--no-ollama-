# AI models used for different tasks
whisperModel = "base.en"  # Model for speech recognition

# Your computer settings
systemOs = 'debian'  # Your operating system
userName = 'taha'  # Your username on the computer

# List of available commands and what they do

# Dont touch this part

def get_command(action, x):

    commands = {
        'Set display brightness level (range: 5000-19200)': f'brightnessctl set {x}%',
        'Display system information and hardware specifications': 'neofetch',
        'Print detailed system and kernel information': 'uname -a',
        'volume_set': f'pamixer --set-volume {x} --allow-boost',
        'volume_up': f'pamixer -i {x} --allow-boost',
        'volume_down': f'pamixer -d {x} --allow-boost',
        'volume_mute': 'pamixer -m',
        'volume_unmute': 'pamixer -u --allow-boost',
        'run app': f'{x}'
    }

    cmd = commands[action]

    return(cmd)