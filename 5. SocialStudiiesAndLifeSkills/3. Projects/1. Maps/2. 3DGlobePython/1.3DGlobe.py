import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import matplotlib.colors as mcolors

def cartesian_to_lonlat(x, y, z, radius=1):
    lat = np.degrees(np.arcsin(z / radius))
    lon = np.degrees(np.arctan2(y, x))
    return lon, lat

def lonlat_to_cartesian(lon, lat, radius=1):
    lon_rad = np.radians(lon)
    lat_rad = np.radians(lat)
    x = radius * np.cos(lat_rad) * np.cos(lon_rad)
    y = radius * np.cos(lat_rad) * np.sin(lon_rad)
    z = radius * np.sin(lat_rad)
    return x, y, z

def create_globe():
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Disable Matplotlib's built-in key press handling
    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


    # --- Sphere ---
    u = np.linspace(0, 2 * np.pi, 200)
    v = np.linspace(0, np.pi, 200)
    v_modified = np.copy(v)
    pole_dip_factor = 0.9
    v_modified[:50] = np.interp(v_modified[:50], [0, np.pi/2], [0, np.pi/2 * pole_dip_factor])
    v_modified[150:] = np.interp(v_modified[150:], [np.pi/2, np.pi], [np.pi/2 + (np.pi/2*(1-pole_dip_factor)), np.pi])
    x = np.outer(np.cos(u), np.sin(v_modified))
    y = np.outer(np.sin(u), np.sin(v_modified))
    z = np.outer(np.ones(np.size(u)), np.cos(v_modified))
    cmap = mcolors.LinearSegmentedColormap.from_list("mycmap", ["white", "lightblue", "white"])
    z_for_color = np.outer(np.ones(np.size(u)), np.cos(v))
    norm = plt.Normalize(vmin=-1, vmax=1)
    colors = cmap(norm(z_for_color))
    ax.plot_surface(x, y, z, facecolors=colors, alpha=0.4, linewidth=0, antialiased=True)

    # --- Stand ---
    stand_radius = 0.2
    stand_height = -1.2
    stand_z = np.linspace(stand_height, -1, 50)
    stand_x = stand_radius * np.cos(u)
    stand_y = stand_radius * np.sin(u)
    ax.plot(stand_x, stand_y, stand_height, color='gray', linewidth=3, zorder=1)
    ax.plot([0, 0], [0, 0], [stand_height, -1], color='gray', linewidth=3, zorder=1)

    # --- Initial Lat/Lon and Marker ---
    current_lon = 0
    current_lat = 0
    marker = None
    line_radius_offset = 1.01

    def update_marker():
        nonlocal marker, current_lat, current_lon
        if marker:
            marker.remove()

        x_mark, y_mark, z_mark = lonlat_to_cartesian(current_lon, current_lat, radius=line_radius_offset)

        # Determine marker color based on x-coordinate
        if x_mark > 0:  # Front half
            marker_color = 'orange'
        else:  # Back half
            marker_color = mcolors.to_rgba('orange', alpha=0.4) # Lighter orange with transparency

        marker, = ax.plot([x_mark], [y_mark], [z_mark], color=marker_color, marker='X', markersize=10, zorder=10, solid_capstyle='round')

        update_lines_and_annotations()
        fig.canvas.draw_idle()

     # --- Lines and Annotations ---
    lines = []
    annotations = []

    north_pole_label = ax.text(0, 0, 1.02, "N", color='red', fontsize=14, ha='center', va='center', zorder=10)
    south_pole_label = ax.text(0, 0, -1.02, "S", color='red', fontsize=14, ha='center', va='center', zorder=10)

    def update_lines_and_annotations():
      nonlocal lines, annotations, ax, current_lon, current_lat

      for line in lines:
          line.remove()
      lines.clear()
      for ann in annotations:
          ann.remove()
      annotations.clear()

      # --- Latitude (Double-sided) ---
      lat_segments = []
      lat_colors = []
      lat_line_theta = np.linspace(0, 2 * np.pi, 101)

      for i in range(len(lat_line_theta) - 1):
          theta1 = lat_line_theta[i]
          theta2 = lat_line_theta[i + 1]
          x1 = np.cos(theta1) * np.cos(np.radians(current_lat)) * line_radius_offset
          y1 = np.sin(theta1) * np.cos(np.radians(current_lat)) * line_radius_offset
          z1 = np.sin(np.radians(current_lat)) * line_radius_offset
          x2 = np.cos(theta2) * np.cos(np.radians(current_lat)) * line_radius_offset
          y2 = np.sin(theta2) * np.cos(np.radians(current_lat)) * line_radius_offset
          z2 = np.sin(np.radians(current_lat)) * line_radius_offset
          lat_segments.append([(x1, y1, z1), (x2, y2, z2)])

          # Determine color based on x-coordinate (simpler front/back)
          if (x1 + x2) / 2 > 0:  # Front half
              lat_colors.append('black')
          else:  # Back half
              lat_colors.append('gray')

      lat_collection = Line3DCollection(lat_segments, colors=lat_colors, linewidths=2, zorder=5)
      ax.add_collection(lat_collection)
      lines.append(lat_collection)

      # --- Longitude (Double-sided, color depends on latitude position) ---
      lon_segments = []
      lon_colors = []
      lon_line_phi = np.linspace(-np.pi / 2, np.pi / 2, 101)

      for i in range(len(lon_line_phi) - 1):
          phi1 = lon_line_phi[i]
          phi2 = lon_line_phi[i + 1]
          x1 = np.cos(np.radians(current_lon)) * np.cos(phi1) * line_radius_offset
          y1 = np.sin(np.radians(current_lon)) * np.cos(phi1) * line_radius_offset
          z1 = np.sin(phi1) * line_radius_offset
          x2 = np.cos(np.radians(current_lon)) * np.cos(phi2) * line_radius_offset
          y2 = np.sin(np.radians(current_lon)) * np.cos(phi2) * line_radius_offset
          z2 = np.sin(phi2) * line_radius_offset
          lon_segments.append([(x1, y1, z1), (x2, y2, z2)])

          # Determine longitude color based on latitude position
          avg_x = (x1 + x2) / 2
          if avg_x > 0: #current lat line is in front
                lon_colors.append('darkred')  # Darker on front
          else:
                lon_colors.append('lightcoral')  # Lighter on back


      lon_collection = Line3DCollection(lon_segments, colors=lon_colors, linewidths=2, zorder=5)
      ax.add_collection(lon_collection)
      lines.append(lon_collection)
        # --- Annotations ---
      lat_str = f"{abs(current_lat):.2f}°{'N' if current_lat >= 0 else 'S'}"
      lon_str = f"{abs(current_lon):.2f}°{'E' if current_lon >= 0 else 'W'}"
      if current_lon < -180:
          lon_str = f"{abs(current_lon + 360):.2f}°{'E'}"
      elif current_lon > 180:
          lon_str = f"{abs(current_lon - 360):.2f}°{'W'}"

      lat_annotation = ax.text2D(0.05, 0.95, f"Lat: {lat_str}",
                                    transform=ax.transAxes, color='black', fontsize=12,
                                    bbox=dict(facecolor='white', alpha=0.8), zorder=5)
      lon_annotation = ax.text2D(0.05, 0.90, f"Lon: {lon_str}",
                                      transform=ax.transAxes, color='darkred', fontsize=12,
                                      bbox=dict(facecolor='white', alpha=0.8), zorder=5)
      annotations.extend([lat_annotation, lon_annotation])

    # --- Keyboard Event Handler ---
    def on_key(event):
        nonlocal current_lon, current_lat, ax
        current_azim = ax.azim
        current_elev = ax.elev

        if event.key == 'left':
            current_lon -= 5
        elif event.key == 'right':
            current_lon += 5
        elif event.key == 'up':
            current_lat += 5
        elif event.key == 'down':
            current_lat -= 5

        current_lon = (current_lon + 180) % 360 - 180
        current_lat = max(-90, min(90, current_lat))
        update_marker()
        ax.view_init(elev=current_elev, azim=current_azim)
        fig.canvas.draw_idle()

    # --- Mouse Rotation Handlers ---
    rotating = False
    last_x = None

    def on_press(event):
        nonlocal rotating, last_x
        if event.button != 1 or event.inaxes != ax:  return
        rotating = True
        last_x = event.x

    def on_release(event):
        nonlocal rotating
        if event.button != 1: return
        rotating = False

    def on_motion(event):
        nonlocal rotating, last_x, ax
        if not rotating or event.inaxes != ax or last_x is None: return
        dx = event.x - last_x
        azim = ax.azim + dx * 0.2
        ax.view_init(elev=ax.elev, azim=azim)
        fig.canvas.draw_idle()
        last_x = event.x

    # --- Connect Event Handlers ---
    fig.canvas.mpl_connect('key_press_event', on_key)
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('button_release_event', on_release)
    fig.canvas.mpl_connect('motion_notify_event', on_motion)

    # --- Initial View and Plot Setup ---
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.set_xlim([-0.7, 0.7])
    ax.set_ylim([-0.7, 0.7])
    ax.set_zlim([-0.7, 0.7])
    ax.view_init(elev=10, azim=0)
    fig.text(0.5, 0.95, "Use arrow keys to move the marker, and mouse click and drag to rotate the globe.", ha='center', fontsize=10)

    update_marker()
    plt.show()

if __name__ == '__main__':
    create_globe()