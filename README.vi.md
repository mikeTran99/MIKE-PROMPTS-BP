# MIKE-PROMPTS-BP

[English](README.md) | **Tiếng Việt**

> ⚡ Bộ công cụ Red Team / Kiểm thử xâm nhập cho bảo mật AI & LLM — **41 Kiểu tấn công · 12 Mã hóa Payload · 21 Hồ sơ AI mục tiêu · 7 Giao diện Luxury · OWASP LLM Top 10 2026**

<p align="center">
  <img src="docs/screenshots/03-logo.jpg" width="200" alt="MIKE-PROMPTS-BP Logo">
</p>

![Screenshot 1](docs/screenshots/screenshot-1.png)

![Screenshot 2](docs/screenshots/screenshot-2.png)

![Screenshot 3](docs/screenshots/screenshot-3.png)

![Screenshot 4](docs/screenshots/screenshot-4.png)

## ⚠️ Tuyên bố miễn trừ

**Công cụ này chỉ dành cho kiểm thử bảo mật được ủy quyền và nghiên cứu an toàn AI.** Sử dụng trái phép đối với các hệ thống bạn không sở hữu hoặc không có quyền kiểm thử rõ ràng là bất hợp pháp. Tác giả không chịu trách nhiệm về việc sử dụng sai mục đích.

## ✨ Tính năng

### 🎯 AI Target Intelligence (21 Hồ sơ)
Hồ sơ phòng thủ chi tiết cho **ChatGPT, Claude, Gemini, Grok, DeepSeek, Cursor, Devin, Windsurf, Codex, Perplexity, Kimi, Replit, Lovable, v0, Manus, Llama, Mistral, Qwen, Command R+, Phi, Copilot** — bao gồm phiên bản, phòng thủ, điểm yếu, tấn công khuyến nghị và ghi chú chiến thuật.

### ⚔️ Nhóm tấn công (7 × 41 loại)
| Nhóm | Loại | Mô tả |
|------|------|-------|
| **OVERRIDE** | Direct, Jailbreak, DevMode, Skeleton Key, System Override v2 | Ghi đè trực tiếp system prompt |
| **STEALTH** | Indirect, Payload, Token Smuggle, Multimodal Inject, RAG Poison, Tool-Call Smuggle | Ẩn payload trong dữ liệu tin cậy |
| **EVASION** | Multilingual, Few-Shot, Virtualization, Context, Flip Attack, Low-Resource Lang, Poetic Format, Emoji Cipher | Né tránh filter |
| **HYBRID** | WormGPT, Persona Layer, Prompt Chain, Crescendo, TAP, GOAT, Self-Replicate | Kỹ thuật nhiều bước / nhiều lớp |
| **RECON** | System Leak, Hierarchy Confusion, Hidden Context, Training Data Extract, Package Hallucination | Thu thập thông tin hệ thống |
| **AGENTIC** | Confused Deputy, Permission Escalation, MCP Tool Abuse, Indirect via RAG, Execution Loop, Memory Poison | Khai thác AI agent |
| **SAFETY** | Do Not Answer, Real Toxicity, XSS via Output, SQL via Output | Benchmark an toàn AI |

### 🏷️ OWASP LLM Top 10 2026
Mỗi kiểu tấn công được ánh xạ tới OWASP LLM Top 10 (2026 Edition) — từ LLM01 (Prompt Injection) đến LLM10 (Improper Output Handling). Badge OWASP hiển thị trong kết quả output.

### 🔐 Mã hóa Payload (12 loại)
`Base64` · `Obfuscate Hex` · `Unicode Escape` · `ROT13` · `Homoglyph` · `Stealth Embed (Zero-Width)` · `Token Split` · `Markdown Inject` · `Morse Code` · `Braille Unicode` · `Pig Latin` · `Reverse Text` — kết hợp nhiều mã hóa để tối đa hiệu quả.

### 📊 Xuất kết quả (3 định dạng)
`TXT` · `JSON (báo cáo có cấu trúc)` · `HTML (báo cáo styled Obsidian & Gold)` — phục vụ kiểm thử bảo mật chuyên nghiệp.

### 🎨 7 Giao diện Luxury
`🌑 Obsidian & Gold` · `💎 Midnight Sapphire` · `🌹 Eclipse Rose` · `🍀 Emerald Noir` · `❄️ Arctic Silver` · `🖤 Dark Pro` · `☀️ Light Mode`

### 🌐 Giao diện Song ngữ
Toàn bộ giao diện **Tiếng Việt / Tiếng Anh** chuyển đổi bằng một nút bấm.

### 🛡️ Stealth Steganography
Ẩn toàn bộ payload tấn công bên trong văn bản trông vô hại bằng ký tự Unicode zero-width — hoàn toàn vô hình với mắt thường.

### 💡 Gợi ý Thông minh
Chọn AI mục tiêu → nhận gợi ý tức thì về kiểu tấn công và mã hóa tối ưu dựa trên dữ liệu kiểm thử thực tế.

## 📦 Tải về

Tải `MikePromptsBP.exe` từ trang [**Releases**](https://github.com/mikeTran99/MIKE-PROMPTS-BP/releases).

> **Portable** — Không cần cài đặt. Chỉ cần tải về và chạy trên Windows.

## 🚀 Hướng dẫn nhanh

1. **Chọn AI mục tiêu** — Chọn từ 21 hồ sơ AI (hoặc để Auto)
2. **Nhập Target Role** — Vai trò ép AI nhận
3. **Nhập System Override** — Lệnh ghi đè (tùy chọn)
4. **Chọn Kiểu tấn công** — Chọn từ 7 tab × 41 loại
5. **Chọn Mã hóa** — Tùy chọn, kết hợp nhiều lớp
6. **Nhấn ⚡ TẠO PAYLOAD** — Tạo prompt
7. **Xuất kết quả** — TXT, JSON, hoặc HTML Report

## ⌨️ Phím tắt

| Phím tắt | Hành động |
|----------|-----------|
| `Ctrl+Shift+C` | Sao chép payload vào clipboard |
| `Ctrl+Shift+S` | Xuất payload ra file .txt |

## 🛠️ Công nghệ sử dụng

- **Python 3.14** — Runtime chính
- **CustomTkinter** — Framework GUI dark theme hiện đại
- **Pillow** — Xử lý hình ảnh cho icon ứng dụng
- **PyInstaller** — Đóng gói `.exe` đơn file

## 📜 Giấy phép

Dự án được cấp phép theo [MIT License](LICENSE).

## 👤 Tác giả

**mikeTran99** — [GitHub](https://github.com/mikeTran99)

---

<p align="center">
  <b>MIKE-PROMPTS-BP v7.0</b> — Luxury Edition<br>
  <i>Chỉ dành cho kiểm thử bảo mật được ủy quyền.</i>
</p>
