import re
from json.decoder import JSONDecodeError
from typing import List

from pygments.formatters.terminal import TerminalFormatter
from pygments.lexer import RegexLexer
from pygments.lexers import guess_lexer
import json

from pygments.lexers.data import JsonLexer
from pygments import highlight

import logging

from pygments.lexers.shell import BashLexer

logger = logging.getLogger(__name__)


class OutputContent(object):

    def __init__(self, lexer: RegexLexer, content: str):
        self.lexer = lexer
        self.content = content


class CurlUtils(object):
    contents: List[OutputContent] = []
    include: bool = False
    verbose: bool = False

    def __init__(self, command: List[str], output: str):
        self._output = output
        self._command = command
        self.command_line_args_parse()
        self.parse_output()

    def command_line_args_parse(self):
        command = self._command
        self.include = '-i' in command or '--include' in command
        self.verbose = '-v' in command or '--verbose' in command

    def _verbose_parse_output(self):
        lines = self._output.splitlines()
        for index, line in enumerate(lines):
            if re.match(r"^<$", line):
                header_content = '\n'.join(lines[:index])
                self.contents.append(OutputContent(BashLexer(), header_content))
                for sub_index, sub_line in enumerate(lines[index:], start=index):
                    if re.match("^\* Connection", sub_line):
                        body_content = '\n'.join(lines[index + 1: sub_index])
                        self.contents.append(OutputContent(self.get_lexer(body_content), body_content))
                        tail_content = '\n'.join(lines[sub_index:])
                        self.contents.append(OutputContent(BashLexer(), tail_content))
                        break
                break

    def parse_output(self):
        output = self._output
        if self.include:
            lines = output.splitlines()
            for index, line in enumerate(lines):
                if line.strip() == '':
                    header_content = '\n'.join(lines[:index])
                    self.contents.append(OutputContent(BashLexer(), header_content))
                    body_content = '\n'.join(lines[index + 1:])
                    self.contents.append(OutputContent(self.get_lexer(body_content), body_content))
                    break

        if self.verbose:
            self._verbose_parse_output()

        if not self.include and not self.verbose:
            self.contents.append(OutputContent(self.get_lexer(output), output))


    @staticmethod
    def get_lexer(content: str) -> RegexLexer:
        try:
            json.loads(content)
            return JsonLexer()
        except JSONDecodeError:
            pass
        return guess_lexer(content)

    def highlight(self):
        for content in self.contents:
            print(highlight(content.content, content.lexer, TerminalFormatter()))