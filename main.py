import os
from dotenv import load_dotenv
import argparse

from google.genai import types
from google import genai

# from Functions.alpha_vantage_data import alpha_vantage_data_schema
from Functions.websearch_results import websearch_results_schema
from Functions.stop_response import stop_response_schema

from Functions.call_function import call_function

from config import SYSTEM_PROMPT, MAX_ITERATIONS

def main():
    
    load_dotenv()
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)

    parser = argparse.ArgumentParser(description="Generate answer using Gemini API")
    parser.add_argument("prompt", type = str, help = "Help user")
    parser.add_argument("--verbose", type=str, help = "print verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    system_prompt = SYSTEM_PROMPT

    available_function = types.Tool(
        # function_declarations=[alpha_vantage_data_schema, websearch_results_schema]
        function_declarations=[websearch_results_schema, stop_response_schema]
    )

    _config = types.GenerateContentConfig(
        tools=[available_function], system_instruction=system_prompt
    )

    result=""
    max_iterations = MAX_ITERATIONS

    for iter in range(max_iterations):
        
        response = client.models.generate_content(
            model='gemini-2.5-flash' , 
            contents=messages ,
            config=_config,
        )

        if response.function_calls is None:
            print(response.text)
        else:
            for fnc_call in response.function_calls:
                if fnc_call.name == "alpha_vantage_data":
                    print(f"Searching in Alpha Vantage for '{fnc_call.args}'")
                elif fnc_call.name == "websearch_results":
                    print(f"Searching Web for '{fnc_call.args['query']}'")

        print(response.text)
            
        if response.candidates:
            for fnc in response.candidates:
                if fnc is None or fnc.content is None:
                    continue
                messages.append(result)
        
        if response.function_calls:
            for fnc in response.function_calls:
                result = call_function(fnc, args.verbose)

                if result == "stop":
                    break
                
                messages.append(result)

        else:
            print(response.text)

if __name__ == "__main__":
    main()
