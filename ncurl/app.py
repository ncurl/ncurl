#!/usr/bin/env python

import subprocess
import sys
import requests

from .curl_utils import CurlUtils

server_url = 'https://ncurl-server.herokuapp.com/api'
web_url = 'https://ncurl.github.io/ncurl-web/instants/'


def do_curl():
    command = ['curl', '-s'] + sys.argv[1:]

    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    curl_utils = CurlUtils(command=command, output=stdout.decode('utf-8'), stderr=stderr.decode('utf-8'))
    curl_utils.highlight()

    upload_contents = list(map(lambda content: dict(content=content.content, highlightName=content.lexer.name.lower()),
                               curl_utils.contents))
    result = requests.post(f'{server_url}/instants', json={
        "commands": ['curl'] + sys.argv[1:],
        "contents": upload_contents
    })
    union_id = result.content.decode("utf-8")
    print(f'\nView and share in: {web_url}?id=/{union_id}')


def main():
    do_curl()


if __name__ == '__main__':
    main()

