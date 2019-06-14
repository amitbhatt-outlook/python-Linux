import os

pcount=0;pcount1=0;pcount2=0;
pname="";
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
for pid in pids:
     f = open("/proc/"+pid+"/status", "r")
     datafile = f.readlines()
     for line in datafile:
        if 'Name' in line:
          pname = line.split(":")[1].strip()
        if 'VmSize' in line:
            vmsize = line.split(":")[1].strip()
            sizeinkb = vmsize.split(" ")[0]
            sizeingb = ((int(sizeinkb)/1024)/1024)
            if sizeingb <= 10:
             pcount=0
            elif sizeingb > 10 and sizeingb <= 15:
             pcount1=pcount1+1
             print("Process with memory more that 10 GB is: "+ pname +" with pid: "+pid)
            elif sizeingb > 15:
             pcount2=pcount2+1
             print("Process with memory more that 15 GB is: "+ pname +" with pid: "+pid)
            else:
             print("error")

if pcount2 != 0:
   exit(2)
else:
   if pcount1 != 0:
      exit(1)
   else:
      exit(0)
