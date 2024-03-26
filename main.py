import thread_manager

from flask import Flask, render_template

# thread_manager.start()

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def home_page():
    return render_template('index.html', title="Home")


@app.route('/database/manga')
def database_manga():
    return render_template("manga_db.html", title="Manga db")

@app.route('/manga.read')
def read_manga():
    return render_template("read_manga.html", title="Manga Reader")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Ends the program pretty much
thread_manager.stop()
