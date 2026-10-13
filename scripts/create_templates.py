"""Build project-authored starter templates, with explicit scopes and trial data."""
import argparse
import hashlib
import json
from pathlib import Path

from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

try:
    from .build_docx import setup_document, add_body, add_numbered, add_table
    from .fill_template import fill_template
except ImportError:
    from build_docx import setup_document, add_body, add_numbered, add_table
    from fill_template import fill_template

LEGAL_SOURCE = 'https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/03/30.signed.pdf'


def borderless(table):
    props = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        node = OxmlElement('w:' + side)
        node.set(qn('w:val'), 'nil')
        borders.append(node)
    props.append(borders)


def role_paragraph(container, text, style, centered=True):
    p = container.add_paragraph(text, style=style)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    if centered:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def rule(container, width_cm, available_cm):
    p = container.add_paragraph()
    p.paragraph_format.left_indent = Cm(max(0, (available_cm-width_cm)/2))
    p.paragraph_format.right_indent = p.paragraph_format.left_indent
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    p.add_run().font.size = Pt(1)
    borders = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    for name, value in {'val': 'single', 'sz': '6', 'space': '0', 'color': '000000'}.items():
        bottom.set(qn('w:' + name), value)
    borders.append(bottom)
    p._p.get_or_add_pPr().append(borders)


