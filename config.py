# AI models used for different tasks
whisperModel = "small.en"  # Model for speech recognition

# Your computer settings
systemOs = 'debian'  # Your operating system


# add the names of the apps that you need and the command that tuns it in the terminal here
# first type the app name then the command that runs it like this example:
#   'terminal' : 'gnome-terminal'
apps = {
    'terminal' : 'gnome-terminal',
    'beeper' : '~/Applications/Beeper_acca4027fa2e4a3d47d5a46b4356cfd2.AppImage --no-sandbox %U',
    'file' or 'files' or 'nautilus': 'nautilus',
    'phone' or 'screen' or 'mobile': 'scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --audio-codec=opus --keyboard=uhid --mouse=uhid --stay-awake --turn-screen-off --kill',
    'task' or 'tasks': 'flatpak run net.nokyan.Resources',
    'browser' or 'zen': '~/Apps/zen/zen %u',
    'code' or 'vscode': 'code',
    'settings' or 'control': 'gnome-control-center',
    'calculator' or 'calc': 'gnome-calculator',
    'calendar': 'gnome-calendar',
}

# the command that is used to take screenshots, its gnome-screenshot by default for gnome
screenshot_cmd = 'gnome-screenshot'
# the command for opening the screenshots folder in the file explorer, this is the default for gnome : nautilus -w Pictures
screenshot_open_path = 'nautilus -w Pictures'

# search command for your browser, put {term} for the search term
def search_cmd(term):
    search = f'{apps["browser"]} --search {term}'
    return search