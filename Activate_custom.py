# ----------------------------------------------------------------------
# |
# |  Activate_custom.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2018-05-07 08:59:57
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2018-19.
# |  Distributed under the Boost Software License, Version 1.0.
# |  (See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
# |
# ----------------------------------------------------------------------
"""Performs repository-specific activation activities."""

import os
import sys

sys.path.insert(0, os.getenv("DEVELOPMENT_ENVIRONMENT_FUNDAMENTAL"))
from RepositoryBootstrap.SetupAndActivate import CommonEnvironment, CurrentShell, DynamicPluginArchitecture
from RepositoryBootstrap.Impl.ActivationActivity import ActivationActivity

del sys.path[0]

# ----------------------------------------------------------------------
_script_fullpath                            = CommonEnvironment.ThisFullpath()
_script_dir, _script_name                   = os.path.split(_script_fullpath)
# ----------------------------------------------------------------------

# Ensure that we are loading custom data from this dir and not some other repository.
sys.modules.pop("_custom_data", None)

from _custom_data import _CUSTOM_DATA

# <Class '<name>' has no '<attr>' member> pylint: disable = E1101
# <Unrearchable code> pylint: disable = W0101
# <Unused argument> pylint: disable = W0613

# ----------------------------------------------------------------------
def GetCustomActions(
    output_stream,
    configuration,
    version_specs,
    generated_dir,
    debug,
    verbose,
    fast,
    repositories,
    is_mixin_repo,
):
    """
    Returns an action or list of actions that should be invoked as part of the activation process.

    Actions are generic command line statements defined in 
    <Common_Environment>/Libraries/Python/CommonEnvironment/v1.0/CommonEnvironment/Shell/Commands/__init__.py
    that are converted into statements appropriate for the current scripting language (in most
    cases, this is Bash on Linux systems and Batch or PowerShell on Windows systems.
    """

    if configuration == "Noop":
        return []

    actions = []

    if fast:
        actions.append(
            CurrentShell.Commands.Message(
                "** FAST: Activating without verifying content. ({})".format(_script_fullpath),
            ),
        )
    else:
        # Verify installations
        for name, version, path_parts in _CUSTOM_DATA:
            this_dir = os.path.join(*([_script_dir] + path_parts))
            assert os.path.isdir(this_dir), this_dir

            actions += [
                CurrentShell.Commands.Execute(
                    'python "{script}" Verify "{name}" "{dir}" "{version}"'.format(
                        script=os.path.join(
                            os.getenv("DEVELOPMENT_ENVIRONMENT_FUNDAMENTAL"),
                            "RepositoryBootstrap",
                            "SetupAndActivate",
                            "AcquireBinaries.py",
                        ),
                        name=name,
                        dir=this_dir,
                        version=version,
                    ),
                ),
                CurrentShell.Commands.Message(""),
            ]

        # Initialize the environment
        actions += [
            CurrentShell.Commands.Set("DEVELOPMENT_ENVIRONMENT_CPP_COMPILER_NAME", "MSVC-2019"),
            CurrentShell.Commands.Augment(
                "DEVELOPMENT_ENVIRONMENT_TESTER_CONFIGURATIONS",
                "c++-coverage_executor-MSVCCodeCoverage",
                update_memory=True,
            ),
        ]

        actions += DynamicPluginArchitecture.CreateRegistrationStatements(
            "DEVELOPMENT_ENVIRONMENT_TEST_EXECUTORS",
            os.path.join(_script_dir, "Scripts", "TestExecutors"),
            lambda fullpath, name, ext: ext == ".py" and name.endswith("TestExecutor"),
        )
    
        # Add the compiler tools
        msvc_dir = ActivationActivity.GetVersionedDirectory(
            version_specs.Tools,
            _script_dir,
            "Tools",
            "MSVC",
        )
        assert os.path.isdir(msvc_dir), msvc_dir

        vcvarsall_filename = os.path.join(msvc_dir, "VC", "Auxiliary", "Build", "vcvarsall.bat")
        assert os.path.isfile(vcvarsall_filename), vcvarsall_filename

        actions += [CurrentShell.Commands.Call('"{}" {}'.format(vcvarsall_filename, configuration)), CurrentShell.Commands.Message("")]

        # Add the debug CRT to the path since it isn't there by default
        msvc_version = os.path.dirname(msvc_dir)        # Remove the OS
        msvc_version = os.path.basename(msvc_version)

        if msvc_version == "v16.0.0":
            debug_crt_dir = os.path.join(
                msvc_dir,
                "VC",
                "Redist",
                "MSVC",
                "14.20.27508",
                "debug_nonredist",
                configuration,
                "Microsoft.VC141.DebugCRT",
            )
            assert os.path.isdir(debug_crt_dir), debug_crt_dir

            actions.append(CurrentShell.Commands.AugmentPath(debug_crt_dir))
        else:
            assert False, msvc_version

        # Add the performance tools to the path
        perf_tools_dir = ActivationActivity.GetVersionedDirectory(
            version_specs.Tools,
            _script_dir,
            "Tools",
            "Performance Tools",
        )
        assert os.path.isdir(perf_tools_dir), perf_tools_dir

        perf_tools_dir = os.path.join(perf_tools_dir, "Team Tools", "Performance Tools")
        if configuration == "x64":
            perf_tools_dir = os.path.join(perf_tools_dir, "x64")

        assert os.path.isdir(perf_tools_dir), perf_tools_dir

        actions.append(CurrentShell.Commands.AugmentPath(perf_tools_dir))

    return actions


# ----------------------------------------------------------------------
def GetCustomScriptExtractors():
    """
    Returns information that can be used to enumerate, extract, and generate documentation
    for scripts stored in the Scripts directory in this repository and all repositories
    that depend upon it.

    ****************************************************
    Note that it is very rare to have the need to implement 
    this method. In most cases, it is safe to delete it.
    ****************************************************

    There concepts are used with custom script extractors:

        - DirGenerator:             Method to enumerate sub-directories when searching for scripts in a
                                    repository's Scripts directory.

                                        def Func(directory, version_sepcs) -> [ (subdir, should_recurse), ... ] 
                                                                              [ subdir, ... ]
                                                                              (subdir, should_recurse)
                                                                              subdir

        - CreateCommands:           Method that creates the shell commands to invoke a script.

                                        def Func(script_filename) -> [ command, ...]
                                                                     command
                                                                     None           # Indicates not supported
        
        - CreateDocumentation:      Method that extracts documentation from a script.

                                        def Func(script_filename) -> documentation string

        - ScriptNameDecorator:      Returns a new name for the script.

                                        def Func(script_filename) -> name string

    See <Common_Environment>/Activate_custom.py for an example of how script extractors
    are used to process Python and PowerShell scripts.
    """

    return
