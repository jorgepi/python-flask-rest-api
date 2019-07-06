# python-flask-rest-api
Rest API in Python

- Example to build the Docker container:
# docker build -t my-python-api .

- Example to test the app:
#docker run -d -p 5000:5000 my-python-api

Tests:

GET:
curl http://localhost:5000/user/Jorge

POST:
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alfred", "age": 34, "occupation": "Cellist"}' http://localhost:5000/user/Alfred

PUT:
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Tom", "age": 25, "occupation": "Tennis Player"}' http://localhost:5000/user/Alice

DELETE:
curl -X DELETE http://localhost:5000/user/Jorge
