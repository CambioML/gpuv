# gpuv
Visual dashboard on top of nvidia-smi/gpustat.

## Release python package:

```
# delete dist/ build/ gpuv.egg-info/
# update version number in setup.py
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
```
Then find new version [here](https://pypi.org/project/gpuview/#history) and install.
