from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Manish Singh',
        'title': 'My Page1',
        'content': 'content abc',
        'date_posted': '21 July 2024'
    },
    {
       'author': 'Sneha Bangari',
        'title': 'My Page2',
        'content': 'content def',
        'date_posted': '21 July 2024' 
    }
]

@app.route("/")
@app.route("/home") # both these routes land on the same page
def home():
    return render_template('index.html', posts=posts)

# about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__=='__main__':
    app.run(debug=True)
