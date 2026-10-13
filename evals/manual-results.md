# Manual behavior evaluation

Phương pháp: thực hiện và rà soát bởi agent đang phát triển skill. Đây là bằng
chứng ví dụ và kiểm tra chức năng, không phải benchmark độc lập hoặc bằng chứng
rằng mọi model sẽ luôn chọn đúng. Cases gốc ở `behavior-cases.json`.

## Text ngắn

Kết quả:

> Nhóm đã hoàn thành phần giao diện. API chưa hoàn thiện nên chưa thể trình diễn hệ thống.

Rà soát: đúng hai câu; giữ ba ý đầu vào; không thêm số liệu, lịch hoặc file Word.

## Khoản và điểm

```text
1. Chuẩn bị: thu thập dữ liệu.
2. Thực hiện:
   a) Kiểm tra dữ liệu;
   b) Tạo bản nháp.
3. Kiểm tra: đối chiếu bản nháp.
```

Rà soát: ba khoản; khoản 2 có hai điểm; giữ các hành động, không tự thêm quy trình.

## Tiếp tục từ mục hiện có

```text
2.4. Kiểm tra nội dung
2.5. Kiểm tra bố cục
```

Rà soát: không restart về 1, không thêm prose hay tạo file.

## Đề xuất chưa được thông qua

> A đề xuất giao B chuẩn bị bản nháp trước ngày 15/10. Đề xuất chưa được thống nhất; người thực hiện và thời hạn chưa được chốt.

Rà soát: hạn 15/10 vẫn gắn với đề xuất; không biến B thành người đã nhận nhiệm vụ.

## DOCX theo ba bối cảnh

Các input giả định `.values.json`, template nguồn và config nằm ở
`assets/templates/`. Các output đã được tạo bằng công cụ skill tại:

- `artifacts/template-suite/office-minutes.filled.docx`: một trang; không có quốc hiệu; bảng phân công và numbering Word; đã xem ảnh.
- `artifacts/template-suite/academic-short-report.filled.docx`: một trang; không tự thêm bìa khóa luận hoặc dữ liệu nghiên cứu; đã xem ảnh.
- `artifacts/template-suite/administrative-notice.filled.docx`: một trang; vị trí các thành phần, font và cỡ theo vai trò đã đối chiếu; không có chữ ký/dấu; đã xem ảnh.

Validation/config và render report ở `artifacts/template-suite/verification.json`.
Pass của validator chỉ áp dụng các kiểm tra được hỗ trợ, không chứng nhận pháp lý.
Ba starter có manifest ghi nguồn, phạm vi và giới hạn; không giả danh mẫu chính thức.

## Mẫu thực tế

`artifacts/research/uit-trial/`: giữ bản nguồn và SHA256, contract/slot map,
edit report, fidelity report và render trước/sau. Đã điền 21 vị trí được chọn,
gồm metadata và hàng dữ liệu giả định. 17 ZIP member khác giữ nguyên byte;
96 paragraph không được chọn giữ nguyên XML. Đã xem hai trang trước/sau;
header, numbering, ô gộp và phân trang còn nguyên. Giữ dòng ý kiến/chữ ký và
hàng dự phòng trống theo contract; không gọi bản thử là biên bản hoàn chỉnh.
Mẫu UIT không đưa vào gói phân phối khi chưa xác định quyền tái phân phối.

## Thiếu nơi tiếp nhận

Phản hồi phù hợp: “Bạn dùng mẫu của trường/chương trình nào, hoặc có file mẫu
để mình áp dụng không?” Chưa chọn mẫu UIT, chưa tạo khóa luận theo trường đoán.
Đây là câu hỏi cần thiết vì dữ liệu thiếu quyết định mẫu bắt buộc; có thể chuẩn
bị nội dung độc lập nếu người dùng đã cung cấp đề tài và dữ liệu.

## Giới hạn đánh giá

Chưa có thử nghiệm người dùng độc lập hoặc so sánh nhiều model. Bộ test Python
kiểm chứng cơ chế DOCX; không được dùng số test pass để suy ra độ chính xác của
agent trong mọi query tự nhiên. Khi phát triển tiếp, chạy lại các case này với
model/môi trường mục tiêu và xem artifact thực.

## Văn phòng chung

`artifacts/office-general/office-notice.docx`: tạo bằng profile office cho thông
báo nội bộ theo đúng các dữ kiện của tình huống giả định trong case. Không có
quốc hiệu, số văn bản hành chính hoặc bìa học thuật; một trang đã render và xem.
Validation/render report ở `artifacts/office-general/verification.json`.
