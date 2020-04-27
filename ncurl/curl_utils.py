import shlex

import uncurl
from requests import Response, request


def curl_command_to_response(command) -> Response:
    """
    change curl to request
    :param command:
    :return: Request
    """
    context = uncurl.parse_context(shlex.join(command))
    return request(method=context.method, url=context.url, headers=context.headers, data=context.data.encode('utf-8'))