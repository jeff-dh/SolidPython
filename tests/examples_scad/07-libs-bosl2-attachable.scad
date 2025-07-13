include <../../solid2/extensions/bosl2/BOSL2/version.scad>;
include <../../solid2/extensions/bosl2/BOSL2/constants.scad>;
include <../../solid2/extensions/bosl2/BOSL2/transforms.scad>;
include <../../solid2/extensions/bosl2/BOSL2/distributors.scad>;
include <../../solid2/extensions/bosl2/BOSL2/miscellaneous.scad>;
include <../../solid2/extensions/bosl2/BOSL2/color.scad>;
include <../../solid2/extensions/bosl2/BOSL2/attachments.scad>;
include <../../solid2/extensions/bosl2/BOSL2/beziers.scad>;
include <../../solid2/extensions/bosl2/BOSL2/shapes3d.scad>;
include <../../solid2/extensions/bosl2/BOSL2/shapes2d.scad>;
include <../../solid2/extensions/bosl2/BOSL2/drawing.scad>;
include <../../solid2/extensions/bosl2/BOSL2/masks3d.scad>;
include <../../solid2/extensions/bosl2/BOSL2/masks2d.scad>;
include <../../solid2/extensions/bosl2/BOSL2/math.scad>;
include <../../solid2/extensions/bosl2/BOSL2/paths.scad>;
include <../../solid2/extensions/bosl2/BOSL2/lists.scad>;
include <../../solid2/extensions/bosl2/BOSL2/comparisons.scad>;
include <../../solid2/extensions/bosl2/BOSL2/linalg.scad>;
include <../../solid2/extensions/bosl2/BOSL2/trigonometry.scad>;
include <../../solid2/extensions/bosl2/BOSL2/vectors.scad>;
include <../../solid2/extensions/bosl2/BOSL2/affine.scad>;
include <../../solid2/extensions/bosl2/BOSL2/coords.scad>;
include <../../solid2/extensions/bosl2/BOSL2/geometry.scad>;
include <../../solid2/extensions/bosl2/BOSL2/regions.scad>;
include <../../solid2/extensions/bosl2/BOSL2/strings.scad>;
include <../../solid2/extensions/bosl2/BOSL2/vnf.scad>;
include <../../solid2/extensions/bosl2/BOSL2/structs.scad>;
include <../../solid2/extensions/bosl2/BOSL2/rounding.scad>;
include <../../solid2/extensions/bosl2/BOSL2/skin.scad>;
include <../../solid2/extensions/bosl2/BOSL2/utility.scad>;
include <../../solid2/extensions/bosl2/BOSL2/partitions.scad>;

attachable(anchor = CENTER, orient = UP, size = [300, 100, 100], spin = 0) {
	union() {
		xcopies(spacing = 200) {
			cube(center = true, size = 100);
		}
		xcyl(d = 25.0, h = 200);
	}
	union() {
		attach(parent = TOP) {
			cube(center = true, size = 50);
		}
		attach(parent = LEFT) {
			sphere(r = 50);
		}
		show_anchors(s = 30);
	}
}
