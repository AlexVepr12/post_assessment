

CREATE TABLE accesor (
	id uuid NOT NULL  PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name text NULL,
	role varchar(255) NULL,
	val INT
);
CREATE TABLE accesor_label (
	id uuid NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
	id_accesor uuid NOT NULL,
	id_label uuid NOT NULL,
	create_time time(0) without time zone DEFAULT now() NOT NULL
);

CREATE TABLE post_label (
	id uuid NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
	id_post uuid NOT NULL,
	id_label uuid NOT NULL,
	elapsed_time time(0) without time zone DEFAULT now() NOT NULL
);

CREATE TABLE post_assessment (
	id uuid NOT NULL DEFAULT  PRIMARY KEY
);

-- Drop table
-- DROP TABLE post_label;
-- DROP TABLE accesor_label;
-- DROP TABLE accesor;
