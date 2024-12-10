INSERT INTO api_roles (roleid, RoleName) VALUES (1, 'Admin');
INSERT INTO api_roles (roleid, RoleName) VALUES (2, 'Helfer');
INSERT INTO api_roles (roleid, RoleName) VALUES (3, 'Laeufer');

--(Hash MD5)
INSERT INTO api_Users 
    (iduser, firstname, lastname, email, password_hash, salt, createdat, roleid, verified) 
VALUES 
    (1,'Admin','DoRunAdmin','Replace@mail.com',''::bytea,''::bytea,now(),1,true);