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
   posts = conn.execute("SELECT * FROM Posts").fetchall()
   conn.close()
   return render_template("discussion-forum.html", posts=posts)

@app.route("/discussion-forum/post/<id>")
def display_post(): # Function to display an individual post and its comments
   pass

# Code for an individual post
@app.route("/discussion-forum/<postNumber>")
def discussion_forum_post(postNumber):
   return render_template("discussion-forum-post.html", content=postNumber)

if __name__ == "__main__":
   app.run(debug=True)