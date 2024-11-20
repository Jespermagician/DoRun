
-----------------------------------------------------
--------------------Obsolet--------------------------
-----------------------------------------------------

-- -- Table: public.Roles
 
-- -- DROP TABLE IF EXISTS public."Roles";
 
-- CREATE TABLE Roles
-- (
--     "RoleID" integer NOT NULL,
--     "Role" text COLLATE pg_catalog."default" NOT NULL,
--     CONSTRAINT "Roles_pkey" PRIMARY KEY ("RoleID")
-- )
 
-- TABLESPACE pg_default;
 
-- ALTER TABLE IF EXISTS Roles
--     OWNER to postgres;
 
 
 
-- -- Table: public.Spendenbelege
 
-- -- DROP TABLE IF EXISTS public."Spendenbelege";

-- CREATE TABLE Spendenbelege
-- (
--     "IdSpendenbeleg" integer NOT NULL,
--     "IdUser" integer NOT NULL,
--     "Name" text COLLATE pg_catalog."default" NOT NULL,
--     "LastName" text COLLATE pg_catalog."default" NOT NULL,
--     "Email" character varying(320) COLLATE pg_catalog."default" NOT NULL,
--     "Street" text COLLATE pg_catalog."default",
--     "HouseNr" text COLLATE pg_catalog."default",
--     "Postcode" text COLLATE pg_catalog."default",
--     "DonationpKm" numeric NOT NULL,
--     "FixedAmount" boolean,
--     "CreatedAt" timestamp with time zone,
--     "VerifiedDono" boolean,
--     CONSTRAINT "Spendenbelege_pkey" PRIMARY KEY ("IdSpendenbeleg")
-- )
 
-- TABLESPACE pg_default;
 
-- ALTER TABLE IF EXISTS Spendenbelege
--     OWNER to postgres;
 
 
-- -- Table: public.User
 
-- -- DROP TABLE IF EXISTS Users;
 
-- CREATE TABLE Users
-- (
--     "IdUser" integer NOT NULL,
--     "Name" text COLLATE pg_catalog."default" NOT NULL,
--     "LastName" text COLLATE pg_catalog."default" NOT NULL,
--     "Email" character varying(320) COLLATE pg_catalog."default" NOT NULL,
--     "Password_hash" bytea NOT NULL,
--     "Salt" bytea NOT NULL,
--     "CreatedAt" timestamp without time zone NOT NULL,
--     "RoleID" integer NOT NULL,
--     "VerifiedUser" boolean,
--     CONSTRAINT "User_pkey" PRIMARY KEY ("IdUser")
-- )
 
-- TABLESPACE pg_default;
 
-- ALTER TABLE IF EXISTS Users
--     OWNER to postgres;

-- INSERT INTO Roles ("RoleID", "Role") VALUES (1, 'Admin');
-- INSERT INTO Roles ("RoleID", "Role") VALUES (2, 'Helfer');

-- --Passwort = 1234 (Hash MD5)
-- INSERT INTO Users ("IdUser","Name","LastName","Email","Password_hash","Salt","CreatedAt","RoleID","VerifiedUser") VALUES (1,'Admin','DoRunAdmin','Replace@mail.com','81dc9bdb52d04dc20036dbd8313ed055','81dc9bdb52d04dc20036dbd8313ed055','20.11.2024',1,true);
