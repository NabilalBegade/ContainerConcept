CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    reg_no VARCHAR(10) UNIQUE,
    name VARCHAR(50),
    vaccination_status VARCHAR(3)
);

INSERT INTO students (reg_no, name, vaccination_status)
VALUES
    ('123', 'John Doe', 'Yes'),
    ('456', 'Jane Doe', 'No'),
    ('789', 'Bob Smith', 'Yes');
