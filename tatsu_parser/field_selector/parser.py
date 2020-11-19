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


class FieldSelectorBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars="",
        **kwargs,
    ):
        super(FieldSelectorBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs,
        )


class FieldSelectorParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=True,
        parseinfo=True,
        keywords=None,
        namechars="",
        buffer_class=FieldSelectorBuffer,
        **kwargs,
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(FieldSelectorParser, self).__init__(
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
        self._field_selector_()
        self._check_eof()

    @tatsumasu()
    def _field_selector_(self):  # noqa
        self._field_()
        self.add_last_node_to_name("fields")

        def block1():
            self._token(",")
            self._field_()
            self.add_last_node_to_name("fields")

        self._closure(block1)
        self.ast._define([], ["fields"])

    @tatsumasu()
    def _field_(self):  # noqa
        self._identifier_()
        self.name_last_node("name")
        with self._optional():
            self._sub_selector_()
            self.name_last_node("sub_fields")
        self.ast._define(["name", "sub_fields"], [])

    @tatsumasu()
    def _sub_selector_(self):  # noqa
        self._token("(")
        self._field_selector_()
        self.name_last_node("@")
        self._token(")")

    @tatsumasu()
    def _identifier_(self):  # noqa
        self._pattern("[_a-z]+")


class FieldSelectorSemantics(object):
    def start(self, ast):  # noqa
        return ast

    def field_selector(self, ast):  # noqa
        return ast

    def field(self, ast):  # noqa
        return ast

    def sub_selector(self, ast):  # noqa
        return ast

    def identifier(self, ast):  # noqa
        return ast
