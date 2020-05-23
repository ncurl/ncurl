#!/usr/bin/env python

import subprocess
import sys
import requests
import colorama

from ncurl.conf import load_or_init_config, Config
from ncurl.utils import join
from ncurl.curl_utils import CurlUtils


def do_curl(config: Config):
    command = ['curl', '-sS'] + sys.argv[1:]

    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    curl_utils = CurlUtils(command=command, output=stdout.decode('utf-8'), stderr=stderr.decode('utf-8'))
    curl_utils.highlight()

    if not config.isUpload:
        return

    upload_contents = list(map(lambda content: dict(content=content.content, highlightName=content.lexer.name.lower()),
                               curl_utils.contents))
    result = requests.post(f'{config.server_url}/instants', json={
        "commands": join(['curl'] + sys.argv[1:]),
        "contents": upload_contents,
        "expire": config.expiredAt
    })
    response = result.json()
    colorama.init()
    if result.status_code == 200:
        print(f'\n {colorama.Fore.GREEN}View and share in: {response.get("webUrl")}')
    else:
        print(f'\n {colorama.Fore.RED}Failed upload to server: {response.content.decode("utf-8")}')
        sys.exit(1)


def main():
    config = load_or_init_config()
    do_curl(config)


if __name__ == '__main__':
    main()

