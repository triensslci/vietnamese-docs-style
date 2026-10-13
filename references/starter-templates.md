# Chọn starter có sẵn

Ưu tiên mẫu của người dùng/nơi tiếp nhận trước các starter. Query chỉ là tín hiệu;
chọn theo mục đích và nơi nhận, không dò một từ rồi gán profile.

| Starter | Chọn khi | Không chọn khi |
| --- | --- | --- |
| `office-minutes` | Biên bản họp nhóm hoặc công ty, ghi thảo luận/quyết định/phân công | Biên bản thủ tục hành chính, hội đồng bảo vệ hoặc xử phạt có mẫu riêng |
| `academic-short-report` | Báo cáo học thuật ngắn, chưa có mẫu trường, các mục mẫu phù hợp nội dung | Khóa luận/luận văn phải theo trường; bài tổng quan không có phương pháp/kết quả tương ứng |
| `administrative-notice` | Thông báo có tên loại, phạm vi hành chính phù hợp hoặc người dùng yêu cầu thể thức đó | Công văn, quyết định, giấy mời, thông báo nội bộ công ty không yêu cầu NĐ30 |

Không có starter phù hợp: dựng bằng helper theo cấu trúc phù hợp hoặc tìm mẫu
chính thức theo `template-selection.md`. Không ép mọi tài liệu vào ba starter.
Hỏi trường/chương trình khi người dùng đòi đúng mẫu trường nhưng chưa xác định.
Chưa biết trường không ngăn việc viết một đoạn text chung mà họ đã yêu cầu rõ.

## File và cách dùng

Mỗi starter ở `assets/templates/` có `.docx`, `.rules.json`, `.values.json`.
Manifest ghi nguồn, version, hash, phạm vi và nghiệm thu. Dữ liệu values là giả
định có nhãn, không phải thông tin để tái dùng cho tài liệu thật.

```bash
python scripts/fill_template.py assets/templates/office-minutes.docx output.docx --values my-values.json
python scripts/validate_docx.py output.docx --profile minutes-general --config assets/templates/office-minutes.rules.json
python scripts/render_docx.py output.docx --png
```

Điền mọi token bằng thông tin người dùng hoặc ghi rõ chỗ thiếu trong bản nháp.
`status_note` có thể là chuỗi rỗng cho tài liệu không cần note; bản thử dùng note
để phân biệt dữ liệu giả. `signature_note` không phải chữ ký và có thể để trống.
Không tạo chữ ký/dấu từ tên người ký. Không coi các tên/số/ngày trong file values
là mặc định. Token một dòng; nội dung dài hoặc nhiều đoạn cần chỉnh cấu trúc
có chủ đích và kiểm tra lại, không nhét vào một run rồi giảm cỡ chữ để vừa trang.

## Nghiệm thu và giới hạn

Ba bản thử mỗi bản một trang đã điền, qua kiểm tra được hỗ trợ và xem ảnh.
Điều đó không chứng minh mọi nội dung sau này đều vừa mẫu. Đặc biệt cần điều
chỉnh độ dài đường kẻ theo tên cơ quan/tiêu ngữ/trích yếu, độ dài chức vụ và
phần ký trong thông báo. Mẫu học thuật không có hiệu lực như quy định của trường.
Đây là starter do dự án tự dựng; mẫu UIT nghiên cứu bên ngoài không được đóng
gói hoặc tuyên bố dùng chung cho mọi trường.
