from fastapi import FastAPI, Query

app = FastAPI(
    title="The API Verse",
    description="An API that performs various math operations.",
    version="1.0.0"
)

@app.get("/math/sum")
def add_numbers(a: float = Query(...), b: float = Query(...)):
    return {"operation": "addition", "inputs": {"a": a, "b": b}, "result": a + b}

@app.get("/math/subtract")
def subtract_numbers(a: float = Query(...), b: float = Query(...)):
    return {"operation": "subtraction", "inputs": {"a": a, "b": b}, "result": a - b}

@app.get("/math/multiply")
def multiply_numbers(a: float = Query(...), b: float = Query(...)):
    return {"operation": "multiplication", "inputs": {"a": a, "b": b}, "result": a * b}

@app.get("/math/divide")
def divide_numbers(a: float = Query(...), b: float = Query(...)):
    if b == 0:
        return {"error": "Division by zero"}
    return {"operation": "division", "inputs": {"a": a, "b": b}, "result": a / b}

@app.get("/math/modulus")
def modulus(a: int = Query(...), b: int = Query(...)):
    if b == 0:
        return {"error": "Modulus by zero"}
    return {"operation": "modulus", "inputs": {"a": a, "b": b}, "result": a % b}

@app.get("/math/power")
def power(a: float = Query(...), b: float = Query(...)):
    return {"operation": "power", "inputs": {"a": a, "b": b}, "result": a ** b}

@app.get("/math/average")
def average(a: float = Query(...), b: float = Query(...)):
    return {"operation": "average", "inputs": {"a": a, "b": b}, "result": (a + b) / 2}

@app.get("/math/max")
def max_of_two(a: float = Query(...), b: float = Query(...)):
    return {"operation": "maximum", "inputs": {"a": a, "b": b}, "result": max(a, b)}

@app.get("/math/min")
def min_of_two(a: float = Query(...), b: float = Query(...)):
    return {"operation": "minimum", "inputs": {"a": a, "b": b}, "result": min(a, b)}

@app.get("/math/square")
def square(a: float = Query(...)):
    return {"operation": "square", "inputs": {"a": a}, "result": a * a}

@app.get("/math/cube")
def cube(a: float = Query(...)):
    return {"operation": "cube", "inputs": {"a": a}, "result": a * a * a}

@app.get("/math/sqrt")
def square_root(a: float = Query(...)):
    if a < 0:
        return {"error": "Cannot take square root of negative number"}
    return {"operation": "square_root", "inputs": {"a": a}, "result": a ** 0.5}
