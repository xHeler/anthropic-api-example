import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
system_prompt = "Imagine you are innovator."
with open("prompt.txt", "r") as file:
    prompt = file.read().strip()

models = {
    "opus": "claude-3-opus-20240229",      # Input: $0.015 / KTok, Output: $0.075 / KTok
    "sonnet": "claude-3-sonnet-20240229",  # Input: $0.003 / KTok, Output: $0.015 / KTok
    "haiku": "claude-3-haiku-20240307",    # Input: $0.00025 / KTok, Output: $0.00125 / KTok
    "claude-2.1": "claude-2.1",            # Input: $0.008 / KTok, Output: $0.024 / KTok
    "claude-2.0": "claude-2.0",            # Input: $0.008 / KTok, Output: $0.024 / KTok  
    "instant": "claude-instant-1.2"        # Input: $0.0008 / KTok, Output: $0.0024 / KTok
}


selected_model = models["instant"]

client = anthropic.Client(api_key=api_key)

response = client.messages.create(
    model=selected_model,
    max_tokens=2000,
    system=system_prompt,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.content[0].text)
