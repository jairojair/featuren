The Featuren is a software for you managing your features in production. In this tutorial you’ll learn how can get and update the features using only service token.

## # Setup

* [Login](api/auth.md)

* [Create a service](api/services.md)

* [Create a feature](api/features.md)



## # Use Featuren

Each service has a unique token. Use this token to get the feature information.

![Example](assets/images/example_feature_by_id.png)

## Get feature

!!! warning "Information"

	Use the service token you created before to access the resource. However, you only will be access to get and update feature information.

	If you want full access to feature resource, see more details [here](api/features.md).


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

```json tab="401"
{"message":"Unauthorized"}
```

```json tab="403"
{"message":"Access denied to resource"}
```

```json tab="404"
{"message": "Feature not found"}
```


## Update feature

!!! Tip

	For more details about feature attributes see [here.](/api/features/#feature-data)

<span class="resource"><span class="base put">PUT</span> /features/{id}</span>

### Request

```HTTP tab='HTTP'
PUT /features/search-button HTTP/1.1
Authorization: Token _Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg
Content-Type: application/json; charset=utf-8
Host: 0.0.0.0:8000

{"enabled":true,"deny":false,"version":"1.0.0"]}
```

```bash tab="Curl"
curl -X "PUT" "http://0.0.0.0:8000/features/search-button" \
     -H 'Authorization: Token _Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
            "enabled": true,
            "deny": false,
            "version": "1.0.0"
         }'
```

```python tab="Python"

# Install the Python Requests library:
# `pip install requests`

import requests

host = "http://0.0.0.0:8000"
token = "_Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg"

feature = {"enabled":True,"deny":False,"version":"1.0.1"}

headers = {"Authorization": f"Token {token}"}
response = requests.put(f"{host}/features/search-button", feature, headers=headers)

print(response.json())

```

### Response

```json tab="200"
{"message": "Feature update successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="403"
{"message":"Access denied to resource."}
```

```json tab="404"
{"message": "Feature not found."}
```

!!! success "You finished! Congratulations!"

    If you have any questions or found a bug, please open an issue [here](https://github.com/jairojair/featuren/issues)
