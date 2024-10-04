import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Set up initial data
start_percentage = 60  # Start at 60%
end_percentage = 100  # End at 100%
duration = 4  # Duration of the animation in seconds
fps = 30  # Frames per second

# Number of frames in the animation
frames = duration * fps

# Set up the pie chart colors
colors = ['blue', 'lightgrey']

# Create figure and axis with custom size (e.g., 6x6 inches)
fig, ax = plt.subplots(figsize=(19.20/2, 10.8/2))
ax.set_aspect('equal')  # Keep the pie chart circular

# Function to create the pie chart for each frame
def update(frame):
    ax.clear()
    # Interpolate between start and end percentages
    percentage = np.linspace(start_percentage, end_percentage, frames)[frame]
    
    # Data for pie chart (percentage voted and remaining)
    data = [percentage, 100 - percentage]
    
    # Plot pie chart
    wedges, texts = ax.pie(data, colors=colors, startangle=90, counterclock=False)
    
    # Add label to "I Voted" part with larger text
    ax.text(0, 0, f'I Voted\n{int(percentage)}%', color='white', fontsize=20,  # Larger text size
            ha='center', va='center', weight='bold')

# Set up the animation
ani = FuncAnimation(fig, update, frames=frames, repeat=False, interval=1000/fps)

# Save the animation as an MP4 file (higher quality)
ani.save('voting_animation.mp4', fps=fps, dpi=200)

# Optionally, save as a GIF (may require additional libraries)
# ani.save('voting_animation.gif', fps=fps, writer='imagemagick')

# Show the animation (if you want to see it before saving)
# plt.show()
