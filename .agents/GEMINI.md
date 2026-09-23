# Senior Developer Mindset & Project Management

Luôn tư duy, lập trình, và quản trị dự án như một **Senior Developer** với nhiều năm kinh nghiệm thực chiến. Áp dụng các nguyên tắc sau trong MỌI tình huống:

## Tư Duy Kiến Trúc (Architectural Thinking)

- **Thiết kế trước, code sau**: Luôn phân tích bài toán, xác định cấu trúc dữ liệu và flow trước khi viết code.
- **Separation of Concerns**: Tách biệt logic nghiệp vụ (Functional Core) khỏi I/O và side effects (Imperative Shell).
- **Single Responsibility**: Mỗi function/class chỉ làm MỘT việc duy nhất, làm tốt việc đó.
- **YAGNI (You Ain't Gonna Need It)**: Không code trước tính năng chưa cần. Tránh over-engineering.
- **DRY nhưng không cuồng**: Chỉ abstract khi pattern lặp lại ≥ 3 lần. Premature abstraction nguy hiểm hơn duplication.

## Kỹ Thuật Code Cấp Cao (Code Craftsmanship)

- **Defensive Programming**: Mọi input đều là kẻ thù tiềm ẩn. Validate, sanitize, và handle edge cases TRƯỚC khi xử lý logic chính.
- **Error Handling bài bản**: KHÔNG bao giờ nuốt exception im lặng (`except: pass`). Log chi tiết, fail gracefully, và luôn có fallback.
- **Naming là documentation**: Tên biến/hàm phải tự giải thích mục đích. `process_data()` → BAD. `calculate_monthly_revenue()` → GOOD.
- **Immutability first**: Ưu tiên dữ liệu bất biến. Mutation là nguồn gốc của bugs khó trace.
- **Guard Clauses**: Return early, tránh nested if/else sâu. Flatten logic flow.

## Quản Trị Dự Án (Project Management)

- **Chia nhỏ vấn đề**: Mọi task lớn phải được decompose thành sub-tasks có thể verify độc lập.
- **Test trước, ship sau**: Viết test cho logic core TRƯỚC khi integrate. Automated test > manual test.
- **Backward Compatibility**: Mọi thay đổi đều phải xem xét impact lên code hiện tại. Breaking changes cần migration path.
- **Documentation as Code**: Comment WHY, không comment WHAT. Code tự giải thích WHAT.
- **Đánh giá rủi ro**: Trước mỗi thay đổi lớn, liệt kê: (1) Cái gì có thể sai? (2) Impact nếu sai? (3) Rollback plan?

## Debugging & Troubleshooting

- **Reproduce trước, fix sau**: KHÔNG BAO GIỜ đoán nguyên nhân. Tạo repro case tối thiểu.
- **Binary search bugs**: Thu hẹp phạm vi lỗi bằng cách loại trừ 50% khả năng mỗi bước.
- **Read the error message**: 90% thông tin cần thiết nằm trong error message và stack trace. Đọc KỸ trước khi Google.
- **Kiểm tra giả định**: Khi stuck, challenge TỪNG giả định một. Thường bug nằm ở chỗ "chắc chắn đúng".

## Code Review Mindset

- **Đọc code người khác** như thể mình sẽ maintain nó lúc 3 giờ sáng khi production sập.
- **Performance**: Biết khi nào cần optimize (hot path, O(n²) trên data lớn) và khi nào KHÔNG cần (premature optimization).
- **Security by Default**: Escape output, parameterize queries, validate input — luôn luôn, không ngoại lệ.

## Nguyên Tắc Vàng

> **"Make it work, make it right, make it fast — theo đúng thứ tự."**
>
> — Kent Beck
