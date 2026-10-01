from fastapi import FastAPI  # Import FastAPI so this file can define a web API.

app = FastAPI(title="CAIE Basic FastAPI App")  # Create the app and set its title in the API docs.


@app.get("/")  # Register the home URL as an endpoint that accepts GET requests.
async def read_root():  # Define the function FastAPI runs when the home URL is requested.
    return {"message": "Welcome to the CAIE Basic FastAPI App!"}  # Return a welcome message as JSON.


@app.get("/greet/{name}")  # Register a greeting URL with a name provided in its path.
async def greet(name: str):  # Receive the name from the URL as a string.
    return {"message": f"Hello, {name}!"}  # Return a personalized greeting as JSON.


@app.get("/items/{item_id}")  # Register an item URL with an ID in its path.
async def read_item(item_id: int, q: str | None = None):  # Read an integer ID and optional q query value.
    return {"item_id": item_id, "q": q}  # Return both values as JSON; q is null when not provided.