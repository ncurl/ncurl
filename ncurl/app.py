#!/usr/bin/env python

import json
import sys

from pygments import highlight
from pygments.lexers.javascript import JavascriptLexer
from pygments.formatters.terminal import TerminalFormatter

from ncurl.curl_utils import curl_command_to_response


def do_curl():
    command = ['curl'] + sys.argv[1:]

    response = curl_command_to_response(command)
    result = response.json()
    # headers_result = highlight(json.dumps(response.headers, indent=4), BashLexer(), TerminalFormatter())
    result = highlight(json.dumps(result, indent=4), JavascriptLexer(), TerminalFormatter())
    # print(headers_result)
    print(result)


def main():
    do_curl()


if __name__ == '__main__':
    main()
