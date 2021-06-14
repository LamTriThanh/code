from colorama import init
from colorama import Fore
init(autoreset=True)
print(Fore.BLUE + 'some red text')
print('automatically back to default color again')