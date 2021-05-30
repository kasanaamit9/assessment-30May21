# assessment-30May21
Announcement Microservice

API has 2 REST endpoints as below.
•	GET - /announcement/list_all - lists all the announcements from json
•	PUT - /announcement/add - adds new announcement into the existing ones

I have used json file to store and read the announcements. I could use SQLAlchemy or NoSQL database as well for that but I do not have much exposure and hands-on experience in the same yet. Although, I will be happy to learn and work with that as well. 

How the API works.
•	Firstly, it loads few paths and configurations from ‘announcement.ini’ and initialize a logger on running the API. The ‘host’ and ‘port’ is being fetched from the environment variables and if env variables are not set then it runs the API with default values, i.e, host=’0.0.0.0’ and port=5000.
•	When user hit any endpoint, the API checks for ‘Authorization’ using ‘basicAuth’. User has to send ‘username’ & ‘password’ as headers for authorization. API has force checks for that. For authorization, API fetches the credentials from ’announcement.ini’ and validates if user is authorized or not and returns relevant message as response with relevant status code (401 or 200).
•	Then based on which endpoint is being hit by the user, API performs the operation like fetching list of announcements or adding new announcement. On completion, API returns either a json containing list of announcements or the message that the new announcement has been added successfully.

Postman collections and test cases.
I have been using ARC (Advanced Rest Client) till now for hitting the API endpoints, so, I am not that familiar with Postman and its test cases. I did some research and tried to work it out by creating the collections and test cases. If you find some discrepancies in the exported collection and sample responses, please consider the fact that I am new to Postman and I am open to have any discussion regarding the same. Please find the exported jsons uploaded to GIT.
•	Wipro.postman_collection.json – this collection contains 4 runs for 4 different scenarios.
•	Auth test – without sending the authorization headers at all.
•	Auth test – sending the auth header but with incorrect username/password.
•	List announcements test – sending correct auth header for listing all announcements
•	Add new announcement test - sending correct auth header for adding a new announcement

•	Wipro.postman_test_run.json – Defined few test cases for status codes in case of success and auth failures.

Swagger documentation/ OpenAPI 3.0
Created swagger document with authorization securities and with proper request body and responses. Please find the document uploaded the GIT.
