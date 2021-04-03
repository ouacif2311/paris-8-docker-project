CREATE TABLE iris (
    id SERIAL,
    sepallength DOUBLE PRECISION,
    sepalwidth DOUBLE PRECISION,
    petallength DOUBLE PRECISION,
    petalwidth DOUBLE PRECISION,
    class VARCHAR(50),
  PRIMARY KEY (id)
);

				
COPY iris(sepallength, sepalwidth, petallength, petalwidth,class)
FROM '/mnt/data/iris_csv.csv'
DELIMITER ','
CSV HEADER;