from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return np.sin(x) + 2*np.cos(y)

res = 100

x = np.linspace(-4,4, num=res)
y = np.linspace(-4,4, num=res)

x, y = np.meshgrid(x,y)

#llamando la funcion
z = f(x,y)

#graficando surpificie
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
                              #para darle con lo que impotamos
surf = ax.plot_surface(x,y,z, cmap=cm.cool)
#que muestre la superficie en grafica de surf
fig.colorbar(surf)