from pydub import AudioSegment
sound = AudioSegment.from_wav("../../sound/hihat.wav")
sound = sound.set_channels(1)
sound.export("../Hihat/sound/hihat.wav", format="wav")
