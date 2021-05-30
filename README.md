# Task 5
## Description
This project represents educational platform, that consists of 2 parts: `Users` and `Courses`.
There is opportunity to log in as User with `Student` or `Teacher` role.
Courses provides: `Course`, `Lecture`, `Task`, `Homework`, `Rating`, `Comment` models.

## How to use
To check docs description you can use the following address: `http://127.0.0.1:8000/swagger/`

There is a possibility to use Django admin, which allows us to interact with different educational platform models.

JWT Authentication is used in the project, so you need to be authorized to test the requests. To authorize you need to follow the next steps:
* create user - `POST http://127.0.0.1:8000/api/user/`
    required fields: `username`, `password`, `role` (teacher or student)
* get access token - `POST http://127.0.0.1:8000/api/token/`
    required fields: `username`, `password`
* Author request perform, copy access token value and put it into the authorization key of the headers of the necessary url

## Tests
There are some tests(educational_platform/courses/tests.py) which proofs that the CRUD operations and authorization work correctly.
