--
--(C'est pas fini, je viens de commencer.)
--
DROP TABLE IF EXISTS Marque;
DROP TABLE IF EXISTS Model;
DROP TABLE IF EXISTS Voiture;

CREATE TABLE Marque(
   idMarque INTEGER PRIMARY KEY AUTOINCREMENT,
   Nom VARCHAR(40),
   Nationalite VARCHAR(40)
);

CREATE TABLE Model(
    idModel INTEGER PRIMARY KEY AUTOINCREMENT,
    

);
  
CREATE TABLE Voiture(
    idVoiture INTEGER PRIMARY KEY AUTOINCREMENT,
    CONSTRAINT pk_marque PRIMARY KEY (idMarque),
    CONSTRAINT pk_model PRIMARY KEY (idModel)
);
