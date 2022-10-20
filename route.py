from flask import Flask

app = Flask("__main__")

@app.route("/home1")
def home1():
    return "welcome to home page of 1 "
 

@app.route("/home")
def home2():
    return "welcome to home page of HOME" 

@app.route("/")
def index():
    return 'This is index'

@app.route('/home')
@app.route("/home/<username>")
def home(username):
    return "welcome to home page of :" + str(username)

@app.route('/blog1')
def blog1():
    msg = "This is a Blog"
    return msg 

# @app.route('/blog')
@app.route("/blog/<blog_no>")
def blog(blog_no):
    return "This is blog Number :" + str(blog_no)

# app.add_url_rule('/get_blogs','blog',blog)

if __name__ == '__main__':
  app.run(debug=True)


