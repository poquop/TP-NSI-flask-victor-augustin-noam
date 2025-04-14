DROP TABLE IF EXISTS Marque;
DROP TABLE IF EXISTS Modele; --Voitures


CREATE TABLE Marque(
   idMarque INTEGER PRIMARY KEY AUTOINCREMENT,
   Nom VARCHAR(40),
   Pays VARCHAR(40)
);

CREATE TABLE Modele(
    idModele INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom VARCHAR(80),
    idMarque INT,
    CONSTRAINT fk_marque FOREIGN KEY (idMarque) REFERENCES Marque(idMarque)
);

INSERT INTO Marque(Nom, Pays) VALUES
('Alfa Romeo', 'Italie'),
('Aston Martin', 'Angleterre'),
('Bugatti', 'France'),
('Corvette', 'Etats-Unis'),
('Mclaren', 'Angleterre'),
('Pagani', 'Italie'),
('Ferrari', 'Italie'),
('Porshe', 'Allemagne'),
('Mercedes', 'Allemagne'),
('BMW', 'Allemagne'),
('Lamborghini', 'Italie'),
('Toyota', 'Japon'),
('Nissan', 'Japon'),
('Koenigsegg', 'Suède')
;

INSERT INTO Modele(Nom, idMarque) VALUES
('', '')
;
