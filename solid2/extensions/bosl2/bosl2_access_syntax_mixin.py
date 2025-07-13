
from solid2.core.object_base import AccessSyntaxMixin as _AccessSyntaxMixin

class Bosl2AccessSyntaxMixin(_AccessSyntaxMixin):

    def _get_std(self):
        from . import std
        return std

    def move(self, v=None, p=None, **kwargs):
        return self._get_std().move(v, p, **kwargs)(self)

    def left(self, x=None, p=None, **kwargs):
        return self._get_std().left(x, p, **kwargs)(self)

    def right(self, x=None, p=None, **kwargs):
        return self._get_std().right(x, p, **kwargs)(self)

    def xmove(self, x=None, p=None, **kwargs):
        return self._get_std().xmove(x, p, **kwargs)(self)

    def fwd(self, y=None, p=None, **kwargs):
        return self._get_std().fwd(y, p, **kwargs)(self)

    def back(self, y=None, p=None, **kwargs):
        return self._get_std().back(y, p, **kwargs)(self)

    def ymove(self, y=None, p=None, **kwargs):
        return self._get_std().ymove(y, p, **kwargs)(self)

    def down(self, z=None, p=None, **kwargs):
        return self._get_std().down(z, p, **kwargs)(self)

    def up(self, z=None, p=None, **kwargs):
        return self._get_std().up(z, p, **kwargs)(self)

    def zmove(self, z=None, p=None, **kwargs):
        return self._get_std().zmove(z, p, **kwargs)(self)

    def rot(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, **kwargs):
        return self._get_std().rot(a, v, cp, _from, to, reverse, **kwargs)(self)

    def xrot(self, a=None, p=None, cp=None, **kwargs):
        return self._get_std().xrot(a, p, cp, **kwargs)(self)

    def yrot(self, a=None, p=None, cp=None, **kwargs):
        return self._get_std().yrot(a, p, cp, **kwargs)(self)

    def zrot(self, a=None, p=None, cp=None, **kwargs):
        return self._get_std().zrot(a, p, cp, **kwargs)(self)

    def tilt(self, to=None, cp=None, reverse=None, **kwargs):
        return self._get_std().tilt(to, cp, reverse, **kwargs)(self)

    def xscale(self, x=None, p=None, cp=None, **kwargs):
        return self._get_std().xscale(x, p, cp, **kwargs)(self)

    def yscale(self, y=None, p=None, cp=None, **kwargs):
        return self._get_std().yscale(y, p, cp, **kwargs)(self)

    def zscale(self, z=None, p=None, cp=None, **kwargs):
        return self._get_std().zscale(z, p, cp, **kwargs)(self)

    def xflip(self, p=None, x=None, **kwargs):
        return self._get_std().xflip(p, x, **kwargs)(self)

    def yflip(self, p=None, y=None, **kwargs):
        return self._get_std().yflip(p, y, **kwargs)(self)

    def zflip(self, p=None, z=None, **kwargs):
        return self._get_std().zflip(p, z, **kwargs)(self)

    def frame_map(self, x=None, y=None, z=None, p=None, reverse=None, **kwargs):
        return self._get_std().frame_map(x, y, z, p, reverse, **kwargs)(self)

    def skew(self, p=None, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, axy=None, axz=None, ayx=None, ayz=None, azx=None, azy=None, **kwargs):
        return self._get_std().skew(p, sxy, sxz, syx, syz, szx, szy, axy, axz, ayx, ayz, azx, azy, **kwargs)(self)

    def translate(self, v=None, **kwargs):
        return self._get_std().translate(v, **kwargs)(self)

    def rotate(self, a=None, v=None, **kwargs):
        return self._get_std().rotate(a, v, **kwargs)(self)

    def scale(self, v=None, **kwargs):
        return self._get_std().scale(v, **kwargs)(self)

    def multmatrix(self, m=None, **kwargs):
        return self._get_std().multmatrix(m, **kwargs)(self)

    def position(self, at=None, _from=None, **kwargs):
        return self._get_std().position(at, _from, **kwargs)(self)

    def orient(self, anchor=None, spin=None, **kwargs):
        return self._get_std().orient(anchor, spin, **kwargs)(self)

    def align(self, anchor=None, align=None, inside=None, inset=None, shiftout=None, overlap=None, **kwargs):
        return self._get_std().align(anchor, align, inside, inset, shiftout, overlap, **kwargs)(self)

    def attach(self, parent=None, child=None, overlap=None, align=None, spin=None, norot=None, inset=None, shiftout=None, inside=None, _from=None, to=None, **kwargs):
        return self._get_std().attach(parent, child, overlap, align, spin, norot, inset, shiftout, inside, _from, to, **kwargs)(self)

    def attach_part(self, name=None, **kwargs):
        return self._get_std().attach_part(name, **kwargs)(self)

    def tag(self, tag=None, **kwargs):
        return self._get_std().tag(tag, **kwargs)(self)

    def tag_this(self, tag=None, **kwargs):
        return self._get_std().tag_this(tag, **kwargs)(self)

    def force_tag(self, tag=None, **kwargs):
        return self._get_std().force_tag(tag, **kwargs)(self)

    def default_tag(self, tag=None, do_tag=None, **kwargs):
        return self._get_std().default_tag(tag, do_tag, **kwargs)(self)

    def tag_scope(self, scope=None, **kwargs):
        return self._get_std().tag_scope(scope, **kwargs)(self)

    def diff(self, remove=None, keep=None, **kwargs):
        return self._get_std().diff(remove, keep, **kwargs)(self)

    def tag_diff(self, tag=None, remove=None, keep=None, **kwargs):
        return self._get_std().tag_diff(tag, remove, keep, **kwargs)(self)

    def intersect(self, intersect=None, keep=None, **kwargs):
        return self._get_std().intersect(intersect, keep, **kwargs)(self)

    def tag_intersect(self, tag=None, intersect=None, keep=None, **kwargs):
        return self._get_std().tag_intersect(tag, intersect, keep, **kwargs)(self)

    def conv_hull(self, keep=None, **kwargs):
        return self._get_std().conv_hull(keep, **kwargs)(self)

    def tag_conv_hull(self, tag=None, keep=None, **kwargs):
        return self._get_std().tag_conv_hull(tag, keep, **kwargs)(self)

    def hide(self, tags=None, **kwargs):
        return self._get_std().hide(tags, **kwargs)(self)

    def hide_this(self, **kwargs):
        return self._get_std().hide_this(**kwargs)(self)

    def show_only(self, tags=None, **kwargs):
        return self._get_std().show_only(tags, **kwargs)(self)

    def show_all(self, **kwargs):
        return self._get_std().show_all(**kwargs)(self)

    def show_int(self, tags=None, **kwargs):
        return self._get_std().show_int(tags, **kwargs)(self)

    def face_mask(self, faces=None, **kwargs):
        return self._get_std().face_mask(faces, **kwargs)(self)

    def edge_mask(self, edges=None, _except=None, **kwargs):
        return self._get_std().edge_mask(edges, _except, **kwargs)(self)

    def corner_mask(self, corners=None, _except=None, **kwargs):
        return self._get_std().corner_mask(corners, _except, **kwargs)(self)

    def face_profile(self, faces=None, r=None, d=None, excess=None, convexity=None, **kwargs):
        return self._get_std().face_profile(faces, r, d, excess, convexity, **kwargs)(self)

    def edge_profile(self, edges=None, _except=None, excess=None, convexity=None, **kwargs):
        return self._get_std().edge_profile(edges, _except, excess, convexity, **kwargs)(self)

    def edge_profile_asym(self, edges=None, _except=None, excess=None, convexity=None, flip=None, corner_type=None, size=None, **kwargs):
        return self._get_std().edge_profile_asym(edges, _except, excess, convexity, flip, corner_type, size, **kwargs)(self)

    def corner_profile(self, corners=None, _except=None, r=None, d=None, convexity=None, **kwargs):
        return self._get_std().corner_profile(corners, _except, r, d, convexity, **kwargs)(self)

    def attachable(self, anchor=None, spin=None, orient=None, size=None, size2=None, shift=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, path=None, region=None, extent=None, cp=None, offset=None, anchors=None, two_d=None, axis=None, override=None, geom=None, parts=None, expose_tags=None, keep_color=None, **kwargs):
        return self._get_std().attachable(anchor, spin, orient, size, size2, shift, r, r1, r2, d, d1, d2, l, h, vnf, path, region, extent, cp, offset, anchors, two_d, axis, override, geom, parts, expose_tags, keep_color, **kwargs)(self)

    def show_anchors(self, s=None, std=None, custom=None, **kwargs):
        return self._get_std().show_anchors(s, std, custom, **kwargs)(self)

    def anchor_arrow(self, s=None, color=None, flag=None, _tag=None, _fn=None, anchor=None, spin=None, orient=None, **kwargs):
        return self._get_std().anchor_arrow(s, color, flag, _tag, _fn, anchor, spin, orient, **kwargs)(self)

    def anchor_arrow2d(self, s=None, color=None, _tag=None, **kwargs):
        return self._get_std().anchor_arrow2d(s, color, _tag, **kwargs)(self)

    def expose_anchors(self, opacity=None, **kwargs):
        return self._get_std().expose_anchors(opacity, **kwargs)(self)

    def show_transform_list(self, tlist=None, s=None, **kwargs):
        return self._get_std().show_transform_list(tlist, s, **kwargs)(self)

    def generic_airplane(self, s=None, **kwargs):
        return self._get_std().generic_airplane(s, **kwargs)(self)

    def frame_ref(self, s=None, opacity=None, **kwargs):
        return self._get_std().frame_ref(s, opacity, **kwargs)(self)

    def restore(self, desc=None, **kwargs):
        return self._get_std().restore(desc, **kwargs)(self)

    def desc_copies(self, transforms=None, **kwargs):
        return self._get_std().desc_copies(transforms, **kwargs)(self)

    def extrude_from_to(self, pt1=None, pt2=None, convexity=None, twist=None, scale=None, slices=None, **kwargs):
        return self._get_std().extrude_from_to(pt1, pt2, convexity, twist, scale, slices, **kwargs)(self)

    def path_extrude2d(self, path=None, caps=None, closed=None, s=None, convexity=None, **kwargs):
        return self._get_std().path_extrude2d(path, caps, closed, s, convexity, **kwargs)(self)

    def path_extrude(self, path=None, convexity=None, clipsize=None, **kwargs):
        return self._get_std().path_extrude(path, convexity, clipsize, **kwargs)(self)

    def cylindrical_extrude(self, ir=None, _or=None, od=None, id=None, size=None, convexity=None, spin=None, orient=None, **kwargs):
        return self._get_std().cylindrical_extrude(ir, _or, od, id, size, convexity, spin, orient, **kwargs)(self)

    def bounding_box(self, excess=None, planar=None, **kwargs):
        return self._get_std().bounding_box(excess, planar, **kwargs)(self)

    def chain_hull(self, **kwargs):
        return self._get_std().chain_hull(**kwargs)(self)

    def minkowski_difference(self, planar=None, **kwargs):
        return self._get_std().minkowski_difference(planar, **kwargs)(self)

    def offset3d(self, r=None, size=None, convexity=None, **kwargs):
        return self._get_std().offset3d(r, size, convexity, **kwargs)(self)

    def round3d(self, r=None, _or=None, ir=None, size=None, **kwargs):
        return self._get_std().round3d(r, _or, ir, size, **kwargs)(self)

    def move_copies(self, a=None, **kwargs):
        return self._get_std().move_copies(a, **kwargs)(self)

    def xcopies(self, spacing=None, n=None, l=None, sp=None, **kwargs):
        return self._get_std().xcopies(spacing, n, l, sp, **kwargs)(self)

    def ycopies(self, spacing=None, n=None, l=None, sp=None, **kwargs):
        return self._get_std().ycopies(spacing, n, l, sp, **kwargs)(self)

    def zcopies(self, spacing=None, n=None, l=None, sp=None, **kwargs):
        return self._get_std().zcopies(spacing, n, l, sp, **kwargs)(self)

    def line_of(self, spacing=None, n=None, l=None, p1=None, p2=None, **kwargs):
        return self._get_std().line_of(spacing, n, l, p1, p2, **kwargs)(self)

    def line_copies(self, spacing=None, n=None, l=None, p1=None, p2=None, **kwargs):
        return self._get_std().line_copies(spacing, n, l, p1, p2, **kwargs)(self)

    def grid2d(self, spacing=None, n=None, size=None, stagger=None, inside=None, nonzero=None, **kwargs):
        return self._get_std().grid2d(spacing, n, size, stagger, inside, nonzero, **kwargs)(self)

    def grid_copies(self, spacing=None, n=None, size=None, stagger=None, inside=None, nonzero=None, axes=None, **kwargs):
        return self._get_std().grid_copies(spacing, n, size, stagger, inside, nonzero, axes, **kwargs)(self)

    def rot_copies(self, rots=None, v=None, cp=None, n=None, sa=None, offset=None, delta=None, subrot=None, **kwargs):
        return self._get_std().rot_copies(rots, v, cp, n, sa, offset, delta, subrot, **kwargs)(self)

    def xrot_copies(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
        return self._get_std().xrot_copies(rots, cp, n, sa, r, d, subrot, **kwargs)(self)

    def yrot_copies(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
        return self._get_std().yrot_copies(rots, cp, n, sa, r, d, subrot, **kwargs)(self)

    def zrot_copies(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
        return self._get_std().zrot_copies(rots, cp, n, sa, r, d, subrot, **kwargs)(self)

    def arc_of(self, n=None, r=None, rx=None, ry=None, d=None, dx=None, dy=None, sa=None, ea=None, rot=None, **kwargs):
        return self._get_std().arc_of(n, r, rx, ry, d, dx, dy, sa, ea, rot, **kwargs)(self)

    def arc_copies(self, n=None, r=None, rx=None, ry=None, d=None, dx=None, dy=None, sa=None, ea=None, rot=None, **kwargs):
        return self._get_std().arc_copies(n, r, rx, ry, d, dx, dy, sa, ea, rot, **kwargs)(self)

    def ovoid_spread(self, n=None, r=None, d=None, cone_ang=None, scale=None, perp=None, **kwargs):
        return self._get_std().ovoid_spread(n, r, d, cone_ang, scale, perp, **kwargs)(self)

    def sphere_copies(self, n=None, r=None, d=None, cone_ang=None, scale=None, perp=None, **kwargs):
        return self._get_std().sphere_copies(n, r, d, cone_ang, scale, perp, **kwargs)(self)

    def path_spread(self, path=None, n=None, spacing=None, sp=None, rotate_children=None, dist=None, closed=None, **kwargs):
        return self._get_std().path_spread(path, n, spacing, sp, rotate_children, dist, closed, **kwargs)(self)

    def path_copies(self, path=None, n=None, spacing=None, sp=None, dist=None, rotate_children=None, closed=None, **kwargs):
        return self._get_std().path_copies(path, n, spacing, sp, dist, rotate_children, closed, **kwargs)(self)

    def xflip_copy(self, offset=None, x=None, **kwargs):
        return self._get_std().xflip_copy(offset, x, **kwargs)(self)

    def yflip_copy(self, offset=None, y=None, **kwargs):
        return self._get_std().yflip_copy(offset, y, **kwargs)(self)

    def zflip_copy(self, offset=None, z=None, **kwargs):
        return self._get_std().zflip_copy(offset, z, **kwargs)(self)

    def mirror_copy(self, v=None, offset=None, cp=None, **kwargs):
        return self._get_std().mirror_copy(v, offset, cp, **kwargs)(self)

    def xdistribute(self, spacing=None, sizes=None, l=None, **kwargs):
        return self._get_std().xdistribute(spacing, sizes, l, **kwargs)(self)

    def ydistribute(self, spacing=None, sizes=None, l=None, **kwargs):
        return self._get_std().ydistribute(spacing, sizes, l, **kwargs)(self)

    def zdistribute(self, spacing=None, sizes=None, l=None, **kwargs):
        return self._get_std().zdistribute(spacing, sizes, l, **kwargs)(self)

    def distribute(self, spacing=None, sizes=None, dir=None, l=None, **kwargs):
        return self._get_std().distribute(spacing, sizes, dir, l, **kwargs)(self)

    def half_of(self, v=None, cp=None, s=None, planar=None, **kwargs):
        return self._get_std().half_of(v, cp, s, planar, **kwargs)(self)

    def left_half(self, s=None, x=None, planar=None, **kwargs):
        return self._get_std().left_half(s, x, planar, **kwargs)(self)

    def right_half(self, s=None, x=None, planar=None, **kwargs):
        return self._get_std().right_half(s, x, planar, **kwargs)(self)

    def front_half(self, s=None, y=None, planar=None, **kwargs):
        return self._get_std().front_half(s, y, planar, **kwargs)(self)

    def back_half(self, s=None, y=None, planar=None, **kwargs):
        return self._get_std().back_half(s, y, planar, **kwargs)(self)

    def bottom_half(self, s=None, z=None, **kwargs):
        return self._get_std().bottom_half(s, z, **kwargs)(self)

    def top_half(self, s=None, z=None, **kwargs):
        return self._get_std().top_half(s, z, **kwargs)(self)

    def partition_mask(self, l=None, w=None, h=None, cutsize=None, cutpath=None, gap=None, cutpath_centered=None, inverse=None, anchor=None, spin=None, orient=None, **kwargs):
        return self._get_std().partition_mask(l, w, h, cutsize, cutpath, gap, cutpath_centered, inverse, anchor, spin, orient, **kwargs)(self)

    def partition_cut_mask(self, l=None, h=None, cutsize=None, cutpath=None, gap=None, cutpath_centered=None, anchor=None, spin=None, orient=None, **kwargs):
        return self._get_std().partition_cut_mask(l, h, cutsize, cutpath, gap, cutpath_centered, anchor, spin, orient, **kwargs)(self)

    def partition(self, size=None, spread=None, cutsize=None, cutpath=None, gap=None, cutpath_centered=None, spin=None, **kwargs):
        return self._get_std().partition(size, spread, cutsize, cutpath, gap, cutpath_centered, spin, **kwargs)(self)

    def recolor(self, c=None, **kwargs):
        return self._get_std().recolor(c, **kwargs)(self)

    def color_this(self, c=None, **kwargs):
        return self._get_std().color_this(c, **kwargs)(self)

    def rainbow(self, list=None, stride=None, maxhues=None, shuffle=None, seed=None, **kwargs):
        return self._get_std().rainbow(list, stride, maxhues, shuffle, seed, **kwargs)(self)

    def color_overlaps(self, color=None, **kwargs):
        return self._get_std().color_overlaps(color, **kwargs)(self)

    def highlight(self, highlight=None, **kwargs):
        return self._get_std().highlight(highlight, **kwargs)(self)

    def highlight_this(self, **kwargs):
        return self._get_std().highlight_this(**kwargs)(self)

    def ghost(self, ghost=None, **kwargs):
        return self._get_std().ghost(ghost, **kwargs)(self)

    def ghost_this(self, **kwargs):
        return self._get_std().ghost_this(**kwargs)(self)

    def hsl(self, h=None, s=None, l=None, a=None, **kwargs):
        return self._get_std().hsl(h, s, l, a, **kwargs)(self)

    def hsv(self, h=None, s=None, v=None, a=None, **kwargs):
        return self._get_std().hsv(h, s, v, a, **kwargs)(self)
