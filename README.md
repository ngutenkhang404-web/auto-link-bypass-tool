# Auto Link Bypass Tool

Tool tự động hóa vượt qua các link rút gọn (layma.net, taplayma.com, link4m.net)

## 🎯 Tính năng

- ✅ Tự động giải captcha (dùng 2Captcha)
- ✅ Tự động chờ countdown
- ✅ Mô phỏng tương tác con người (scroll, click)
- ✅ Hỗ trợ nhiều links
- ✅ Logging chi tiết

## 📋 Yêu cầu

- Python 3.8+
- Chrome/Chromium browser
- ChromeDriver (phiên bản tương ứng)

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/ngutenkhang404-web/auto-link-bypass-tool.git
cd auto-link-bypass-tool
```

### 2. Tạo virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate  # Windows
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Download ChromeDriver
- Tải từ: https://chromedriver.chromium.org/
- Lưu vào project folder hoặc `/usr/local/bin/`

### 5. Setup environment variables
```bash
cp .env.example .env
```

Sửa `.env`:
```
TWO_CAPTCHA_API_KEY=your_api_key_here
CHROME_DRIVER_PATH=/path/to/chromedriver
HEADLESS_MODE=False
```

## 🎮 Sử dụng

```bash
python main.py
```

## 📝 Cấu trúc project

```
auto-link-bypass-tool/
├── main.py              # Script chính
├── config.py            # Cấu hình
├── utils.py             # Utilities
├── requirements.txt     # Dependencies
├── .env.example         # Template environment
├── .gitignore          # Git ignore
└── README.md           # Documentation
```

## 🔧 Configuration

### Lấy 2Captcha API Key

1. Đăng ký tại https://2captcha.com
2. Nạp tiền (tối thiểu ~$1)
3. Lấy API Key từ dashboard
4. Thêm vào `.env`

### Chrome Driver

```bash
# Kiểm tra phiên bản Chrome
google-chrome --version

# Download phiên bản tương ứng từ:
https://chromedriver.chromium.org/
```

## 📌 TODO

- [ ] Implement captcha solving
- [ ] Implement countdown detection
- [ ] Implement task extraction
- [ ] Implement code copy/paste
- [ ] Add logging system
- [ ] Add error handling
- [ ] Add proxy support
- [ ] Add retry mechanism

## ⚠️ Disclaimer

Tool này dùng cho automation hợp pháp. Bạn chịu trách nhiệm về việc sử dụng tool này phù hợp với điều khoản dịch vụ của các trang web.

## 📞 Support

Nếu có vấn đề, tạo issue trên GitHub.

## 📄 License

MIT License
