from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


def baixar_video_youtube(url, path='temp.mp4'):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(filename=path)
    return path


def juntar_videos(video_youtube_url, start_youtube=None, end_youtube=None):
    video_youtube = baixar_video_youtube(video_youtube_url)
    if start_youtube or end_youtube:
        clip_youtube = VideoFileClip(video_youtube).subclip(start_youtube, end_youtube)
    else:
        clip_youtube = VideoFileClip(video_youtube)
    clip_local = VideoFileClip('theoffice.mp4').subclip(0, 5)

    final_clip = concatenate_videoclips([clip_youtube, clip_local], method='compose')

    final_clip.write_videofile('video_final.mp4', codec="libx264", fps=24)

    os.remove(video_youtube)


juntar_videos("https://youtu.be/KJKy7xjE9F4?si=_hCk2CR5h49th9Kf", 74, 81)
