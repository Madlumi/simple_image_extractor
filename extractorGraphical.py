import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import extracter

def getDir(field):
    t= filedialog.askdirectory()
    field.delete(0,tk.END)
    field.insert(0,t)

def mk_folders_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(0, weight=6)
    frame.columnconfigure(0, weight=1)
    
    #Input folder
    ttk.Label(frame, text='Input folder: ').grid(column=0, row=0, sticky=tk.W)
    iFol_entry = ttk.Entry(frame,name="ifol", width=40)
    iFol_entry.focus()
    iFol_entry.grid(column=1, row=0, sticky=tk.W)
    iFol_button = tk.Button(frame,text="[f]",command = lambda: getDir(iFol_entry))
    iFol_button.grid(column=2, row=0, sticky=tk.W)
    iFol_entry.insert(0,  r'C:\Users\user\pictures\input')
    #Output folder
    ttk.Label(frame, text='Output folder:').grid(column=0, row=1, sticky=tk.W)
    oFol_entry = ttk.Entry(frame,name="ofol", width=40)
    oFol_entry.grid(column=1, row=1, sticky=tk.W)
    oFol_button = tk.Button(frame,text="[f]",command = lambda: getDir(oFol_entry))
    oFol_button.grid(column=2, row=1, sticky=tk.W)
    oFol_entry.insert(0, r'C:\Users\user\pictures\output')
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def mk_options_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    #Fps
    ttk.Label(frame, text='Prefix:                     ').grid(column=0, row=0, sticky=tk.W)
   
    prefix = ttk.Entry(frame,name="prefix", width=22)    
    prefix.focus()
    prefix.grid(column=1, row=0, sticky=tk.W,padx=10)
    prefix.insert(0, 'file')
    #repeats
    ttk.Label(frame, text='repeats: ').grid(column=3, row=0, sticky=tk.W)
    repeats = ttk.Entry(frame,name="repeats", width=5)
    repeats.focus()
    repeats.insert(0, '1')
    repeats.grid(column=4, row=0, sticky=tk.W)
    

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def mk_vid_check(container,vframe):
    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)

    ttk.Label(frame, text='').grid(column=0, row=0, sticky=tk.W)

    expVid = tk.IntVar(name="expv")
    expVid_check = ttk.Checkbutton(
        frame,
        variable=expVid,
        text='Export_Video',
        command=lambda: vidCheck(expVid,vframe)
        #lambda: print(expVid.get())
    )
    expVid_check.grid(column=1, row=0, sticky=tk.W)

    
    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=8)

    return frame


def mk_Vfolders_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(0, weight=6)
    frame.columnconfigure(0, weight=1)
    
    #Input folder
    ttk.Label(frame, text='Output folder: ').grid(column=0, row=0, sticky=tk.W)
    vFol_entry = ttk.Entry(frame,name="vfol", width=40)
    vFol_entry.insert(0, r'C:\Users\user\Videos')
    vFol_entry.grid(column=1, row=0, sticky=tk.W)
    vFol_button = tk.Button(frame,text="[f]",command = lambda: getDir(vFol_entry))
    vFol_button.grid(column=2, row=0, sticky=tk.W)
    

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame

def mk_VName_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(0, weight=6)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

   
    #name
    ttk.Label(frame, text='Video name:  ').grid(column=0,padx=5, pady=5 ,row=0, sticky=tk.W)
    vName_entry = ttk.Entry(frame,name="vname", width=27)
    vName_entry.insert(0, 'VideoName')
    vName_entry.grid(column=1, row=0, sticky=tk.E)

    ttk.Label(frame, text=' . ').grid(column=2, row=0, padx=0,sticky=tk.E)
    vExt_entry = ttk.Entry(frame,name="vext", width=10)
    vExt_entry.insert(0, 'avi')
    vExt_entry.grid(column=3, row=0, sticky=tk.W)

    ttk.Label(frame, text='     ').grid(column=4, padx=10, pady=5 ,row=0, sticky=tk.E)
    #for widget in frame.winfo_children():
    #    widget.grid(padx=5, pady=5)

    return frame
def mk_Voptions_frame(container):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(0, weight=0)
    #Fps
    ttk.Label(frame, text='Fps:                         ').grid(column=0, row=0, sticky=tk.W)
    fps = ttk.Entry(frame,name="fps", width=10)
    fps.insert(0, '24')
    fps.grid(column=1, row=0, sticky=tk.W,padx=10)

    #repeats
    ttk.Label(frame, text='Bitrate:  ').grid(column=3, row=0, sticky=tk.W)
    Bitrate = ttk.Entry(frame,name="bitrate", width=18)

    Bitrate.insert(0, '10000')
    Bitrate.grid(column=4, row=0, sticky=tk.W)
    ttk.Label(frame, text='k').grid(column=5, row=0, sticky=tk.W)

    delImg = tk.IntVar()
    delImg_check = ttk.Checkbutton(
        frame,
        variable=delImg,
        text='Delete extracted images',
        command=lambda: delImgUpd(delImg.get())
    )
    delImg_check.grid(column=0,columnspan = 2, row=2, sticky=tk.W)
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame
def delImgUpd(i):
    global delimg
    delimg = i

