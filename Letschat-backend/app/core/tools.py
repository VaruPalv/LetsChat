from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression and return the result as a string."""
    expression = expression.lower()
    expression = expression.replace("times", "*")
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("divided by", "/")
    expression = expression.replace("over", "/")
    expression = expression.replace("squared", "**")
    expression = expression.replace("mod", "%")
    expression = expression.replace("added to", "+")
    
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {e}"
