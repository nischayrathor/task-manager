\connect postgres

-- Creation of table
CREATE TABLE IF NOT EXISTS task_details (
  task_id INT NOT NULL,
  task_name varchar(250) NOT NULL,
  task_owner varchar(250) NOT NULL,
  task_status BOOLEAN NOT NULL,
  PRIMARY KEY (task_id)
);

INSERT INTO task_details (task_id, task_name, task_owner, task_status)
VALUES
  (1, 'go-to-gym', 'Nischay', true),
  (2, 'go-to-school', 'Ravi', true),
  (3, 'go-to-temple', 'Sanjay', false);

