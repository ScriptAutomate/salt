import os
import time

import pytest

from tests.support.case import ModuleCase
from tests.support.runtests import RUNTIME_VARS


@pytest.mark.windows_whitelisted
class LoaderOverridesTest(ModuleCase):
    def setUp(self):
        self.run_function("saltutil.sync_modules")

    @pytest.mark.slow_test
    @pytest.mark.timeout_unless_on_windows(120)
    def test_overridden_internal(self):
        # To avoid a race condition on Windows, we need to make sure the
        # `override_test.py` file is present in the _modules directory before
        # trying to list all functions. This test may execute before the
        # minion has finished syncing down the files it needs.
        module = os.path.join(
            RUNTIME_VARS.TMP,
            "rootdir",
            "cache",
            "files",
            "base",
            "_modules",
            "override_test.py",
        )
        tries = 0
        while not os.path.exists(module):
            tries += 1
            if tries > 60:
                break
            time.sleep(1)

        funcs = self.run_function("sys.list_functions")

        # We placed a test module under _modules.
        # The previous functions should also still exist.
        self.assertIn("test.ping", funcs)

        # A non existing function should, of course, not exist
        self.assertNotIn("brain.left_hemisphere", funcs)

        # There should be a new function for the test module, recho
        self.assertIn("test.recho", funcs)

        text = "foo bar baz quo qux"
        self.assertEqual(
            self.run_function("test.echo", arg=[text])[::-1],
            self.run_function("test.recho", arg=[text]),
        )
