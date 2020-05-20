import unittest
import re

from pygments.lexers.data import JsonLexer
from pygments.lexers.html import XmlLexer

from ncurl.curl_utils import CurlUtils


class TestCurlUtils(unittest.TestCase):

    def test_regex(self):
        line = "{ [1 bytes data]"
        if not re.match(r"^{ \[\d+ bytes data\]", line):
            print("match")


    def test_json_content(self):
        """
        :return:
        """
        output = """{
    "args": {},
    "headers": {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.23.0",
        "X-Amzn-Trace-Id": "Root=1-5ec0cfab-55de92d8a72a390406b9fb88"
    },
    "origin": "103.90.76.242",
    "url": "http://httpbin.org/get"
}"""
        command = ["curl", "-X", "GET", "http://httpbin.org/get", "-H", "accept: application/json"]
        utils = CurlUtils(command, output)
        lexer = utils.get_lexer(output)
        self.assertTrue(isinstance(lexer, JsonLexer))

    def test_html_content(self):
        """
        :return:
        """
        output = """<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>"""
        command = ["curl", "http://example.com/"]
        utils = CurlUtils(command, output)
        self.assertTrue(len(utils.contents) == 2)
        lexer = utils.get_lexer(utils.contents[1].content)
        self.assertTrue(isinstance(lexer, XmlLexer))

    def test_include(self):
        """
        curl -i -X GET "http://httpbin.org/get" -H "accept: application/json"
        :return:
        """
        output = """HTTP/1.1 200 OK
Date: Sun, 17 May 2020 06:34:10 GMT
Content-Type: application/json
Content-Length: 267
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

{
  "args": {},
  "headers": {
    "Accept": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.64.1",
    "X-Amzn-Trace-Id": "Root=1-5ec0dae2-767fbad5b9437e9dd8fd1529"
  },
  "origin": "103.90.76.242",
  "url": "http://httpbin.org/get"
}"""
        command = ["curl", "-i", "-X", "GET", "http://httpbin.org/get", "-H" "accept: application/json"]
        utils = CurlUtils(command, output)
        print("---------------------------------")
        print(utils.contents)
        print("---------------------------------")
        self.assertEqual(len(utils.contents), 2)

    def test_verbose(self):
        """
        :return:
        """
        output = """{
  "args": {},
  "headers": {
    "Accept": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.64.1",
    "X-Amzn-Trace-Id": "Root=1-5ec0df6f-aea7952b9cfd49660222e4e3"
  },
  "origin": "103.90.76.242",
  "url": "http://httpbin.org/get"
}"""
        stderr = """Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 35.170.216.115...
* TCP_NODELAY set
* Connected to httpbin.org (35.170.216.115) port 80 (#0)
> GET /get HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/7.64.1
> accept: application/json
>
< HTTP/1.1 200 OK
< Date: Sun, 17 May 2020 06:53:35 GMT
< Content-Type: application/json
< Content-Length: 267
< Connection: keep-alive
< Server: gunicorn/19.9.0
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
<
{ [268 bytes data]
* Connection #0 to host httpbin.org left intact
* Closing connection 0"""
        command = ["curl", "-v", "-X", "GET", "http://httpbin.org/get", "-H" "accept: application/json"]
        utils = CurlUtils(command, output, stderr=stderr)
        lexer = utils.get_lexer(output)
        self.assertTrue(isinstance(lexer, JsonLexer))
        utils.highlight()