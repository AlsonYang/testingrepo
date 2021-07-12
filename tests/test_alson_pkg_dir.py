#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_alson_pkg_dir
----------------------------------

Tests for `alson_pkg_dir` module.
"""

import unittest

import alson_pkg_dir


class TestAlson_pkg_dir(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(alson_pkg_dir.__version__)

    def tearDown(self):
        pass
