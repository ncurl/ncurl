# NB cURL

## install

```
pip install ncurl
```

## Usage

Support all curl options, just change `curl` to `ncurl`

```
ncurl -X POST "http://httpbin.org/post" -H "accept: application/json"
```

## How to deploy

```shell script
$ pip install wheel twine
$ rm -rf dist/
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```
