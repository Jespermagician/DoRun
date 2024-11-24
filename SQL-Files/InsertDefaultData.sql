INSERT INTO Roles (roleid, rolenamedefault) VALUES (1, 'Admin');
INSERT INTO Roles (roleid, rolenamedefault) VALUES (2, 'Helfer');
INSERT INTO Roles (roleid, rolenamedefault) VALUES (3, 'Laeufer');

--Passwort = 1234 (Hash MD5)
INSERT INTO api_Users 
    (userid, firstname, lastname, email, password_hash, salt, createdat, roleid, verified) 
VALUES 
    (1,'Admin','DoRunAdmin','Replace@mail.com','81dc9bdb52d04dc20036dbd8313ed055'::bytea,'81dc9bdb52d04dc20036dbd8313ed055'::bytea,'20.11.2024',1,true);



INSERT INTO api_Users 
    (userid, firstname, lastname, email, password_hash, salt, roleid) 
VALUES 
    (2,'Test','User','test@mail.com', '81dc9bdb52d04dc20036dbd8313ed055'::bytea, '81dc9bdb52d04dc20036dbd8313ed055'::bytea, 1);