# ----------------------------------------------------------------------
# |
# |  MSVCCodeCoverageTestExecutor.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2019-04-10 23:00:53
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2019
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the TestExecutor object"""

import os
import textwrap

import CommonEnvironment
from CommonEnvironment import Interface

from CppMSVCCommon.TestExecutorImpl import TestExecutorImpl

# ----------------------------------------------------------------------
_script_fullpath                            = CommonEnvironment.ThisFullpath()
_script_dir, _script_name                   = os.path.split(_script_fullpath)
#  ----------------------------------------------------------------------

# ----------------------------------------------------------------------
@Interface.staticderived
class TestExecutor(TestExecutorImpl):
    # ----------------------------------------------------------------------
    # |  Properties
    Name                                    = Interface.DerivedProperty("MSVCCodeCoverage")
    Description                             = Interface.DerivedProperty(
        "Extracts code coverage information using MSVC Performance Tools.",
    )

    # ----------------------------------------------------------------------
    # |  Methods
    @classmethod
    @Interface.override
    def ValidateEnvironment(cls):
        result = super(TestExecutor, cls).ValidateEnvironment()
        if result is not None:
            return result
        
        repo_root = os.path.realpath(os.path.join(_script_dir, "..", ".."))

        # This code uses a COM object that must be registered. Unfortunately,
        # this registration requires admin access. Provide instructions if these
        # activities have not yet been completed.
        if not os.path.isfile(os.path.join(repo_root, "admin_setup.complete")):
            raise Exception(
                textwrap.dedent(
                    """\


                    In order to use the MSVCCodeCoverageTestExecutor, you must first perform
                    one-time setup activities from an administrator command prompt.

                        1) Windows Start button
                        2) Type 'cmd' (do not press enter)
                        3) Right-click "Command Prompt"
                        4) Select "Run as Administrator"

                        5) `{}\\admin_setup.cmd`

                    """,
                ).format(repo_root),
            )
