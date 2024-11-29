-- Table: public.Roles
 
-- DROP TABLE IF EXISTS public."Roles";
 
CREATE TABLE api_roles
(
    RoleID integer NOT NULL,
    RoleName text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT Roles_pkey PRIMARY KEY (RoleID)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS api_roles
    OWNER to "Hackerman";
 
 
-- Table: public.User
 
-- DROP TABLE IF EXISTS Users;
 
CREATE TABLE api_users
(
    iduser integer PRIMARY KEY,
    firstname text NOT NULL,
    lastname text NOT NULL,
    email VARCHAR(320) NOT NULL UNIQUE,
    password_hash bytea NOT NULL,
    salt bytea NOT NULL,
    createdat timestamp without time zone DEFAULT NOW(),
    roleid integer NOT NULL,    -- ForeignKey
    verified boolean default false,
    CONSTRAINT fk_Role
        FOREIGN KEY(roleid)
            REFERENCES api_roles(RoleID)
                    ON UPDATE CASCADE
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS api_users
    OWNER to "Hackerman";



-- Table: public.DonationRecord
 
-- DROP TABLE IF EXISTS public.DonationRecord;

CREATE TABLE api_donationrecord
(
    donationrecid integer PRIMARY KEY,
    iduser integer NOT NULL,
    firstname text NOT NULL,
    lastname text NOT NULL,
    email VARCHAR(320) NOT NULL,
    street text,
    housenr text,
    postcode text,
    donation numeric NOT NULL,
    fixedamount boolean default false,
    createdat timestamp without time zone DEFAULT NOW(),
    verified boolean default false,
    CONSTRAINT fk_User
        FOREIGN KEY(iduser)
            REFERENCES api_users(IDUser)
                ON DELETE CASCADE
                ON UPDATE CASCADE
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS api_DonationRecord
    OWNER to "Hackerman";