def mk_bot(container,root):

    frame = ttk.Frame(container)
    frame.columnconfigure(0, weight=4)
    frame.columnconfigure(0, weight=0)
    frame.rowconfigure(0, weight=5)
    frame.rowconfigure(1, weight=0)
    frame.rowconfigure(2, weight=0)
    ttk.Label(frame, text='   ').grid(column=0, row=0, sticky=tk.W)
    ttk.Label(frame, text='   ').grid(column=0, row=1, sticky=tk.W)

    ttk.Label(frame,name="ptext", text='...').grid(column=0, row=2, sticky=tk.W)
    
    bar = ttk.Progressbar(frame,name="pbar", orient = "horizontal", length = 330 , mode = 'determinate').grid(column=0, row=3, sticky=tk.W)
    vFol_button = tk.Button(frame,text="   start   ",name="",command = lambda: start(root))
    vFol_button.grid(column=1, row=3, sticky=tk.W)
    #vFol_button.configure(state='disable')
    
    for widget in frame.winfo_children():
        widget.grid(padx=4, pady=0)

    return frame
def vidCheck(v,f):
    
    i = v.get()

    global export
    export = i
    
    for c in f.winfo_children():
        for ch in c.winfo_children():
            try:
                if(i=='0'):
                    ch.configure(state='disable')
                else:
                    ch.configure(state='normal')
            except:
                print("uwu")

def getNode(name,root):
     for c in root.winfo_children():
        if(name in c.winfo_name()):
            return c
        for c1 in c.winfo_children():
            if(name in c1.winfo_name()):
                return c1
            for c2 in c1.winfo_children():
                if(name in c2.winfo_name()):
                    return c2
def start(f):
    #winfo_parent
    #f.frame.vFol_button.configure(state='disable')
    iFol = getNode('ifol',f).get()
    oFol = getNode('ofol',f).get()
    pre = getNode('prefix',f).get()
    repeats = getNode('repeats',f).get()
    
    fps = getNode('fps',f).get()
    oVid = getNode('vname',f).get()+"."+getNode('vext',f).get()
    oVidFol = getNode('vfol',f).get()
    bitrate = getNode('bitrate',f).get()
    
    print(iFol)
    print(oFol)
    print(pre)
    print(repeats)
    print(fps)
    print(oVid)
    print(oVidFol)
    print(bitrate)
    
    print(export)
    print(delimg)

    extracter.runExtractor(iFol,oFol,pre,repeats,export,fps,oVid,oVidFol,bitrate,delimg)

def tree():
    for c in f.winfo_children():
        try:
            if('!' not in c.winfo_name()):
                print("   "+str(c.winfo_name()))
            for ch in c.winfo_children():
                try:
                    if('!' not in str(ch.winfo_name())):
                        print("      "+str(ch.winfo_name()))
                    for chi in ch.winfo_children():
                        try:
                            if('!' not in str(chi.winfo_name())):
                                print("         "+str(chi.winfo_name()))
                        except:
                            print("uwu")
                except:
                    print("uwu1")
        except:
                print("uwu2")

                
     
    
    
    #extracter.runExtractor(iFol,oFol,pre,repeats,export,fps,oVid,oVidFol,bitrate,deleteImg):



def Main():

    # root window
    root = tk.Tk()
    root.title('Extractor')
    root.geometry('400x351')
    root.resizable(0, 0)
    
    root.attributes('-toolwindow', True)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    #root.columnconfigure(1, weight=4)

    folders_frame = mk_folders_frame(root)
    folders_frame.grid(column=0, row=0,sticky="nsew")

    option_frame = mk_options_frame(root)
    option_frame.grid(column=0, row=1,sticky="nsew")
    
    ttk.Label(text='____________________________________________________________________').grid(column=0, row=2,sticky="e")

    vframe = tk.Frame(root,bg='blue')
    vframe.columnconfigure(0, weight=4)
        
    vid_check = mk_vid_check(root,vframe)
    vid_check.grid(column=0, row=2,sticky="w")
    
    
    vframe.grid(column=0, row=3,sticky="nsew")

    
    Vfolders_frame = mk_Vfolders_frame(vframe)
    Vfolders_frame.grid(column=0, row=0,sticky="nsew")

    VName_frame = mk_VName_frame(vframe)
    VName_frame.grid(column=0, row=1,sticky="nsew")
    
    Voption_frame = mk_Voptions_frame(vframe)
    Voption_frame.grid(column=0, row=2,sticky="nsew")

    Voption_frame = mk_Voptions_frame(vframe)
    Voption_frame.grid(column=0, row=2,sticky="nsew")
    #--------------------------
    botframe = tk.Frame(root,bg='blue')
    botframe.columnconfigure(0, weight=4)
    botframe.grid(column=0, row=4,sticky="nsew")

    bot = mk_bot(botframe,root)
    bot.grid(column=0, row=0,sticky="nsew")
    
    for c in vframe.winfo_children():
        for child in c.winfo_children():
            try:
                child.configure(state='disable')
            except:
                print("uwu")
    
    root.mainloop()

frame=0
iFol=""
oFol=""
pre=""
repeats=1

fps=24
oVid="vidname"
oVidFol=""
bitrate=1000
global delimg
delimg = 0
global export
export = 0

if __name__ == "__main__":
    Main()
