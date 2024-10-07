# pip install moviepy
import moviepy.editor
# replace the parameter with the location of video.
video=moviepy.editor.VideoFileClip("video_path\pasupati.avi")

audio_date=video.audio
# replace the parameter with the location
# along with filename
audio_date.write_audiofile("video_path\pasupati.mp3")