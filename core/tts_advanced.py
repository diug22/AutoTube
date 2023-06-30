from elevenlabs import generate, play, set_api_key


set_api_key("d9a98c93031a821dd023b4937c0b5f24")
audio = generate(
        text="no lo descargo porque ya lo tengo",
        voice="Bella",
        model="eleven_monolingual_v1"
    )

play(audio)