from solid2 import CustomizerDropdownVariable, \
                   CustomizerSliderVariable, \
                   cube, scad_range, scad_for, scad_if

number_of_cubes = CustomizerSliderVariable("number_of_cubes", 7)
alt_color = CustomizerDropdownVariable("alt_color", "red", ["red", "blue", "green"])

def f_loop(i):
    c = scad_if(i % 2 == 0, cube(), cube().color(alt_color))
    return c.up(i*2)

scad_for(scad_range(0, number_of_cubes), f_loop).save_as_scad()
