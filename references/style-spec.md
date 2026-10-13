# Triển khai DOCX

Mã helper duy trì tại `scripts/build_docx.py`, không sao chép code vào reference.
Các hàm body/bullet/table nhận `doc` làm đối số đầu tiên.

Tạo mới chưa có mẫu:
```python
from docx import Document
from scripts.build_docx import setup_document, add_body

doc = Document()
setup_document(doc, profile="academic")
add_body(doc, "Nội dung từ đầu vào đã xác minh.")
doc.save("output.docx")
```

`setup_document` nhận profile và config dùng chung với validator. Custom không
config giữ nguyên. Các helper kế thừa style, không gán font cứng lên mọi run.
Mặc định kỹ thuật không thay thế cỡ chữ và bố cục từng thành phần hành chính.
Xem `tooling.md` cho config, điền template và giới hạn kiểm tra.

Với file/template có sẵn, mở `Document(template_path)`; không ghi đè bằng setup
mặc định. Giữ numbering, style, section, field, bảng và header/footer. Công cụ
không hỗ trợ đầy đủ mọi thành phần Word: kiểm tra sau lưu, không chỉ khả năng mở.

Thông số theo nguồn/mẫu đã chọn. Không hard-code địa danh, năm, người ký hoặc
bảng thành viên/rủi ro từ ví dụ riêng. Dùng bảng khi dữ liệu có quan hệ hàng/cột.
Kiểm tra theo `validation-checklist.md`; render thành công chưa phải bằng chứng đã xem mọi trang.
