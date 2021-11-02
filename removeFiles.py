import time
import os
import shutil

path = 'E://WhitehatJr//project-99//testFolder'
days = 30
seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
        ctime = os.stat(path).st_ctime

        if ctime > seconds:
            os.remove(path)
        
        else:
            print("Nothing's old...(like you)")

else:
    print("The path does not exist....")