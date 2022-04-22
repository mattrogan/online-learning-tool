from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
   return render_template("discussion-forum.html")

if __name__ == "__main__":
   app.run(debug=True)