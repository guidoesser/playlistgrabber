import os
import subprocess
from pytube import Playlist

pl = Playlist("https://www.youtube.com/playlist?list=PLafb_w9QSxG_yJmJN368cPc6aURTBx6N6")

# download to a specific directory
path = os.path.dirname(os.path.abspath(__file__))
print(path)
pl.download_all()
print(path+'/mp4tomp3.sh')
subprocess.call(path+'/mp4tomp3.sh')
#print(os.path.dirname(os.path.abspath(__file__)))
#os.chdir(os.pardir)
subprocess.call('rm *.mp4', shell=True) # with shell = True you pass string, not list
# chmod +x ./mp4tomp3.sh

