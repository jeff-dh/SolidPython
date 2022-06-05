from solid import *

#this imports (and enables) the extension
import childOptimizerExtension

#some SolidPython model to be optimized
c = cube(2)
m1 = cube(1) + sphere(2)
m2 = circle(5) + c + c + m1
model1 = m1 - m2 + m1.translateX(10)

#render (and optimize it)
print(model1)
