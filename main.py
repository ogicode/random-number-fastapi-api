from fastapi import FastAPI
import random

# Initialize the FastAPI app
app = FastAPI()

# Root endpoint - similar to the Go "home" function
@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Number API! Use /random to get a random number."}

# GET endpoint for generating random numbers - similar to the Go "randomNumber" function
@app.get("/random")
def get_random_number():
    number = random.randint(0, 99)  # Generate a random number between 0 and 99
    return {"random_number": number}

