import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

audio_path = '../../sound/snare1a.wav'
y,sr = librosa.load(audio_path)

D = np.abs(librosa.stft(y))
log_D = librosa.amplitude_to_db(D,ref=np.max)

plt.figure(figsize=(20,3))

librosa.display.specshow(log_D, x_axis='time', y_axis='log')
plt.savefig("./plot_img/snare_spgram.png")
plt.close()
