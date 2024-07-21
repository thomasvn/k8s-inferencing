import os
import time
from transformers import pipeline, set_seed
from huggingface_hub import login

tok = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
mod = os.getenv("MODEL_NAME")  # Ex: "openai-community/gpt2", "mistralai/Mixtral-8x7B-Instruct-v0.1"
dev = os.getenv("DEVICE")  # Ex: "cuda", "mps", "cpu"

login(token=tok)
generator = pipeline("text-generation", model=mod, device=dev)
set_seed(42)

# Infinitely loops and generates text. Dumb implementation so process doesn't
# exit resulting in a CrashLoopBackoff container.
while True:
    result = generator("Hello, I'm a language model,", truncation=True, max_length=30, num_return_sequences=5)
    print(result)
    time.sleep(10)
