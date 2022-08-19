from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_content = response.json()

all_post = []
for posts in blog_content:
    post = Post(posts["id"], posts["title"], posts["subtitle"], posts["body"])
    all_post.append(post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=blog_content)


@app.route("/post/<int:num>")
def posts(num):
    for post in all_post:
        if post.id == num:
            requested_post = post
        return render_template("post.html", post=requested_post)

# alternative without using the post class
# @app.route("/post/<int:num>")
# def posts(num):
#     for post in blog_content:
#         if post["id"] == num:
#             return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
