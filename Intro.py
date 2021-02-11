from tkinter import *
import numpy as np
import pygame
import matplotlib.pyplot as plt
from itertools import product, combinations
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Application(Frame):

    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg="thistle3")
        self.v = IntVar(root, 0)

        Label(root, text="""Elija una opcion:""", font="Times 20", justify=LEFT, bg="thistle3", padx=20, pady=20).pack()

        Radiobutton(root, text="Punto", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=1,
                    command=self.crear_punto).pack(anchor=W)

        Radiobutton(root, text="Linea", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=2,
                    command=self.crear_linea).pack(anchor=W)

        Radiobutton(root, text="Circulo", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=3,
                    command=self.crear_circulo).pack(anchor=W)

        Radiobutton(root, text="Poligonos", padx=150, font="Times 14 italic", bg="thistle3", variable=self.v, value=4,
                    command=self.crear_poligono).pack(anchor=W)

        Radiobutton(root, text="Figura Geometrica", font="Times 14 italic", bg="thistle3", padx=150, variable=self.v,
                    value=5, command=self.crear_geometricas).pack(anchor=W)

        Radiobutton(root, text="Dibujo c:", font="Times 14 italic", bg="thistle3", padx=150, variable=self.v, value=6,
                    command=self.dibujar).pack(anchor=W)

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

# Nuevo codigo agregado usando libreria de pygame para dibujar una casa usando figuras geometricas basicas

    def dibujar(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))

        def draw_tree(x, y):
            pygame.draw.rect(screen, (117, 90, 0), (x+12, y - 100, 25, 100))
            pygame.draw.circle(screen, (27, 117, 0), (x + 25, y - 120), 50)

        def draw_house(x, y):
            pygame.draw.rect(screen, (159, 199, 50), (x, y-180, 200, 180))
            pygame.draw.rect(screen, (89, 71, 0), (x+80, y-60, 40, 60))
            pygame.draw.circle(screen, (255, 204, 0), (x+112, y-30), 4)
            pygame.draw.polygon(screen, (199, 80, 50), ((x, y - 180), (x + 100, y - 250), (x + 200, y - 180)))
            draw_window(x + 20, y - 90)
            draw_window(x + 130, y - 90)
            draw_window(x + 20, y - 20)
            draw_window(x + 130, y - 20)

        def draw_window(x, y):
            pygame.draw.rect(screen, (255, 244, 128), (x, y-50, 50, 50))
            pygame.draw.rect(screen, (0, 0, 0), (x, y-50, 50, 50), 5)
            pygame.draw.rect(screen, (0, 0, 0), (x+23, y-50, 5, 50))
            pygame.draw.rect(screen, (0, 0, 0), (x, y-27, 50, 5))

        def draw_cloud(x, y, size):
            pygame.draw.circle(screen, (255, 255, 255), (x, y), int(size * .5))
            pygame.draw.circle(screen, (255, 255, 255), (int(x + size * .5), y), int(size * .6))
            pygame.draw.circle(screen, (255, 255, 255), (x + size, int(y - size * .1)), int(size * .4))

        pygame.draw.rect(screen, (0, 160, 3), (0, 400, 640, 80))
        pygame.draw.rect(screen, (135, 255, 255), (0, 0, 640, 400))

        draw_tree(60, 400)
        draw_tree(550, 400)

        draw_house(225, 400)

        draw_cloud(60, 120, 80)
        draw_cloud(200, 50, 40)
        draw_cloud(450, 100, 120)
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


root = Tk()
root.geometry("725x300")
root.config(bg="thistle3")
root.resizable(False, False)
root.title("Animation")
app = Application()
# mainloop
mainloop()
