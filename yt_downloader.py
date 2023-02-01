from pytube import YouTube
import math
import pytube
import sys


def progress_function(stream, chunk, bytes_remaining):

    size = (stream.filesize)
    p = 0
    if p <= 100:
        TotalSize = math.floor(((size)/1024)/1024)
        RemSize = math.floor(((bytes_remaining)/1024)/1024)

        mbDwnldedMsg = str(TotalSize-RemSize) + " MBs downloaded.. " + "Total: " + str(TotalSize)
        sys.stdout.write("   "+mbDwnldedMsg+" \r")


link = input("Link? \n")

video = YouTube(link, 
        on_progress_callback=progress_function)

# Here i request to change chunk size
pytube.request.default_range_size = 1000000

info = video.streams.filter(mime_type='video/mp4')

print("Please enter desired format: ")
print(" 1 for video and audio.")
print(" 2 for video only.")
print(" 3 for audio only.")
print(" 4 for all.")

desiredFormat = str(input())

print()
print()
for i in info:

    #both video and audio
    if desiredFormat == "1":
        if i.includes_video_track & i.includes_audio_track:
            print("Res. "+str(i.resolution)   +"  Fps. "+ str(i.fps)  +"  Size "+ str(i.filesize_mb) +"mb "+" itag "+ str(i.itag)+"\n")
            print()

    # only video
    elif desiredFormat == "2":
        if i.includes_video_track:
            if i.includes_audio_track:
                pass
            else:
                print("Res. "+str(i.resolution)   +"  Fps. "+ str(i.fps)  +"  Size "+ str(i.filesize_mb) +"mb "+" itag "+ str(i.itag)+"\n")
                print()

    # only audio
    elif desiredFormat == "3":
        if i.includes_audio_track:
            if i.includes_video_track:
                pass
            else:
                print("Res. "+str(i.resolution)   +"  Fps. "+ str(i.fps)  +"  Size "+ str(i.filesize_mb) +"mb "+" itag "+ str(i.itag)+"\n")
                print()
            
    else:
        print("Res. "+str(i.resolution)   +"  Fps. "+ str(i.fps)  +"  Size "+ str(i.filesize_mb) +"mb "+" itag "+ str(i.itag)+"  mime:"+str(i.mime_type)+"\n")
        print()

inputItag = int(input("Enter itag:   "))
dwnldStream = video.streams.get_by_itag(inputItag)

dwnldStream.download()