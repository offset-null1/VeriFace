-- create table subjects (sub_id char(8) PRIMARY KEY,sub_name varchar(60));

create table students (
    usn varchar(20) PRIMARY KEY,
    fname VARCHAR(10),
    lname VARCHAR(10),
    email VARCHAR(20),
    phone_no CHAR(11),
    sem enum(1,2,3,4,5,6,7,8),
    branch VARCHAR(4),
    embedding VARCHAR(20),
    constraint mail_ph unique(email,phone_no)
);

--independent

create table semesters (sem_id enum('1','2','3','4','5','6','7','8'),
                        sub_id char(8) PRIMARY KEY,
                        sub_name  varchar(60)
                        branch char(3),
                        branch_name varchar(30));

--independent
/* create table branches (branch char(3) primary key,
                       branch_name varchar(30)); */


create table in_sub_categories( sub_id CHAR(8),
                               assignment_id varchar(10),
                               project_id varchar(10),
                               lab_id varchar(10),
                               FOREIGN KEY(sub_id) REFERENCES semesters(sub_id),
                               unique(assignment_id,project_id,lab_id));

create TABLE marks (usn varchar(20),
                    assignment_id varchar(10),
                    assignment_marks FLOAT,
                    project_id varchar(10),
                    project_marks FLOAT,
                    lab_id varchar(10),
                    lab_marks FLOAT,
                    ia_no INT,
                    ia_marks FLOAT,
                    foreign key(usn) REFERENCES students(usn),
                    foreign key(assignment_id, project_id,lab_id) REFERENCES in_sub_categories(assignment_id,project_id,lab_id));


-- create view stud_sub as select sub_id,sub_name from semesters inner join students on semesters.sem_id =students.sem_id;

-- create view stud_marks as SELECT 
create table attendance (usn varchar(20),
                         `login` TIMESTAMP,
                         logout TIMESTAMP, 
                         `date` DATE,
                         sub_id char(8) ,
                         FOREIGN KEY(usn) REFERENCES students(usn),
                         FOREIGN KEY(sub_id) REFERENCES semesters(sub_id));

create view usn_embed as SELECT usn, embedding FROM `students` order by usn;