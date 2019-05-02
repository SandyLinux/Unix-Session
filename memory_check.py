from __future__ import print_function
import psutil

import os
print(psutil.cpu_percent())
print(psutil.virtual_memory())  # physical memory usage

print('memory % used:', psutil.virtual_memory()[2])

pid = os.getpid()
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think

CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

#print results
print("CPU Usage = " + CPU_Pct)
print('memory use:', memoryUse)

mem = str(os.popen('free -t  -m ').readlines())

T_ind = mem.index('T')
print('Tind',T_ind)
mem_G = mem[T_ind+14:-4]
"""

S1_ind=mem_G.index(' ')
print('s1 ind',S1_ind)
mem_T=mem_G[0:S1_ind]
mem_G1=mem_G[S1_ind+8:]

S2_ind=mem_G1.index(' ')
print('s2 ind',S2_ind)
mem_U=mem_G1[0:S2_ind]

mem_F=mem_G1[S2_ind+8:]
print ('Summary = ' + mem_G)
print ('Total Memory = ' + mem_T +' MB')
print ('Used Memory = ' + mem_U +' MB')
"""
print ('Free Memory = ' + mem_G +' MB')
mems = (str.split(mem_G.strip(' ')))
print('------------')
print ('Summary = ' + mems[0] + 'MB')
print ('Free Memory = ' + mems[2] +' MB')
print ('Used Memory = ' + mems[1] +' MB')
