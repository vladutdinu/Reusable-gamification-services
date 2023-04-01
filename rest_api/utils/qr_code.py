import segno
import io
import base64

def generate_qr_code(text):
    qr = segno.make_qr(text)
    buffer = io.BytesIO()
    qr.save(buffer, kind='png')
    qr_code = 'data: image/png;base64, '+base64.b64encode(buffer.getvalue()).decode('utf-8')
    return str(qr_code)