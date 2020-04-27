import json
import shlex

import uncurl
from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.text import TexLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.shell import BashLexer
from requests import Response, request


def curl_command_to_response(command) -> Response:
    """
    change curl to request
    :param command:
    :return: Request
    """
    context = uncurl.parse_context(shlex.join(command))
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

    result = None
    try:
        content_type = response.headers.get("Content-Type")
        if content_type.startswith("application/json"):
            result = highlight(json.dumps(response.json(), indent=4, sort_keys=True), JavascriptLexer(),
                               TerminalFormatter())
        elif content_type.startswith("text/html"):
            result = highlight(response.content.decode("utf-8"), HtmlLexer(),
                               TerminalFormatter())
    except ValueError:
        result = highlight(response.content.decode("utf-8"), TexLexer(), TerminalFormatter())
    print(result)