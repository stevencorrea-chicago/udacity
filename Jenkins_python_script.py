import sys
import os
import shutil

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
    
try: 
    os.mkdir("/home/steve/Python/DeleteMe") 
except OSError as error: 
    print(error)  

shutil.chown("/home/steve/Python/DeleteMe", 1000, 1000)
