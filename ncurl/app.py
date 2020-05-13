#!/usr/bin/env python

import subprocess
import json
import sys

from pygments import highlight
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.shell import BashLexer
from pygments.formatters.terminal import TerminalFormatter


def do_curl():
    command = ['curl'] + sys.argv[1:]

    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    headers = stdout[:stdout.index(b"{")]
    json_data = stdout[stdout.index(b"{"):]
    d = json.loads(json_data)
    headers_result = highlight(headers.decode(), BashLexer(), TerminalFormatter())
    result = highlight(json.dumps(d, indent=4), JavascriptLexer(), TerminalFormatter())
    print(headers_result)
    print(result)


def main():
    do_curl()


if __name__ == '__main__':
    main()

