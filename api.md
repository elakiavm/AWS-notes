# # Authentication types

* Baisc Authentication
 --It is sending username and the password to the server for every request making to the server 
--This is inconvenient and security risk even if the transport is through the secure http the client appliction must have the credential stored without encryption to be able to send them with these request

* Token and Bearer
--token is a string that server generates for the client 

OAUTH
---------------------------------------------------------------------
FastAPI 
API is very fast to make 
When we create a API we actual defining all of the value that API is expecting

In generally in all the type fo the API we will not say the type of the information in API is in the end points.
data validation 
check to ensure type of the information we get 

We write a lot of code to check API is in the correct type

Data  Validation 
auto Documentation
----------------------------------------------
We need to have a end point 

like /hello, /end 

type methods :

GET = It will get value and return the information

POST = ur sending the request to endpoint  (into database)

PUT = for updating something which is existing already in (update database)

DELETE = delete the info (delete from database)