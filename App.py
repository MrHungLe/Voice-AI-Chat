import whisper

model = whisper.load_model("medium")
langs = ["vi", "ja", "en"]

for lang in langs:
    print(f"\n🌍 Đang nhận diện ngôn ngữ: {lang}")
    result = model.transcribe("audio.wav", language=lang)
    print("🗣 Văn bản:", result["text"])


print("Bạn nói:")
print(result["text"])
