# coding-sphere-test

First, clone the repo and make sure you are in `coding_sphere` folder

We will run the api as a docker container

First, run the following command to build a docker image locally

```bash
docker build -t cs-api-image .
```

Now run following command which will spin up a docker container

```bash
docker run -d --name cs-api -e SECRET_KEY=fr4e2iun43vroin2 -e MONGO_URI="mongodb+srv://ashutoshb2000:ztHaCsud0qR1FpBS@cluster0.nzrbe.mongodb.net/projectdb?retryWrites=true&w=majority" -p 8000:8000 cs-api-image
```

At this moment the api is running on port 8000 locally and you should be able to hit the endpoints.

Please find the swagger docs here:

```bash
http://localhost:8000/docs
```

Below are examples of login and register endpoints which doesn't require JWT auth.

Register:

```bash
POST http://localhost:8000/users/register

with body:
{
    "username" : "coolcoder",
    "password" : "password000",
    "role": "admin" (optional, with user role as default)
}
```

Login:

```bash
POST http://localhost:8000/users/login

with body:
{
    "username" : "coolcoder",
    "password" : "password000"
}
```

Get all projects endpoint, requires JWT, both user and admin can hit. Please add the token returned from the login endpoint as a bearer token.

```bash

GET http://localhost:8000/projects

```

Create project endpoint that requires JWT with admin role, user role cannot hit this endpoint. Please add the token returned from the login endpoint as a bearer token. Similar can be followed for update and delete as well

```bash

POST http://localhost:8000/projects

with body:
{
    "name": "foo",
    "description": "demo description"
}
```
