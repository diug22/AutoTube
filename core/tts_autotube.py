import os
from gtts import gTTS
from pydub import AudioSegment
import pocketsphinx


def text_to_speech_with_timings(text, output_file, speed=1.5, cluster_size=1):
    tts = gTTS(text, lang='es')
    tts.save("./temp/tmp_audio.mp3")

    audio = AudioSegment.from_file("./temp/tmp_audio.mp3")
    os.remove("./temp/tmp_audio.mp3")

    # Calculate speed modification factor
    speed_factor = 1 / speed

    # Get word timings
    word_timings = []
    words = text.split()
    total_duration = audio.duration_seconds * speed_factor  # Total duration of the audio after speed modification
    start_time = 0
    for i in range(0, len(words), cluster_size):
        cluster = words[i:i + cluster_size]
        word_duration = total_duration / len(words) * len(cluster)  # Duration of the cluster based on the total duration and number of words
        end_time = start_time + word_duration
        cluster_timings = ' '.join(cluster)
        word_timings.append((cluster_timings, start_time, end_time))
        start_time = end_time

    audio = audio.speedup(playback_speed=speed)
    audio.export(output_file, format="wav")
    print("DONE: Voice")
    return word_timings