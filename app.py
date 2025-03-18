from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

menu_links = [
    {"name": "Accueil", "url": "/"},
    {"name": "Concessions", "url": "/concessions"},
    {"name": "À propos", "url": "/about"}
]



@app.route('/')
def index():
    return render_template('index.html', menu_links=menu_links)

@app.route('/concessions')
def concessions():
    
    return render_template('concessions.html', menu_links=menu_links)

@app.route('/about')
def about():
    return render_template('about.html', menu_links=menu_links)

if __name__ == '__main__':
    app.run(debug=True)
