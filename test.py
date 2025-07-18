from fastapi import FastAPI, Query

app = FastAPI(
    title="The API Verse",
    description="A simple API that returns the sum of two numbers.",
    version="1.0.0"
)

@app.get("/math/sum")
def add_numbers(a: float = Query(..., description="First number"),
                b: float = Query(..., description="Second number")):
    """
    Returns the sum of two numbers passed as query parameters.
    Example: /math/sum?a=5&b=7
    """
    result = a + b
    return {
        "operation": "addition",
        "inputs": {"a": a, "b": b},
        "result": result
    }
