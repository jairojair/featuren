# Services

!!! info "You must be authenticated to use this resource."

## Create a new service

<span class="resource"><span class="base post">POST</span> /services/</span>


### Request
```bash
curl -X "POST" "http://0.0.0.0:8000/services/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
           "name": "service-1",
           "description": "service description"
         }'

```

### Response
```json tab="201"
{"message": "Service created successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

## Get all services
<span class="resource"><span class="base get">GET</span> /services/</span>

### Request
```bash
curl "http://0.0.0.0:8000/services/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
[
  {
    "id": 1,
    "name": "Service-1",
    "description": "Service-1",
    "token": "_Ld_k_26y7H-Ar9og6cEz54rkNZEDkW1BIrkgSAFFg"
  },
  {
    "id": 2,
    "name": "Service-2",
    "description": "Service-2",
    "token": "_wm-zTzCP4owZAIxsvT9jQ6h0mv3JZf-E_UR-LBXgQ"
  }
]
```

```json tab="401"
{"message": "Unauthorized."}
```

## Get service by id
<span class="resource"><span class="base get">GET</span> /service/{id}</span>

### Request
```bash
curl "http://0.0.0.0:8000/services/1" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
{
  "id": 1,
  "name": "service-1",
  "description": "service description",
}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Service not found."}
```


## Update service
<span class="resource"><span class="base put">PUT</span> /services/{id}</span>

### Request
```bash
curl -X "PUT" "http://0.0.0.0:8000/services/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
            "name": "service-1",
            "description": "new service description"
          }'
```

### Response

```json tab="200"
{"message": "Service update successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Service not found."}
```

## Delete service
<span class="resource"><span class="base delete">DELETE</span> /services/{id}</span>

### Request

```bash
curl "http://0.0.0.0:8000/services/1" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response

```json tab="200"
{"message": "Service deleted successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Service not found."}
```

### Service data
<table>
  <thead>
    <tr class="header">
      <th width="15%">Field</th>
      <th width="15%">Type</th>
      <th width="70%">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>String</td>
      <td>Service name.</td>
    </tr>
    <tr>
      <td>description</td>
      <td>String</td>
      <td>Service description.</td>
    </tr>
  </tbody>
</table>
