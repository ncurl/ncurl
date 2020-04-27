#!/usr/bin/env python

import json
import sys

from pygments import highlight
from pygments.lexers.javascript import JavascriptLexer
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.shell import BashLexer

from ncurl.utils import curl_command_to_response, response_to_head_str


def do_curl():
    command = ['curl'] + sys.argv[1:]

    response = curl_command_to_response(command)
    head_str = response_to_head_str(response)
    headers_result = highlight(head_str, BashLexer(), TerminalFormatter())
    print(headers_result)

    try:
        result = highlight(json.dumps(response.json(), indent=4, sort_keys=True), JavascriptLexer(), TerminalFormatter())
        print(result)
    except ValueError:
        result = highlight(response.content.decode("utf-8"), JavascriptLexer(), TerminalFormatter())
        print(result)


def main():
    do_curl()


if __name__ == '__main__':
    main()
