import numpy as np

points = np.arange(0,1, .05)

##cubic bezier equation: B(t) = (1-t)^3
start_point = np.array([0,0])
control_1 = np.array([])
control_2 = np.array([])
end_point = np.array([])

