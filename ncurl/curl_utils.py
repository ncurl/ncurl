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

    def __str__(self) -> str:
        return f"content: {self.content}, lexer: {self.lexer}"

    def __repr__(self) -> str:
        return self.__str__()


class CurlUtils(object):
    contents: List[OutputContent] = None
    include: bool = False
    verbose: bool = False

    def __init__(self, command: List[str], output: str, stderr: str = ''):
        self._output = output
        self._stderr = stderr
        self._command = command
        self.contents = []
        self.command_line_args_parse()
        self.parse_output()

    def command_line_args_parse(self):
        command = self._command
        self.include = '-i' in command or '--include' in command
        self.verbose = '-v' in command or '--verbose' in command

    def _verbose_parse_output(self):
        stderr_lines = self._stderr.splitlines()
        lines = []
        for index, line in enumerate(stderr_lines):
            if not re.match(r"^{|} \[\d+ bytes data\]", line):
                lines.append(line)

        for index, line in enumerate(lines):
            if re.match(r"^<$", line.strip()):
                header_content = '\n'.join(lines[:index+1])
                self.contents.append(OutputContent(BashLexer(), header_content))
                for sub_index, sub_line in enumerate(lines[index+1:], start=index+1):
                    if re.match("^\* Connection .* left intact", sub_line.strip()):
                        body_content = '\n'.join(self._output.splitlines())
                        self.contents.append(OutputContent(self.get_lexer(body_content), body_content))
                        tail_content = '\n'.join(lines[sub_index:])
                        self.contents.append(OutputContent(BashLexer(), tail_content))
                        break
                return

        self.contents.append(OutputContent(BashLexer(), self._stderr))
        body_content = '\n'.join(self._output.splitlines())
        self.contents.append(OutputContent(self.get_lexer(body_content), body_content))

    def _include_parse_output(self):
        if self._stderr.strip() != '':
            self.contents.append(OutputContent(BashLexer(), self._stderr))
        lines = self._output.splitlines()
        for index, line in enumerate(lines):
            if line.strip() == '':
                header_content = '\n'.join(lines[:index])
                self.contents.append(OutputContent(BashLexer(), header_content))
                body_content = '\n'.join(lines[index + 1:])
                self.contents.append(OutputContent(self.get_lexer(body_content), body_content))
                break


    def parse_output(self):
        if self.include and not self.verbose:
            self._include_parse_output()
        if self.verbose:
            self._verbose_parse_output()
        if not self.include and not self.verbose:
            output = self._output
            stderr = self._stderr
            self.contents.append(OutputContent(BashLexer(), stderr))
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
            text = content.content
            if isinstance(content.lexer, JsonLexer):
                text = json.dumps(json.loads(text), ensure_ascii=False, indent=4)
            print(highlight(text, content.lexer, TerminalFormatter()), sep=' ', end='')