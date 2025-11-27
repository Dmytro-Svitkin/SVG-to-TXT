import os,sys
import tkinter as tk
from tkinter import filedialog

def Path(resource):
    if hasattr(sys,"_MEIPASS"):return os.path.join(sys._MEIPASS,resource)
    return os.path.join(os.path.abspath("."),resource)

def ChopExtra(text):
    start=text.find("<svg")if"<svg"in text else 0;end=text.find("</svg>")if"</svg>"in text else len(text)-1
    return text[start:end+6]

def OneLine(text):
    text=text.replace("\t"," ").replace("\n"," ")
    recol=len(text);text=text.replace("  "," ")
    while recol!=len(text):
        recol=len(text);text=text.replace("  "," ")
    return ChopExtra(text).strip().replace("\" ","\"").replace("> ",">").replace(", ",",").replace(" (","(")

def Duplicate(name):
    global output
    base=os.path.splitext(os.path.basename(name))[0]
    suffix="";counter=1
    while os.path.exists(os.path.join(output,base+suffix+".txt")):
        suffix="("+str(counter)+")";counter+=1
    return suffix    

window=tk.Tk();window.withdraw();window.iconbitmap(Path("../assets/SVG-to-TXT.ico"))
svgs=filedialog.askopenfilenames(title="SVG-to-TXT → Select SVG file(s)",filetypes=[("svg files","*.svg")])
if svgs:
    output=filedialog.askdirectory(parent=window,title="SVG-to-TXT → Select output folder")
    if not output:output=os.path.dirname(svgs[-1])
    for svg in svgs:
        with open(svg,"r",encoding="utf-8")as inputFile:inputContent=inputFile.read()
        outputContent=OneLine(inputContent)
        with open(os.path.join(output,os.path.splitext(os.path.basename(svg))[0]+Duplicate(svg)+".txt"),"w",encoding="utf-8")as outputFile:outputFile.write(outputContent)
window.quit();window.destroy()
