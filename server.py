import os

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from img_to_hex import img_to_hex

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["SECRET_KEY"] = os.urandom(100)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.files)
        if "file" not in request.files:
            flash("001 No file Chosen, try again.")
            return redirect(url_for("home"))
        file = request.files["file"]
        file_name = file.filename
        if file_name == "":
            flash("002 No file chosen, try again")
            return redirect(url_for("home"))
        if file and allowed_file(file_name):
            sec_filename = secure_filename(file_name)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], sec_filename)
            file.save(file_path)
            hex_colours = img_to_hex(file_path)
            return render_template("index.html", colours=hex_colours)
    return render_template("index.html")


if "__main__" == __name__:
    app.run(debug=True, port=4455)
