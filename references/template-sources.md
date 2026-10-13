# Nguồn mẫu và tình huống

Ngày khảo sát: 2026-10-13. Đây là danh mục nguồn; chưa phải bộ DOCX đã tải,
render và nghiệm thu. Kiểm tra lại phiên bản phù hợp trước khi dùng.

## Quy định hành chính

[NĐ30 — Cổng TTĐT Chính phủ](https://chinhphu.vn/default.aspx?docid=199378&pageid=27160)
và [bản ký](https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/03/30.signed.pdf).
Nguồn gốc để đối chiếu phạm vi, thể thức và mẫu đúng tên loại. Bản chép trong
repo có thể có lỗi OCR. Kiểm tra hiệu lực/sửa đổi riêng khi cần khẳng định hiện hành.

## Học thuật

- [Đại học Việt Nhật](https://vju.ac.vn/quy-dinh-huong-dan-va-cac-bieu-mau/): đã đọc chỉ mục Quyết định 520/QĐ-ĐHVN ngày 06/05/2026, có quy cách, bìa, cam đoan, tóm tắt, nhật ký, giải trình và biểu mẫu bảo vệ. Chưa kiểm tra file đính kèm; phải chọn đúng chương trình/đối tượng.
- [UIT](https://oep.uit.edu.vn/vi/mau-khoa-luan-tot-nghiep): đã đọc chỉ mục có mẫu trình bày, bìa, đề cương, biên bản hội đồng. Đã tải và đọc ba file: mẫu trình bày có 4 section, mẫu biên bản hội đồng có 4 bảng, phụ lục hướng dẫn có 2 section. Mẫu trình bày thuộc chương trình tiên tiến Hệ thống thông tin, có nội dung tiếng Anh; file hướng dẫn nêu lề khác một số section của mẫu. Chưa xác minh phiên bản hiện hành cho từng khóa. Riêng biên bản hội đồng đã render bản nguồn và bản điền thử 21 vị trí giả định; xem cả hai trang trước/sau và kiểm chứng giữ nguyên 17 ZIP member cùng 96 paragraph ngoài vùng sửa. Đây là thử nghiệm sửa có phạm vi, không chứng nhận biên bản hoàn chỉnh hoặc chấp nhận của trường. Biên bản hội đồng không phải mẫu họp nội bộ chung. File nghiên cứu lưu ngoài gói phát hành do chưa xác định quyền tái phân phối.
- [Đại học Hạ Long](https://uhl.edu.vn/HuongdantrinhbayKhoaluantotnghiep_11829.htm): đã đọc hướng dẫn HTML công bố 05/03/2026. Lề và cấu trúc riêng cho khóa luận minh họa vì sao không thể áp mặc định hành chính lên mọi bài học thuật. Trang có ví dụ giải thích số hình không nhất quán; đối chiếu hướng dẫn gốc, không sao chép lỗi đó thành quy tắc.

## Văn bản thực tế

[Bộ Dân tộc và Tôn giáo — lịch tiếp công dân 2026](https://bdttg.gov.vn/lich-tiep-cong-dan/lich-tiep-cong-dan-cua-bo-truong-bo-dan-toc-va-ton-giao-nam-2025.htm).
Đã đọc HTML ngày đăng 14/01/2026; slug ghi 2025 nhưng nội dung ghi 2026.
Tình huống thông báo lịch định kỳ: mở đầu nêu cơ sở và hành động thông báo,
lịch nhiều kỳ đưa thành bảng. Chỉ là quan sát cấu trúc web, chưa xác minh
font/lề bản ký. Không mang lịch hoặc căn cứ sang văn bản mới.

## Văn phòng

Có starter nội bộ do dự án tự dựng và nghiệm thu với dữ liệu giả định, xem `starter-templates.md`. Chưa có mẫu riêng của một tổ chức được chứng nhận. Dùng cấu trúc tối thiểu theo mục đích;
không coi mẫu trường/cơ quan nhà nước là chuẩn chung cho mọi công ty.

## Điều kiện thêm mẫu vào assets

Đọc file thật, ghi nguồn/phạm vi, kiểm tra quyền phân phối, loại dữ kiện riêng,
điền thử dữ liệu giả có nhãn, kiểm tra style/numbering/section và render.
Chưa đủ các bước thì giữ trạng thái ứng viên, không ghi là mẫu đã hỗ trợ.

## Nguồn gốc và bản ký đã kiểm tra

Bản ký NĐ30 tải từ Cổng Chính phủ ngày 2026-10-13, SHA256
`be2514460c953141923579e4a0ddd0249c611643a59514976790dc1d90589178`.
Đã xem Điều 1–2, các trang Phụ lục I liên quan và mẫu 1.4/1.5 Phụ lục III;
không chỉ dựa bản OCR. Tình trạng tra cứu và giới hạn live ở
`administrative-format-nd30.md`. Ba starter trong gói là code/cấu trúc do dự án
viết; không sao chép mẫu DOCX UIT hoặc toàn bộ nội dung trường vào gói.
