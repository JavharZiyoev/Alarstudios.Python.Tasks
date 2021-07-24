DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Privileges;

CREATE TABLE public.Users (
	"id" serial NOT NULL,
	"name" TEXT NOT NULL UNIQUE,
	"password" TEXT NOT NULL,
	"privilege_id" int2 NOT NULL,
	CONSTRAINT "Users_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE public.Privileges (
	"id" serial NOT NULL,
	"name" TEXT NOT NULL UNIQUE,
	CONSTRAINT "Privileges_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



ALTER TABLE public.Users ADD CONSTRAINT "Users_fk0" FOREIGN KEY ("privilege_id") REFERENCES public.Privileges("id");



