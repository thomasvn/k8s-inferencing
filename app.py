import os

from transformers import pipeline, set_seed
from huggingface_hub import login

login(token=os.getenv("HUGGINGFACE_ACCESS_TOKEN"))

generator = pipeline("text-generation", model="openai-community/gpt2")
set_seed(42)
result = generator("Hello, I'm a language model,", truncation=True, max_length=30, num_return_sequences=5)
print(result)
