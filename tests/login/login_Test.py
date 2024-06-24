from pages.login_module.login_page import login
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class login_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = login(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.loginSamsung()
