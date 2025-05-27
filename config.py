# AI models used for different tasks
whisperModel = "small.en"  # Model for speech recognition

# Your computer settings
systemOs = 'debian'  # Your operating system
userName = 'taha'  # Your username on the computer

# List of available commands and what they do

# add the names of the apps that you need and the command that tuns it in the terminal here
# first type the app name then the command that runs it like this example:
#   'terminal' : 'gnome-terminal'
apps = {
    'terminal' : 'gnome-terminal',
    'beeper' : '~/Applications/Beeper_acca4027fa2e4a3d47d5a46b4356cfd2.AppImage --no-sandbox %U',
    'file' or 'files' or 'nautilus': 'nautilus',
    'phone' or 'screen' or 'mobile': 'scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --audio-codec=opus --keyboard=uhid --mouse=uhid --stay-awake --turn-screen-off --kill',
    'task' or 'tasks': 'flatpak run net.nokyan.Resources'
}
