import sys, os, stat
import shutil

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
    
try: 
    os.mkdir("/home/steve/Python/DeleteMe") 
except OSError as error: 
    print(error)  

os.chmod("/home/steve/Python/DeleteMe", stat.S_IWRITE)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IREAD)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IEXEC)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IWGRP)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IRGRP)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IXGRP)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IROTH)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IWOTH)
os.chmod("/home/steve/Python/DeleteMe", stat.S_IXOTH)

shutil.chown("/home/steve/Python/DeleteMe", 1000, 1000)
