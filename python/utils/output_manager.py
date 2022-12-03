import os
import sys

_DEVNULL = open(os.devnull, "w")
_ORIG_STDOUT = sys.stdout
_CLEAR_LINE = "\x1b[1A\x1b[2K"
DELIM = 80 * "="

_TRESET = '\033[0m'
_TBOLD = '\033[1m'
_TRED = '\033[31m'


def invalidate_print():
    global _DEVNULL
    sys.stdout = _DEVNULL


def printf(text):
    global _ORIG_STDOUT, _DEVNULL
    sys.stdout = _ORIG_STDOUT
    print(text)
    sys.stdout = _DEVNULL


def clear_line(lines=1):
    printf(lines * _CLEAR_LINE)

BANNER = f"""
  _   _  ____ _____ _____  
 | \ | |/ __ \_   _|  __ \ 
 |  \| | |  | || | | |  | |
 | . ` | |  | || | | |  | |
 | |\  | |__| || |_| |__| |
 |_| \_|\____/_____|_____/ 
                           
NOID (NO IDEA) WPA2 Handshake Nonce Recursion Exploit
evan.systems                        
                                         
                                         
"""
