#!/usr/bin/env python

import sys


from ncurl.utils import curl_command_to_response, print_response


def do_curl():
    command = ['curl'] + sys.argv[1:]

    response = curl_command_to_response(command)
    print_response(response)


def main():
    do_curl()


if __name__ == '__main__':
    main()
