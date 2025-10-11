import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def get_prompt():
    if len(sys.argv) <= 1:
        print("prompt not provided")
        sys.exit(1)
    prompt = ""
    for i in range(1, len(sys.argv)):
        if i != len(sys.argv)-1:
            prompt = prompt + sys.argv[i] + " "
        else:
            prompt = prompt + sys.argv[i]
    return prompt

prompt = get_prompt()
client = client.models.generate_content(model = "gemini-2.0-flash-001", contents = prompt)

prompt_tokens = client.usage_metadata.prompt_token_count
response_tokens = client.usage_metadata.candidates_token_count

print(client.text)
print("Prompt tokens: " + str(prompt_tokens)+"\n"+ "Response tokens: " + str(response_tokens))
