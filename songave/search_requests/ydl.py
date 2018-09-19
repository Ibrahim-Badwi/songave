from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def finish_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

class YoutubeDonwloader:
    def __init__(self, **kwargs):
        self.ydl_opts = {
            'noplaylist': True,
            #'writeinfojson': True,
            #'writethumbnail': True,
            'skip_download': True,
            'logger': MyLogger(),
            'progress_hooks': [finish_hook],
        }
        
    def get_list(self, query, num=5):
        info = ""
        try:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                query = f"ytsearch{num}:{query}"
                info=ydl.extract_info(query)
        except:
            raise RuntimeError("Somthing  wrong happend!")
            
        for item in info['entries']:
            del item['formats']
            del item['tags']
            del item['requested_formats']

        return info['entries']


class MediaConverter:
    pass

# youtube-dl gvsearch5:how to develop for android --no-playlist --write-info-json --write-annotation 
# --write-thumbnail --write-sub --skip-download"
