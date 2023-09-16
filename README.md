
# A REST API for Persons Resource

This is a simple restful api for performing crud functionalities on a Person resource.

## Usage/Examples

Create Person: /persons/POST with JSON data {
    "name": "John Doe",
    "age": 20,
    "origin":"country",
    "email":"johndoe@example.net"
}

Get Person: GET /persons/{id}
Get Person: GET /persons/{name}

Update Person: PATCH /persons/{id} with JSON data {"name": "Updated Name"}
Update Person: PATCH /persons/{name} with JSON data {"name": "Updated Name"}

Delete Person: DELETE /persons/{id}.
Delete Person: DELETE /persons/{name}.


## API Reference

#### Get all persons

```http
  GET /api/perons
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api` | `string` |  http://127.0.0.1:5555/api/ |

#### Get person

```http
  GET /api/persons/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | http://127.0.0.1:5555/api/{id} |


#### Update person

```http
  PATCH /api/persons/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | http://127.0.0.1:5555/api/{id} |


#### delete person

```http
  delete /api/persons/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | http://127.0.0.1:5555/api/{id} |

```http
  POST /api/persons/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `api'    | `string` | http://127.0.0.1:5555/api |




## Authors

- [@Rolex](https://www.github.com/Rolex46)


## 🚀 About Me
I'm a full stack developer


## Run Locally

Clone the project

```bash
  https://github.com/Rolex46/restful-API
```

Go to the project directory

```bash
  cd restful-API
```

Create virtual environment

```bash
  pipenv install && pipenv shell
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py

```


## Support

For support, email rolexomondi46@gmail.com.


## Tech Stack


**Server:** python, Flask

