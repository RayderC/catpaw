import db_manager
import thread_manager

from flask import Flask, render_template

thread_manager.start()

app = Flask(__name__)
app.secret_key = "secret key"

db_manager.update("db/manga_downloads.db", "manga", "name", "name", 1)
db_manager.list_all("db/manga_downloads.db", "manga")

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/database/manga')
def database_manga():
    return render_template("manga_db.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

# Ends the program pretty much
thread_manager.stop()
