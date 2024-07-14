# K8s Inferencing

(attempting to) Deploy a pre-trained model to k8s for inferencing. Note, that this will require downloading model sizes of approximately 100GB.

## Usage

Local run:

```sh
# Setup virtualenv
python3 -m venv .venv
source venv/bin/activate
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

<!--
https://huggingface.co/
https://huggingface.co/docs/transformers/quicktour
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
-->

<!--
aws ec2 describe-volumes --volume-ids <volume-id>
aws ec2 detach-volume --volume-id <volume-id>
-->

<!-- TODO:
- MOST IMPORTANT. Need to be able to quickly iterate on the model. Download model once then save to disk.
- Run the model with lower precision so it doesn't max out node usage
- Makefile?
- https://hub.docker.com/r/pytorch/pytorch
-->

<!-- DONE: (most recent to least recent)
- Dockerfile
- k8s manifest
-->