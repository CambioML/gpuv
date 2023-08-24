# gpuv
Visual dashboard on top of nvidia-smi/gpustat.

## pip install and use
```
pip3 install gpuv
python gpuv -s
```

## dev setup and use
```
pip3 install poetry
poetry install --no-root
python -m gpuv -s
```

## Release python package:

```
poetry publish --build
```
Then find new version [here](https://pypi.org/project/gpuv/#history) and install.
