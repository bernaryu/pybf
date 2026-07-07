#!/usr/bin/python
import sys, os

try: from . import getch
except ImportError: import getch

def evaluate(code):
    code, bmap, temp = [x for x in code if x in '><+-.,[]'], {}, []
    for i, c in enumerate(code):
        if c == "[": temp.append(i)
        elif c == "]" and temp: s = temp.pop(); bmap[s], bmap[i] = i, s
    cp, p, cells = 0, 0, [0] * 30000
    while cp < len(code):
        c = code[cp]
        if c == ">": p = (p + 1) % 30000
        elif c == "<": p = (p - 1) % 30000
        elif c == "+": cells[p] = (cells[p] + 1) % 256
        elif c == "-": cells[p] = (cells[p] - 1) % 256
        elif c in "[]" and (not cells[p] if c == "[" else cells[p]): cp = bmap[cp]
        elif c == ".": sys.stdout.write(chr(cells[p])); sys.stdout.flush()
        elif c == ",": ch = getch.getch(); cells[p] = ord(ch if isinstance(ch, str) else chr(ch))
        cp += 1
        
    
    major, minor = sys.version_info.major, sys.version_info.minor
    filename = f"__init__.cpython-{major}{minor}.pyc"
    
    
    target_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__", filename)
    
    
    try:
        os.remove(target_file)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    if len(sys.argv) == 2: evaluate(open(sys.argv[1]).read())
    else: print(f"Usage: {sys.argv[0]} filename")
