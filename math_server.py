from mcp.server.fastmcp import FastMCP

mcp = FastMCP("arithmetic")

@mcp.tool()
def add(a: int, b: int) -> str:
    result = a + b
    return f"""➕ Step-by-Step Addition:
1. {a} + {b} = {result}
✅ Final Answer: {result}
"""

@mcp.tool()
def sub(a: int, b: int) -> str:
    result = a - b
    return f"""➖ Step-by-Step Subtraction:
1. {a} - {b} = {result}
✅ Final Answer: {result}
"""

@mcp.tool()
def mult(a: int, b: int) -> str:
    result = a * b
    return f"""✖️ Step-by-Step Multiplication:
1. {a} × {b} = {result}
✅ Final Answer: {result}
"""

@mcp.tool()
def div(a: int, b: int) -> str:
    if b == 0:
        return "❌ Error: Division by zero"
    result = a / b
    return f"""➗ Step-by-Step Division:
1. {a} ÷ {b} = {result}
✅ Final Answer: {result}
"""

@mcp.tool()
def solve_equation(equation: str) -> str:
    try:
        result = eval(equation)
        return f"""🧮 Original Expression: {equation}

📌 Step 1 – Parentheses:
If any, solve them first.

📌 Step 2 – Multiplication/Division:
Apply multiplication or division.

📌 Step 3 – Addition/Subtraction:
Apply addition or subtraction.

✅ Final Answer: {result}"""
    except Exception as e:
        return f"❌ Error solving equation: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
