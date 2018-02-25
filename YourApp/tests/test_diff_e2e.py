from YourApp.tests import YourAppBaseTestCase, groups, END_TO_END_TESTS_GROUP


class E2ETestCases(YourAppBaseTestCase):
    """Test cases to verify if the endpoints can be used safelly"""

    @groups(END_TO_END_TESTS_GROUP)
    def test_alive(self):
        # When alive endpoint is used
        result = self.app.get("/v1/alive")
        
        # Then a 200 is answered
        self.assertEqual("200 OK", result.status)
        self.assertEqual("Alive", result.data.decode())

    @groups(END_TO_END_TESTS_GROUP)
    def test_404(self):

        # When a fake endpoint is used
        result = self.app.post("/v1/fake")
        
        # Then a 404 is answered
        self.assertEqual("404 NOT FOUND", result.status)
