# ----------------------------------------------------------------------
# |
# |  _custom_data.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2019-04-08 16:04:51
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2019
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Data used by both Setup_custom.py and Activate_custom.py"""

import os

import CommonEnvironment

# ----------------------------------------------------------------------
_script_fullpath                            = CommonEnvironment.ThisFullpath()
_script_dir, _script_name                   = os.path.split(_script_fullpath)
#  ----------------------------------------------------------------------

_CUSTOM_DATA                                = [
    (
        "MSVC - 16.0.0",
        "BFBAA1DCD06618C95BA6A6C5179343BE35D6D9433DDC5E1B2172C602C891EFAB",
        [
            "Tools",
            "MSVC",
            "v16.0.0",
            "Windows",
        ],
    ),
    (
        "Visual Studio Performance Tools - 16.0.0",
        "94470CBF0B5914BF30FF1377ED1F8F3F96098E596853B14C0A441C4513D41F93",
        [
            "Tools",
            "Performance Tools",
            "v16.0.0",
            "Windows",
        ],
    ), 
]
