# Understanding Django's struct

[Struct ref ](https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8)

- MVT : Model-Database View-interface and handles data processing? Template-static files?
- CORS: CORS is a mechanism to allow interaction with resources hosted on different domains. Let’s assume you have a web application that lives in domain.com. But, to save user information, the app calls an API hosted in another URL—for example, api.domain.com. So, when a request to save data is sent to api.domain.com, the server evaluates the requests based on its headers and the request’s source.

## creating dj project 
**Reason to choose DRF is coz we want to create api to interact with frontend**

[DRF setup guide](https://medium.com/@codexistslonglastingnotfog/django-rest-framework-a-step-by-step-guide-with-code-examples-efe9665b59d8)

1. create venv --> actiavte --> install dj, drf, cors-headers --> dj startproject --> app called core created
2. add the created app in the installed apps of *"setting.py"*

### To learn!!
1. wsgi and asgi(async http req)
2. serializer       