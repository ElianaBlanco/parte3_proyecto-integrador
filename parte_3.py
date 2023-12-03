
import os
import msvcrt
import time

def clear_terminal():
    os.system('cls')

def main():
    number = 0

    while number <= 50:
        clear_terminal()
        print(f"Número actual: {number}")
        time.sleep(0.1)
        number += 1

        # Esperar a que se presione la tecla 'n' para continuar
        while not msvcrt.kbhit():
            pass
        key = msvcrt.getch().decode('utf-8')
        if key == 'n':
            continue

if __name__ == "__main__":
    main()
