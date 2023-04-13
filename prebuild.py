#!/usr/bin/env python
"""Pre-build steps run before packaging solid2.

The preferred method to build solid2 is via poetry:

% poetry build

You should have poethepoet plugin installed before doing the above:

% poetry self add 'poethepoet[poetry_plugin]'
"""
import subprocess


def main():
    subprocess.check_call("./bosl2_generator.py", cwd="./solid2/extensions")


if __name__ == "__main__":
    main()
