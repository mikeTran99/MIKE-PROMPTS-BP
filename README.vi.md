# MIKE-PROMPTS-BP

[English](README.md) | **Tiếng Việt**

> ⚡ Bộ công cụ Red Team / Kiểm thử xâm nhập cho bảo mật AI & LLM — **15 Kiểu tấn công · 8 Mã hóa Payload · 15 Hồ sơ AI mục tiêu · 7 Giao diện Luxury**

![Giao diện chính](docs/screenshots/01-main-ui.png)

![Kết quả Payload](docs/screenshots/02-payload-output.png)

## ⚠️ Tuyên bố miễn trừ

**Công cụ này chỉ dành cho kiểm thử bảo mật được ủy quyền và nghiên cứu an toàn AI.** Sử dụng trái phép đối với các hệ thống bạn không sở hữu hoặc không có quyền kiểm thử rõ ràng là bất hợp pháp. Tác giả không chịu trách nhiệm về việc sử dụng sai mục đích.

## ✨ Tính năng

### 🎯 AI Target Intelligence (15 Hồ sơ)
Hồ sơ phòng thủ chi tiết cho **ChatGPT, Claude, Gemini, Grok, DeepSeek, Cursor, Devin, Windsurf, Codex, Perplexity, Kimi, Replit, Lovable, v0, Manus** — bao gồm phiên bản, phòng thủ, điểm yếu, tấn công khuyến nghị và ghi chú chiến thuật.

### ⚔️ Nhóm tấn công (5 × 15 loại)
| Nhóm | Loại | Mô tả |
|------|------|-------|
| **OVERRIDE** | Direct Injection, Jailbreak, DevMode | Ghi đè trực tiếp system prompt |
| **STEALTH** | Indirect, Payload Injection, Token Smuggle | Ẩn payload trong dữ liệu tin cậy |
| **EVASION** | Multilingual, Few-Shot, Virtualization, Context Manipulation | Né tránh filter |
| **HYBRID** | WormGPT, Persona Layer, Prompt Chain | Kỹ thuật nhiều bước / nhiều lớp |
| **RECON** | System Leak, Hierarchy Confusion | Thu thập thông tin hệ thống |

### 🔐 Mã hóa Payload (8 loại)
`Base64` · `Obfuscate Hex` · `Unicode Escape` · `ROT13` · `Homoglyph` · `Stealth Embed (Zero-Width)` · `Token Split` · `Markdown Inject` — kết hợp nhiều mã hóa để tối đa hiệu quả.

### 🎨 7 Giao diện Luxury
`🌑 Obsidian & Gold` · `💎 Midnight Sapphire` · `🌹 Eclipse Rose` · `🍀 Emerald Noir` · `❄️ Arctic Silver` · `🖤 Dark Pro` · `☀️ Light Mode`

### 🌐 Giao diện Song ngữ
Toàn bộ giao diện **Tiếng Việt / Tiếng Anh** chuyển đổi bằng một nút bấm.

### 🛡️ Stealth Steganography
Ẩn toàn bộ payload tấn công bên trong văn bản trông vô hại bằng ký tự Unicode zero-width — hoàn toàn vô hình với mắt thường.

### 💡 Gợi ý Thông minh
Chọn AI mục tiêu → nhận gợi ý tức thì về kiểu tấn công và mã hóa tối ưu dựa trên dữ liệu kiểm thử thực tế.

## 📦 Cài đặt

### Cách 1: File thực thi (Windows)
Tải `MikePromptsBP.exe` từ trang [Releases](https://github.com/mikeTran99/MIKE-PROMPTS-BP/releases). Không cần cài đặt — chỉ cần chạy.

### Cách 2: Chạy từ mã nguồn
```bash
git clone https://github.com/mikeTran99/MIKE-PROMPTS-BP.git
cd MIKE-PROMPTS-BP
pip install -r requirements.txt
python inject.py
```

## 🚀 Hướng dẫn nhanh

1. **Chọn AI mục tiêu** — Chọn từ 15 hồ sơ AI (hoặc để Auto)
2. **Nhập Target Role** — Vai trò ép AI nhận
3. **Nhập System Override** — Lệnh ghi đè (tùy chọn)
4. **Chọn Kiểu tấn công** — Chọn từ 5 tab × 15 loại
5. **Chọn Mã hóa** — Tùy chọn, kết hợp nhiều lớp
6. **Nhấn ⚡ TẠO PAYLOAD** — Tạo prompt
7. **Sao chép hoặc Xuất** — `Ctrl+Shift+C` để copy, `Ctrl+Shift+S` để xuất file

## ⌨️ Phím tắt

| Phím tắt | Hành động |
|----------|-----------|
| `Ctrl+Shift+C` | Sao chép payload vào clipboard |
| `Ctrl+Shift+S` | Xuất payload ra file .txt |

## 🛠️ Công nghệ sử dụng

- **Python 3.14** — Runtime chính
- **CustomTkinter** — Framework GUI dark theme hiện đại
- **Pillow** — Xử lý hình ảnh cho icon ứng dụng
- **IME Fix v3** — Chống crash khi gõ tiếng Việt (Windows)
- **PyInstaller** — Đóng gói `.exe` đơn file

## 🧪 Kiểm thử

```bash
python tests/test_inject.py    # 114 tests — encoders, templates, pipeline
python tests/test_stealth.py   # 12 tests — steganography encode/decode
```

## 📜 Giấy phép

Dự án được cấp phép theo [MIT License](LICENSE).

## 👤 Tác giả

**mikeTran99** — [GitHub](https://github.com/mikeTran99)

---

<p align="center">
  <b>MIKE-PROMPTS-BP v6.0</b> — Luxury Edition<br>
  <i>Chỉ dành cho kiểm thử bảo mật được ủy quyền.</i>
</p>
