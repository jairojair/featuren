# Features

!!! info "You must be authenticated to use this resource."

## Create a new feature

<span class="resource"><span class="base post">POST</span> /features/</span>


### Request
```bash
curl -X "POST" "http://0.0.0.0:8000/features/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
            "id": "search-button",
            "enabled": true,
            "deny": false,
            "services": [],
            "version": "1.0.0"
         }'

```

### Response
```json tab="201"
{"message": "Feature created successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="409"
{"message": "The feature id isn't available. Please try another."}
```


## Get all features
<span class="resource"><span class="base get">GET</span> /features/</span>

### Request
```bash
curl "http://{host}/features/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
[
  {
    "id": "search-button",
    "version": "1.0.0",
    "enabled": true,
    "deny": false,
    "services": []
  },
  {
    "id": "footer",
    "version": "1.0.1",
    "enabled": true,
    "deny": false,
    "services": []
  },
]
```

```json tab="401"
{"message": "Unauthorized."}
```

## Get feature by id
<span class="resource"><span class="base get">GET</span> /features/{id}</span>

### Request
```bash
curl "http://{host}/features/search-button" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
{
  "id": "search-button",
  "version": "1.0.0",
  "enabled": true,
  "deny": false,
  "services": []
}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Feature not found."}
```

## Update feature
<span class="resource"><span class="base put">PUT</span> /features/{id}</span>

### Request
```bash
curl -X "PUT" "http://0.0.0.0:8000/features/search-button" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
            "enabled": true,
            "deny": false,
            "services": [1,2],
            "version": "1.0.2"
         }'
```

### Response

```json tab="200"
{"message": "Feature update successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Feature not found."}
```

## Delete feature
<span class="resource"><span class="base delete">DELETE</span> /features/{id}</span>

### Request

```bash
curl "http://0.0.0.0:8000/features/search-button" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response

```json tab="200"
{"message": "Feature deleted successfully."}
```

```json tab="401"
{"message": "Unauthorized."}
```

```json tab="404"
{"message": "Feature not found."}
```

### Feature data
<table>
  <thead>
    <tr class="header">
      <th width="10%">Field</th>
      <th width="10%">Type</th>
      <th width="80%">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>id</td>
      <td>String</td>
      <td>Feature name.</td>
    </tr>
    <tr>
      <td>version</td>
      <td>String</td>
      <td>Feature version.</td>
    </tr>
    <tr>
      <td>enabled</td>
      <td>Bool</td>
      <td>If value is <b>true</b> the feature can be used by all services. If value is <b>false</b> only services in services list can be use this feature.</td>
    </tr>
    <tr>
      <td>deny</td>
      <td>Bool</td>
      <td>If value is <b>​true</b> ​the feature can be used by all services except the services in services list.</td>
    </tr>
    <tr>
      <td>services</td>
      <td>Array</td>
      <td>Services list.</td>
    </tr>

  </tbody>
</table>
