#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from tatsu.buffering import Buffer
from tatsu.parsing import Parser
from tatsu.parsing import tatsumasu

KEYWORDS = {}  # type: ignore


class LogicalOperatorBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=True,
        namechars="",
        **kwargs,
    ):
        super(LogicalOperatorBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs,
        )


class LogicalOperatorParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=True,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars="",
        buffer_class=LogicalOperatorBuffer,
        **kwargs,
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(LogicalOperatorParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs,
        )

    @tatsumasu()
    def _start_(self):  # noqa
        self._expression_()
        self._check_eof()

    @tatsumasu()
    def _expression_(self):  # noqa
        with self._choice():
            with self._option():
                self._boolean_()
                self.name_last_node("value")
            with self._option():
                self._and__()
                self.name_last_node("func")
            with self._option():
                self._or__()
                self.name_last_node("func")
            self._error("no available options")
        self.ast._define(["func", "value"], [])

    @tatsumasu()
    def _boolean_(self):  # noqa
        with self._choice():
            with self._option():
                self._token("true")
            with self._option():
                self._token("false")
            self._error("no available options")

    @tatsumasu()
    def _and__(self):  # noqa
        self._token("and_")
        self.name_last_node("name")
        self._token("(")
        self._expression_()
        self.add_last_node_to_name("expressions")

        def block2():
            self._token(",")
            self._expression_()
            self.add_last_node_to_name("expressions")

        self._closure(block2)
        self._token(")")
        self.ast._define(["name"], ["expressions"])

    @tatsumasu()
    def _or__(self):  # noqa
        self._token("or_")
        self.name_last_node("name")
        self._token("(")
        self._expression_()
        self.add_last_node_to_name("expressions")

        def block2():
            self._token(",")
            self._expression_()
            self.add_last_node_to_name("expressions")

        self._closure(block2)
        self._token(")")
        self.ast._define(["name"], ["expressions"])


class LogicalOperatorSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def expression(self, ast):
        return ast

    def and_(self, ast):  # noqa
        return ast

    def or_(self, ast):  # noqa
        return ast