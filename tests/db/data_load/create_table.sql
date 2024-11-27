CREATE TABLE DEPARTMENTS (
    DEPARTMENT_ID INT PRIMARY KEY,
    DEPARTMENT_NAME VARCHAR(50) NOT NULL
);

CREATE TABLE EMPLOYEES (
    EMPLOYEE_ID INT PRIMARY KEY,
    EMPLOYEE_NAME VARCHAR(50) NOT NULL,
    DEPARTMENT_ID INT,
    FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID)
);

CREATE TABLE PROJECTS (
    PROJECT_ID INT PRIMARY KEY,
    PROJECT_NAME VARCHAR(100) NOT NULL,
    START_DATE DATE NOT NULL,
    END_DATE DATE NOT NULL
);

CREATE TABLE EMPLOYEE_PROJECTS (
    EMPLOYEE_ID INT,
    PROJECT_ID INT,
    PRIMARY KEY (EMPLOYEE_ID, PROJECT_ID),
    FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEES(EMPLOYEE_ID),
    FOREIGN KEY (PROJECT_ID) REFERENCES PROJECTS(PROJECT_ID)
);