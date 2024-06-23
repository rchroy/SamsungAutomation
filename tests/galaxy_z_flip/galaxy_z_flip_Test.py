from pages.galaxy_z_flip.galaxy_z_flip_page import galaxy_z_flip
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class galaxy_z_flip_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.brp = galaxy_z_flip(self.driver)

    @pytest.mark.run
    def test_browsing(self):
        self.brp.galaxy_z_flip_browsing()
