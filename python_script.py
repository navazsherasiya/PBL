import os
import shutil
import datetime
import time

path="d:/pbl"
list_ = os.listdir(path)

for file_ in list_:
    #print(path+'/'+file_)
    created = os.path.getctime(path+'/'+file_)
    #print(os.path.getctime(path+'/'+file_))
    year,month,day,hour,minute,second=time.localtime(created)[:6]
    name, ext = os.path.splitext(file_)

    if ext == '':
        continue
    
    if os.path.exists(path+'/'+str(year)+'/'+str(month)+" month"+'/'+str(day)+'/'+ext):
        shutil.move(path+'/'+file_, path+'/'+str(year)+'/'+str(month)+" month"+'/'+str(day)+'/'+ext+'/'+file_)
    else:
        os.makedirs(path+'/'+str(year)+'/'+str(month)+" month"+'/'+str(day)+'/'+ext)
        shutil.move(path+'/'+file_, path+'/'+str(year)+'/'+str(month)+" month"+'/'+str(day)+'/'+ext+'/'+file_)

    


    



