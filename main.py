from fastapi import FastAPI, Query, HTTPException
import httpx
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["GET"],
	allow_headers=["*"]
)

def is_prime(n):
	"""Check if a number is prime."""
	if n < 2:
	   return False
	for i in range(2, int(n **0.5) + 1):
	   if n % i == 0:
		   return False
	return True

def is_perfect(n):
	"""Check if a number is perfect."""
	if n < 1:
		return False

	sum = 0
	for i in range(1,n):
		if n % i == 0:
			sum +=i
	return sum == n

def is_armstrong(n):
	"""Check if a number is an Armstrong number."""
	if n < 0:
		return False

	digits = [int(d) for d in str(abs(n))]
	power = len(digits)
	return sum(d ** power for d in digits) == abs(n)

def digit_sum(n):
	"""Return the sum of the digits of the number"""
	return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(n):
	"""Fetch a fun fact about the number using Numpers API."""
	response = requests.get(f"http://numbersapi.com/{n}/math?json")
	if response.status_code == 200:
		return response.json().get("text", "No fun fact available.")
	return "No fun fact available."

@app.get("/")
def read_root():
	return {"message": "API is running. Use /api/classify-number?number=<value> to classify a number."}

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="The number to classify")):
	"""Classify a number based on mathematical properties."""

	# Ensure the input is a valid integer (handles negative numbers too)
	try:
		number = int(number)
	except ValueError:
		return JSONResponse (
			status_code = 400,
			content ={
			"number": number,
			"error": True
			}
		)


	# Determine properties
	properties = []
	if is_armstrong(number):
		properties.append("armstrong")
	properties.append("even" if number % 2 == 0 else "odd")

	result = {
		"number": number,
		"is_prime": is_prime(number),
		"is_perfect": is_perfect(number),
		"properties": properties,
		"digit_sum": digit_sum(number),
		"fun_fact": get_fun_fact(number),
	}

	return result
