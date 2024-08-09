# 3D Plotting with Plotly

This repository contains Python scripts that generate 3D Mesh, Surface, and Volume plots using Plotly. Each script includes multiple equations that can be toggled through buttons in the plot interface.

## Mesh3d Equations

The `Mesh/mesh.py` script generates 3D mesh plots based on the following equations:

1. **Equation 1:**  
   $`x = u \cdot \cos(v), \quad y = u \cdot \sin(v), \quad z = u`$
   
2. **Equation 2:**  
   $`x = \cos(u) \cdot \sin(v), \quad y = \sin(u) \cdot \sin(v), \quad z = \cos(v)`$
   
3. **Equation 3:**  
   $`x = u \cdot \cos(v), \quad y = u \cdot \sin(v), \quad z = \sin(u)`$
   
4. **Equation 4:**  
   $`x = \sin(u) \cdot \cos(v), \quad y = \sin(u) \cdot \sin(v), \quad z = \cos(u)`$
   
5. **Equation 5:**  
   $`x = u, \quad y = v, \quad z = \sin(u^2 + v^2)`$

You can explore these equations by running the [`Mesh/mesh.py`](Mesh/mesh.py) script.

## Surface Equations

The `Surface/surface.py` script generates 3D surface plots based on the following equations:

1. **Equation 1:**  
   $`z = \sin(x^2 + y^2)`$
   
2. **Equation 2:**  
   $`z = x^2 + y^2`$
   
3. **Equation 3:**  
   $`z = \sin(x) \cdot \cos(y)`$
   
4. **Equation 4:**  
   $`z = \exp(-x^2 - y^2)`$
   
5. **Equation 5:**  
   $`z = \cos(x^2 + y^2)`$

You can explore these equations by running the [`Surface/surface.py`](Surface/surface.py) script.

## Volume Equations

The `Volume/volume.py` script generates 3D volume plots based on the following equations:

1. **Equation 1:**  
   $`values = \exp\left(-\frac{x^2 + y^2 + z^2}{2 \cdot 0.5^2}\right)`$
   
2. **Equation 2:**  
   $`values = \sin(x) \cdot \sin(y) \cdot \sin(z)`$
   
3. **Equation 3:**  
   $`values = x^2 + y^2 + z^2`$
   
4. **Equation 4:**  
   $`values = \cos(x) \cdot \cos(y) \cdot \cos(z)`$
   
5. **Equation 5:**  
   $`values = \exp(-x^2 - y^2 - z^2)`$

You can explore these equations by running the [`Volume/volume.py`](Volume/volume.py) script.
