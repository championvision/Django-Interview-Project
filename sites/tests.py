# Imported the summary view from sites.views

import unittest
from sites.views import qs_sum


class TestBasic(unittest.TestCase):
    # qs_sum gets querysets as input. qs is the return of
    # models.objects.values() test_positive is for the case
    # that all elements are positive. test_positive_negative
    # is for the case that all elements are positive and negatives
    # test_negative is for the case that all elements are negative
    # test_null is for the case that all elements are positive,
    # negatives and zero
    def test_positive(self):
        a = 84.0
        qs = [{'a_value': 12.0}, {'a_value': 24.0}, {'a_value': 48.0}]
        self.assertEqual(qs_sum(qs), a)

    def test_positive_negative(self):
        a = 60.0
        qs = [{'a_value': -12.0}, {'a_value': 24.0}, {'a_value': 48.0}]
        self.assertEqual(qs_sum(qs), a)

    def test_negative(self):
        a = -84.0
        qs = [{'a_value': -12.0}, {'a_value': -24.0}, {'a_value': -48.0}]
        self.assertEqual(qs_sum(qs), a)

    def test_null(self):
        a = 24.0
        qs = [{'a_value': 0.0}, {'a_value': -24.0}, {'a_value': 48.0}]
        self.assertEqual(qs_sum(qs), a)
