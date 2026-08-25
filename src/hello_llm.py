from pathlib import Path
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

#client = OpenAI()
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

question = " ".join(sys.argv[1:]).strip()

if not question:
    question = input("Ask the AI a question: ").strip()

if not question:
    raise SystemExit("Please enter a question.")

#response = client.responses.create(
#    model="gpt-5.6",
#    input=question,
#)
response = client.responses.create(
    model="openai/gpt-oss-20b",
    input=question,
)

answer = response.output_text

print("\nAI response:\n")
print(answer)

output_directory = Path("responses")
output_directory.mkdir(exist_ok=True)

output_file = output_directory / "latest_response.txt"
output_file.write_text(
    f"Question:\n{question}\n\nResponse:\n{answer}\n",
    encoding="utf-8",
)

print(f"\nResponse saved to: {output_file}")
