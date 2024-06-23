from pages.galaxy_fold.galaxy_fold_page import galaxy_fold
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class galaxy_fold_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = galaxy_fold(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.galaxy_fold_browsing()
