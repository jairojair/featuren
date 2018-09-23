# Users

!!! info "You must be authenticated to use this resource."

## Create a new user

<span class="resource"><span class="base post">POST</span> /users/</span>


### Request
```bash
curl -X "POST" "http://0.0.0.0:8000/users/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
           "username": "user-1",
           "password": "secret"
         }'

```

### Response
```json tab="201"
{"message": "User created successfully"}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="409"
{"message": "The username isn't available. Please try another."}
```

## Get all users
<span class="resource"><span class="base get">GET</span> /users/</span>

### Request
```bash
curl "http://0.0.0.0:8000/users/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
[
  {
    "id": 1,
    "username": "user-1",
    "admin": true,
  },
  {
    "id": 2,
    "username": "user-2",
    "admin": false,
  }
]
```

```json tab="401"
{"message": "Unauthorized."}
```

## Get user by id
<span class="resource"><span class="base get">GET</span> /users/{id}</span>

### Request
```bash
curl "http://0.0.0.0:8000/users/1" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
{
  "id": 1,
  "username": "user-1",
  "admin": true,
}
```

```json tab="404"
{"message": "User not found"}
```

```json tab="401"
{"message": "Unauthorized."}
```

## Update user
<span class="resource"><span class="base put">PUT</span> /users/{id}</span>

### Request
```bash
curl -X "PUT" "http://0.0.0.0:8000/users/1" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
            "username": "user",
            "password": "secret"
          }'
```

### Response

```json tab="200"
{"message": "User update successfully"}
```

```json tab="404"
{"message": "User not found"}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="409"
{"message": "The username isn't available. Please try another."}
```

## Delete user
<span class="resource"><span class="base delete">DELETE</span> /users/{id}</span>

### Request

```bash
curl "http://0.0.0.0:8000/users/1" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response

```json tab="200"
{"message": "User deleted successfully"}
```

```json tab="404"
{"message": "User not found"}
```

```json tab="401"
{"message": "Unauthorized."}
```


### User data
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
      <td>String</td>
      <td>Username.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>String</td>
      <td>Password.</td>
    </tr>
  </tbody>
</table>
