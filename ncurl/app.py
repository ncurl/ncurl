#!/usr/bin/env python

import sys


from ncurl.utils import request_by_context, print_response, curl_command_to_context


def do_curl():
    command = ['curl'] + sys.argv[1:]
    context = curl_command_to_context(command)
    response = request_by_context(context)
    # FIXME upload command context and response to server
    print_response(response)


def main():
    do_curl()


if __name__ == '__main__':
    main()
