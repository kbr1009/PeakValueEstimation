from pydub import AudioSegment
sound = AudioSegment.from_wav("../../sound/bass2ch.wav")
sound = sound.set_channels(1)
sound.export("../../sound/bass1ch.wav", format="wav")
