import numpy as np

class User:
    p, q, h = None, None, None

    def __init__(self, p, q):
        self.p = p
        self.q = q

    # Evaluates G_h(d_i)
    def evaluate_G(self, d_i, h):

    def gaussianKernel(self, ):
    # Return evaluations to the server
    def updateServer(self, destination, ):
        Server(destination)

class Server:
    h = None
    grid_cords = None

    def __init__(self, corner1_x, corner1_y, corner2_x, corner2_y, h):
        self.h = h

        x_vals = np.linspace(corner1_x, corner2_x, abs(corner2_x - corner1_x))
        y_vals = np.linspace(corner1_y, corner2_y, abs(corner2_y - corner1_y))

        grid_x, grid_y = np.meshgrid(x_vals, y_vals)
        self.grid_cords = np.vstack([grid_x.ravel(), grid_y.ravel()]).T


def federated_KDE(user_locations, server):

    for user in N: # Running in parallel
        user.evaluate_G()
        user.returnToServer()
PxQ =
if __name__ == "__main__":

    # Inputs
    x, y = np.linspace(-5, 5, 50), np.linspace(-5, 5, 50)
    grid_p, grid_q = np.meshgrid(x, y)
    grid_cords = np.vstack([grid_p.ravel(), grid_q.ravel()]).T
    N = [User(1, 1), User(1, 2), ..., User(4, 4), User(5, 5)]

    # Server Initialization
    server = Server(0, 0, 10, 10, 1)


    federated_KDE(N, server)

    server.recieve()