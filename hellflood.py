import os
import sys
from core.utils import clear, loading
from core.ui import menu
from core.methods import start_attack

clear()
loading()
menu()

try:
    while True:
        option = input("╭─[ HellFlood ]\n╰─> ")
        if option == "1":
            start_attack("http")
        elif option == "2":
            start_attack("udp")
        elif option == "3":
            start_attack("syn")
        elif option == "0":
            sys.exit()
        else:
            print("Unknown option!")
except KeyboardInterrupt:
    print("\nExiting...")