def notice():
    config = {
        'profile': 'administrative',
        'source': 'Project-authored notice starter; NĐ30 Appendix I and Appendix III model 1.4; human review required',
        'style_rules': {
            'AdminAgency': {'size_pt': [12, 13], 'bold': True, 'italic': False},
            'AdminNational': {'size_pt': [12, 13], 'bold': True, 'italic': False},
            'AdminMotto': {'size_pt': [13, 14], 'bold': True, 'italic': False},
            'AdminNumber': {'size_pt': [13, 13], 'bold': False, 'italic': False},
            'AdminDate': {'size_pt': [13, 14], 'bold': False, 'italic': True},
            'Title': {'size_pt': [14, 14], 'bold': True, 'italic': False},
            'AdminSubject': {'size_pt': [13, 14], 'bold': True, 'italic': False},
            'AdminBody': {'size_pt': [13, 14], 'bold': False, 'italic': False},
            'AdminSigner': {'size_pt': [13, 14], 'bold': True, 'italic': False},
            'AdminRecipientsLabel': {'size_pt': [12, 12], 'bold': True, 'italic': True},
            'AdminRecipients': {'size_pt': [11, 11], 'bold': False, 'italic': False},
        },
        'required_text': ['CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', 'Độc lập - Tự do - Hạnh phúc', 'THÔNG BÁO', 'Nơi nhận:'],
    }
    doc = Document()
    setup_document(doc, 'administrative', config)
    doc.sections[0].different_first_page_header_footer = True
    top = doc.add_table(rows=1, cols=2)
    top.autofit = False
    top.columns[0].width, top.columns[1].width = Cm(7), Cm(9.5)
    top.cell(0, 0).width, top.cell(0, 1).width = Cm(7), Cm(9.5)
    borderless(top)
    left, right = top.rows[0].cells
    for cell in (left, right):
        first = cell.paragraphs[0]
        first.paragraph_format.space_after = Pt(0)
        first.paragraph_format.line_spacing = Pt(1)
        first.add_run().font.size = Pt(1)
    role_paragraph(left, '{{organization}}', 'AdminAgency')
    rule(left, 1.8, 6.6)
    role_paragraph(left, 'Số: {{number}}', 'AdminNumber')
    role_paragraph(right, 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', 'AdminNational')
    role_paragraph(right, 'Độc lập - Tự do - Hạnh phúc', 'AdminMotto')
    rule(right, 6.5, 9.1)
    role_paragraph(right, '{{date}}', 'AdminDate')
    title = doc.add_paragraph('THÔNG BÁO', style='Title')
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.first_line_indent = Cm(0)
    title.paragraph_format.space_before, title.paragraph_format.space_after = Pt(12), Pt(0)
    role_paragraph(doc, '{{subject}}', 'AdminSubject')
    rule(doc, 4.5, 16.5)
    for name in ('opening', 'time', 'location', 'participants', 'request'):
        doc.add_paragraph('{{' + name + '}}', style='AdminBody')
    add_body(doc, '{{status_note}}')
    bottom = doc.add_table(rows=1, cols=2)
    borderless(bottom)
    for cell in bottom.rows[0].cells:
        cell.paragraphs[0].paragraph_format.space_after = Pt(0)
        cell.paragraphs[0].add_run().font.size = Pt(1)
    left, right = bottom.rows[0].cells
    role_paragraph(left, 'Nơi nhận:', 'AdminRecipientsLabel', False)
    role_paragraph(left, '- {{recipients}};', 'AdminRecipients', False)
    role_paragraph(left, '- Lưu: VT.', 'AdminRecipients', False)
    role_paragraph(right, '{{position}}', 'AdminSigner')
    p = role_paragraph(right, '{{signature_note}}', 'AdminBody')
    p.paragraph_format.space_after = Pt(24)
    role_paragraph(right, '{{signer}}', 'AdminSigner')
    values = {
        'organization': 'ĐƠN VỊ THỬ NGHIỆM', 'number': '01/TB-TN',
        'date': 'Hà Nội, ngày 13 tháng 10 năm 2026',
        'subject': 'Về lịch họp rà soát tài liệu thử nghiệm',
        'opening': 'Đơn vị thử nghiệm thông báo lịch họp rà soát tài liệu như sau:',
        'time': '1. Thời gian: 09 giờ ngày 15 tháng 10 năm 2026 (giả định).',
        'location': '2. Địa điểm: phòng thử nghiệm (giả định).',
        'participants': '3. Thành phần: nhóm biên soạn tài liệu thử nghiệm.',
        'request': 'Đề nghị thành viên trong tình huống giả định chuẩn bị bản nháp để trao đổi tại cuộc họp./.',
        'recipients': 'Nhóm thử nghiệm', 'position': 'NGƯỜI PHỤ TRÁCH THỬ NGHIỆM',
        'signer': 'Nguyễn Văn A (giả định)',
        'status_note': 'Tài liệu thử nghiệm; dữ liệu giả định, không dùng để ban hành.',
        'signature_note': '(Không có chữ ký trong bản thử nghiệm)',
    }
    return doc, config, values


def academic():
    config = {'profile': 'academic', 'source': 'Project-authored short report; no university compliance claim',
              'margins_cm': {'left': [2.5, 2.5], 'right': [2, 2], 'top': [2.5, 2.5], 'bottom': [2.5, 2.5]},
              'style_rules': {'Normal': {'size_pt': [13, 13]}, 'Title': {'size_pt': [16, 16], 'bold': True}},
              'required_text': ['Mục đích', 'Phương pháp', 'Kết quả', 'Hạn chế', 'Tài liệu tham khảo']}
    doc = Document()
    setup_document(doc, 'academic', config)
    doc.add_paragraph('{{title}}', style='Title')
    add_body(doc, 'Tác giả: {{author}}')
    add_body(doc, '{{status_note}}')
    for heading, name in [('1. Mục đích', 'purpose'), ('2. Phương pháp', 'method'),
                          ('3. Kết quả', 'results'), ('4. Hạn chế', 'limitations'),
                          ('5. Tài liệu tham khảo', 'references')]:
        doc.add_heading(heading, level=1)
        add_body(doc, '{{' + name + '}}')
    add_table(doc, ['Hạng mục kiểm tra', 'Kỳ vọng'], [['Đánh số', 'Giữ cấp và thứ tự'], ['Dữ kiện', 'Không tự thêm thông tin']], 'academic')
    values = {'title': 'Báo cáo thử nghiệm tạo tài liệu tiếng Việt', 'author': 'Nhóm thử nghiệm (giả định)',
              'purpose': 'Kiểm tra cách tổ chức báo cáo ngắn bằng tiếng Việt và giữ nội dung đầu vào.',
              'method': 'Tạo mẫu có token, điền chuỗi tiếng Việt và đối chiếu nội dung sau khi lưu.',
              'results': 'Ví dụ này trình bày các phần của báo cáo. Không có khảo sát hoặc số liệu thực nghiệm để kết luận hiệu quả.',
              'limitations': 'Mẫu không thay thế hướng dẫn của trường hoặc yêu cầu riêng của giảng viên.',
              'references': 'Tài liệu minh họa không sử dụng nguồn nghiên cứu bên ngoài.',
              'status_note': 'Đây là tài liệu kiểm thử cấu trúc; dữ liệu minh họa, không phải kết quả nghiên cứu đã công bố.'}
    return doc, config, values


def office():
    config = {'profile': 'minutes-general', 'source': 'Project-authored internal meeting notes starter',
              'required_text': ['Nội dung', 'Quyết định', 'Phân công']}
    doc = Document()
    setup_document(doc, 'minutes-general', config)
    doc.add_paragraph('{{title}}', style='Title')
    add_body(doc, '{{metadata}}')
    add_body(doc, '{{status_note}}')
    doc.add_heading('Nội dung', level=1)
    add_body(doc, '{{discussion}}')
    doc.add_heading('Quyết định', level=1)
    add_numbered(doc, ['{{decision}}'])
    doc.add_heading('Phân công', level=1)
    add_table(doc, ['Công việc', 'Phụ trách', 'Thời hạn'], [['{{task}}', '{{owner}}', '{{deadline}}']], 'minutes-general')
    values = {'title': 'Biên bản họp nội bộ thử nghiệm', 'metadata': '09 giờ ngày 13/10/2026; phòng thử nghiệm; nhóm A (giả định).',
              'discussion': 'Nhóm trao đổi về cấu trúc tài liệu và cách ghi nhận công việc.',
              'decision': 'Trong tình huống giả định, nhóm thống nhất chuẩn bị một bản nháp để rà soát.',
              'task': 'Chuẩn bị bản nháp', 'owner': 'Thành viên A (giả định)', 'deadline': '15/10/2026 (giả định)',
              'status_note': 'Tình huống thử nghiệm; các tên và thời hạn dưới đây là giả định.'}
    return doc, config, values


BUILDERS = {'administrative-notice': notice, 'academic-short-report': academic, 'office-minutes': office}


def create_templates(destination):
    folder = Path(destination)
    folder.mkdir(parents=True, exist_ok=True)
    manifest = []
    for name, builder in BUILDERS.items():
        doc, config, values = builder()
        template = folder / (name + '.docx')
        doc.save(template)
        for suffix, data in [('rules', config), ('values', values)]:
            (folder / f'{name}.{suffix}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        fill_template(template, folder / (name + '.filled.docx'), values)
        manifest.append({'id': name, 'template': template.name, 'profile': config['profile'],
                         'origin': 'project-authored', 'version': 1,
                         'sha256': hashlib.sha256(template.read_bytes()).hexdigest(),
                         'source': LEGAL_SOURCE if name == 'administrative-notice' else 'Original project structure',
                         'scope': config['source'], 'external_template_copied': False,
                         'status': 'generated; visual verification is recorded separately',
                         'limitations': 'Starter with single-line slots. Adapt long content and organization-specific requirements; not certified compliance.'})
    (folder / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', default='artifacts/template-suite')
    args = parser.parse_args()
    print(json.dumps(create_templates(args.output_dir), ensure_ascii=False, indent=2))
