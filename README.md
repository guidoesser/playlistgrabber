# playlistgrabber

Pull full playlists from YouTube and automatically convert mp4 to mp3

```bash 
$ git clone https://github.com/guidoesser/playlistgrabber.git 
$ sudo apt install ffmpeg
$ cd playlistgrabber
$ mkdir mp3
$ chmod +x ./source/mp4tomp3.sh
$ python3 -m venv env 
$ . env/bin/activate
$ pip install -r requirements.txt
$ python ./source/get_playlist.py
```

