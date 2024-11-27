-- Table: public.Roles
 
-- DROP TABLE IF EXISTS public."Roles";
 
CREATE TABLE api_roles
(
    roleid integer PRIMARY KEY,
    rolename NOT NULL
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS Roles
    OWNER to postgres;
 
 
-- Table: public.User
 
-- DROP TABLE IF EXISTS Users;
 
CREATE TABLE api_users
(
    userid integer PRIMARY KEY,
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
            REFERENCES Roles(RoleID)
                    ON UPDATE CASCADE
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS Users
    OWNER to postgres;



-- Table: public.DonationRecord
 
-- DROP TABLE IF EXISTS public.DonationRecord;

CREATE TABLE api_donationrecord
(
    donationrecid integer PRIMARY KEY,
    userid integer NOT NULL,
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
        FOREIGN KEY(userid)
            REFERENCES Users(UserID)
                ON DELETE CASCADE
                ON UPDATE CASCADE
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS DonationRecord
    OWNER to postgres;
 
 
