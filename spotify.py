import os
import time
import sys

RED = "\033[31m"
RESET = "\033[0m"

def enable_ansi_on_windows():
    """Enable ANSI escape sequences on Windows 10+."""
    if os.name == 'nt':
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)

enable_ansi_on_windows()

os.system("cls" if os.name == "nt" else "clear")

ascii_art = r"""                                                                             
88b           d88    ,ad8888ba,      ,ad8888ba,   888888888888  88888888888  
888b         d888   d8"'    `"8b    d8"'    `"8b           ,88  88           
88`8b       d8'88  d8'        `8b  d8'        `8b        ,88"   88           
88 `8b     d8' 88  88          88  88          88      ,88"     88aaaaa      
88  `8b   d8'  88  88          88  88          88    ,88"       88      
88   `8b d8'   88  Y8,        ,8P  Y8,        ,8P  ,88"         88           
88    `888'    88   Y8a.    .a8P    Y8a.    .a8P  88"           88           
88     `8'     88    `"Y8888Y"'      `"Y8888Y"'   888888888888  88888888888                                                                                                                                             
"""

print(ascii_art)


print(f"[{RED}-{RESET}] Key: ", end="", flush=True)
key = input()

sys.stdout.write("\033[F")  # Cursor up
sys.stdout.write("\033[K")  # Clear line
sys.stdout.flush()

print(f"[{RED}-{RESET}] Authenticating...")
time.sleep(2)
print("[+] Access Granted!")


