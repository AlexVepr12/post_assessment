CREATE TABLE labels (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	objectivity INT,
	perspective INT,
	doubts INT,
	doubts_success INT,
	meeting_needs INT
);

-- Drop table

-- DROP TABLE labels;