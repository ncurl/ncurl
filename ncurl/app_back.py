#!/usr/bin/env python
import sys

import requests

from ncurl.utils import request_by_context, print_response, curl_command_to_context

server_url = 'https://ncurl-server.herokuapp.com/api'
web_url = 'https://ncurl.sh/instants/'


def do_curl():
    command = ['curl'] + sys.argv[1:]
    context = curl_command_to_context(command)
    response = request_by_context(context)
    print_response(response)

    result = requests.post(f'{server_url}/instants', json={
        "commands": command,
        "response": response.content.decode('utf-8')
    })
    print(f'View and share in: {web_url}?id=/{result.content.decode("utf-8")}')


def main():
    do_curl()


if __name__ == '__main__':
    main()
