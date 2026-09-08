import os, json, urllib.request, urllib.error
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

req = urllib.request.Request(
    "https://api.groq.com/openai/v1/models",
    headers={
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "curl/8.0",
    },
)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    for m in data.get("data", []):
        print(m["id"])
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode()}")
