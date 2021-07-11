# Habbit-assignment

Endpoints 

Register : 

  Method = POST
  URL = https://infinite-fjord-85317.herokuapp.com/account/register/
  Body = {
    "username":"akashkumar",
    "email":"akashkumar@email.com",
    "password":"akash123",
    "password2": "akash123"
   }
   
   Response = {
    "response": "Registration Successful",
    "username": "akashkumar",
    "email": "akashkumar@email.com",
    "token": "71aaae52012ed59b70ffa5343be4308d8c0591d0"
 }

------------------------------------------------------------------------------

Login:

 Method = POST
 URL = https://infinite-fjord-85317.herokuapp.com/account/login/
 Body = {
    "username":"akashkumar",
    "password":"akash123"
}

Response = {
    "token": "71aaae52012ed59b70ffa5343be4308d8c0591d0"
}

------------------------------------------------------------------------------

Get Course List

Method = GET
URL = https://infinite-fjord-85317.herokuapp.com/syllabus/course/
Response = 
[
    {
        "id": 1,
        "course_name": "Python Course",
        "author_name": "Sam",
        "created_date": "2021-07-11T15:04:17.129807Z",
        "price": 1000.0
    },
    {
        "id": 2,
        "course_name": "Django course",
        "author_name": "John",
        "created_date": "2021-07-11T15:04:33.293076Z",
        "price": 5000.0
    },
    {
        "id": 3,
        "course_name": "Java Course",
        "author_name": "Ed",
        "created_date": "2021-07-11T15:04:57.302510Z",
        "price": 7000.0
    },
    {
        "id": 4,
        "course_name": "DEV OPS",
        "author_name": "Akash",
        "created_date": "2021-07-11T15:07:44.812861Z",
        "price": 1000.0
    }
]


-------------------------------------------------------------------------------
 Get Single Course :
 
 Method = GET
 URL = https://infinite-fjord-85317.herokuapp.com/syllabus/course/1/
 Response = {
    "id": 1,
    "users_enrolled": [
        {
            "id": 1,
            "user": "admin",
            "confirm": true
        }
    ],
    "course_name": "Python Course",
    "author_name": "Sam",
    "created_date": "2021-07-11T15:04:17.129807Z",
    "price": 1000.0
}

-------------------------------------------------------------------------------

Add Course to wishlist 

Method = POST
URL = https://infinite-fjord-85317.herokuapp.com/syllabus/course/1/add-to-wishlist/
Body = {
    "confirm":"True"
}
Response = {
    "id": 2,
    "wishlist_user": {
        "id": 5,
        "first_name": "",
        "last_name": "",
        "username": "akashkumar"
    },
    "wishlist_course": "Python Course",
    "confirm": true
}

----------------------------------------------------------------------------------

Enroll to a course 

Method = POST
URL = https://infinite-fjord-85317.herokuapp.com/syllabus/course/1/enroll/
Body = {
    "confirm":"True"
}

Response = {
    "id": 2,
    "user": "akashkumar",
    "confirm": true
}
----------------------------------------------------------------------------------

 Get Single Course :
 
 Method = GET
 URL = https://infinite-fjord-85317.herokuapp.com/syllabus/course/1/
 Response = {
    "id": 1,
    "users_enrolled": [
        {
            "id": 1,
            "user": "admin",
            "confirm": true
        },
        {
            "id": 2,
            "user": "akashkumar",
            "confirm": true
        }
    ],
    "course_name": "Python Course",
    "author_name": "Sam",
    "created_date": "2021-07-11T15:04:17.129807Z",
    "price": 1000.0
}

-----------------------------------------------------------------------------------

Get Wishlist

Method = GET
URL = https://infinite-fjord-85317.herokuapp.com/syllabus/wishlist/

Response = [
    {
        "id": 2,
        "wishlist_user": {
            "id": 5,
            "first_name": "",
            "last_name": "",
            "username": "akashkumar"
        },
        "wishlist_course": "Python Course",
        "confirm": true
    }
]

-------------------------------------------------------------------------------------

Logout

Methos = POST
URL = https://infinite-fjord-85317.herokuapp.com/account/logout/

body = -
Response = -
Token gets deleted from database
