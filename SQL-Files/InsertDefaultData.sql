INSERT INTO Roles (RoleID, RoleNamedefault) VALUES (1, 'Admin');
INSERT INTO Roles (RoleID, RoleNamedefault) VALUES (2, 'Helfer');
INSERT INTO Roles (RoleID, RoleNamedefault) VALUES (3, 'Laeufer');

--Passwort = 1234 (Hash MD5)
INSERT INTO Users 
    (UserID, FirstName, LastName, Email, Password_Hash, Salt, CreatedAt, fk_RoleID, Verified) 
VALUES 
    (1,'Admin','DoRunAdmin','Replace@mail.com','81dc9bdb52d04dc20036dbd8313ed055'::bytea,'81dc9bdb52d04dc20036dbd8313ed055'::bytea,'20.11.2024',1,true);



INSERT INTO Users 
    (UserID, FirstName, LastName, Email, Password_Hash, Salt, fk_RoleID) 
VALUES 
    (2,'Test','User','test@mail.com', '81dc9bdb52d04dc20036dbd8313ed055'::bytea, '81dc9bdb52d04dc20036dbd8313ed055'::bytea, 1);