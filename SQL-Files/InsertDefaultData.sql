ALTER TABLE IF EXISTS Users
    OWNER to postgres;

INSERT INTO Roles ("RoleID", "Role") VALUES (1, 'Admin');
INSERT INTO Roles ("RoleID", "Role") VALUES (2, 'Helfer');
INSERT INTO Roles ("RoleID", "Role") VALUES (3, 'Laeufer');

--Passwort = 1234 (Hash MD5)
INSERT INTO Users 
    ("IdUser","Name","LastName","Email","Password_hash","Salt","CreatedAt","RoleID","VerifiedUser") 
VALUES 
    (1,'Admin','DoRunAdmin','Replace@mail.com','81dc9bdb52d04dc20036dbd8313ed055','81dc9bdb52d04dc20036dbd8313ed055','20.11.2024',1,true);
