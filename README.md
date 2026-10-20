# API Fundamentals with Python

A practical project for learning HTTP APIs, client-server communication, GET/POST requests, status codes, headers, JSON, and the request/response lifecycle.

## Concepts Covered

- API and client-server communication
- HTTP request/response lifecycle
- GET and POST
- Status codes
- Request/response headers
- Query parameters
- JSON bodies
- Timeouts and basic error handling
- Public API testing with Python and curl/Postman
- How API fundamentals apply to AI and LLM systems

## Public API

This project uses JSONPlaceholder:

`https://jsonplaceholder.typicode.com`

No API key is required.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python get_request.py
python post_request.py
python request_lifecycle.py
python api_client.py
```

## GET vs POST

**GET** retrieves data from a server.

```python
requests.get(url, timeout=10)
```

**POST** sends data to a server.

```python
requests.post(url, json=payload, timeout=10)
```

## Common Status Codes

- 200 OK
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 404 Not Found
- 429 Too Many Requests
- 500 Internal Server Error

## Headers

Common examples:

```text
Content-Type: application/json
Accept: application/json
Authorization: Bearer <token>
```

## JSON

Send a Python dictionary as JSON:

```python
requests.post(url, json=payload)
```

Parse a JSON response:

```python
response.json()
```

## Request/Response Lifecycle

```text
Client
  ↓
HTTP Request
  ↓
Server
  ↓
Processing
  ↓
HTTP Response
  ↓
Client
```

## Use in AI

The same concepts are used in LLM APIs, model-serving endpoints, RAG systems, AI agents, computer-vision APIs, and healthcare AI applications.

Typical flow:

```text
User Input → Application → POST Request → AI API → Model → JSON Response → Application
```

## Security Note

Never hardcode real API keys in source code. Use environment variables and keep `.env` out of Git repositories.
