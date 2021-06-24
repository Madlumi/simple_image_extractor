import os
from pathlib import Path
import re
from shutil import copyfile

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)



iFol=r'input folder'
oFol=r'output folder'
pre='file'

if not os.path.exists(oFol):
    os.makedirs(oFol)


iii = [x[0] for x in os.walk(iFol)]
sort_nicely(iii)

i = 0
for f in iii:
    #print(f)
    for file in os.listdir(f):
        if file.endswith(".png"):
            fn= (pre+"_"+(f'{i:05d}')+".png")
            print(os.path.join(f, file)+"  "+os.path.join(oFol, fn))
            copyfile(os.path.join(f, file),os.path.join(oFol, fn))
        
            i=i+1
        if file.endswith(".jpg"):
            fn= (pre+"_"+(f'{i:05d}')+".jpg")
            print(os.path.join(f, file)+"  "+os.path.join(oFol, fn))
            copyfile(os.path.join(f, file),os.path.join(oFol, fn))
        
            i=i+1
