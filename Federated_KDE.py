import numpy as np
import matplotlib.pyplot as plt

class User:
    def __init__(self, x, y):
        self.location = np.array([x, y])  # d_i

    def compute_density_grid(self, grid, h):
        P, Q, _ = grid.shape
        out = np.zeros((P, Q))
        for p in range(P):       # Rows (Y)
            for q in range(Q):   # Columns (X)
                diff = self.location - grid[p, q]
                dist_sq = np.sum(diff ** 2)
                out[p, q] = np.exp(-dist_sq / (2 * h ** 2))
        return out


class Server:
    def __init__(self, x_min, y_min, x_max, y_max, h):
        self.h = h
        self.x_min, self.y_min = x_min, y_min
        self.x_max, self.y_max = x_max, y_max

        # Define grid
        self.x_vals = np.linspace(x_min, x_max, x_max - x_min)
        self.y_vals = np.linspace(y_min, y_max, y_max - y_min)
        grid_x, grid_y = np.meshgrid(self.x_vals, self.y_vals)
        self.grid = np.stack([grid_x, grid_y], axis=2)  # shape: (P, Q, 2)

        self.user_estimates = []

    def broadcast_grid(self):
        return self.grid, self.h

    def receive_estimate(self, user_grid):
        self.user_estimates.append(user_grid)

    def finalize_density(self):
        if not self.user_estimates:
            raise ValueError("No user estimates received.")
        self.density = np.mean(self.user_estimates, axis=0)

    def plot(self, user_locations):
        plt.imshow(self.density.T, extent=(self.x_min, self.x_max, self.y_min, self.y_max),
                   origin='lower', cmap='hot', aspect='auto')
        plt.colorbar(label='Estimated Density')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Federated KDE Estimate")

        if user_locations is not None:
            user_locations = np.array(user_locations)
            plt.scatter(user_locations[:, 0], user_locations[:, 1], c='blue', s=20, label='True User Locations')
            plt.legend()

        plt.show()


if __name__ == "__main__":
    # Initialize server
    server = Server(0, 0, 10, 10, h=1.0)

    # Simulate N users
    rng = np.random.default_rng(seed=4)
    user_locs = rng.uniform(0, 10, size=(1, 2))
    users = [User(x, y) for x, y in user_locs]

    # Federated KDE loop
    grid, h = server.broadcast_grid()
    for user in users:
        local_density = user.compute_density_grid(grid, h)  # local computation only
        server.receive_estimate(local_density)              # send result to server
        print("location: ", user.location)

    # Final aggregation and plot
    server.finalize_density()
    server.plot(user_locs)
