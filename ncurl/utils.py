import json
import re
from typing import List

from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.text import TexLexer
from pygments.lexers.shell import BashLexer
from requests import Response, request

from ncurl.api import parse_context, ParsedContext


def curl_command_to_context(command: List[str]) -> ParsedContext:
    return parse_context(command)


def request_by_context(context: ParsedContext) -> Response:
    """
    change curl to request
    :param context:
    :return: Request
    """
    data = context.data.encode('utf-8') if context.data else None
    return request(method=context.method, url=context.url, headers=context.headers, data=data,
                   cookies=dict(context.cookies), verify=context.verify)


def response_to_head_str(response: Response) -> str:
    """
    response status and header to string
    :param response:
    :return:
    """
    head_str = ''
    head_str += f'HTTP {response.status_code} {response.reason}\n'
    for key, value in response.headers.items():
        head_str += f"{key}: {value}\n"
    return head_str


def print_response(response: Response) -> None:
    head_str = response_to_head_str(response)
    headers_result = highlight(head_str, BashLexer(), TerminalFormatter())
    print(headers_result)

    try:
        result = highlight(json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False), JavascriptLexer(),
                           TerminalFormatter())
    except ValueError as e:
        result = highlight(response.content.decode("utf-8"), TexLexer(), TerminalFormatter())
    print(result)


def join(split_command):
    """Return a shell-escaped string from *split_command*."""
    return ' '.join(quote(arg) for arg in split_command)


_find_unsafe = re.compile(r'[^\w@%+=:,./-]', re.ASCII).search


def quote(s):
    """Return a shell-escaped version of the string *s*."""
    if not s:
        return "''"
    if _find_unsafe(s) is None:
        return s

    # use single quotes, and put single quotes into double quotes
    # the string $'b is then quoted as '$'"'"'b'
    return "'" + s.replace("'", "'\"'\"'") + "'"
