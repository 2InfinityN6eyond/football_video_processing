# usage : python PYTHON_FILE_NAAME URL_TO_VIDEO

import yt_dlp
import os
import sys
import json

def main(url) :
    out_dir = os.path.join('.', url.split('=')[1])


    if os.path.isdir(out_dir) :
        print("directory of ID of video you are trying to download is already exists")
        print("perhaps you already downloaded this video?")
        exit()

    os.mkdir(out_dir)
    
    with yt_dlp.YoutubeDL({}) as ydl :
        meta = ydl.extract_info(url, download=False)
    
    video_file_name = os.path.join(out_dir, )
    video_metadata_file_name = os.path.join(out_dir, "info.json")

    with open(video_metadata_file_name, "w") as fp :
        json.dump(meta, fp, indent=4)


    ydl_opt = {
        "outtmpl" : os.path.join(out_dir, "%(title)s.%(ext)s"),
        "format" : "bestvideo+bestaudio"
    }

    with yt_dlp.YoutubeDL(ydl_opt) as ydl :
        ydl.download([url])


if __name__ == "__main__" :
    main(sys.argv[1])