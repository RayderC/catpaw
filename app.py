from flask import Flask, render_template, send_file, current_app
import os
from werkzeug.exceptions import NotFound

app = Flask(__name__, template_folder='html')

@app.route('/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def index(req_path):
    BASE_DIR = '/'  # Set your base directory here

    # Join the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return current_app.make_response(
            current_app.handle_user_exception(NotFound()))

    # Check if path is a file and serve it
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run()
