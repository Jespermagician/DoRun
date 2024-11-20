-- Table: public.Roles
 
-- DROP TABLE IF EXISTS public."Roles";
 
CREATE TABLE Roles
(
    RoleID integer PRIMARY KEY,
    RoleName NOT NULL
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS Roles
    OWNER to postgres;
 
 
-- Table: public.User
 
-- DROP TABLE IF EXISTS Users;
 
CREATE TABLE Users
(
    UserID integer PRIMARY KEY,
    FirstName text NOT NULL,
    LastName text NOT NULL,
    Email VARCHAR(320) NOT NULL UNIQUE,
    Password_Hash bytea NOT NULL,
    Salt bytea NOT NULL,
    CreatedAt timestamp without time zone DEFAULT NOW(),
    fk_RoleID integer NOT NULL,    -- ForeignKey
    Verified boolean default false,
    CONSTRAINT fk_Role
        FOREIGN KEY(fk_RoleID)
            REFERENCES Roles(RoleID)
                    ON UPDATE CASCADE
)


TABLESPACE pg_default;

ALTER TABLE IF EXISTS Users
    OWNER to postgres;



-- Table: public.DonationRecord
 
-- DROP TABLE IF EXISTS public.DonationRecord;

CREATE TABLE DonationRecord
(
    DonationRecID integer PRIMARY KEY,
    fk_UserID integer NOT NULL,
    FirstName text NOT NULL,
    LastName text NOT NULL,
    Email VARCHAR(320) NOT NULL,
    Street text,
    HouseNr text,
    Postcode text,
    Donation numeric NOT NULL,
    FixedAmount boolean default false,
    CreatedAt timestamp without time zone DEFAULT NOW(),
    Verified boolean default false,
    CONSTRAINT fk_User
        FOREIGN KEY(fk_UserID)
            REFERENCES Users(UserID)
                ON DELETE CASCADE
                ON UPDATE CASCADE
)
 
TABLESPACE pg_default;
 
ALTER TABLE IF EXISTS DonationRecord
    OWNER to postgres;
 
 
