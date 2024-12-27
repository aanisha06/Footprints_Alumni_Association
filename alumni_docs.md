# Understanding Django's struct

[Struct ref ](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8)

- MVT : Model-Database View-interface and handles data processing? Template-static files?
- CORS: CORS is a mechanism to allow interaction with resources hosted on different domains. Let’s assume you have a web application that lives in domain.com. But, to save user information, the app calls an API hosted in another URL—for example, api.domain.com. So, when a request to save data is sent to api.domain.com, the server evaluates the requests based on its headers and the request’s source.

## creating dj project 
**Reason to choose DRF is coz we want to create api to interact with frontend**

[DRF setup guide](https://medium.com/@codexistslonglastingnotfog/django-rest-framework-a-step-by-step-guide-with-code-examples-efe9665b59d8)

1. create venv --> actiavte --> install dj, drf, cors-headers --> dj startproject --> app called core created
2. add the created app in the installed apps of *"setting.py"*
3. install mysqlclient -->

## Database
- For auto resizing of files, try imagemagick.
- Remember file name format
- store metadata for fast retrieval? but how?
- proper indexing to fetch it efficiently
- securi                    ty? huh


**db selection crisis duh!!!**

[ref site](https://akridata.ai/blog/store-images-in-database/)
1. BLOBS?
2. storing file paths in db (i.e) have separate storage besides db

1. postgres vs mysql : mysql is good since we need more read op than parallel writing or locks
    
choose blobs if no frequent access of image  

**db batch namings**
```
{
    "MSInt": 110,
    "MS": 120,
    "MSInt-Exit": 111,
    "MCA": 210,
    "MTechNIE": 310,
    "MTechNIS": 320,
    "MTechCSE": 330, 
}
```

- little problem with how int-exit should be added, maybe a new table? 
YES! a separate table for exits would be efficient, after adding stu in exit table , have to write a function to delete it from official table. solved. simply add them in the main table with diff batch id
- how to store mobile number? text or int? based on op the decision should be taken.
what are going to do with mobile? contact them? i think varchar is good coz we can write function to get numbers only or to our requirement.
- few have given personal mail id as inst mail and vice versa

**used sqlizer to convert excel sheets to sqlquery files**

## Functionalities 

1. verify the user - how? take creds and cross check with the main db
if not do manual cross checking. And add the new record
2. next step



### To learn!!
1. wsgi and asgi(async http req)    
2. serializer  
3. models in django     