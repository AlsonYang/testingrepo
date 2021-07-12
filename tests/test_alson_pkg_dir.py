#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_alson_pkg_dir
----------------------------------

Tests for `alson_pkg_dir` module.
"""

import unittest

import alson_pkg_dir

import os

class TestAlson_pkg_dir(unittest.TestCase):

    def setUp(self):
        self.cli_result = 'return Hello World'

    def test_something(self):
        assert(alson_pkg_dir.__version__)
        assert(alson_pkg_dir.cli() == self.cli_result)

    # def test_file_exist(self):
    #     alson_pkg_dir.create()
    #     assert os.path.isfile('./data/test.csv')

    def tearDown(self):
        pass
