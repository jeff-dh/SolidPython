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
include <../../solid2/extensions/bosl2/BOSL2/gears.scad>;
include <../../solid2/extensions/bosl2/BOSL2/screws.scad>;
include <../../solid2/extensions/bosl2/BOSL2/cubetruss.scad>;

$fa = 1;
$fs = 1;

xdistribute(spacing = 50) {
	recolor(c = "#f77") {
		diff(remove = "hole") {
			cuboid(anchor = FRONT, chamfer = 10, edges = [(RIGHT + BACK), (RIGHT + FRONT)], size = [45, 45, 10]) {
				tag(tag = "hole") {
					cuboid(chamfer = 5, edges = [(RIGHT + BACK), (RIGHT + FRONT)], size = [30, 30, 11]);
				}
				attach(child = BACK, overlap = 5, parent = FRONT) {
					cuboid(edges = [(RIGHT + BACK), (RIGHT + FRONT)], rounding = 15, size = [45, 45, 10]) {
						tag(tag = "hole") {
							cuboid(edges = [(RIGHT + BACK), (RIGHT + FRONT)], rounding = 10, size = [30, 30, 11]);
						}
					}
				}
			}
		}
	}
	recolor(c = "#7f7") {
		bevel_gear(face_width = 12, pitch = 8, pitch_angle = 45, shaft_diam = 25, slices = 12, spiral_angle = 30, teeth = 20);
	}
	recolor(c = "#99f") {
		path_sweep(path = bezpath_curve(bezpath = [[-18, -20], [-18, -45], [18, -45], [18, -20], [18, 0], [-18, 0], [-18, 20], [-18, 45], [18, 45], [18, 20]]), shape = regular_ngon(d = 10, n = 3, spin = 90));
	}
	recolor(c = "#0bf") {
		move(v = [-15, -35, 0]) {
			cubetruss_corner(bracing = false, clipthick = 0, extents = [3, 8, 0, 0, 0], h = 1, size = 10, strut = 1);
		}
	}
	recolor(c = "#777") {
		xdistribute(spacing = 24) {
			screw(anchor = "origin", head = "hex", orient = BACK, spec = "M12,70") {
				attach(child = CENTER, parent = BOT) {
					nut(spec = "M12", thickness = 10);
				}
			}
			screw(anchor = "origin", head = "hex", orient = BACK, spec = "M12,70") {
				attach(child = CENTER, parent = BOT) {
					nut(spec = "M12", thickness = 10);
				}
			}
		}
	}
}
