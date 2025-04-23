-- Table: public.api_roles
 
-- DROP TABLE IF EXISTS public."api_roles";
 
CREATE TABLE api_roles
(
    RoleID integer NOT NULL,
    RoleName text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT Roles_pkey PRIMARY KEY (RoleID)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS api_roles
    OWNER to "admin";
 
 
-- Table: public.api_users
 
-- DROP TABLE IF EXISTS api_users;
 
CREATE TABLE api_users
(
    iduser integer PRIMARY KEY,
    firstname text NOT NULL,
    lastname text NOT NULL,
    email VARCHAR(320) NOT NULL UNIQUE,
    password_hash bytea,
    salt bytea,
    Kilometers integer default 0,
    createdat timestamp without time zone DEFAULT NOW(),
    roleid integer NOT NULL,    -- ForeignKey
    verified boolean default false,
    logintrys integer default 0,
    CONSTRAINT fk_Role
        FOREIGN KEY(roleid)
            REFERENCES api_roles(RoleID)
                    ON UPDATE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS api_users
    OWNER to "admin";



-- Table: public.api_donationrecord
 
-- DROP TABLE IF EXISTS public.api_donationrecord;

CREATE TABLE api_donationrecord
(
    donationrecid integer PRIMARY KEY,
    iduser integer,
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
    isCertReq boolean default false,
    CONSTRAINT fk_User
        FOREIGN KEY(iduser)
            REFERENCES api_users(IDUser)
                ON DELETE CASCADE
                ON UPDATE CASCADE
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS api_DonationRecord
    OWNER to "admin";
