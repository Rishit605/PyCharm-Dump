import pytube
from pytube import YouTube
link = '''INPUT URL'''
video = pytube.YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download("C:/Users/pc/Desktop/YT Downloaded Videos/")