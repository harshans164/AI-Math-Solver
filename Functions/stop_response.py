from google.genai import types

stop_response_schema = types.FunctionDeclaration(
    name="stop_response",
    description="Call this function to explicitly stop generating any further response, or to signal that the current task is fully complete.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={}, 
    )
)

def stop_response(
) -> str:
    return "stop"

if __name__ == "__main__":
    print(stop_response())