from exa_py import Exa
from dotenv import load_dotenv
import os

from google.genai import types


websearch_results_schema = types.FunctionDeclaration(
        name="websearch_results",
        description="Searches the web using the Exa API and returns highlighted snippets of the top search results. Use this to find up-to-date information.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "query": types.Schema(
                    type=types.Type.STRING,
                    description="The search query string to look up on the web.",
                )
            },
            required=["query"]
        )
    )
# exa api is better uses less tokens
def websearch_results(query: str) -> str:
    load_dotenv()
    exa = Exa(os.environ.get("EXA_API_KEY"))
    result = exa.search(
            query,
            num_results = 6,
            type = "auto",
            contents = {
                "highlights": True
            }
    )
    
    result = result.results
    info = ""
    for index, data in enumerate(result):
        info += (str(index+1) + " . ")
        info += ("Title: " + data.title + "\n")
        info += ("Body: " + " ".join(data.highlights))
        info += "\n =========================================== \n"

    return info

if __name__=="__main__":

    
    
    # Test the standalone function
    print(websearch_results("How to write using a pen"))