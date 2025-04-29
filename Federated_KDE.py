import pandas as pd
import numpy as np
class User:
    def __init__(self, d):
        self.D = pd.Series() # What exactly would the user's location vector look like?

    # Evaluates G_h(d_i)
    def evaluate(self, d_i):

    def gaussianKernel(self, ):
    # Return evaluations to the server
    def updateServer(self, destination, ):
        Server(destination)

class Server:
    def __init__(self, corner1, corner2, h):
        self.h = h




PxQ =
if __name__ == "__main__":

    d1, d2, di_1, di = (1, 1), (2, 2), (3, 3), (4, 4)
    grid_x, grid_y = np.meshgrid(x, y)
    grid_coords = np.vstack([grid_x.ravel(), grid_y.ravel()]).T

    # Inputs
    N = [User(d1), User(d2), ..., User(di_1), User(di)]
    for user in N: # Running in parallel
        user.evaluate()
        user.returnToServer()
