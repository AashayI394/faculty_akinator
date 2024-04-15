
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


## Run Locally

Clone the project

```bash
  git clone https://github.com/roguexsubmarine/faculty_akinator.git
```

Go to the project directory

```bash
  cd faculty_akinator/
```

Install dependencies

```bash
  rm -rf .venv
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```




## How It Works

**Faculty Recommendation Mode:**



![](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/4ae62215-1f01-4fcc-aefd-da0dff4ee5c0)




There are primarily 3 user input fields: ___Department, Year of Study and Subject.___
Initially, **all faculty cards** are displayed in a random order.
On the subsequent choice of selection, the faculty cards get filtered out, and only the faculty cards **relevant** to the user choice are displayed. 


**Parallel** to this, the available options in the input fields are also updated automatically. 
For example, if the Department selected is "Computer Engineering", and Year of Study selected is "2", then the Subject input field will only show the subjects taught in Computer Engineering Department for 2nd Year.

If you already know the faculty name and wish to get their contact details using our Recommendation Mode, you can use our **Live Search Bar** to get the contact card of the faculty you were searching for.

  
**Game Mode**





![](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/ee9e77b4-4a08-48a4-a67b-0df80777ee4d)


This is a **"Guess Who?"** game curated for the students of COEP Tech, consisting of faculties of our University.
**Facinator Genie** goes on asking simple **Yes/No** questions about the faculty you have in your mind. After a series of questions, it narrows down possible list of faculties and tries to guess the faculty you had in your mind. 


## Features Preview


  **Home**
![Home](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/79b39a25-e662-4254-8d83-1e184905fe4e)




  **Connect With Faculty**
![Connect With Faculty](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/807972ac-894b-4b5c-9423-8c972032d8a9)




  **Help Us Improve**
![Help Us Improve](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/6a3e1552-5a26-4d75-8b95-04c03e643873)




  **Admin Login**
![Admin Login](https://github.com/roguexsubmarine/faculty_akinator/assets/152835157/e279d730-1600-4aca-aa52-0f77f3659c36)

