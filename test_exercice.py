#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from unittest import mock
import inspect
import random

from character import *
from magician import *


class TestSpell(unittest.TestCase):
	def setUp(self):
		self.s1 = Spell("s1", 1, 69)
		self.s2 = Spell("s2", 69, 1)
		self.s3 = Spell("s3", 69, 42)


if __name__ == '__main__':
	if not os.path.exists('logs'):
		os.mkdir('logs')
	with open('logs/tests_results.txt', 'w') as f:
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])
		unittest.TextTestRunner(f, verbosity=2).run(suite)
	print(open('logs/tests_results.txt', 'r').read())
