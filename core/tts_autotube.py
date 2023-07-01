import os
from pydub import AudioSegment
from elevenlabs import generate, save, set_api_key

set_api_key("d9a98c93031a821dd023b4937c0b5f24") #TODO: Move to config file

SRC_AUDIO_TEMP = './temp/tmp_audio.mp3'
SRC_AUDIO_OUT = './temp/out_audio.mp3'
SRC_FORMAT_OUT = 'mp3'

TTS_VOICE = "Adam"
TTS_MODEL = "eleven_multilingual_v1"

def text_to_speech_with_timings(text, cluster_size=4):
    generate_text_to_speech(text)
    return calculate_word_timings(text, cluster_size)

def generate_text_to_speech(text):
    audio = generate(
        text=text,
        voice=TTS_VOICE,
        model=TTS_MODEL
    )
    save(audio,SRC_AUDIO_TEMP)
    
    
def calculate_word_timings(text,cluster_size=4): 
    audio = AudioSegment.from_file(SRC_AUDIO_TEMP)
    #os.remove(SRC_AUDIO_TEMP)
    word_timings = []
    words = text.split()
    total_duration = audio.duration_seconds
    start_time = 0
    for i in range(0, len(words), cluster_size):
        cluster = words[i:i + cluster_size]
        word_duration = total_duration / len(words) * len(cluster)  # Duration of the cluster based on the total duration and number of words
        end_time = start_time + word_duration
        cluster_timings = ' '.join(cluster)
        word_timings.append((cluster_timings, start_time, end_time))
        start_time = end_time

    audio = audio.speedup(playback_speed=1)
    audio.export(SRC_AUDIO_OUT, format=SRC_FORMAT_OUT)
    print("DONE: Voice")
    return word_timings