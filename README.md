# NcURL - Next generation of cURL

Fully compatible with cURL. And with JSON support, syntax highlight, easy to share with others.

![Travis (.com)](https://img.shields.io/travis/com/ncurl/ncurl)
![PyPI](https://img.shields.io/pypi/v/ncurl)
[![Maintenance Status][maintenance-image]](#maintenance-status)

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

Fully compatible with cURL, support all curl options, just change `curl` to `ncurl`

```
$ ncurl -i -X POST http://httpbin.org/post -H "accept: application/json"
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

## LICENSE

MIT

## Maintenance Status

**Active:** Formidable is actively working on this project, and we expect to continue for work for the foreseeable future. Bug reports, feature requests and pull requests are welcome.

[maintenance-image]: https://img.shields.io/badge/maintenance-active-green.svg
