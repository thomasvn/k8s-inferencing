# Python Inference

## Setup

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```sh
source .env
python3 app.py
```

```sh
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t thomasvn/python-inference . --push
docker push thomasvn/python-inference

kubectl aply k8s.yaml
```

<!--
https://huggingface.co/
https://huggingface.co/docs/transformers/quicktour
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
-->

<!-- TODO:
- MOST IMPORTANT. Need to be able to quickly iterate on the model. Download model once then save to disk.
- k8s manifest
- python3: can't open file '/app/app.py': [Errno 2] No such file or directory
- Makefile ?
- https://hub.docker.com/r/pytorch/pytorch
-->

<!-- DONE: (most recent to least recent)
- Dockerfile
-->