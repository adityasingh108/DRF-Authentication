## Django Rest Framework Authentication 
1. BasicAuthentication
2. SessionAuthentication
3. TokenAuthentication

### Generate Token 
1. Using Admin Application
2. By command line:
  - ` python manage.py drf_create_token <username> ` this command return token 
4. By Exposing an Api Endpoint
5. Using Signals


### Access the Api from http 
1. GET :
 - `http http://127.0.0.1:8000/api/student/ 'Authorization:Token 79fc78c9296b7be81b453 ' `

2.  POST:
  - ` http -f POST  http://127.0.0.1:8000/api/student/ name=jack rollno= 107 city=delhi  'Authorization:Token 79fc78c9296b7be81b453' `
3.  PUT:
   - ` http  PUT  http://127.0.0.1:8000/api/student/4/ name=jackiuput rollno=1077 city=delhiPut  'Authorization:Token 79fc78c9296b7be81b453' `
4. DELETE:
-  `http DELETE  http://127.0.0.1:8000/api/student/4/  'Authorization:Token http  DELETE  http://127.0.0.1:8000/api/student/4/  'Authorization:Token 79fc78c9296b7be81b453' `



