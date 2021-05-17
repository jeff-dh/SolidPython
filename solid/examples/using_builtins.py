import sys

from solid import *
from solid import scad_render_to_file

def demo_builtins():
    return debug(color("RED")(rotate(v=[0, 0, 90], a=1)(sphere(10))))

if __name__ == '__main__':
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    a = demo_builtins()
    file_out = scad_render_to_file(a, out_dir=out_dir)
    print(f"{__file__}: SCAD file written to: \n{file_out}")
