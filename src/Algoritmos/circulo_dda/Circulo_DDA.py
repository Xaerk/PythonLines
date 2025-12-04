
import math


def circulo_DDA(surface,xc,yc,r,color):

    r2 = r*r
    x = 0
    x2 = x*x
    y = r
    cuntdown = r2

    while (cuntdown > 0):
        cuntdown = r2 - x2
        yfloat = math.sqrt(r2 - x2)
        y = round(yfloat)
        #rendertime

        xr = xc + x
        yr = yc - y
        surface.set_at((xr,yr),color)
        xr = xc + x
        yr = yc + y
        surface.set_at((xr,yr),color)
        xr = xc - x
        yr = yc + y
        surface.set_at((xr,yr),color)
        xr = xc - x
        yr = yc - y
        surface.set_at((xr, yr), color)
        xr = xc + y
        yr = yc - x
        surface.set_at((xr,yr), color)
        xr = xc + y
        yr = yc + x
        surface.set_at((xr,yr), color)
        xr = xc - y
        yr = yc + x
        surface.set_at((xr,yr), color)
        xr = xc - y
        yr = yc - x
        surface.set_at((xr,yr), color)



        #print(f"({xr},{yr})")
        #print(cuntdown)

        x = x+1
        x2 = x * x


