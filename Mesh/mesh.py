import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.io import show

# Functions for mesh equations
def mesh_equation1(u, v):
    x = u * np.cos(v)
    y = u * np.sin(v)
    z = u
    return x, y, z

def mesh_equation2(u, v):
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    return x, y, z

# Create mesh3d plot
def create_mesh_plot(eq_index):
    u = np.linspace(0, 1, 30)
    v = np.linspace(0, 2 * np.pi, 30)
    u, v = np.meshgrid(u, v)
    
    if eq_index == 1:
        x, y, z = mesh_equation1(u, v)
    elif eq_index == 2:
        x, y, z = mesh_equation2(u, v)
    
    return go.Mesh3d(x=x.flatten(), y=y.flatten(), z=z.flatten(), color='lightblue', opacity=0.50, visible=(eq_index == 1))

# Create subplots
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'mesh3d'}]])

# Add both mesh plots to the figure
fig.add_trace(create_mesh_plot(1))
fig.add_trace(create_mesh_plot(2))

# Initially, hide the second plot
fig.data[1].visible = False

# Define buttons for toggling between plots
buttons = []
for i in range(1, 3):
    buttons.append(dict(
        args=[{"visible": [i == j + 1 for j in range(2)]}],
        label=f"Equation {i}",
        method="update"
    ))

# Add buttons to layout
fig.update_layout(
    updatemenus=[dict(
        type="buttons",
        direction="right",
        buttons=buttons,
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.1,
        yanchor="top"
    )],
    title_text="3D Mesh Plots with Toggle",
    scene=dict(aspectmode="cube")
)

show(fig)
