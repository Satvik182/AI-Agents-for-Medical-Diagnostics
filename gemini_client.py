import os
import re
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from local env file (project root).
_env_path = os.path.join(os.path.dirname(__file__), "apikey.env")
load_dotenv(_env_path)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use an available fast/free model for Gemini API keys.
model = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(prompt: str) -> str:
    last_error: Exception | None = None

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            last_error = e
            msg = str(e)

            # Basic free-tier rate-limit handling (HTTP 429).
            if "429" in msg or "Quota exceeded" in msg:
                wait_s = 60
                m = re.search(r"Please retry in ([0-9]+)", msg)
                if m:
                    wait_s = int(m.group(1))
                time.sleep(wait_s)
                continue

            raise

    raise last_error  # type: ignore[misc]

