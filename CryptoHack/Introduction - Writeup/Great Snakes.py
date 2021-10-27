import sys

if sys.version_info.major == 2:
    #if you are using python2, please update to python3 first.

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("flag:")
print("".join(chr(o ^ 0x32) for o in ords))
