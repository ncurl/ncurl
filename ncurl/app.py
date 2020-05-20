#!/usr/bin/env python

import subprocess
import sys
import shlex

import requests

from ncurl.utils import join
from .curl_utils import CurlUtils

server_url = 'https://api.ncurl.sh/api'
web_url = 'https://ncurl.sh/instants/'


def do_curl():
    command = ['curl', '-sS'] + sys.argv[1:]

    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    curl_utils = CurlUtils(command=command, output=stdout.decode('utf-8'), stderr=stderr.decode('utf-8'))
    curl_utils.highlight()

    upload_contents = list(map(lambda content: dict(content=content.content, highlightName=content.lexer.name.lower()),
                               curl_utils.contents))
    result = requests.post(f'{server_url}/instants', json={
        "commands": join(['curl'] + sys.argv[1:]),
        "contents": upload_contents
    })
    response_str = result.content.decode("utf-8")
    if result.status_code == 200:
        print(f'\nView and share in: {web_url}?id=/{response_str}')
    else:
        print(f'Failed upload to server: {response_str}')
        sys.exit(1)


def main():
    do_curl()


if __name__ == '__main__':
    main()

