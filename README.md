# K8s Inferencing

(attempting to) Deploy a pre-trained model to k8s for inferencing. Note, that this will require downloading models which can range from 500MB to 100GB.

## Usage

Local run:

```sh
# Setup virtualenv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run
source .env
python3 app.py
```

Kubernetes run:

```sh
docker buildx build --platform linux/amd64,linux/arm64 -t thomasvn/python-inference . --push
docker push thomasvn/python-inference

source .env
envsubst < k8s.yaml | kubectl apply -f -
```

## Model Types

- [openai-community/gpt2](https://huggingface.co/openai-community/gpt2). ~525MB. 137M Params.
- [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1). ~87GB. 46.7B Params.

<!--
https://huggingface.co/
https://huggingface.co/docs/transformers/quicktour
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
-->

<!-- 
Small/lightweight models:
- https://huggingface.co/openai-community/gpt2
- https://huggingface.co/distilbert/distilgpt2/tree/main
- https://huggingface.co/distilbert/distilbert-base-uncased
- https://huggingface.co/microsoft/Phi-3-mini-4k-instruct
-->

<!--
aws ec2 describe-volumes --volume-ids <volume-id>
aws ec2 detach-volume --volume-id <volume-id>
-->

<!-- TODO:

~ faster iterations ~

- Force GPT2 to actually use the GPU? I want to be able to measure GPU usage here.
  - https://huggingface.co/docs/transformers/main/en/model_doc/gpt2
- Use the `pipeline()` API and specify a GPU device to run on. "Hardware accelerator e.g. GPU is available in the environment, but no `device` argument is passed to the `Pipeline` object. Model will be on CPU."
- More investigation on what is `.to("cuda")`
- Run the model with lower precision so it doesn't max out node usage?
- Makefile?
- https://hub.docker.com/r/pytorch/pytorch
- https://matt.sh/python-project-structure-2024
- GH Actions Docker Build Cache?
      - name: Cache Docker layers
        uses: actions/cache@v3
        with:
          path: /tmp/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildx-
- GH Actions speed up multiarch build?
-->

<!-- DONE: (most recent to least recent)
- Use Github Actions to build & push docker image
- Switch to GPT2 for faster iterations
- Dockerfile
- k8s manifest
-->
