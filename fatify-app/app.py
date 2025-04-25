
from flask import Flask, render_template, request
import os
from fatify import simulate_fatify
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            filename = f"{uuid.uuid4().hex}.jpg"
            original_path = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(original_path)

            fat_img = simulate_fatify(original_path)
            output_path = os.path.join(UPLOAD_FOLDER, f"fat_{filename}")
            fat_img.save(output_path)

            return render_template('index.html', original=original_path, result=output_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
