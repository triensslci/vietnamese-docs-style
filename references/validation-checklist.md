# Kiểm tra theo đầu ra và mẫu

Ghi từng kiểm tra là đạt, không đạt, chưa kiểm tra hoặc không áp dụng.
Phân biệt bản nháp có trường thiếu đã công bố với bản hoàn chỉnh.

## Mọi đầu ra
- Đúng phạm vi, loại văn bản, ngôn ngữ và độ dài yêu cầu.
- Không thêm dữ kiện, căn cứ, nguồn hoặc quyết định không có đầu vào.
- Đánh số đúng cấp/thứ tự; dẫn chiếu cập nhật sau chỉnh sửa.
- Thuật ngữ, số liệu, thời gian nhất quán; biên tập không đổi nghĩa.
- Công bố placeholder còn lại và trạng thái bản nháp.

## DOCX
- Đúng mẫu, phiên bản, thành phần bắt buộc của đúng loại.
- Khổ, hướng và lề từng section theo mẫu, không ép mọi trang thành A4 dọc.
- Font/cỡ/màu/spacing theo thành phần, gồm style kế thừa, bảng, header/footer.
- Heading, numbering, restart/continue, mục lục và dẫn chiếu đúng.
- Bảng vừa vùng in, không mất chữ/ảnh hoặc trang trắng bất thường.
- Số trang, trang đầu khác biệt và section break đúng mẫu.
- Giữ phần ngoài phạm vi chỉnh sửa khi sửa tài liệu sẵn có.

## Giới hạn hiện tại

Validator hỗ trợ cấu hình profile/template, khổ/lề từng section, font/màu
trực tiếp và chuỗi style, placeholder trong body/bảng/header/footer, literal
bắt buộc và bullet/shading khi cấu hình yêu cầu. Đọc `tooling.md` và trường
unchecked trong report; chưa kiểm tra toàn bộ bố cục, luật hoặc nội dung Word.

Render helper chuyển DOCX thật qua LibreOffice; `--png` tạo ảnh bằng PyMuPDF.
Chỉ ghi đã kiểm tra trực quan khi đã mở xem kết quả. Thiếu công cụ thì công bố
giới hạn. Không coi bullet, shading, thiếu bìa, ngôi thứ nhất hoặc mục tiêu
chưa định lượng là lỗi chung.
