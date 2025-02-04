from fastapi import FastAPI, Query, HTTPException
import requests

app = FastAPI()

def is_prime(n: int) -> bool:
	"""Check if a number is prime."""
	if n < 2:
	   return False
	for i in range(2, int(n **0.5) + 1):
	   if n % i == 0:
		   return False
	return True

def is_armstrong(n: int) -> bool:
	"""Check if a number is an Armstrong number."""
	digits = [int(d) for d in str(n)]
	power = len(digits)
	return sum(d ** power for d in digits) == n

def get_fun_fact(n: int) -> str:
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
		raise HTTPException(status_code=400, detail={"number": number, "error": True})

	number = int(number) # Convert invalid string to integer

	# Determine properties
	properties = []
	if is_armstrong(number):
		properties.append("armstrong")
	properties.append("even" if number % 2 == 0 else "odd")

	result = {
		"number": number,
		"is_prime": is_prime(number),
		"is_perfect": False,
		"properties": properties,
		"digit_sum": sum(int(digit) for digit in str(number)),
		"fun_fact": get_fun_fact(number),
	}

	return result
