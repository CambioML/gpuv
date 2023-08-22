# gpuv
Visual dashboard on top of nvidia-smi/gpustat.

## Release python package:

```
# delete dist/
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
```
