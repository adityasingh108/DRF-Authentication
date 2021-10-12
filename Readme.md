## Django Rest Framework Authentication 
1. BasicAuthentication
2. SessionAuthentication
3. TokenAuthentication
4. CustomAuthentication
5. JsonWebToken Authentication

### Generate Token 
* Using Admin Application
* By command line:
  ``` 
  python manage.py drf_create_token <username> 
  ``` 
* By Exposing an Api Endpoint
* Using Signals


### Access the Api from http With TokenAuthentication
* GET 
``` 
http http://127.0.0.1:8000/api/student/ 'Authorization:Token 79fc78c9296b7be81b453' 
```

*  POST
```
http -f POST  http://127.0.0.1:8000/api/student/ name=jack rollno= 107 city=delhi  'Authorization:Token 79fc78c9296b7be81b453' 
 ```
*  PUT
  ``` 
  http  PUT  http://127.0.0.1:8000/api/student/4/ name=jackiuput rollno=1077 city=delhiPut  'Authorization:Token 79fc78c9296b7be81b453'
  ```

*  DELETE
  ``` 
  http DELETE  http://127.0.0.1:8000/api/student/4/  'Authorization:Token http  DELETE  http://127.0.0.1:8000/api/student/4/  'Authorization:Token 79fc78c9296b7be81b453'
  ``` 
  


### Create, Verify,Refresh Token with JSONWebToken
* Obtain Token

```
  http POST http://127.0.0.1:8000/api/token/ username="username" password="password"
```
* Verify  Token
```
  http POST http://127.0.0.1:8000/api/token/verifytoken/ token="token"
```
* Refresh Token
```
  http POST http://127.0.0.1:8000/api/token/verifytoken/ refresh="token"
```

### Access the api With JsonWebToken

```
http http://127.0.0.1/api/student/ "Authentication:Bearer token "
```
