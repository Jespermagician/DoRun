-- Table: public.Roles
 
-- DROP TABLE IF EXISTS public."Roles";
 
CREATE TABLE Roles
(
    "RoleID" integer NOT NULL,
    "Role" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Roles_pkey" PRIMARY KEY ("RoleID")
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS Roles
    OWNER to postgres;
 
 
 
-- Table: public.Spendenbelege
 
-- DROP TABLE IF EXISTS public."Spendenbelege";

CREATE TABLE Spendenbelege
(
    "IdSpendenbeleg" integer NOT NULL,
    "IdUser" integer NOT NULL,
    "Name" text COLLATE pg_catalog."default" NOT NULL,
    "LastName" text COLLATE pg_catalog."default" NOT NULL,
    "Email" character varying(320) COLLATE pg_catalog."default" NOT NULL,
    "Street" text COLLATE pg_catalog."default",
    "HouseNr" text COLLATE pg_catalog."default",
    "Postcode" text COLLATE pg_catalog."default",
    "DonationpKm" numeric NOT NULL,
    "FixedAmount" boolean,
    "CreatedAt" timestamp with time zone,
    "VerifiedDono" boolean,
    CONSTRAINT "Spendenbelege_pkey" PRIMARY KEY ("IdSpendenbeleg")
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS Spendenbelege
    OWNER to postgres;
 
 
-- Table: public.User
 
-- DROP TABLE IF EXISTS Users;
 
CREATE TABLE Users
(
    "IdUser" integer NOT NULL,
    "Name" text COLLATE pg_catalog."default" NOT NULL,
    "LastName" text COLLATE pg_catalog."default" NOT NULL,
    "Email" character varying(320) COLLATE pg_catalog."default" NOT NULL,
    "Password_hash" bytea NOT NULL,
    "Salt" bytea NOT NULL,
    "CreatedAt" timestamp without time zone NOT NULL,
    "RoleID" integer NOT NULL,
    "VerifiedUser" boolean,
    CONSTRAINT "User_pkey" PRIMARY KEY ("IdUser")
)


TABLESPACE pg_default;