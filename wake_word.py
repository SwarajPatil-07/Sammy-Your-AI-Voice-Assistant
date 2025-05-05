# wake_word.py
import pvporcupine
import pyaudio
import struct
from config import PORCUPINE_API_KEY

def detect_wake_word():
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_API_KEY,
        keyword_paths=["sammy_assistant\models\Hey-Sammy_en_windows_v3_0_0.ppn"]  # Adjust based on OS
    )

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🔊 Listening for wake word: 'Hey Sammy'...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("🟢 Wake word detected!")
                break
    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
