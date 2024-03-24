# from flask import Flask, render_template, request
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def load_image(self, file):
#        if file:
#         # Read the image file from the uploaded file object
#         image_bytes = file.read()
#         # Open the image from the bytes
#         self.image = Image.open(BytesIO(image_bytes))
#         self.image.thumbnail((5000,5000))


#     def convert_to_grayscale(self):
#         if self.image:
#             self.image = ImageOps.grayscale(self.image)

#     def rotate_image(self):
#         if self.image:
#             self.image = self.image.rotate(-90)

#     def blur_image(self):
#         if self.image:
#             self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2))

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 20)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None

# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "load_image" in request.form:
#             file = request.files["image"]
#             if file:
#                 image_processor.load_image(file)
#         elif "grayscale" in request.form:
#             image_processor.convert_to_grayscale()
#         elif "rotate" in request.form:
#             image_processor.rotate_image()
#         elif "blur" in request.form:
#             image_processor.blur_image()
#         elif "write_text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "crop" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#     return render_template("index.html", image_data=image_processor.get_image_data())

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def convert_to_grayscale(self):
#         if self.image:
#             self.image = ImageOps.grayscale(self.image)

#     def rotate_image(self):
#         if self.image:
#             self.image = self.image.rotate(-90)

#     def blur_image(self):
#         if self.image:
#             self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2))

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 20)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None

# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             file = request.files["image"]
#             if file:
#                 # Read the image file from the uploaded file object
#                 image_bytes = file.read()
#                 # Open the image from the bytes
#                 image_processor.image = Image.open(BytesIO(image_bytes))
#                 image_processor.image.thumbnail((5000,5000))
#         elif "grayscale" in request.form:
#             image_processor.convert_to_grayscale()
#         elif "rotate" in request.form:
#             image_processor.rotate_image()
#         elif "blur" in request.form:
#             image_processor.blur_image()
#         elif "write_text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "crop" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#     return render_template("index.html", image_data=image_processor.get_image_data())

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def convert_to_grayscale(self):
#         if self.image:
#             self.image = ImageOps.grayscale(self.image)

#     def rotate_image(self):
#         if self.image:
#             self.image = self.image.rotate(-90)

#     def blur_image(self, blur_amount):
#         if self.image:
#             self.image = self.image.filter(ImageFilter.GaussianBlur(radius=blur_amount))

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 20)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None

# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             file = request.files["image"]
#             if file:
#                 # Read the image file from the uploaded file object
#                 image_bytes = file.read()
#                 # Open the image from the bytes
#                 image_processor.image = Image.open(BytesIO(image_bytes))
#                 image_processor.image.thumbnail((5000,5000))
#         elif "grayscale" in request.form:
#             image_processor.convert_to_grayscale()
#         elif "rotate" in request.form:
#             image_processor.rotate_image()
#         elif "blur" in request.form:
#             blur_amount = int(request.form["blur_amount"])
#             image_processor.blur_image(blur_amount)
#         elif "write_text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "crop" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#     return render_template("index.html", image_data=image_processor.get_image_data())

# @app.route("/rotate_image", methods=["POST"])
# def rotate_image():
#     image_processor.rotate_image()
#     return jsonify({"image_data": image_processor.get_image_data()})

# if __name__ == "__main__":
#     app.run(debug=True)
#i have add crop 
# from flask import Flask, render_template, request, jsonify
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def convert_to_grayscale(self):
#         if self.image:
#             self.image = ImageOps.grayscale(self.image)

#     def rotate_image(self):
#         if self.image:
#             self.image = self.image.rotate(-90)

#     def blur_image(self, blur_type):
#         if self.image:
#             if blur_type == 'original':
#                 pass  # Do nothing, return original image
#             elif blur_type == 'gaussian':
#                 self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2))
#             elif blur_type == 'box':
#                 self.image = self.image.filter(ImageFilter.BoxBlur(radius=2))
#             elif blur_type == 'median':
#                 self.image = self.image.filter(ImageFilter.MedianFilter(size=3))
#             elif blur_type == 'contour':
#                 self.image = self.image.filter(ImageFilter.CONTOUR)
#             elif blur_type == 'detail':
#                 self.image = self.image.filter(ImageFilter.DETAIL)
#             elif blur_type == 'edge_enhance':
#                 self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
#             elif blur_type == 'emboss':
#                 self.image = self.image.filter(ImageFilter.EMBOSS)

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 20)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None

# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             file = request.files["image"]
#             if file:
#                 # Read the image file from the uploaded file object
#                 image_bytes = file.read()
#                 # Open the image from the bytes
#                 image_processor.image = Image.open(BytesIO(image_bytes))
#                 image_processor.image.thumbnail((5000,5000))
#         elif "grayscale" in request.form:
#             image_processor.convert_to_grayscale()
#         elif "rotate" in request.form:
#             image_processor.rotate_image()
#         elif "blur" in request.form:
#             blur_type = request.form["blur_type"]
#             image_processor.blur_image(blur_type)
#         elif "write_text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "crop" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#     return render_template("index.html", image_data=image_processor.get_image_data())

# @app.route("/rotate_image", methods=["POST"])
# def rotate_image():
#     image_processor.rotate_image()
#     return jsonify({"image_data": image_processor.get_image_data()})

# if __name__ == "__main__":
#     app.run(debug=True)
#modification to add crop and bliur 
# from flask import Flask, render_template, request, jsonify
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def apply_blur(self, blur_type):
#         if self.image:
#             if blur_type == 'gaussian':
#                 self.image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
#             elif blur_type == 'box':
#                 self.image = self.image.filter(ImageFilter.BoxBlur(radius=2))
#             elif blur_type == 'motion':
#                 self.image = self.image.filter(ImageFilter.MotionBlur(angle=45, radius=10))
#             # Add more cases for other blur effects

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 30)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None



# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             file = request.files["image"]
#             if file:
#                 # Read the image file from the uploaded file object
#                 image_bytes = file.read()
#                 # Open the image from the bytes
#                 image_processor.image = Image.open(BytesIO(image_bytes))
#         elif "blur_type" in request.form:
#             blur_type = request.form["blur_type"]
#             image_processor.apply_blur(blur_type)
#         elif "text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "x1" in request.form and "y1" in request.form and "x2" in request.form and "y2" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#     return render_template("index.html", image_data=image_processor.get_image_data())

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
# from io import BytesIO
# import base64

# app = Flask(__name__)

# class ImageProcessor:
#     def __init__(self):
#         self.image = None

#     def apply_blur(self, blur_type):
#         if self.image:
#             if blur_type == 'gaussian':
#                 self.image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
#             elif blur_type == 'box':
#                 self.image = self.image.filter(ImageFilter.BoxBlur(radius=2))
#             elif blur_type == 'motion':
#                 self.image = self.image.filter(ImageFilter.MotionBlur(angle=45, radius=10))
#             # Add more cases for other blur effects

#     def write_text_on_image(self, text):
#         if self.image and text:
#             draw = ImageDraw.Draw(self.image)
#             font = ImageFont.truetype("arial.ttf", 30)
#             color = "white"
#             text_width, text_height = draw.textsize(text, font=font)
#             x = (self.image.width - text_width) // 2
#             y = (self.image.height - text_height) // 2
#             draw.text((x, y), text, fill=color, font=font)

#     def crop_image(self, x1, y1, x2, y2):
#         if self.image:
#             self.image = self.image.crop((x1, y1, x2, y2))

#     def rotate_image(self):
#         if self.image:
#             self.image = self.image.rotate(-90)

#     def get_image_data(self):
#         if self.image:
#             buffered = BytesIO()
#             self.image.save(buffered, format="JPEG")
#             return base64.b64encode(buffered.getvalue()).decode("utf-8")
#         return None

# image_processor = ImageProcessor()

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         if "image" in request.files:
#             file = request.files["image"]
#             if file:
#                 # Read the image file from the uploaded file object
#                 image_bytes = file.read()
#                 # Open the image from the bytes
#                 image_processor.image = Image.open(BytesIO(image_bytes))
#         elif "blur_type" in request.form:
#             blur_type = request.form["blur_type"]
#             image_processor.apply_blur(blur_type)
#         elif "text" in request.form:
#             text = request.form["text"]
#             image_processor.write_text_on_image(text)
#         elif "x1" in request.form and "y1" in request.form and "x2" in request.form and "y2" in request.form:
#             x1 = int(request.form["x1"])
#             y1 = int(request.form["y1"])
#             x2 = int(request.form["x2"])
#             y2 = int(request.form["y2"])
#             image_processor.crop_image(x1, y1, x2, y2)
#         elif "rotate" in request.form:
#             image_processor.rotate_image()
#     return render_template("index.html", image_data=image_processor.get_image_data())

