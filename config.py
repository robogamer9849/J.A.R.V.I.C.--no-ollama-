# AI models used for different tasks
whisperModel = "base.en"  # Model for speech recognition

# Your computer settings
systemOs = 'debian'  # Your operating system
userName = 'taha'  # Your username on the computer

# List of available commands and what they do

# Dont touch this part

def get_command(action, x):

    commands = {
        f'brightnessctl set {x}%': 'Set display brightness level (range: 5000-19200)',
        'neofetch': 'Display system information and hardware specifications',
        'uname -a': 'Print detailed system and kernel information',
        f'pamixer --allow-boost {x} --set-volume': 'Set audio volume level (integer 0-100)',
        f'pamixer -i {x}' : 'volume up',
        f'pamixer -d {x}' : 'volume down',
        'pamixer -m' : 'mute',
        f'{x}' : 'run app'
    }

    cmd = ''

    return(cmd)