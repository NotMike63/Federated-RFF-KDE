import numpy as np
import matplotlib.pyplot as plt

class User:
    def __init__(self, x, y, B, h):
        self.location = np.array([x, y])
        self.B = B
        self.h = h
        self.omega = np.random.normal(loc=0.0, scale=1.0 / h, size=(B, 2))  # B x 2

    # KDE with a Gaussian kernel
    def gaussian_KDE(self, ):
        gauss_numerator = abs(self.location[0] - self.location[1])
        np.e(gauss_numerator / (2 * self.h))
        pass

    # Calculates Probability Matrix
    def gh(self, grid):
        for p in range(grid.shape[0]):
            for q in range(grid.shape[1]):
                gaussian_KDE()

    def compute_rff_density_grid(self, grid):
        P, Q, _ = grid.shape
        out = np.zeros((P, Q))

        for b in range(self.B):
            w = self.omega[b]
            dot_user = np.dot(w, self.location)

            for p in range(P):
                for q in range(Q):
                    gpq = grid[p, q]
                    dot_grid = np.dot(w, gpq)
                    phi = np.cos(dot_grid - dot_user)
                    out[p, q] += phi

        return out


class Server:
    def __init__(self, x_min, y_min, x_max, y_max, h, B):
        self.h = h
        self.B = B
        self.x_min, self.y_min = x_min, y_min
        self.x_max, self.y_max = x_max, y_max

        # Define grid
        self.x_vals = np.linspace(x_min, x_max, x_max - x_min)
        self.y_vals = np.linspace(y_min, y_max, y_max - y_min)
        grid_x, grid_y = np.meshgrid(self.x_vals, self.y_vals)
        self.grid = np.stack([grid_x, grid_y], axis=2)  # shape: (P, Q, 2)

        self.user_estimates = []

    def broadcast_grid_and_params(self):
        return self.grid, self.h, self.B

    def receive_estimate(self, user_grid):
        self.user_estimates.append(user_grid)

    def finalize_density(self):
        if not self.user_estimates:
            raise ValueError("No user estimates received.")
        self.density = np.mean(self.user_estimates, axis=0) / self.B

    def plot(self, user_locations):
        plt.imshow(self.density, extent=(self.x_min, self.x_max, self.y_min, self.y_max),
                   origin='lower', cmap='hot', aspect='auto')
        plt.colorbar(label='Estimated Density')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(f"Federated RFF KDE Estimate (B={self.B})")

        if user_locations is not None:
            user_locations = np.array(user_locations)
            plt.scatter(user_locations[:, 0], user_locations[:, 1], c='blue', s=20, label='True User Locations')
            plt.legend()

        plt.show()


if __name__ == "__main__":
    # Server parameters
    B = 10  # number of random features
    h = 20.0
    server = Server(0, 0, 100, 100, h=h, B=B)

    # Simulate N users
    rng = np.random.default_rng(seed=4)
    user_locs = rng.uniform(0, 100, size=(5, 2))
    users = [User(x, y, B=B, h=h) for x, y in user_locs]

    # Federated RFF KDE loop
    grid, h, B = server.broadcast_grid_and_params()
    for user in users:
        local_density = user.compute_rff_density_grid(grid)
        server.receive_estimate(local_density)
        #print("location:", user.location)

    # Final aggregation and plot
    server.finalize_density()
    server.plot(user_locs)


