from solid import *
from exportReturnValueAsModuleExtension import exportReturnValueAsModule

@exportReturnValueAsModule
def blub(a, children):
    #this does not "compile", because you can't compare / evaluate a ScadValue
    #because it's value is unknown at python runtime
    #if a == 1:
    #    assert(False)

    return circle(a) + \
           translate(0, 5, 0)(children(0)) + \
           translate(0, -5, 0)(children(1))


import time
myChildModel = square(2)

myModel = union()
myModel += translate(10, 0, 0)(blub(3, myChildModel, myChildModel))
myModel += translate(20, 0, 0)(blub(4))
myModel += translate(30, 0, 0)(blub(time.time()%10, myChildModel))

#render scad code
print(scad_render(myModel))

