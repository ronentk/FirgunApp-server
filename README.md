# FirgunApp-server

## Installation
- Install py-eve using `pip install eve`
- Set up Mongo-DB

## Server-side
- In one shell window, start one instance of database: `mongod --dbpath data/db --port 27010`
- In second shell window, start Flask webserver: `python server.py`
- Config details- Local: `127.0.0.1`, Remote Google host: `35.229.18.203`

## Client-side
### Requests
Get all firguns by `curl http://<hostname>:5000/firguns`.
### Add Firgun
Add new firgun by `curl -d '[{"category": "eco", "latitude": "23.4254", "longitude": "12.32423", "description": "Cool place!"}]' -H 'Content-Type: application/json'  http://<hostname>:5000/firguns`
