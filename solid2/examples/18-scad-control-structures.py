from solid2 import cube, get_animation_time, scad_for, scad_if, scad_range

cubes_stacked = scad_for(scad_range(0, 7), lambda i: cube(1).up(i*2))

c = cube(3).left(5)
cube_blinking = scad_if(get_animation_time() < 0.5, c, c.color("red"))

(cubes_stacked + cube_blinking).save_as_scad()

