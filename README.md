# Number Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/number-count?text=`

## Example

Request:
`/v1/number-count?text=Order%20123%20has%204%20items`

Response:
```json
{
  "input": "Order 123 has 4 items",
  "number_count": 4
}
