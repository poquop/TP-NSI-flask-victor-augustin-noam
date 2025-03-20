from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)

menu_links = [
    {"name": "Accueil", "url": "/"},
    {"name": "Concessions", "url": "/concessions"},
    {"name": "À propos", "url": "/about"},
    {"name": "rajouter un lien", "url" : "/ajoutage"}
]

links = []
@app.route('/ajoutage')
def ajoutage():
    return render_template('page_pour_ajouter', menu_links[3])

@app.route('/')
def index():
    return render_template('index.html', menu_links=menu_links)

@app.route('/concessions')
def concessions():
    
    return render_template('concessions.html', menu_links=menu_links)

@app.route('/about')
def about():
    return render_template('about.html', menu_links=menu_links)


@app.route('/')
def index2():
    return render_template('index.html')

@app.route('/links', methods=['GET'])
def get_links():
    return jsonify(links)

@app.route('/add_link', methods=['POST'])
def add_link():
    data = request.json
    links.append({'name': data['name'], 'url': data['url']})
    return jsonify({'message': 'Lien ajouté', 'links': links}), 201

@app.route('/edit_link/<int:index>', methods=['PUT'])
def edit_link(index):
    if 0 <= index < len(links):
        data = request.json
        links[index] = {'name': data['name'], 'url': data['url']}
        return jsonify({'message': 'Lien modifié', 'links': links}), 200
    return jsonify({'error': 'Index invalide'}), 400

@app.route('/delete_link/<int:index>', methods=['DELETE'])
def delete_link(index):
    if 0 <= index < len(links):
        del links[index]
        return jsonify({'message': 'Lien supprimé', 'links': links}), 200
    return jsonify({'error': 'Index invalide'}), 400

if __name__ == '__main__':
    app.run(debug=True)


