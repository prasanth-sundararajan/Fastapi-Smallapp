# CAIE Basic FastAPI App

## Purpose

This small app demonstrates how an API receives a web request and returns data as JSON. A browser, website, or another program can make a request to one of the app's URLs and use the response.

For example, `/items/42?q=blue` asks for item `42` and includes the optional value `blue`. FastAPI puts those URL values into the function parameters. The current demo returns the values it received; it does not search a database or retrieve a real product.

## Endpoints

| Method | URL | What it returns |
| --- | --- | --- |
| `GET` | `/` | A welcome message |
| `GET` | `/greet/{name}` | A greeting using the name in the URL |
| `GET` | `/items/{item_id}` | The item ID and optional `q` query value |

`{item_id}` is a required integer in the URL. `q` is optional and follows a `?`, for example `/items/42?q=blue`. If it is omitted, the response contains `"q": null`.

## Run the App

In PowerShell, run this from the workspace root (`C:\Users\HP\GenAI_Program`):

```powershell
.\venv\Scripts\python.exe -m uvicorn main:app --app-dir fastapi-smallapp --reload --port 8002
```

Keep the terminal open while the server runs. If port `8002` is already in use, replace it with another port, such as `8003`, in both the command and the URLs below. Stop the server with `Ctrl+C`.

## Try the App

Open these URLs in a browser:

- Home: <http://127.0.0.1:8002/>
- Greeting: <http://127.0.0.1:8002/greet/Ada>
- Item without `q`: <http://127.0.0.1:8002/items/42>
- Item with `q`: <http://127.0.0.1:8002/items/42?q=blue>
- Interactive API documentation: <http://127.0.0.1:8002/docs>

You can also check the item responses from a second PowerShell terminal:

```powershell
Invoke-RestMethod "http://127.0.0.1:8002/items/42"
Invoke-RestMethod "http://127.0.0.1:8002/items/42?q=blue"
```

Expected JSON responses:

```json
{"item_id": 42, "q": null}
{"item_id": 42, "q": "blue"}
```

## Screenshots

Home response:

![Home endpoint response](screenshots/home-response.png)

Greeting response:

![Greeting endpoint response](screenshots/greeting-response.png)

Item response without the optional query value:

![Item response without q](screenshots/item-without-query.png)

Item response with `q=blue`:

![Item response with q](screenshots/item-with-query.png)

Interactive API documentation:

![FastAPI interactive docs listing the app endpoints](screenshots/interactive-docs.png)