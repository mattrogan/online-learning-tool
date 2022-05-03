import sqlite3
import sqlite3
from flask import Flask, redirect, render_template

app = Flask(__name__)

def get_db_connection():
   conn = sqlite3.connect("forum_posts.db")
   conn.row_factory = sqlite3.Row
   return conn

@app.route('/')
def default():
   return redirect("home")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/learning-materials")
def learning_materials():
   return render_template("learning-materials.html")

@app.route("/practicals")
def practicals():
   return render_template("practicals.html")

@app.route("/discussion-forum")
def discussion_forum():
   # Establish connection with database
   conn = get_db_connection()
   posts = conn.execute("SELECT * FROM Posts ORDER BY DatePosted DESC").fetchall()
   conn.close()
   return render_template("discussion-forum.html", posts=posts)

# Code for an individual post
@app.route("/post<post_id>")
def discussion_forum_post(post_id):
   # Establish connection with database
   conn = get_db_connection()
   post = conn.execute("SELECT * FROM Posts WHERE PostID=?",(post_id,)).fetchone()
   return render_template("post.html", post=post)

# Code to add new post 
@app.route("/new-post")
def new_post():
   conn = get_db_connection()
   return render_template("new-post.html", conn=conn)

if __name__ == "__main__":
   app.run(debug=True)