import os

from transformers import pipeline
from huggingface_hub import login

login(token=os.getenv("HUGGINGFACE_ACCESS_TOKEN"))

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="mistralai/Mixtral-8x7B-Instruct-v0.1")
pipe(messages)
