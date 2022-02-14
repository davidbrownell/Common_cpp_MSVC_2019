# ----------------------------------------------------------------------
# |
# |  _custom_data.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2019-04-08 16:04:51
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2019-22
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
# ----------------------------------------------------------------------

_CUSTOM_DATA                                = [
    (
        "MSVC - 16.0.0",
        "bfbaa1dcd06618c95ba6a6c5179343be35d6d9433ddc5e1b2172c602c891efab",
        [
            "Tools",
            "MSVC",
            "v16.0.0",
            "Windows",
        ],
    ),
    (
        "Visual Studio Performance Tools - 16.0.0",
        "94470cbf0b5914bf30ff1377ed1f8f3f96098e596853b14c0a441c4513d41f93",
        [
            "Tools",
            "Performance Tools",
            "v16.0.0",
            "Windows",
        ],
    ),
]
