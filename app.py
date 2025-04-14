from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)

DATABASE = 'data/data.db'
PROF_PASSWORD = "secret123" # A changer peut-être '-'

# Pour les deux fonctions suivantes, j'ai copié collé le code d'exemple du prof
# Fonction générique pour exécuter une requête SELECT et récupérer les résultats sous forme de liste de dictionnaires
def fetch_all(query, params=()):
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = [dict(row) for row in cursor.fetchall()]  
    conn.close()
    return results

# Fonction générique pour exécuter une requête INSERT, UPDATE ou DELETE
def execute_query(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()  
    last_id = cursor.lastrowid  
    conn.close()
    return last_id

# Pour le reste du code, j'ai codé en fonction des besoins que j'ai pensé utile par rapport au cahier des charges.
def get_marques():
    return fetch_all("SELECT idMarque, Nom, Pays FROM Marque")

def get_modeles():
    return fetch_all("""SELECT mo.idModele, mo.Nom, mo.idModele 
                          FROM Modele mo, Marque ma
                           AND ma.idModele == ma.idModele """")
############# A continuer...


menu_links = [
    {"name": "Accueil", "url": "/"},
    {"name": "Concessions", "url": "/concessions"},
    {"name": "À propos", "url": "/about"},
    {"name": "rajouter un lien", "url" : "/page_pour_add"}
]

links = []
@app.route('/page_pour_add')
def ajoutage():
    return render_template('page_pour_add.html', menu_links=menu_links)

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


