import colorama
from colorama import Fore

colorama.init(autoreset=True)

def Listen() -> str:
    print()
    print(Fore.MAGENTA + "ENTER YOUR COMMAND: ")
    # print()
    
    # Take text input from the user
    text = input(Fore.GREEN + ">>> ")
    # print()
    print(Fore.YELLOW + "YOU ENTERED: " + text)
    print()
    return text

# if __name__=="__main__":
#     while True:
#         command = Listen()
        # Your code logic using the command goes here
