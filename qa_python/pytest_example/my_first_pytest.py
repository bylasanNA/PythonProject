import unittest

class myFirstPytest(unittest.TestCase):

    def setUp(self):
        print("into setup")
        self.num1 = 2
        self.num2 = 3

    def tearDown(self):
        print("into test end")

    def test_summary(self):
        summary = self.num1 + self.num2
        # summary = 3 + 4
        # if summary == 9:
        #     print("test passed")
        # else:
        #     print("test failed")

        assert summary == 5, "the summary of num1 and num2 should be 5"
        result = summary * 2
        print(result)

    def test_multiple(self):
        multiple = self.num1 * self.num2
        assert multiple == 6, "our code did not support multiple"