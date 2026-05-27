from .alpha_vantage_data import alpha_vantage_data
from .websearch_results import websearch_results

from google.genai import types

def call_function(function_call: types.FunctionCall, verbose: bool = False
                  ) -> types.Content:
    

    #ditch this if this is the culprit for repetitive response, if ditched then leave it
    # if verbose:
    #     if function_call.name == "alpha_vantage_data":
    #         print(f"Searching in Alpha Vantage for '{function_call.args[0]}' '{function_call.args[1]}'")
    #     elif function_call.name == "websearch_results":
    #         print(f"Searching Web for '{function_call.args[0]}'")
    # else:
    #     if function_call.name == "alpha_v antage_data":
    #         print("Searching in Alpha Vantage for realtime stock performance...")
    #     elif function_call.name == "websearch_results":
    #         print("Searching Web...")
    result = ""
    if function_call.name == "alpha_vantage_data":
        result = alpha_vantage_data(**function_call.args)
    elif function_call.name == "websearch_results":
        result = websearch_results(**function_call.args)
    elif function_call.name == "":
        return types.Content(
            role= "tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={
                        "error": f"unknown function call '{function_call.name}'"
                    }
                )
            ]
        )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response={
                    "result":result
                },
            )
        ]
    )