import sys
import os

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
    
try: 
    os.mkdir("/home/steve/Python/DeleteMe") 
except OSError as error: 
    print(error)  
