import platform
import unittest
import shutil
import subprocess
import re
from pathlib import Path


class ExamplesTest(unittest.TestCase):
    def test_examples(self):
        def get_openscad_executable():
            OPENSCAD_EXECUTABLES = {
                'Darwin': "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD",
                'Linux': "openscad"
            }
            return OPENSCAD_EXECUTABLES[platform.system()]

        root = Path(__file__).parent.parent

        for f in sorted(Path(root / "solid2" / "examples/").iterdir()):
            if not re.match("[0-9][0-9]-.*\.py", f.name):
                continue
            if f.stem.endswith(".x"):
                continue

            test_scad_file = root / "test" / "examples_scad" \
                             / f.with_suffix('.scad').name

            print(f)

            # call example (generate *.scad file)
            subprocess.check_call(["python3", f.as_posix()])
            # copy generated scad file to examples_scad/
            shutil.copyfile(f.with_suffix(".scad"), test_scad_file)
            # call git diff test/examples_scad/{f}.scad
            diff = subprocess.check_output(["git", "diff",
                                            test_scad_file.as_posix()])
            # make sure there's no diff
            self.assertEqual(diff.decode(), "")
            # render with openscad
            subprocess.check_call([get_openscad_executable(), "-o",
                                   test_scad_file.with_suffix(".png"),
                                   "--preview", "-",
                                   test_scad_file],
                                   stderr=subprocess.DEVNULL)
