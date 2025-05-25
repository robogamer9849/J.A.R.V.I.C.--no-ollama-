import subprocess
from pathlib import Path

subprocess.Popen(f'/bin/python {Path(__file__).parent.resolve()}/talkToMe.py', shell = True)