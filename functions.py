from pathlib import Path

class Bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    HUEVIY_RED = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Proceed:

    colors = Bcolors()
    def script_handler(script):
        src = Path('/scripts/task'+script+'.py')
        if src.is_file():
            print(Bcolors.GREEN+"Yeah, found it. Running..."+Bcolors.WHITE)
        else:
            print(Bcolors.FAIL+"No file found. L0L."+Bcolors.WHITE)
        print(script)

    def script_mapper(num):
       print (num)