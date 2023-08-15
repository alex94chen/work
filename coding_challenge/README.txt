Team Task Tracking System

## How to Run the Product
1. Navigate to the project directory: `C:\work\coding_challenge`.
2. Open CMD or a terminal in the project directory: `coding_challenge`.

3. Create a shared internal network:
 
   docker network create my_net .

4. Launch a Redis container:

   docker run -d --network my_net --name my_red redis

5. Build a Docker Image:

   docker build -t imag_fastapi .

6. Verify that the Redis container is running:

   docker logs my_red

7. Start 2 containers (alice, bob):

   docker run --name alice -p 8000:80 -it --network my_net imag_fastapi:latest
   docker run --name bob -p 8080:80 -it --network my_net imag_fastapi:latest

## Using the Product
The service in the product is implemented as two instances of HTTP service (alice, bob) running in different ports.

Access the user interface using the following links:
- (http://127.0.0.1:8080/docs#/)
- (http://127.0.0.1:8000/docs#/)

Each user can perform the following actions:
1. Create new tasks:
   - A task includes a title and description.
   - Tasks can share the same title or description.

2. View all existing tasks:
   - Including tasks created by other users.

3. Remove tasks when completed.

## General Points:
- Assume Docker is installed on the computer.
- The commands are provided for the CMD interface - you can also use different CLI tools accordingly.
- It's possible to delete all data from the database by removing the comment in the DB.py file.
* Stop and delete the container instances, then restore the necessary actions for Docker Image creation (names and ports can also be changed without deleting the commas).
- Different ports can be used in the container startup commands to match entry to the FastAPI interface.
- It's possible to run containers for additional users in the same way, with different names and ports, for example:

  docker run --name mor -p 8008:80 -it --network my_net imag_fastapi:latest
  docker run --name tom -p 8888:80 -it --network my_net imag_fastapi:latest

## Things Not Done Due to Time Constraints:
- Verification of reasonable response time (under 200 milliseconds).
- Unit testing - using the pytest library to create a separate file for testing various functions' edge cases.
* At a more advanced stage, I would also perform App Testing when the application is ready for deployment - but at the moment, it's an early stage of the system.
- Improvement of outputs to create a consistent format and add outputs for tracking (log for the code).
- Adding a third file to the Task class to improve modularity and code readability.
- Deeper understanding of container communication and deciding on communication implementation between them (using a shared internal network here).
* Using Docker Compose might have been efficient, but I did not delve into it.
- Enhancement of asynchronous implementation and handling the time for sending and receiving requests (reader details are not involved).
