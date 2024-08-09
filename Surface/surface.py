import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.io import show

# Functions for surface equations
def surface_equation1(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

def surface_equation2(x, y):
    return x**2 + y**2

# Create surface plot
def create_surface_plot(eq_index):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    
    if eq_index == 1:
        z = surface_equation1(x, y)
    elif eq_index == 2:
        z = surface_equation2(x, y)
    
    return go.Surface(z=z, x=x, y=y, colorscale='Viridis', visible=(eq_index == 1))

# Create subplots
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

# Add both surface plots to the figure
fig.add_trace(create_surface_plot(1))
fig.add_trace(create_surface_plot(2))

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
    title_text="3D Surface Plots with Toggle",
    scene=dict(aspectmode="cube")
)

show(fig)
