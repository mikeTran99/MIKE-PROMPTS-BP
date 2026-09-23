# Auto-Update Knowledge Rule — MIKE-PROMPTS-BP

Mỗi khi kết thúc một conversation liên quan đến dự án **MIKE-PROMPTS-BP** (thư mục `Promp_H`), hãy tự động:

1. **Đọc KI hiện tại** tại `C:\Users\Mr Trung\.gemini\antigravity-ide\knowledge\MIKE_PROMPTS_BP_v8_Arsenal\artifacts\architecture.md`
2. **Cập nhật** với:
   - Mọi thay đổi code mới (features, bug fixes, refactors)
   - Gotchas và known issues mới phát hiện
   - Thay đổi version, build command, hoặc dependencies
   - Bug fixes với root cause analysis
3. **Cập nhật `metadata.json`** — bump `updated_at` timestamp
4. **KHÔNG xóa** thông tin cũ — chỉ thêm mới hoặc sửa nếu outdated

Áp dụng cho MỌI conversation có chỉnh sửa file trong `e:\Projects\TOOLS\Promp_H\`.
