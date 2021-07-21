## This code takes the captured VescStateStamped message from /sensors/core as a .txt file and offer options to graph them either in one or two plots

import tkinter 
from tkinter import *
from tkinter.filedialog import askopenfilename


class param:
    def __init__(self, List, Name, Unit):
        self.List = List
        self.Name = Name
        self.ListMax = max(self.List)
        self.ListMin = min(self.List)
        self.Unit = Unit

    def addselftoplotlist(self):
        selectedList.append(self)
        selectroot.destroy()
        plot_one()

root=tkinter.Tk()
canvas=tkinter.Canvas(root, height=725,width=1100)
canvas.pack()


def plot_one():
    global canvas    
    canvas.delete("all")
    canvas.create_text(550,25,anchor = "n", text = filename.split("/")[len(filename.split("/"))-1])
    if (plotflag == 0):
        if (len(selectedList) == 2):
            pass
        else:
            button = tkinter.Button(canvas, text = "Add", command = add)
            button_window = canvas.create_window(450,695,height=30,width = 100, anchor = "n", window = button)
        button = tkinter.Button(canvas, text = "Subplot", command = changeplotflag)
        button_window = canvas.create_window(650,695,height=30,width = 100, anchor = "n", window = button)
        for i in range(21):
            canvas.create_line(50,50+30*i,1050,50+30*i)
            canvas.create_line(50+50*i,50,50+50*i,650)
            canvas.create_text(50+50*i,675,text=str(round((end-start)/20*i,3)))
        side = [25,1075]
        legendline = [25,925]
        textpos = [110,1010]
        color = ["red","blue"]
        counter = 0
        for j in selectedList:
            for i in range(len(j.List)-1):
                canvas.create_line((sec[i]-start)/(end-start)*1000+50, 50+(j.ListMax-j.List[i])*600/(j.ListMax-j.ListMin),(sec[i+1]-start)/(end-start)*1000+50, 50+(j.ListMax-j.List[i+1])*600/(j.ListMax-j.ListMin), width=2, fill=color[counter])
            for i in range(21):
                canvas.create_text(side[counter],50+30*i, text=str(round((j.ListMax-j.ListMin)/20*(20-i)+j.ListMin,3)))
            canvas.create_line(legendline[counter],25,legendline[counter]+75,25,width=2,fill=color[counter])
            canvas.create_text(textpos[counter],25,anchor="w",text=j.Name+" "+j.Unit)
            counter+=1
            
    if (plotflag == 1):
        if (len(selectedList) == 4):
            pass
        else:
            button = tkinter.Button(canvas, text = "Add", command = add)
            button_window = canvas.create_window(450,695,height=30,width = 100, anchor = "n", window = button)
        if(len(selectedList) >2):
            pass
        else:
            button = tkinter.Button(canvas, text = "Single Plot", command = changeplotflag)
            button_window = canvas.create_window(650,695,height=30,width = 100, anchor = "n", window = button)
        for i in range(21):
            canvas.create_line(50+50*i,50,50+50*i,300)
            canvas.create_line(50+50*i,400,50+50*i,650)
            canvas.create_text(50+50*i,675,text=str(round((end-start)/20*i,3)))
        for i in range(11):
            canvas.create_line(50,50+25*i,1050,50+25*i)
            canvas.create_line(50,400+25*i,1050,400+25*i)
        side = [25,1075]
        legendline = [25,925]
        textpos = [110,1010]
        color = ["red","blue","green","orange"]
        counter = 0
        for j in selectedList:
            if(counter<2):
                for i in range(len(j.List)-1):
                    canvas.create_line((sec[i]-start)/(end-start)*1000+50, 50+(j.ListMax-j.List[i])*250/(j.ListMax-j.ListMin),(sec[i+1]-start)/(end-start)*1000+50, 50+(j.ListMax-j.List[i+1])*250/(j.ListMax-j.ListMin), width=2, fill=color[counter])
                for i in range(11):
                    canvas.create_text(side[counter],50+25*i, text=str(round((j.ListMax-j.ListMin)/10*(10-i)+j.ListMin,3)))
                canvas.create_line(legendline[counter],25,legendline[counter]+75,25,width=2,fill=color[counter])
                canvas.create_text(textpos[counter],25,anchor="w",text=j.Name+" "+j.Unit)
            if(counter>=2):
                for i in range(len(j.List)-1):
                    canvas.create_line((sec[i]-start)/(end-start)*1000+50, 400+(j.ListMax-j.List[i])*250/(j.ListMax-j.ListMin),(sec[i+1]-start)/(end-start)*1000+50, 400+(j.ListMax-j.List[i+1])*250/(j.ListMax-j.ListMin), width=2, fill=color[counter])
                for i in range(11):
                    canvas.create_text(side[counter-2],400+25*i, text=str(round((j.ListMax-j.ListMin)/10*(10-i)+j.ListMin,3)))
                canvas.create_line(legendline[counter-2],375,legendline[counter-2]+75,375,width=2,fill=color[counter])
                canvas.create_text(textpos[counter-2],375,anchor="w",text=j.Name+" "+j.Unit)
            counter+=1
    button = tkinter.Button(canvas, text = "Re-select", command = reselect)
    button_window = canvas.create_window(850,695,height=30,width = 100, anchor = "n", window = button)
            
    
