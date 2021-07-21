## This code takes the /sensors/core readings as a .txt file and create a .csv file based on the data inside.
## Automatically create a .csv file for every .txt file in the directory

from os import listdir

listoffile = listdir()

for ind in listoffile:
    file_name_split_dot = ind.split(".")
    if(file_name_split_dot[len(file_name_split_dot)-1] == "txt"):
        speed=[]
        current=[]
        sec=[]
        nsec=  []
        dc=[]
        inputc=[]
        currentq=[]
        file=open(ind)
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

        file=open((ind.split(".txt")[0]+".csv"),"w")
        seg = "time;input_current;motor_current;q-axis_current;speed;duty_cycle;\n"
        file.writelines(seg)

        for i in range(len(sec)):
            seg = str(sec[i]-sec[0])+";"+str(inputc[i])+";"+str(current[i])+";"+str(currentq[i])+";"+str(speed[i])+";"+str(dc[i])+"\n"
            file.writelines(seg)
            
        file.close()


