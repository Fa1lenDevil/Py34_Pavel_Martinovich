import sqlite3
from flask import Flask, render_template, request, redirect, url_for


def get_db_connection():
    database = sqlite3.connect('database.db')
    database.row_factory = sqlite3.Row
    return database

def get_post(id):
    database = get_db_connection()
    post = database.execute("SELECT * FROM posts WHERE id = ?", (id, )).fetchone()
    return post


app = Flask(__name__)


@app.route('/')
def index():
    database = get_db_connection()
    posts = database.execute('SELECT * FROM posts ORDER BY posts.dateOfRegistration DESC').fetchall()
    return render_template('index.html', posts=posts)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('newPost.html')

    elif request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        database = get_db_connection()
        database.execute("INSERT INTO posts (username, password, dateOfRegistration) VALUES (?, ?, ?)", (author, title, content))
        database.commit()
        database.close()
        return redirect(url_for('index'))

@app.route('/post-<int:id>/')
def post(id):
    post = get_post(id)
    return render_template('detailPost.html', post=post)



if __name__ == "__main__":
    app.config['TIMEZONE'] = 'UTC-4'
    app.run(debug=True)