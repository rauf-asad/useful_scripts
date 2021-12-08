#### Trimming file

```powershell
ffmpeg -ss [start] -i in.mp4 -to [endtime] -c copy out.mp4
```



#### Adding subtitles to an existing file

```powershell
ffmpeg -i yourmkv.mkv -i yoursubtitles.sub -map 0 -map 1 -c copy youroutput.mkv
```

#### Adding audio to video

```powershell
ffmpeg -i video.webm -i audio.webm -map 0 -map 1:a -c:v copy -shortest output.webm
```