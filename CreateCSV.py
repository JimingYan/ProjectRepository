## This code takes the /sensors/core readings as a .txt file and create a .csv file based on the data inside. 

from tkinter import *
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename()

speed=[]
current=[]
sec=[]
nsec=  []
dc=[]
inputc=[]
currentq=[]
file=open(filename)
file=file.readlines()
for i in file:
    i_sep=i.split(":")
    if(i_sep[0] =="  speed"):
        speed.append(float(i_sep[1]))
    if(i_sep[0]=="  current_motor"):
        current.append(float(i_sep[1]))
    if(i_sep[0]=="  duty_cycle"):
        dc.append(100*float(i_sep[1]))
    if(i_sep[0]=="    nsecs"):
        nsec.append(float(i_sep[1]))
    if(i_sep[0]=="    secs"):
        sec.append(float(i_sep[1]))
    if(i_sep[0]=="  current_input"):
        inputc.append(float(i_sep[1]))
    if(i_sep[0]=="  current_q"):
        currentq.append(float(i_sep[1]))
        
for i in range(len(speed)):
    sec[i] = sec[i]+nsec[i]/(10**9)

file=open((filename.split(".txt")[0]+".csv"),"a+")
seg = "time;input_current;motor_current;q-axis_current;speed;duty_cycle;\n"
file.writelines(seg)

for i in range(len(sec)):
    seg = str(sec[i]-sec[0])+";"+str(inputc[i])+";"+str(current[i])+";"+str(currentq[i])+";"+str(speed[i])+";"+str(dc[i])+"\n"
    file.writelines(seg)
    
file.close()


