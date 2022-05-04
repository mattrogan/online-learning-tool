import sqlite3
import sqlite3
from flask import Flask, redirect, render_template, url_for, request

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
   
   # Get comments for the post
   comments = conn.execute("SELECT * FROM Comments WHERE PostID=? ORDER BY DatePosted DESC",(post_id,)).fetchall()
   
   return render_template("post.html", post=post, comments=comments)

# Code to add new post 
@app.route("/new-post")
def new_post():
   conn = get_db_connection()
   return render_template("new-post.html", conn=conn)

# Function to add new posts into database
@app.route("/addpost", methods=["POST","GET"])
def addpost():
   if request.method == "POST":
      try:
         # Get data from form
         name = request.form["name"]
         qtitle = request.form["qtitle"]
         qdesc = request.form["qdesc"]
         
         print(f"""Data received from form:
               name={name},
               qtitle={qtitle}
               qdesc={qdesc}""")
         
         print("Establishing connection...")
         conn = get_db_connection()
         
         print("Getting cursor")
         cursor = conn.cursor()
         
         print("Executing SQL...")
         cursor.execute("INSERT INTO Posts (Author, QuestionTitle, QuestionDescription) VALUES (?,?,?)", (name,qtitle,qdesc))
         
         print("Committing changes")
         conn.commit()
         status_msg = "Post successfully added"
      except:
         conn.rollback()
         status_msg = "Error in adding post - try again"
      finally:
         return render_template("addpost.html", status_msg=status_msg)
         
         
      

if __name__ == "__main__":
   app.run(debug=True)