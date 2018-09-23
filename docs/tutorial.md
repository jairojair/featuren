The Featuren is a software for you managing your features in production, this way..

## # Setup

### Create user

### login user

### Create two services

### Create feature



## # Use Featuren

Each service has a unique token, use this token to get the respective features.

![Example](assets/images/example_feature_by_id.png)

## Get feature by id

This request is very similiar to here, but now we will use <b>service token</b> for authorization.

<span class="resource"><span class="base get">GET</span> /features/{id}</span>

###  Request

```http tab="HTTP"

GET /features/search-button HTTP/1.1
Authorization: Token _Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg
```



```bash tab="Curl"
curl "http://0.0.0.0:8000/features/search-button" \
     -H 'Authorization: Token _Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg'
```

```python tab="Python"

# Install the Python Requests library:
# `pip install requests`

import requests

host = "http://0.0.0.0:8000"
token = "_Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg"

headers = {"Authorization": f"Token {token}"}
response = requests.get(f"{host}/features/search-button", headers=headers)

print(response.json())


```

### Response
```json tab="200"
{"id":"search-button","version":"1.0.0"}
```

```json tab="400"
{"message":"Unauthorized, invalid token"}
```

```json tab="403"
{"message":"Access denied to resource"}
```

```json tab="404"
{"message": "Feature not found"}
```


### Change feature availability

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


