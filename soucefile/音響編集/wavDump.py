import wave
from scipy import fromstring, int16
import sys
 
args = sys.argv
wavfile = args[1]
 
# WAVファイルを開く
wr = wave.open(wavfile, "rb")
 
# WAVファイルの情報を表示（別にいらん）
print ("Channel num : ", wr.getnchannels())
print ("Sample size : ", wr.getsampwidth())
print ("Sampling rate : ", wr.getframerate())
print ("Frame num : ", wr.getnframes())
print ("Prams : ", wr.getparams())
print ("Sec : ", float(wr.getnframes()) / wr.getframerate())
 
# データの読み込み
data = wr.readframes(wr.getnframes())
 
# 文字型から数値型に
num_data = fromstring(data, dtype = int16)
print ("Data : ", hex(num_data[0])," ",hex(num_data[1])," ",hex(num_data[2])," ",hex(num_data[3])," ")
if (wr.getnchannels() == 2):
    # 左チャンネル
    left = num_data[::2]
    # 右チャンネル
    right = num_data[1::2]
 
wr.close()
