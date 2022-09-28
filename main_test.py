import unittest
from hello_cv import vcheck


class MainTest(unittest.TestCase):
    def test_hellocv(self):
        ret = vcheck()
        self.assertEqual(ret, "hello, openCV4.6.0")  # openCV version check


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
    # python -m unittest discover -p "*_test.py"
    # -> unit test 실행
    # coverage run --source=./ -m unittest discover -p "*_test.py"
    # coverage xml
