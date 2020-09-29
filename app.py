from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/videos")
def video():
    return render_template('video.html')
    
@app.route("/blog_post")
def blog():
    return render_template('blog.html')


@app.route("/about_us")
def About():
    return render_template('about.html')

@app.route("/contact_us")
def contact():
    return render_template('contact.html')

app.run(debug=True)

