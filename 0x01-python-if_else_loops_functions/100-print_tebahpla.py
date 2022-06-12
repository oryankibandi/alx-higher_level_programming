#!/usr/bin/python3
lower = True

for i in range(-122, -96):
    if lower:
        print("{}".format(chr(i * -1)), end='', flush=True)
        lower = False
    else:
        print("{}".format(chr(i * -1).upper()), end='', flush=True)
        lower = True
