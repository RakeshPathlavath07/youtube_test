import traceback
import requests
from http.cookiejar import MozillaCookieJar
from youtube_transcript_api import YouTubeTranscriptApi

try:
    session = requests.Session()
    cookie_jar = MozillaCookieJar('cookies.txt')
    cookie_jar.load(ignore_discard=True, ignore_expires=True)
    
    # Clean non-ASCII cookies
    for c in list(cookie_jar):
        try:
            c.name.encode('ascii')
            c.value.encode('ascii')
        except UnicodeEncodeError:
            cookie_jar.clear(c.domain, c.path, c.name)
            
    session.cookies = cookie_jar
    api = YouTubeTranscriptApi(http_client=session)
    api.fetch('dQw4w9WgXcQ', languages=['en'])
    print("Test Fetch Success!")
except Exception as e:
    traceback.print_exc()