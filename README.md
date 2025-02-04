**Number Classification API**

This API classifies a given number based on various mathematical properties and provides a fun fact about it.


**Features**

-Determines if a number is prime.
-Checks if a number is an Armstrong number.
-Identifies if a number is even or odd.
-Computes the sum of its digits.
-Retrieves a fun fact about the number using the Numbers API.
-Handles invalid input gracefully and returns appropriate error messages.

**API Specification**

Base URL: https://hng12-backend-api-stage2.onrender.com

**Endpoints:**

**Root Endpoint**

GET /

Response:

{
    "message": "Welcome to the Number Classification API!",
    "endpoints": {
        "Classify Number": "/api/classify-number?number=371",
        "API Docs": "/docs"
    }
}

**Number Classification Endpoint**

GET /api/classify-number?number=<value>

Response Format

Success Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Response (400 Bad Request)

{
    "detail": {
        "number": "abc",
        "error": true
    }
}



**Installation & Setup**

**Prerequisites:**

Python 3.12+

FastAPI

Uvicorn

**Installation:**

# Clone the repository
git clone <your-repo-url>
cd <your-repo-name>

# Install dependencies
pip install fastapi uvicorn requests

**Run the API Locally**

uvicorn main:app --reload --host 0.0.0.0 --port 8000

Test the API

Once running, open your browser or use a tool like curl or Postman:

curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"

**Deployment**

This API is deployed on Render and is accessible at:

https://hng12-backend-api-stage2.onrender.com
