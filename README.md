# NB cURL

```shell script
$ pip install wheel twine
$ rm dist/*
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```