# @app.route("/rotate_image", methods=["POST"])
# def rotate_image():
#     image_processor.rotate_image()
#     return jsonify({"image_data": image_processor.get_image_data()})

# if __name__ == "__main__":
#      app.run(debug=True)
# Add necessary imports
# from flask import Flask, flash, request, redirect, url_for, render_template
# from werkzeug.utils import secure_filename
# import os
# import cv2

# # Initialize Flask app
# app = Flask(__name__)
# app.secret_key = 'super_secret_key'

# # Configuration
# UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# # Ensure the UPLOAD_FOLDER exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Helper functions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def crop_image(image, x, y, w, h):
#     return image[y:y+h, x:x+w]

# def blur_image(image, amount):
#     return cv2.GaussianBlur(image, (amount, amount), 0)

# def rotate_image(image, angle):
#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated_image = cv2.warpAffine(image, M, (w, h))
#     return rotated_image

# # Routes
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     filename = None
#     image_path = None
#     if request.method == 'POST' and 'file' in request.files:
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
#             flash('File uploaded successfully')
#             image_path = url_for('static', filename='uploads/' + filename)

#     return render_template('index.html', filename=filename, image_path=image_path)


# @app.route('/enhance/<filename>', methods=['POST'])
# def enhance_image(filename):
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(filepath):  # Check if the file exists
#         image = cv2.imread(filepath)
#         if image is not None:  # Check if the image is loaded successfully
#             operation = request.form.get('operation')
#             if operation == 'crop':
#                 # Process crop operation...
#                 x = int(request.form.get('x', 0))
#                 y = int(request.form.get('y', 0))
#                 w = int(request.form.get('w', image.shape[1]))
#                 h = int(request.form.get('h', image.shape[0]))
#                 image = crop_image(image, x, y, w, h)
#             elif operation == 'blur':
#                 # Process blur operation...
#                 amount = int(request.form.get('amount', 5))
#                 image = blur_image(image, amount)
#             elif operation == 'rotate':
#                 # Process rotate operation...
#                 angle = int(request.form.get('angle', 0))
#                 image = rotate_image(image, angle)
#             else:
#                 flash('Invalid operation')

#             cv2.imwrite(filepath, image)  # Save the modified image

#         else:
#             flash('Failed to load image')
#     else:
#         flash('File not found')

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, flash, request, redirect, url_for, render_template
# from werkzeug.utils import secure_filename
# import os
# import cv2

# # Initialize Flask app
# app = Flask(__name__)
# app.secret_key = 'super_secret_key'

# # Configuration
# UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# # Ensure the UPLOAD_FOLDER exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Helper functions
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def crop_image(image, x, y, w, h):
#     return image[y:y+h, x:x+w]

# def blur_image(image, amount):
#     return cv2.GaussianBlur(image, (amount, amount), 0)

# def rotate_image(image, angle):
#     (h, w) = image.shape[:2]
#     center = (w // 2, h // 2)
#     M = cv2.getRotationMatrix2D(center, angle, 1.0)
#     rotated_image = cv2.warpAffine(image, M, (w, h))
#     return rotated_image

# # Routes
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     filename = None
#     image_path = None
#     if request.method == 'POST' and 'file' in request.files:
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(filepath)
#             flash('File uploaded successfully')
#             image_path = url_for('static', filename='uploads/' + filename)

#     return render_template('index.html', filename=filename, image_path=image_path)



# @app.route('/enhance/<filename>', methods=['POST'])
# def enhance_image(filename):
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     if os.path.exists(filepath):  # Check if the file exists
#         image = cv2.imread(filepath)
#         if image is not None:  # Check if the image is loaded successfully
#             operation = request.form.get('operation')
#             if operation == 'crop':
#                 # Process crop operation...
#                 x = int(request.form.get('x', 0))
#                 y = int(request.form.get('y', 0))
#                 w = int(request.form.get('w', image.shape[1]))
#                 h = int(request.form.get('h', image.shape[0]))
#                 image = crop_image(image, x, y, w, h)
#             elif operation == 'blur':
#                 # Process blur operation...
#                 amount = int(request.form.get('amount', 5))
#                 image = blur_image(image, amount)
#             elif operation == 'rotate':
#                 # Process rotate operation...
#                 angle = int(request.form.get('angle', 0))
#                 image = rotate_image(image, angle)
#             else:
#                 flash('Invalid operation')

#             cv2.imwrite(filepath, image)  # Save the modified image

#         else:
#             flash('Failed to load image')
#     else:Z-
#         flash('File not found')

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
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




