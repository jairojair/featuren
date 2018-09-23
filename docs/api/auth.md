# Authentication

## Login
<span class="resource"><span class="base post">POST</span> /auth/login</span>

!!! warning "Use the credentials created before in [Quickstart](../started.md) to login."

### Request

```http tab="HTTP"

POST /auth/login HTTP/1.1
Content-Type: application/json; charset=utf-8
Host: 0.0.0.0:8000
Connection: close

{"username":"user","password":"secret"}
```



```bash tab="Curl"
curl -X "POST" "http://0.0.0.0:8000/auth/login" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
           "username": "user",
           "password": "secret"
         }'
```

```python tab="Python"

# Install the Python Requests library:
# `pip install requests`

import requests

host = "http://0.0.0.0:8000"

user = {"username": "user", "password": "secret"}
response = requests.post(f"{host}/auth/login", user)

print(response.json())
```

### Response
```json tab="200"
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}
```

```json tab="400"
{"message": "Wrong credentials"}
```

!!! tip "Authorization header"

    Every new request you will made is necessary add this 'token' on authorization header.


### Example

```http tab="HTTP"
GET /users/ HTTP/1.1
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

```bash tab="Curl"
curl "http://{host}/users/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

```python tab="Python"

# Install the Python Requests library:
# `pip install requests`

import requests

host  = "http://0.0.0.0:8000"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."

headers  = {"authorization": f"Bearer {token}"}
response = requests.get(f"{host}/users/", headers=headers)

print(response.json())
```



### Login data
<table>
  <thead>
    <tr class="header">
      <th width="15%">Field</th>
      <th width="30%">Type</th>
      <th width="55%">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>Username.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>string</td>
      <td>Password.</td>
    </tr>
  </tbody>
</table>
