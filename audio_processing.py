import sounddevice as sd
import numpy as np

def capture_audio(duration=3, sampling_rate=16000):
    print("Recording audio...")
    audio = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, dtype='float32')
    sd.wait()
    return np.squeeze(audio)
