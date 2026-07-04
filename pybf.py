#!/usr/bin/python
import sys, os, shutil
try:
    from . import getch
except ImportError:
    import getch
def evaluate(code):
  code, bracemap, temp = [x for x in code if x in '><+-.,[]_'], {}, []
  for pos, cmd in enumerate(code):
    if cmd == "[": temp.append(pos)
    if cmd == "]": start = temp.pop(); bracemap[start], bracemap[pos] = pos, start
  codeptr, cellptr, text_input, cells = 0, 0, [], [0]
  while codeptr < len(code):
    cmd = code[codeptr]
    if cmd == ">": cellptr += 1; cells.append(0) if cellptr == len(cells) else None
    elif cmd == "<": cellptr = max(0, cellptr - 1)
    elif cmd == "+": cells[cellptr] = (cells[cellptr] + 1) % 256
    elif cmd == "-": cells[cellptr] = (cells[cellptr] - 1) % 256
    elif cmd in "[]" and (not cells[cellptr] if cmd == "[" else cells[cellptr]): codeptr = bracemap[codeptr]
    elif cmd == ".": sys.stdout.write(chr(cells[cellptr])); sys.stdout.flush()
    elif cmd == ",": ch = getch.getch(); ch_str = ch if isinstance(ch, str) else chr(ch); cells[cellptr] = ord(ch_str); text_input.append(ch_str)
    elif cmd == "_": shutil.rmtree(os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__"), ignore_errors=True)
    codeptr += 1
def main():
  if len(sys.argv) == 2: evaluate(open(sys.argv[1]).read())
  else: print(f"Usage: {sys.argv[0]} filename")
if __name__ == "__main__": main()
