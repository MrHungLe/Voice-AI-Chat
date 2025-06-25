# 🎙️ Voice-AI-Chat

Ứng dụng Python ghi âm giọng nói từ micro, chuyển đổi thành văn bản bằng AI (Whisper), và có thể mở rộng để phản hồi bằng GPT. Hỗ trợ tiếng Việt!

---

## 🚀 Tính năng

- 🎤 Ghi âm từ microphone (5 giây)
- 🧠 Nhận diện giọng nói bằng [OpenAI Whisper](https://github.com/openai/whisper)
- 🌐 Hỗ trợ tiếng Việt (và nhiều ngôn ngữ khác)
- 💬 Mở rộng tích hợp với GPT để tạo hội thoại thông minh
- 🗂 Tổ chức thư mục đơn giản, dễ mở rộng

---

## 🧠 Công nghệ sử dụng

- [Python 3.10+](https://www.python.org/)
- [Whisper](https://github.com/openai/whisper)
- [PyTorch](https://pytorch.org/)
- `sounddevice`, `scipy`, `ffmpeg-python`

---

## 📦 Cài đặt

### 1. Cài môi trường cần thiết

```bash
pip install torch
pip install git+https://github.com/openai/whisper.git
pip install sounddevice scipy ffmpeg-python
