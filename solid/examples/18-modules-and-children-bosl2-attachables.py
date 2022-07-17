from solid.extensions.exportResultAsModule import children, exportResultAsModule
from solid.extensions.bosl2 import *

@exportResultAsModule
def cubic_barbell(s=102, anchor=CENTER, spin=0, orient=UP):
    return attachable(anchor,spin,orient, size=[s*3,s,s]) (
        union() (
            xcopies(2*s)(cube(s, center=True)),
            xcyl(h=2*s, d=s/4)
        ),
        children()
    )

print(cubic_barbell(100)(show_anchors(30)).as_scad())
