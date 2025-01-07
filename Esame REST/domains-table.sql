begin transaction;
-- Creazione dei domini

-- Create custom types and domains
CREATE TYPE Stato AS ENUM('LIBERO', 'OCCUPATO');
CREATE TYPE TipoAf AS ENUM('PARZIALE', 'TOTALE');
CREATE DOMAIN PosInteger AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN Civico AS VARCHAR(5) CHECK (VALUE ~ '[0-9]+(/[a-z]+)?');
CREATE DOMAIN Denaro AS REAL CHECK (VALUE >= 0);

-- Table: filiali
CREATE TABLE filiali (
    partita_iva VARCHAR(16) NOT NULL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    indirizzo_sede VARCHAR(255) NOT NULL,
    civico Civico NOT NULL,
    telefono VARCHAR(20) NOT NULL
);

-- Table: case_in_vendita
CREATE TABLE case_in_vendita (
    catastale VARCHAR(50) NOT NULL PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    numero_civico Civico NOT NULL,
    piano PosInteger NOT NULL,
    metri PosInteger NOT NULL,
    vani PosInteger NOT NULL,
    prezzo Denaro NOT NULL,
    stato Stato NOT NULL,
    filiale_proponente VARCHAR(16) NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva) deferrable
);

-- Table: case_in_affitto
CREATE TABLE case_in_affitto (
    catastale VARCHAR(50) NOT NULL PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    civico Civico NOT NULL,
    tipo_affitto TipoAf NOT NULL,
    bagno_personale BOOLEAN NOT NULL,
    prezzo_mensile Denaro NOT NULL,
    filiale_proponente VARCHAR(16) NOT NULL,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva) deferrable
);

-- Table: vendite_casa
CREATE TABLE vendite_casa (
    catastale VARCHAR(50) NOT NULL,
    data_vendita DATE NOT NULL,
    filiale_proponente VARCHAR(16) NOT NULL,
    filiale_venditrice VARCHAR(16) NOT NULL,
    prezzo_vendita Denaro NOT NULL,
    PRIMARY KEY (catastale, data_vendita),
    FOREIGN KEY (catastale) REFERENCES case_in_vendita(catastale),
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva) deferrable,
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva) deferrable
);

-- Table: affitti_casa
CREATE TABLE affitti_casa (
    catastale VARCHAR(50) NOT NULL,
    data_affitto DATE NOT NULL,
    filiale_proponente VARCHAR(16) NOT NULL,
    filiale_venditrice VARCHAR(16) NOT NULL,
    prezzo_affitto Denaro NOT NULL,
    durata_contratto PosInteger NOT NULL, -- Durata in mesi
    PRIMARY KEY (catastale, data_affitto),
    FOREIGN KEY (catastale) REFERENCES case_in_affitto(catastale) deferrable,
    FOREIGN KEY (filiale_proponente) REFERENCES filiali(partita_iva) deferrable,
    FOREIGN KEY (filiale_venditrice) REFERENCES filiali(partita_iva) deferrable
);

commit;
