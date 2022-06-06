from ctypes import sizeof
from audiomentations import Compose, AddGaussianNoise, AddShortNoises, AddBackgroundNoise, TimeStretch, PitchShift, Shift
import numpy as np
import os

#install ffmpeg for mp3


#python package for audio and music
import librosa

#write audio files
import soundfile as sf

aug = Compose([
    AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015, p=0.5),
    TimeStretch(min_rate=0.8, max_rate=1.25, p=1), #slow fast
    PitchShift(min_semitones=-10, max_semitones=10, p=1),
    Shift(min_fraction=-0.5, max_fraction=0.5, p=0.5),
])

# # Generate 2 seconds of dummy audio for the sake of example
# samples = np.random.uniform(low=-0.2, high=0.2, size=(32000,)).astype(np.float32)

# # Augment/transform/perturb the audio data
# augmented_samples = augment(samples=samples, sample_rate=16000)

if __name__ == "__main__":
    file_path = "/home/****/workshop/audio-augmentation/myaudio-aug/audio_files/combined_good_data.mp3"

    #get file name
    dirname, file_name = os.path.split(file_path)

    signal, sample_rate = librosa.load(path=file_path,sr=None)

    # print("Shape of Audio:", signal.shape)
    # print("Sample Rate Audio:", sample_rate)
    
    augmented_signal = aug(signal, sample_rate)
    print(augmented_signal)
    
    sf.write(file=os.path.join(dirname,"output.wav"),data=augmented_signal,samplerate=sample_rate)
    