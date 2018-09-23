# Features

!!! info "You must be authenticated to use this resource."

## Create a new feature

<span class="resource"><span class="base post">POST</span> /features/</span>


### Request
```bash
curl -X "POST" "http://0.0.0.0:8000/services/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
            "id": "new-search-button",
            "enabled": true,
            "deny": false,
            "services": [],
            "version": "1.0.0"
         }'

```

### Response
```json tab="201"
{"message": "Feature created successfully"}
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
curl "http://{host}/services/" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
[
  {
    "id": "new-search-button",
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
<span class="resource"><span class="base get">GET</span> /features/new-search-button</span>

### Request
```bash
curl "http://{host}/features/new-search-button" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response
```json tab="200"
{
  "id": "new-search-button",
  "version": "1.0.0",
  "enabled": true,
  "deny": false,
  "services": []
}
```

```json tab="404"
{"message": "Feature not found"}
```

```json tab="401"
{"message": "Unauthorized."}
```


## Update feature
<span class="resource"><span class="base put">PUT</span> /features/new-search-button</span>

### Request
```bash
curl -X "PUT" "http://{host}/services/new-search-button" \
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
{"message": "Feature update successfully"}
```

```json tab="404"
{"message": "Feature not found"}
```

```json tab="401"
{"message": "Unauthorized."}
```

## Delete feature
<span class="resource"><span class="base delete">DELETE</span> /features/new-search-button</span>

### Request

```bash
curl "http://{host}/features/new-search-button" \
     -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...'
```

### Response

```json tab="200"
{"message": "Feature deleted successfully"}
```

```json tab="404"
{"message": "Feature not found"}
```

```json tab="401"
{"message": "Unauthorized."}
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
      <td>Feature enabled.</td>
    </tr>
    <tr>
      <td>deny</td>
      <td>Bool</td>
      <td>Feature deny.</td>
    </tr>
    <tr>
      <td>services</td>
      <td>Array</td>
      <td>Feature services</td>
    </tr>

  </tbody>
</table>
