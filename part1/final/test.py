import app
import sys
import unittest
from pathlib import Path
import os


BASENAME = 'lesson18-and-tests'
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import ResponseTestsMixin  # noqa: E402


class FinalTestCase(SkyproTestCase):

    def test_views_files_has_namespace_vars(self):
        from views import books
        from views import reviews
        namespaces_vars = ['book_ns', 'review_ns']
        for var, module in zip (namespaces_vars, [books, reviews]):   
            self.assertTrue(
                hasattr(module, var), 
                f'%@ Проверте что модуль {module} содержит переменную {var}'
            )

    def test_book_ns_has_correct_resources(self):
        from views import books
        ns_var = books.book_ns
        namespace = ns_var.name
        resources_list = [res.urls[0] for res in ns_var.resources]
        expected_resources = ['/', '/<int:bid>']
        for expected in expected_resources:
            self.assertIn(expected, resources_list,
            '%@ Проверьте что фаил books содержит view-функцию для '
            f' адреса /"{namespace}{expected}"')

    def test_book_ns_has_correct_resources(self):
        from views import authors
        ns_var = authors.book_ns
        namespace = ns_var.name
        resources_list = [res.urls[0] for res in ns_var.resources]
        expected_resources = ['/', '/<int:bid>']
        for expected in expected_resources:
            self.assertIn(expected, resources_list,
            '%@ Проверьте что фаил books содержит view-функцию для '
            f' адреса /"{namespace}{expected}"')


class ApplicationTestCase(SkyproTestCase,
                          ResponseTestsMixin):

    def setUp(self):
        self.student_app = app.app.test_client()


    def test_view_books_get_is_available_and_works_correct(self):
        url = '/books/'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.student_app.get(
                url, json=""),
            "expected": list,
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_post_is_available_and_works_correct(self):
        url = '/books/'
        test_options = {
            "url": url,
            "method": 'POST',
            "code": [200, 201, 204],
            "student_response": self.student_app.post(
                url, json=""),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/books/1'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.student_app.get(
                url, json=""),
            "expected": dict
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/books/1'
        test_options = {
            "url": url,
            "method": 'PUT',
            "code": [200, 204],
            "student_response": self.student_app.get(
                url, json=""),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/books/1'
        test_options = {
            "url": url,
            "method": 'DELETE',
            "code": [200, 204],
            "student_response": self.student_app.get(
                url, json=""),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_get_is_available_and_works_correct(self):
        url = '/reviews/'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.student_app.get(
                url, json=""),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_post_is_available_and_works_correct(self):
        url = '/authors/'
        test_options = {
            "url": url,
            "method": 'POST',
            "code": [200, 201, 204],
            "student_response": self.student_app.post(
                url, json=""),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/authors/1'
        test_options = {
            "url": url,
            "method": 'GET',
            "code": [200],
            "student_response": self.student_app.get(
                url, json=""),
            "expected": dict
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/authors/1'
        test_options = {
            "url": url,
            "method": 'PUT',
            "code": [200, 204],
            "student_response": self.student_app.get(
                url, json="")
        }
        self.check_status_code_jsonify_and_expected(**test_options)

def test_view_books_id_get_is_available_and_works_correct(self):
        url = '/authors/1'
        test_options = {
            "url": url,
            "method": 'DELETE',
            "code": [200, 204],
            "student_response": self.student_app.get(
                url, json="")
        }
        self.check_status_code_jsonify_and_expected(**test_options)

if __name__ == "__main__":
    unittest.main()