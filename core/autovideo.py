import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, ColorClip
from pydub import AudioSegment
import random
from core.tts_autotube import text_to_speech_with_timings
from core.video_item import VideoItem


class AutoVideo :
    timeline = []
    bg_list = []
    video_item : VideoItem
    
    def __init__(self, video_item, h, w, file_name, bg_video) :
        self.video_item = video_item
        self.text = self.video_item.content
        self.h = h
        self.w = w
        self.bg_video = bg_video
        self.file_name = file_name
        self.load_bgs()
        
    def load_bgs(self):
        path = "./media/video"
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            tags = file.split(".")[0].split(",")
            tags = [tag.strip() for tag in tags]
            self.bg_list.append((tags, file_path))
            
    def gen_timeline(self):
        self.timeline = text_to_speech_with_timings(self.text, "./temp/out_audio.mp3", 1.5)
        
    def crop_random_segment(self, background_clip, audio_duration):
        segment_length = audio_duration
        max_start_time = background_clip.duration - segment_length
        start_time = random.uniform(0, max_start_time)

        desired_width, desired_height = 1080, 1920

        random_segment = background_clip.subclip(start_time, start_time + segment_length)

        original_width, original_height = random_segment.size
        desired_aspect_ratio = 9 / 16
        actual_width = original_height * desired_aspect_ratio
        x_offset = (original_width - actual_width) // 2

        cropped_segment = random_segment.crop(x1=x_offset, y1=0, x2=x_offset + actual_width, y2=original_height)
        return cropped_segment
    

    def generate_video(self):
        self.gen_timeline()
        audio_voice = AudioSegment.from_file("./temp/out_audio.mp3").apply_gain(0)  # Set gain to 0 for voice audio
        
        # TODO : Create method to select random music
        audio_music = AudioSegment.from_file("./media/music/sad, crepy, mistery.mp3").apply_gain(-10)  # Set gain to -10 for music audio
        
        background_clip = VideoFileClip(self.bg_video, audio=False)
        audio_duration = audio_voice.duration_seconds
        cropped_segment = self.crop_random_segment(background_clip, audio_duration)

        def create_text_clip(text, start_time, end_time):
            duration = end_time - start_time
            text_size = (cropped_segment.size[0], cropped_segment.size[1])
            square_color = (0, 0, 0)  # Adjust the color of the square as needed
            
            text_clip = TextClip(text, fontsize=25, font='Arial Black', color='white', size=text_size)
            square_clip = ColorClip(text_clip.size, col=square_color).set_opacity(0.5)
            
            composite_clip = CompositeVideoClip([square_clip, text_clip])
            composite_clip = composite_clip.set_duration(duration).set_start(start_time)
            
            return composite_clip

        text_clips = []
        for word, start_time, end_time in self.timeline:
            text_clip = create_text_clip(word, start_time, end_time)
            text_clips.append(text_clip)
        
        
        audio = audio_voice.overlay(audio_music, position=0)

        temp_audio_path = "./temp/temp_audio.wav"
        audio.export(temp_audio_path, format='wav')
        
        
        
        final_clip = CompositeVideoClip([cropped_segment] + text_clips)
        
        final_clip = final_clip.set_audio(AudioFileClip(temp_audio_path))

        # Export the final video
        final_clip.write_videofile(
            "./out/" + self.file_name,
            codec='libx264',
            threads=4,
            audio_codec='aac',
            remove_temp=True,
            fps=30,  # Adjust the frames per second (lower value for faster rendering)
            bitrate='1500k'
        )

        