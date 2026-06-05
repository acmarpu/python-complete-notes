----------------------------------------------------------------------------------------------
### API Basics 
----------------------------------------------------------------------------------------------




* **HTTP Methods (Operations)**
GET    ------->  Retrive Data  /users
POST   ------->  Create Data   /Users
PUT    ------->  Update Data   /user/1
DELETE ------->  Delete Data   /user/1

* **API Request Structure**

https://    api.example.com   /users?id=10&  role=admin
-----       ---------------   -----------    ----------
protocol       Domain           Endpoint     Parameter



|          **Headers**               |    **Request Body(JSON)**     | **Parameters**    | 
|------------------------------------|-------------------------------|-------------------|
| * Authorization: Bearer Token      |{ "name": "Ashoka",            | * id = 10         |
| * Content-Type: Application/json   |  "emai": "ashoka@gmail.com",  | * role = admin    |
| * Accept: Application/json         |  "role: "Student",            | * page = 1        |
| * User- Agent: Chrome/124.0        |  "city: "Hyderabad"           | * limit = 20      |
|                                    | }                             |                   |

* Whenever utilizing API
1. URL (domain name and endpoint)
2. Header 
3. Payloud 
4. Parameters or filters



* **HTTP STatus Codes**
* 200 --  Ok            --  Success
* 201 --  Created       --  Resource Created
* 400 --  Bad Request   --  Invalid Input
* 401 --  Unauthorized  --  Not authorized
* 403 --  Forbidden     --  Access Dined
* 404 --  Not Found     --  Resource not found
* 500 --  Internal Server error
* 501 not Implemented   --  Not Supported 