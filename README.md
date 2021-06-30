# 1-BYTE
A Blended Learning Academic Portal 

### Project Summary
This software system is an online blended learning academic portal for any university wishing to manage their academic needs online and diminish the semantic gap between students and their teachers.
The system provide features to the user of an educational institute to be part of different types of groups, share data and documents amongst different users, have discussion threads and Video Calling 

# Installation

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/ritikjain14299/1-BYTE.git
$ cd 1-BYTE
```

Create a virtual environment to install dependencies in and activate it using Command prompt:

```sh
 pip install virtualenv
 virtualenv env
 env\Scripts\activate.bat
```

Then install the dependencies:

```sh
(env) pip install -r requirements.txt
```

Note the `(env)` in front of the Command prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env) python manage.py makemigrations
(env) python manage.py migrate
(env) python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/` or `LocalHost`

### Login Details for Admin 

```
adminx2@gmail.com
adminx2
```

### Login Details for Teachers 

```
teacher@gmail.com
teacher
```

### Login Details for Student

```
pratik@gmail.com
pratik
```


 # Features
 ### Admin
  Admin Login
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Admin%20login.png" >
  Admin Dashboard
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Admin%20dashboard.png" >
  Add Course
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Add%20Course.png" >
  Add Staff
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Add%20staff.png">
  Add Student
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Add%20student.png">
  Manage Session
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Manage%20session.png" >
 Edit Student
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Edit%20student.png" >
 Edit Staff
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Edit%20staff.png" >
 Manage Course 
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Manage%20course.png" >
 Manage Student
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Manage%20student.png" >
 Manage Subject
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Manage%20subject.png" >
 Manage Staff
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Manage%20staff.png" >
 Send Notification Staff
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Send%20notification-%20Staff.png" >
 Send Notification Student
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Admin_ss/Send%20notification%20-%20student.png" >
 


 ### Teacher
 Teacher Dashboard
 <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Teacher%20Dashboard.png" >
 Teacher Login
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Login.png" >
 Add Result
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Add%20Results.png" >
 Edit Result
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Edit%20Results.png" >
 Ask Question
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Ask_question.png" >
 Live Class
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Live%20Class.png" >
 Start Live Class
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Start%20Live%20class.png">
 Discussion Forum
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Discussion%20Forum.png" > 
 Discussion Forum Reply Section
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Discussion%20forum%20-Reply%20Section.png" >
 Teacher Notification
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Teacher_ss/Notification.png" >
 
 ### Student
 Student Login
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/Login.png" >
 Student Dashboard 
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/student%20dashboard.png" >
 Subject Grade
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/Grade%20card.png" >
 Ask Question
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/Ask_question.png" > 
 Discussion Forum
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/Discussion%20form.png" >
 Discussion Forum Reply Section
  <img  src="https://github.com/ritikjain14299/1-BYTE/blob/main/screenshots/Student_ss/Discussion%20forum-%20Reply%20section.png" >

 # Tech
 + [Django](https://www.djangoproject.com/) - A python based web-Framework 
 + [Sqlite3](https://www.sqlite.org/) - Database used for project








