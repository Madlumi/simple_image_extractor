import os
from pathlib import Path
import re
import shutil
from shutil import copyfile
import subprocess

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

#ffmpeg output function
def output(fps,pre,oFol,oName,bitrate):
    ffmpeg_path= 'ffmpeg'
    cmd = ffmpeg_path+' -y -framerate '+str(fps)+' -i '+oFol+'\\' +pre+r'_%05d.png' + ' -b '+str(bitrate)+' '+oName
    print(cmd)
    return subprocess.check_output(cmd, shell=True)



#file paths--------------------------------------------------------
iFol=r'C:\Users\user\Pictures\inputimagefolder'
oFol=r'C:\Users\user\Pictures\outputimagefolder'
pre='file'

repeats = 1

#export options, requres ffmpeg-----------------------------------
export=True
fps=12
oVid="videoname.avi"
oVidFol=r'C:\Users\user\videos'
bitrate='51200k'

#delete images after done if exporting(note this will require oFol and oVidFol to be different)
deleteImg=True

#Extract-----------------------------------------------------------
if not os.path.exists(oFol):
    os.makedirs(oFol)
#get file list
iii = [x[0] for x in os.walk(iFol)]
sort_nicely(iii)
#export loop
i = 0
for iiii in range(0,repeats):
    for f in iii:
        #copy files, only supports png, jpg
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
#Export Video----------------------------------------------------
#delete images after done if exporting(note this will require oFol and oVidFol to be different)
deleteImg=True

#Extract-----------------------------------------------------------
if not os.path.exists(oFol):
    os.makedirs(oFol)
#get file list
iii = [x[0] for x in os.walk(iFol)]
sort_nicely(iii)
#export loop
i = 0
for iiii in range(0,repeats):
    for f in iii:
        #copy files, only supports png, jpg
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
#Export Video----------------------------------------------------
if(export==True):
    if not os.path.exists(oVidFol):
        os.makedirs(oVidFol)
    o = output(fps,pre,oFol,oVidFol+'\\'+oVid,bitrate)
    if(o==b''):
        print("successful export!")
    else:
        print(o)
    #delete images after done
    if(deleteImg):
        try:
            shutil.rmtree(oFol)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        



