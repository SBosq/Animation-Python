from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.linalg import norm


class Application(Frame):

    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg="thistle3")
        self.v = IntVar(root, 1)

        Label(root, text="""Choose a programming language:""", font="Times 20", justify=LEFT, bg="thistle3", padx=20, pady=20).pack()

        Radiobutton(root, text="Punto", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=1, command=self.crear_punto).pack(anchor=W)

        Radiobutton(root, text="Linea", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=2, command=self.crear_linea).pack(anchor=W)

        Radiobutton(root, text="Circulo", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=3, command=self.crear_circulo).pack(anchor=W)

        Radiobutton(root, text="Poligonos", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=4, command=self.crear_poligono).pack(anchor=W)

        Radiobutton(root, text="Figura Geometrica", font="Times 14 italic", bg="thistle3", padx=150, variable=self.v, value=5, command=self.crear_geometricas).pack(anchor=W)

    def crear_linea(self):
        VecStart_x = [0, 1, 3, 5]
        VecStart_y = [2, 2, 5, 5]
        VecStart_z = [0, 1, 1, 5]
        VecEnd_x = [1, 2, -1, 6]
        VecEnd_y = [3, 1, -2, 7]
        VecEnd_z = [1, 0, 4, 9]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(4):
            ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i], VecEnd_y[i]], zs=[VecStart_z[i], VecEnd_z[i]])
        plt.show()

    def crear_punto(self):
        np.random.seed(19680801)

        def randrange(n, vmin, vmax):
            '''
            Helper function to make an array of random numbers having shape (n, )
            with each number distributed Uniform(vmin, vmax).
            '''
            return (vmax - vmin) * np.random.rand(n) + vmin

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        n = 100

        # For each set of style and range settings, plot n random points in the box
        # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
            xs = randrange(n, 23, 32)
            ys = randrange(n, 0, 100)
            zs = randrange(n, zlow, zhigh)
            ax.scatter(xs, ys, zs, marker=m)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()

    def crear_circulo(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect("auto")
        # draw sphere
        u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
        x = np.cos(u) * np.sin(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(v)
        ax.plot_wireframe(x, y, z, color="green")
        plt.show()

    def crear_poligono(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        x = [0, 1, 1, 0]
        y = [0, 0, 1, 1]
        z = [0, 1, 0, 1]
        verts = [list(zip(x, y, z))]
        ax.add_collection3d(Poly3DCollection(verts))
        plt.show()

    def crear_geometricas(self):
        """p0 = np.array([1, 3, 2])
        p1 = np.array([8, 5, 9])
        R = 5

        v = p1 - p0

        mag = norm(v)

        v = v / mag

        not_v = np.array([1, 0, 0])
        if (v == not_v).all():
            not_v = np.array([0, 1, 0])

        n1 = np.cross(v, not_v)

        n1 /= norm(n1)


        n2 = np.cross(v, n1)

        t = np.linspace(0, mag, 2)
        theta = np.linspace(0, 2 * np.pi, 100)
        rsample = np.linspace(0, R, 2)

        t, theta2 = np.meshgrid(t, theta)

        rsample, theta = np.meshgrid(rsample, theta)

        X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta2) * n1[i] + R * np.cos(theta2) * n2[i] for i in [0, 1, 2]]

        X2, Y2, Z2 = [p0[i] + rsample[i] * np.sin(theta) * n1[i] + rsample[i] * np.cos(theta) * n2[i] for i in [0, 1, 2]]

        X3, Y3, Z3 = [p0[i] + v[i] * mag + rsample[i] * np.sin(theta) * n1[i] + rsample[i] * np.cos(theta) * n2[i] for i in [0, 1, 2]]

        ax = plt.subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, color='blue')
        ax.plot_surface(X2, Y2, Z2, color='blue')
        ax.plot_surface(X3, Y3, Z3, color='blue')

        plt.show()"""

        def data_for_cylinder_along_z(center_x, center_y, radius, height_z):
            z = np.linspace(0, height_z, 50)
            theta = np.linspace(0, 2 * np.pi, 50)
            theta_grid, z_grid = np.meshgrid(theta, z)
            x_grid = radius * np.cos(theta_grid) + center_x
            y_grid = radius * np.sin(theta_grid) + center_y
            return x_grid, y_grid, z_grid

        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        Xc, Yc, Zc = data_for_cylinder_along_z(0.2, 0.2, 0.05, 0.1)
        ax.plot_surface(Xc, Yc, Zc, alpha=0.5)

        plt.show()


root = Tk()
root.geometry("725x300")
root.config(bg="thistle3")
root.resizable(False, False)
root.title("Animation")
app = Application()
# mainloop
mainloop()
