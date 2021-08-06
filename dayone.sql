-- ~~~~~~~~~~~~~~~ E 1 ~~~~~~~~~~~~~~~~~~~~
-- Write a SQL query that retrieves the personal data about alumni who scored above 16 on their calculus exam.



CREATE TABLE alumni (
	student_id SERIAL PRIMARY KEY,
	name text,
  	surname text,
  	birth_date date,
  	faculty text
);

CREATE TABLE eval (
	student_id SERIAL REFERENCES alumni,
	class_id SERIAL PRIMARY KEY,
	exam_date DATE,
	grade INT
);

CREATE TABLE curricula (
	class_id SERIAL REFERENCES eval,
  	class_name text,
  	professor_id SERIAL,
  	semester text
);

INSERT INTO alumni (name,surname, birth_date, faculty) VALUES ('asad', 'siddiqui', '1995-04-23', 'nuclear');

INSERT INTO alumni (name,surname, birth_date, faculty) VALUES ('zero', 'siddiqui', now(), 'prince');

INSERT INTO alumni (name,surname, birth_date, faculty) VALUES ('ali', 'atif', now(), 'genius');

INSERT INTO eval (exam_date, grade ) VALUES (now(), '16');

INSERT INTO eval (exam_date, grade ) VALUES (now(), '15');


INSERT INTO curricula (class_name, semester) VALUES ('calculus', 'fall');

INSERT INTO curricula (class_name, semester) VALUES ('diff', 'fall');

-------


-- Write a SQL query that retrieves the personal data about alumni who scored above 16 on their calculus exam

SELECT a.name, a.surname, a.birth_date, a.faculty, e.grade
	FROM alumni as a
INNER JOIN eval as e
	ON a.student_id = e.student_id
INNER JOIN curricula as c
	on e.class_id = c.class_id
WHERE e.grade >= 16 AND c.class_name = 'calculus';

SELECT * FROM alumni;
SELECT * FROM eval;
SELECT * FROM curricula;
