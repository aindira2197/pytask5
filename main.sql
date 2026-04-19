CREATE TABLE hisoblash_dasturi(
    id INT PRIMARY KEY,
    ism VARCHAR(255),
    familya VARCHAR(255),
    vazifa VARCHAR(255)
);

CREATE TABLE hisob-kitob(
    id INT PRIMARY KEY,
    hisob_id INT,
    kitob_id INT,
    hisoblash_turi VARCHAR(255),
    FOREIGN KEY (hisob_id) REFERENCES hisoblash_dasturi(id),
    FOREIGN KEY (kitob_id) REFERENCES hisoblash_dasturi(id)
);

INSERT INTO hisoblash_dasturi (id, ism, familya, vazifa) 
VALUES 
(1, 'John', 'Doe', 'hisobchi'),
(2, 'Jane', 'Doe', 'hisobchi'),
(3, 'Bob', 'Smith', 'hisobchi');

CREATE FUNCTION hisoblash(x INT, y INT) RETURNS INT 
BEGIN 
    DECLARE z INT;
    SET z = x + y;
    RETURN z;
END;

CREATE PROCEDURE hisob_kitob_protsedurasi() 
BEGIN 
    DECLARE i INT DEFAULT 1;
    DECLARE j INT DEFAULT 1;
    DECLARE k INT DEFAULT 0;
    DECLARE m INT;
    WHILE i <= 10 DO 
        SET k = hisoblash(i, j);
        SET m = hisoblash(i, k);
        INSERT INTO hisob-kitob (id, hisob_id, kitob_id, hisoblash_turi) 
        VALUES (i, i, j, 'hisob-kitob');
        SET i = i + 1;
        SET j = j + 1;
    END WHILE;
END;

CALL hisob_kitob_protsedurasi();

SELECT * FROM hisob-kitob;

CREATE VIEW hisob_kitob_view AS 
SELECT * FROM hisob-kitob;

SELECT * FROM hisob_kitob_view;

CREATE INDEX hisob_id_index ON hisob-kitob (hisob_id);

CREATE INDEX kitob_id_index ON hisob-kitob (kitob_id);

CREATE TRIGGER hisob_kitob_trigger 
AFTER INSERT ON hisob-kitob 
FOR EACH ROW 
INSERT INTO hisob_kitob_view (id, hisob_id, kitob_id, hisoblash_turi) 
VALUES (NEW.id, NEW.hisob_id, NEW.kitob_id, NEW.hisoblash_turi);

CREATE TRIGGER hisob_kitob_triggerDelete 
AFTER DELETE ON hisob-kitob 
FOR EACH ROW 
DELETE FROM hisob_kitob_view 
WHERE id = OLD.id;

CREATE TRIGGER hisob_kitob_triggerUpdate 
AFTER UPDATE ON hisob-kitob 
FOR EACH ROW 
UPDATE hisob_kitob_view 
SET hisob_id = NEW.hisob_id, kitob_id = NEW.kitob_id, hisoblash_turi = NEW.hisoblash_turi 
WHERE id = NEW.id;

DROP TRIGGER hisob_kitob_trigger;

DROP TRIGGER hisob_kitob_triggerDelete;

DROP TRIGGER hisob_kitob_triggerUpdate;

DROP TABLE hisob-kitob;

DROP TABLE hisoblash_dasturi;

DROP VIEW hisob_kitob_view;

DROP FUNCTION hisoblash;

DROP PROCEDURE hisob_kitob_protsedurasi;