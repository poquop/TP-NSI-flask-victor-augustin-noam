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
('Bugatti Veyron 16.4', '3'),
('Bugatti Chiron', '3'),
('BMW M4 Competition', '10'),
('BMW M6 Coupé', '10'),
('Corvette Z06', '4'),
('Corvette C6', '4'),
('McLaren 765LT Spider', '5'),
('Mclaren 620R', '5'),
('Lamborghini Urus', '11'),
('Lamborghini Gallardo Superleggera', '11'),
('Mercedes GLE', '9'),
('Mercedes classe C', '9'), 
('Porshe 911', '8'),
('Porshe Taycan', '8'),
('Nissan 370Z', '13'),
('Nissan Juke', '13'),
('Toyota RAV4', '12'),
('Toyota Corolla', '12'),
('Alfa Romeo Giulia', '1'),
('Alfa Romeo Stelvio', '1'),
('Ferrari SP48 Unica', '7'),
('Ferrari SF90 Stradale', '7'),
('Aston Martin DB11', '2'), 
('Aston Martin Vulcan', '2'),
('Pagani Huayra Roadster BC', '6'),
('Pagani Zonda', '6'),
('Koenigsegg Jesko Absolut', '14'),
('Koenigsegg Gemera', '14')
;
