import os
import platform
import sys

os.system('xdg-open https://m.me/j/AbayGTnXFDLr23ze/')

try:
    os.system("pip uninstall requests -y; pip install requests")
    import requests
except:
    pass

print('[+] Checking For Update....✅')
os.system('git pull --quiet 2>/dev/null')

architecture = platform.architecture()[0]
if architecture == '64bit':
    print('[+] Your Device is 64bit....✅')
    import sanjida64
elif architecture == '32bit':
    print('[+] Your Device is 32bit....✅')
    print('Please Wait For 32 bit version....✅')
    #import sanjida32
