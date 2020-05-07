# NB cURL

## Install

### Mac

```
$ brew tap ncurl/ncurl
$ brew install ncurl
```

### by PYPI

```shell
$ pip install ncurl
```

## Usage

Support all curl options, just change `curl` to `ncurl`

```
$ ncurl -X POST "http://httpbin.org/post" -H "accept: application/json"
HTTP 200 OK
Date: Tue, 28 Apr 2020 10:44:29 GMT
Content-Type: application/json
Content-Length: 412
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "0",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.23.0",
        "X-Amzn-Trace-Id": "Root=1-5ea8090d-7f133020f65ad4709c281960"
    },
    "json": null,
    "origin": "124.126.18.162",
    "url": "http://httpbin.org/post"
}
```

## How to deploy

```shell script
$ pip install wheel twine
$ rm -rf dist/
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```
