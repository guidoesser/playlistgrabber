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

At the moment you will get the following error message:  
"pytube.exceptions.RegexMatchError: regex pattern (\W[\'"]?t[\'"]?: ?[\'"](.+?)[\'"]) had zero matches"

You have to change pytube in your environment:
```bash
$ nano ./playlistgrabber/env/lib/python3.6/site-packages/pytube/extract.py
```
Change
```python
    if age_restricted:
        sts = regex_search(r'"sts"\s*:\s*(\d+)', embed_html, group=1)
        # Here we use ``OrderedDict`` so that the output is consistent between
        # Python 2.7+.
        params = OrderedDict([
            ('video_id', video_id),
            ('eurl', eurl(video_id)),
            ('sts', sts),
        ])
    else:
        # I'm not entirely sure what ``t`` represents. Looks to represent a
        # boolean.
        t = regex_search(
            r'\W[\'"]?t[\'"]?: ?[\'"](.+?)[\'"]', watch_html,
            group=0,
        )
        params = OrderedDict([
            ('video_id', video_id),
            ('el', '$el'),
            ('ps', 'default'),
            ('eurl', quote(watch_url)),
            ('hl', 'en_US'),
            ('t', quote(t)),
        ])
```
to
```python
    if age_restricted:
        sts = regex_search(r'"sts"\s*:\s*(\d+)', embed_html, group=1)
        # Here we use ``OrderedDict`` so that the output is consistent between
        # Python 2.7+.
        params = OrderedDict([
            ('video_id', video_id),
            ('eurl', eurl(video_id)),
            ('sts', sts),
        ])
    else:
        # I'm not entirely sure what ``t`` represents. Looks to represent a
        # boolean.
        #t = regex_search(
        #    r'\W[\'"]?t[\'"]?: ?[\'"](.+?)[\'"]', watch_html,
        #    group=0,
        #)
        params = OrderedDict([
            ('video_id', video_id),
            ('el', '$el'),
            ('ps', 'default'),
            ('eurl', quote(watch_url)),
            ('hl', 'en_US'),
        #   ('t', quote(t)),
        ])
```
Then try again
```bash
$ python ./source/get_playlist.py
```
