import json
import os.path
from pathlib import Path

json_Path ='D:/Tsai/eye/GazeCapture-master/GAZEDATA/'

a = []

for i in range(0,3523):
    fname = json_Path + str(i).zfill(5) + '/info.json'
    # print(fname)
    if os.path.isfile(fname):
        print(i)
        with open(fname) as f:
            j = json.load(f)
            if 'iPad' in j['DeviceName']:
                a.append(i)
print(a)
with open('D:\Tsai\eye\GazeCapture-master\ipad_list.txt') as o:
    for A in a:
        o.write(str(A))

