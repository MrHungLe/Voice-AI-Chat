import whisper

model = whisper.load_model("medium")
result = model.transcribe("audio.wav", language="vi")

print("Bạn nói:")
print(result["text"])
