from pytube import Playlist
playlist = Playlist("https://www.youtube.com/playlist?list=PLLC9OIbXopRINGfjkdll7eDaiyJw4Ddm7")
for video in playlist:
video.streams.get_highest_resolution().download()
