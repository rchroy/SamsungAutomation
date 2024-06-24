import unittest
from tests.galaxy_z_flip.galaxy_z_flip_Test import galaxy_z_flip_Tests
from tests.galaxy_fold.galaxy_fold_Test import galaxy_fold_Tests
from tests.login.login_Test import login_Tests

tc1 = unittest.TestLoader().loadTestsFromTestCase(galaxy_z_flip_Tests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(galaxy_fold_Tests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(login_Tests)

smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
