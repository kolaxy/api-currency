# Currency
## Tech stack
- Docker
- Django + DRF
- Poetry
- PSQL
### Build and up containers
```bash
docker compose up
```
### Request example
```curl
curl --location 'http://localhost:8000/get-current-usd'
```
### Response example
```
{
    "current_exchange_rate": {
        "code": "USD",
        "codein": "RUB",
        "name": "Dólar Americano/Rublo Russo",
        "high": "88",
        "low": "88",
        "varBid": "0",
        "pctChange": "0",
        "bid": "87.99",
        "ask": "88.01",
        "timestamp": "1706022102",
        "create_date": "2024-01-23 12:01:42"
    },
    "history": [
        {
            "id": 1,
            "created_at": "2024-01-23T15:01:50.501166Z",
            "bid": 87.99,
            "ask": 88.01
        }
    ]
}
```
### 10 seconds between requests. If not :
```
{
    "detail": "You do not have permission to perform this action."
}
```