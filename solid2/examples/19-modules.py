#! /usr/bin/env python

from solid2 import cube, cylinder, difference, module, set_global_fn, sphere, translate

set_global_fn(72)

# Example 1: Module with custom name
# Create a complex shape that we'll reuse multiple times
complex_shape = difference()(
    cube([10, 10, 10]), sphere(6), cylinder(r=2, h=12, center=True)
)

# Wrap it in a module for performance
my_module = module(complex_shape, name="complex_shape")

# Use the module multiple times with transformations
scene = (
    my_module()
    + my_module().translate([15, 0, 0])
    + my_module().translate([0, 15, 0])
    + my_module().translate([15, 15, 0])
)

scene.save_as_scad()

# When you run this, you'll see that the module definition appears once at the top
# of the generated SCAD file, and then it's instantiated 4 times.
# This is more efficient than repeating the entire geometry 4 times!
#
# Generated SCAD will look like:
#
# module complex_shape() {
#     difference() {
#         cube(size = [10, 10, 10]);
#         sphere(r = 6);
#         cylinder(r = 2, h = 12, center = true);
#     }
# }
#
# complex_shape();
# translate(v = [15, 0, 0]) {
#     complex_shape();
# }
# ... etc


# Example 2: Module with auto-generated name
# If you don't specify a name, a stable name is generated based on content hash
gear_shape = cylinder(r=5, h=2)
gear_module = module(gear_shape)  # Name will be like "mod_a3f2c1b8"

# Example 2b: Module with custom prefix
# You can customize the prefix for auto-generated names
gear_with_prefix = module(
    gear_shape, name_prefix="gear"
)  # Name will be like "gear_a3f2c1b8"

# Example 3: Multiple modules
wheel = cylinder(r=3, h=1)
axle = cylinder(r=0.5, h=10, center=True)

wheel_mod = module(wheel, name="wheel")
axle_mod = module(axle, name="axle")

# Build a simple car with 4 wheels and 2 axles
car = (
    wheel_mod().translate([0, 0, 0])
    + wheel_mod().translate([8, 0, 0])
    + wheel_mod().translate([0, 6, 0])
    + wheel_mod().translate([8, 6, 0])
    + axle_mod().translate([4, 0, 0])
    + axle_mod().translate([4, 6, 0])
)
