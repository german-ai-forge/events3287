from flask import Flask, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """Generate a QR code and provide a download link."""
    data = request.json.get('data')
    if not data:
        return {"error": "Data for QR code is missing"}, 400

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Save QR code to a temporary file
    file_path = "ticket_qr.png"
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    # Provide the download link
    return {
        "message": "QR Code generated successfully.",
        "download_link": f"/download_qr"
    }

@app.route('/download_qr', methods=['GET'])
def download_qr():
    """Serve the QR code image as a downloadable file."""
    file_path = "ticket_qr.png"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return {"error": "QR Code file not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)
