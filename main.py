import thread_manager

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

# thread_manager.start()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# sqlite
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Flask app routes
@app.route('/')
def home_page():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', title="Home", posts=posts)


@app.route('/database/manga', methods=["POST", "GET"])
def database_manga():
    dbfile = request.form.get("dbfile")
    dbtable = request.form.get("dbtable")
    name = request.form.get("name")
    link = request.form.get("link")

    print(dbfile, dbtable, name, link)

    return render_template("manga_db.html", title="Manga db")

@app.route('/manga.read')
def read_manga():
    return render_template("read_manga.html", title="Manga Reader")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# Ends the program pretty much
# thread_manager.stop()
