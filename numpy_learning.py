# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(np_baseball)


# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# baseball is available as a regular list of lists

# # Import numpy package
# import numpy as np
#
# # Create np_baseball (2 cols)
# np_baseball = np.array(baseball)
#
# # Print out the 50th row of np_baseball
# print(np_baseball[49,:])
#
# # Select the entire second column of np_baseball: np_weight_lb
# np_weight_lb = np_baseball[:,1]
#
# # Print out height of 124th player
# print(np_baseball[123,0])

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat
