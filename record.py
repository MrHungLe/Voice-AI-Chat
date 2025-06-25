import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("🎙 Bắt đầu ghi âm...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
print("✅ Ghi xong!")

# Chuẩn hóa âm lượng để dễ nghe hơn
scaled = np.int16(recording/np.max(np.abs(recording)) * 32767)
write("audio.wav", fs, scaled)
print("✅ File đã lưu: audio.wav")
