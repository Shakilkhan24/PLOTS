import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.io import show

# Functions for volume equations
def volume_equation1(x, y, z):
    sigma = 0.5
    values = np.exp(-(x**2 + y**2 + z**2) / (2 * sigma**2))
    return values

def volume_equation2(x, y, z):
    values = np.sin(x) * np.sin(y) * np.sin(z)
    return values

# Create volume plot
def create_volume_plot(eq_index):
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 2, 50)
    z = np.linspace(-2, 2, 50)
    x, y, z = np.meshgrid(x, y, z)
    
    if eq_index == 1:
        values = volume_equation1(x, y, z)
    elif eq_index == 2:
        values = volume_equation2(x, y, z)
    
    volume = go.Volume(
        x=x.flatten(), y=y.flatten(), z=z.flatten(), value=values.flatten(),
        isomin=0.1, isomax=1.0, opacity=0.1, surface_count=15
    )
    return volume

# Create subplots
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'volume'}]])

# Add initial plot
fig.add_trace(create_volume_plot(1))

# Define buttons for toggling between plots
buttons = []
for i in range(1, 3):  # Creating buttons for 2 equations
    buttons.append(dict(
        args=[{"visible": [i == j for j in range(1, 3)]}],
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
    title_text="3D Volume Plots with Toggle",
    scene=dict(aspectmode="cube")
)

# Add both plots to figure
for i in range(1, 3):
    fig.add_trace(create_volume_plot(i))

# Initially show only the first plot
fig.data[1].visible = False

show(fig)