def changeplotflag():
    global plotflag
    global canvas
    canvas.delete("all")
    plotflag ^=1
    plot_one()
    
def add():
    global selectedList
    global selectroot
    selectroot = tkinter.Tk()
    selectcanvas = tkinter.Canvas(selectroot, height = 150, width = 125)
    selectcanvas.pack()
    buttonlist = []
    for i in range(len(paramlist)):
        newButton = tkinter.Button(selectroot , text = paramlist[i].Name, command = paramlist[i].addselftoplotlist)
        buttonlist.append(newButton)
        buttonlist[i].pack()
        newButtonWindow = selectcanvas.create_window(125/2,i*30,height=30,width=125,anchor = "n" , window = buttonlist[i])
        

def start():
    global filename
    Tk().withdraw() 
    filename = askopenfilename()
    selectedfileread()

def reselect():
    global filename
    canvas.delete("all")
    Tk().withdraw() 
    filename = askopenfilename()
    selectedfileread()
    
def selectedfileread():
    global selectedList
    global end
    global start
    global plotflag
    global canvas
    global paramlist
    global sec
    plotflag = 0
    selectedList=[]
    speed=[]
    current=[]
    nsec=[]
    sec=[]
    dc=[]
    inputc=[]
    currentq=[]
    file=open(filename)
    file=file.readlines()
    for i in file:
        a = i.strip(" ")
        i_sep=a.split(":")
        if(i_sep[0] =="speed"):
            speed.append(float(i_sep[1]))
        if(i_sep[0]=="current_motor"):
            current.append(float(i_sep[1]))
        if(i_sep[0]=="duty_cycle"):
            dc.append(100*float(i_sep[1]))
        if(i_sep[0]=="nsecs"):
            nsec.append(float(i_sep[1]))
        if(i_sep[0]=="secs"):
            sec.append(float(i_sep[1]))
        if(i_sep[0]=="current_input"):
            inputc.append(float(i_sep[1]))
        if(i_sep[0]=="current_q"):
            currentq.append(float(i_sep[1]))


    for i in range(len(speed)):
        sec[i] = sec[i]+nsec[i]/(10**9)

    start = sec[0]
    end = sec[len(sec)-1]
    xscale=600/(end-start)

    paramlist = [param(speed,"speed","(ERPM)"), param(current, "motor current", "(A)"), param(dc, "duty cycle","(%)"), param(inputc, "input current", "(A)"), param(currentq , "q-axis current", "(A)")]
    plot_one()

start()
mainloop()
