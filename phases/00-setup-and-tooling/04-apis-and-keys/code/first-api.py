import os
from unittest import result
from urllib import response
from groq import Groq
import json
import urllib.request

from openai import api_key

def call_with_sdk():

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    MODEL = os.environ.get("LLM_MODEL", "openai/gpt-oss-120b")

    print(f"Using model: {MODEL}")

    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
    )

    print(response.choices[0].message.content)

def call_with_http():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
        "Content-Type": "application/json",
        "User-Agent": (
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
      ),
    }
    body = json.dumps({
        "model": os.environ.get("LLM_MODEL", "openai/gpt-oss-120b"),
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
        # Extracción formato OpenAI / Groq
        print(result["choices"][0]["message"]["content"])
    


if __name__ == "__main__":
    print("=== API Calls ===\n")
    print("1. Using the SDK:")
    call_with_sdk()
    print("\n2. Using HTTP requests:")
    call_with_http()
  