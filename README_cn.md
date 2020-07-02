# NcURL - 下一代cURL

完全兼容cURL、JSON格式支持、语法高亮展示并方便在线查看和分享

![Travis (.com)](https://img.shields.io/travis/com/ncurl/ncurl)
![PyPI](https://img.shields.io/pypi/v/ncurl)
[![Maintenance Status][maintenance-image]](#maintenance-status)

![](./resources/preview.png)

## 安装

### Mac

```
$ brew tap ncurl/ncurl
$ brew install ncurl
```

### 通过 PYPI

```shell
$ pip install ncurl
```

## 使用

跟cURL使用完全一样，你需要做的就是把 `curl` 替换成 `ncurl`

```
$ ncurl -i -X POST http://httpbin.org/post -H "accept: application/json"
HTTP/1.1 200 OK
Date: Thu, 21 May 2020 03:42:47 GMT
Content-Type: application/json
Content-Length: 332
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
        "Host": "httpbin.org",
        "User-Agent": "curl/7.64.1",
        "X-Amzn-Trace-Id": "Root=1-5ec5f8b7-7fd4fd30651bab20b5be86b0"
    },
    "json": null,
    "origin": "124.126.18.162",
    "url": "http://httpbin.org/post"
}

View and share in: https://ncurl.sh/instants/?id=/rZAGCMGcKP
```

## 许可

MIT

## 维护状态

**Active:** 欢迎提交BUG、MR

[maintenance-image]: https://img.shields.io/badge/maintenance-active-green.svg
