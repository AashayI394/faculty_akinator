
# Facinator

Facinator (Faculty-Akinator) is a faculty recommendation system, with an additional game mode that efficiently guesses the faculty of COEP Technological University, drawing inspiration from the internet guessing-game, Akinator. 

## Usage

Facinator serves the following purposes:

**Faculty Recommendation Mode:**
1. Provides a simple way of finding the faculties relevant to the department and the year of study a student belongs to, and also helps reach out to individual faculties teaching a particular course. 
2. On finding the most relevant faculty, you can reach out to them with your subject related queries, by mentioning the subject and contents of your email. On a click, the draft email is generated in your default mail client, which can be reviewed and then sent to the desired faculty.  
  
 
**Game Mode:**

Prerequisite: You should know enough information about the faculty you want the Facinator to guess.

1. On the basis of a series of Yes/No questions regarding the department, course name, gender, doctorate status, office location,the year/semester for which the faculty conducts a course, Facinator efficiently guesses the name of the faculty the user had in mind while answering the questions.
2. A question thread will be generated automatically to help the user keep track of the questions that have been asked previously and their corresponding response to them.


  
**Help-Us-Improve:**
  
In case you are unable to find the desired faculty, or if a faculty that you know is missing in Facinator, you can visit the Help-Us-Improve tab and fill out a short form regarding the missing faculty details. On submission of the form, you can check out our Pending Requests tab to review your submission. Our admin will review the form submission as soon as possible and update the database accordingly.




## Features

- Faculty Recommendation Mode
- Faculty Search Bar (AJAX Live Search)
- Game Mode (Guessing the Faculty)
- Help-Us-Improve Section
- Pending Requests Viewer
- Admin Login

## Tech Stack

**Frontend:** HTML5, CSS, Jinja2 Templating, JavaScript, AJAX

**Backend:** Flask, Python3, SQLite3

## How It Works

**Faculty Recommendation Mode:**



![](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator7.png)




There are primarily 3 user input fields: ___Department, Year of Study and Subject.___
Initially, **all faculty cards** are displayed in a random order.
On the subsequent choice of selection, the faculty cards get filtered out, and only the faculty cards **relevant** to the user choice are displayed. 


**Parallel** to this, the available options in the input fields are also updated automatically. 
For example, if the Department selected is "Computer Engineering", and Year of Study selected is "2", then the Subject input field will only show the subjects taught in Computer Engineering Department for 2nd Year.

If you already know the faculty name and wish to get their contact details using our Recommendation Mode, you can use our **Live Search Bar** to get the contact card of the faculty you were searching for.

  
**Game Mode**





![](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator2.png)


This is a **"Guess Who?"** game curated for the students of COEP Tech, consisting of faculties of our University.
**Facinator Genie** goes on asking simple **Yes/No** questions about the faculty you have in your mind. After a series of questions, it narrows down possible list of faculties and tries to guess the faculty you had in your mind. 


## Features Preview



![Home](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator1.png)




![Connect With Faculty](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator8.png)




![Help Us Improve](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator3.png)




![Admin Login](https://github.com/roguexsubmarine/faculty_akinator/static/README_img/facinator5.png)

