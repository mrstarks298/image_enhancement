from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image, ImageDraw, ImageFont
import cv2

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the UPLOAD_FOLDER exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to rotate image
def rotate_image(image_path, angle):
    try:
        original_image = Image.open(image_path)
        rotated_image = original_image.rotate(angle)
        rotated_image_path = os.path.join(UPLOAD_FOLDER, 'rotated_' + secure_filename(image_path))
        rotated_image.save(rotated_image_path)
        return rotated_image_path
    except Exception as e:
        print(f"Error rotating image: {str(e)}")
        return None

# Function to crop image
def crop_image(image_path, x, y, w, h):
    try:
        original_image = Image.open(image_path)
        cropped_image = original_image.crop((x, y, x+w, y+h))
        cropped_image_path = os.path.join(UPLOAD_FOLDER, 'cropped_' + secure_filename(image_path))
        cropped_image.save(cropped_image_path)
        return cropped_image_path
    except Exception as e:
        print(f"Error cropping image: {str(e)}")
        return None

# Function to blur image
def blur_image(image_path, amount):
    try:
        original_image = cv2.imread(image_path)
        blurred_image = cv2.GaussianBlur(original_image, (amount, amount), 0)
        blurred_image_path = os.path.join(UPLOAD_FOLDER, 'blurred_' + secure_filename(image_path))
        cv2.imwrite(blurred_image_path, blurred_image)
        return blurred_image_path
    except Exception as e:
        print(f"Error blurring image: {str(e)}")
        return None

# Function to add text to image
def add_text_to_image(image_path, text, position):
    try:
        original_image = Image.open(image_path)
        draw = ImageDraw.Draw(original_image)
        font = ImageFont.truetype("arial.ttf", 20)  # You can change the font and size here
        draw.text(position, text, fill="white", font=font)
        text_image_path = os.path.join(UPLOAD_FOLDER, 'text_' + secure_filename(image_path))
        original_image.save(text_image_path)
        return text_image_path
    except Exception as e:
        print(f"Error adding text to image: {str(e)}")
        return None

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    image_path = None
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('File uploaded successfully')
            image_path = url_for('static', filename='uploads/' + filename)  # Adjust this line
    return render_template('index.html', filename=filename, image_path=image_path)


@app.route('/enhance/<filename>', methods=['POST'])
def enhance_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):  # Check if the file exists
        operation = request.form.get('operation')
        if operation == 'rotate':
            angle = int(request.form.get('angle', 0))
            rotated_image_path = rotate_image(filepath, angle)
            if rotated_image_path:
                return redirect(url_for('index', filename=os.path.basename(rotated_image_path)))
            else:
                flash('Failed to rotate image')
        elif operation == 'crop':
            x = int(request.form.get('x', 0))
            y = int(request.form.get('y', 0))
            w = int(request.form.get('w', 0))
            h = int(request.form.get('h', 0))
            cropped_image_path = crop_image(filepath, x, y, w, h)
            if cropped_image_path:
                return redirect(url_for('index', filename=os.path.basename(cropped_image_path)))
            else:
                flash('Failed to crop image')
        elif operation == 'blur':
            amount = int(request.form.get('amount', 5))
            blurred_image_path = blur_image(filepath, amount)
            if blurred_image_path:
                return redirect(url_for('index', filename=os.path.basename(blurred_image_path)))
            else:
                flash('Failed to blur image')
        elif operation == 'add_text':
            text = request.form.get('text', '')
            position_x = int(request.form.get('position_x', 0))
            position_y = int(request.form.get('position_y', 0))
            text_image_path = add_text_to_image(filepath, text, (position_x, position_y))
            if text_image_path:
                return redirect(url_for('index', filename=os.path.basename(text_image_path)))
            else:
                flash('Failed to add text to image')
        else:
            flash('Invalid operation')
    else:
        flash('File not found')

    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
