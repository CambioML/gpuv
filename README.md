# gpuv

gpuv (gpu _visual_) is a python library that provides an interactive dashboard to monitor your gpu usage:

[gif]

## Installation

Install with `pip`:

```
pip3 install gpuv
```

## Usage

To use `gpuv`, simply run the start command from the cli:

```
python gpuv -s
```

This will launch the interface on another port. Navigate there to monitor your gpu usage live.

## EC2 Usage

On EC2, you will have to tunnel to the port `5000`. This can be done by spinning up th ec2 with port forwarding enabled, e.g.

```
ssh -i <pemkey> -L 5000:127.0.0.1:5000 ubuntu@ec2<...>.com
```

Then, just run `gpuv start` in the cli of your ec2, navigate to that port, and you're good to go!

## Demo

Here's a quick demo video (for those who prefer watching vs reading):

video

## Dev Setup

To set up gpuv for your own development/extension, use `poetry`:

```
pip3 install poetry
poetry install --no-root
python -m gpuv -s
```

## Coming Soon

- [ ] Support multiple gpu's in one view.
- [ ] Local data collection (that you can save to csv).
