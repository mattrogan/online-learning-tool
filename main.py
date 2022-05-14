import sqlite3
import sqlite3
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

def get_db_connection():
   conn = sqlite3.connect("database.db")
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
   posts = conn.execute("""SELECT Posts.*, COUNT(Comments.PostID) AS NumComments
                           FROM Posts
                           LEFT JOIN Comments
                           ON (Posts.PostID == Comments.PostID)
                           GROUP BY Posts.PostID
                           ORDER BY DatePosted DESC
   """).fetchall()
   conn.close()
   return render_template("discussion-forum.html", posts=posts)

# Code for an individual post
@app.route("/post<post_id>")
def discussion_forum_post(post_id):
   # Establish connection with database
   conn = get_db_connection()
   post = conn.execute("SELECT * FROM Posts WHERE PostID=?",(post_id,)).fetchone()
   
   # Get comments for the post
   comments = conn.execute("SELECT * FROM Comments WHERE PostID=? ORDER BY DatePosted ASC",(post_id,)).fetchall()
   
   return render_template("post.html", post=post, comments=comments)

# Code to add new post 
@app.route("/new-post")
def new_post():
   conn = get_db_connection()
   return render_template("new-post.html", conn=conn)

# Function to add new posts into database
@app.route("/addpost", methods=["POST", "GET"])
def addpost():
   if request.method == "POST":
      try:
         # Get data from form
         name = request.form["name"]
         qtitle = request.form["qtitle"]
         qdesc = request.form["qdesc"]
         
         conn = get_db_connection()
         cursor = conn.cursor()
         cursor.execute("INSERT INTO Posts (Author, QuestionTitle, QuestionDescription) VALUES (?,?,?)", (name,qtitle,qdesc))

         conn.commit()
         status_msg = "Post successfully added"

      except:
         conn.rollback()
         status_msg = "Error in adding post - please try again"
      finally:
         return render_template("addpost.html", status_msg=status_msg)
         
@app.route("/addcomment", methods=["POST", "GET"])
def addcomment():
   if request.method == "POST":
      try:
         # Get data from the reply form
         post_id = request.form["post_id"]
         name = request.form["name"]
         rtitle = request.form["rtitle"]
         rdesc = request.form["rdesc"]

         conn = get_db_connection()
         cursor = conn.cursor()

         cursor.execute("INSERT INTO Comments (Author, ReplyTitle, ReplyDesc, PostID) VALUES (?,?,?,?)", (name,rtitle,rdesc,post_id))

         conn.commit()
         status_msg = "Comment added successfully"
      except:
         status_msg = "Error in adding comment - please try again"
      finally:
         return render_template("addcomment.html", status_msg=status_msg)

# Page to show content for an individual topic
@app.route("/topic<topic_no>")
def topic(topic_no):
   print("Establishing database connection")
   conn = get_db_connection()

   topic_details = conn.execute("SELECT * FROM Topics WHERE TopicID=?",(topic_no,)).fetchone()

   # Ensure "next" and "previous" topics wrap around to avoid errors
   if int(topic_no) == 1:
      prev_topic = 7
      next_topic = 2
   elif int(topic_no) == 7:
      next_topic = 1
      prev_topic = 6
   else:
      next_topic = int(topic_no)+1
      prev_topic = int(topic_no)-1

   return render_template("topic.html", topic_details=topic_details, prev_topic=prev_topic, next_topic=next_topic)


if __name__ == "__main__":
   app.run(debug=True)