import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.colors as mcolors
import geopandas as gpd
import os
import zipfile  # Import zipfile

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
    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)

    # --- Load Map Data (Local, with Extraction) ---
    zip_filename = "ne_110m_admin_0_countries.zip"  # Name of the ZIP file
    extract_path = "natural_earth_data"  # Extraction folder
    shapefile_name = "ne_110m_admin_0_countries.shp"
    shapefile_path = os.path.join(extract_path, shapefile_name)

    # --- Extract ZIP if needed ---
    if not os.path.exists(shapefile_path):  # Check if the shapefile exists
        if not os.path.exists(zip_filename):
            print(f"Error: ZIP file '{zip_filename}' not found.")
            print("Place the downloaded ZIP file in the same directory as the script.")
            return
        try:
            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extractall(extract_path)  # Extract to the specified folder
            print(f"Extracted '{zip_filename}' to '{extract_path}'")
        except zipfile.BadZipFile:
            print(f"Error: '{zip_filename}' is not a valid ZIP file.")
            return
        except Exception as e:
            print(f"Error during extraction: {e}")
            return

    # --- Load Shapefile ---
    try:
        world = gpd.read_file(shapefile_path)
    except Exception as e:
        print(f"Error loading shapefile: {e}")
        return


   # --- Create the sphere with polar caps ---
    u, v = np.linspace(0, 2 * np.pi, 200), np.linspace(0, np.pi, 200)
    v_modified = np.copy(v)
    pole_dip_factor = 0.9
    v_modified[:50] = np.interp(v_modified[:50], [0, np.pi / 2], [0, np.pi / 2 * pole_dip_factor])
    v_modified[150:] = np.interp(v_modified[150:], [np.pi / 2, np.pi],
                                 [np.pi / 2 + (np.pi / 2 * (1 - pole_dip_factor)), np.pi])
    x = np.outer(np.cos(u), np.sin(v_modified))
    y = np.outer(np.sin(u), np.sin(v_modified))
    z = np.outer(np.ones(np.size(u)), np.cos(v_modified))

    # --- Plot Land and Ocean ---
    land_color = '#C2B280'
    land_color = 'brown'
    ocean_color = '#77B5FE'
    ax.plot_surface(x, y, z, color=ocean_color, alpha=0.4, linewidth=0, antialiased=True, zorder=1)

    for geom in world.geometry:
        if geom.geom_type == 'Polygon':
            lons, lats = geom.exterior.xy
            xs, ys, zs = lonlat_to_cartesian(np.array(lons), np.array(lats))
            ax.plot(xs, ys, zs, color='black', linewidth=0.5, zorder=2, alpha = 0.4)
            ax.add_collection(Poly3DCollection([list(zip(xs, ys, zs))], color=land_color, alpha=0.4, zorder=2))
        elif geom.geom_type == 'MultiPolygon':
            for polygon in geom.geoms:
                lons, lats = polygon.exterior.xy
                xs, ys, zs = lonlat_to_cartesian(np.array(lons), np.array(lats))
                ax.plot(xs, ys, zs, color='black', linewidth=0.5, zorder=2, alpha=0.4)
                ax.add_collection(Poly3DCollection([list(zip(xs, ys, zs))], color=land_color, alpha=0.4, zorder=2))

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

        marker_color = 'orange'

        marker, = ax.plot([x_mark], [y_mark], [z_mark], color=marker_color, marker='X', markersize=10,
                          zorder=20, solid_capstyle='round')
        update_lines_and_annotations()
        fig.canvas.draw_idle()

     # --- Lines and Annotations ---
    latitude_collection = None
    longitude_collection = None
    north_pole_label = ax.text(0, 0, 1.02, "N", color='red', fontsize=14, ha='center', va='center', zorder=10)
    south_pole_label = ax.text(0, 0, -1.02, "S", color='red', fontsize=14, ha='center', va='center', zorder=10)
    lat_annotation, lon_annotation = None, None


    def update_lines_and_annotations():
        nonlocal latitude_collection, longitude_collection, lat_annotation, lon_annotation

        # Remove previous lines and annotations
        if latitude_collection:
            latitude_collection.remove()
        if longitude_collection:
            longitude_collection.remove()

        if lat_annotation:
          lat_annotation.remove()
        if lon_annotation:
          lon_annotation.remove()

        # --- Latitude (Double-sided) ---
        lat_segments = []
        lat_colors = []
        for theta1, theta2 in zip(np.linspace(0, 2 * np.pi, 101)[:-1], np.linspace(0, 2 * np.pi, 101)[1:]):
            x1, y1, z1 = lonlat_to_cartesian(np.degrees(theta1), current_lat, radius=line_radius_offset)
            x2, y2, z2 = lonlat_to_cartesian(np.degrees(theta2), current_lat, radius=line_radius_offset)
            lat_segments.append([(x1, y1, z1), (x2, y2, z2)])
            lat_colors.append('black' if (x1 + x2) / 2 > 0 else 'gray')
        latitude_collection = Line3DCollection(lat_segments, colors=lat_colors, linewidths=2, zorder=15)
        ax.add_collection(latitude_collection)


        # --- Longitude (Double-sided) ---
        lon_segments = []
        lon_colors = []
        for phi1, phi2 in zip(np.linspace(-np.pi / 2, np.pi / 2, 101)[:-1], np.linspace(-np.pi/2, np.pi/2, 101)[1:]):
          x1, y1, z1 = lonlat_to_cartesian(current_lon, np.degrees(phi1), radius=line_radius_offset)
          x2, y2, z2 = lonlat_to_cartesian(current_lon, np.degrees(phi2), radius=line_radius_offset)
          lon_segments.append([(x1, y1, z1), (x2, y2, z2)])
          lon_colors.append('darkred' if (x1 + x2) / 2 > 0 else 'lightcoral')

        longitude_collection = Line3DCollection(lon_segments, colors=lon_colors, linewidths=2, zorder=10)
        ax.add_collection(longitude_collection)


        # --- Annotations ---
        lat_str = f"{abs(current_lat):.2f}°{'N' if current_lat >= 0 else 'S'}"
        lon_str = f"{abs(current_lon):.2f}°{'E' if current_lon >= 0 else 'W'}"
        if current_lon < -180: lon_str = f"{abs(current_lon + 360):.2f}°{'E'}"
        elif current_lon > 180: lon_str = f"{abs(current_lon - 360):.2f}°{'W'}"

        lat_annotation = ax.text2D(0.05, 0.95, f"Lat: {lat_str}", transform=ax.transAxes, color='black', fontsize=12, bbox=dict(facecolor='white', alpha=0.8), zorder=5)
        lon_annotation = ax.text2D(0.05, 0.90, f"Lon: {lon_str}", transform=ax.transAxes, color='darkred', fontsize=12, bbox=dict(facecolor='white', alpha=0.8), zorder=5)

    # --- Keyboard and Mouse Event Handlers ---
    def on_key(event):
        nonlocal current_lon, current_lat, ax
        current_azim = ax.azim  # Store current view
        current_elev = ax.elev

        if event.key in ('left', 'right', 'up', 'down'):
            if event.key == 'left':  current_lon -= 5
            elif event.key == 'right': current_lon += 5
            elif event.key == 'up':   current_lat += 5
            elif event.key == 'down': current_lat -= 5
            current_lon = (current_lon + 180) % 360 - 180
            current_lat = max(-90, min(90, current_lat))
            update_marker()
            ax.view_init(elev=current_elev, azim=current_azim)  # Restore view
            fig.canvas.draw_idle()

        elif event.key in ('shift+right', 'shift+left', 'shift+up', 'shift+down'):
            current_azim = ax.azim
            current_elev = ax.elev
            if event.key == 'shift+right':
                current_azim -= 5
            elif event.key == 'shift+left':
                current_azim += 5
            elif event.key == 'shift+up':
                current_elev += 5
            elif event.key == 'shift+down':
                current_elev -= 5
            ax.view_init(azim=current_azim, elev=current_elev)
            fig.canvas.draw_idle()

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
        ax.view_init(elev=ax.elev, azim=ax.azim + dx * 0.2)
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
    ax.set_xlim([-.7, .7])
    ax.set_ylim([-.7, .7])
    ax.set_zlim([-.7, .7])
    ax.view_init(elev=10, azim=0)
    fig.text(0.5, 0.95, "Use arrow keys to shift marker; Use shift+arrow keys to rotate the globe", ha='center', fontsize=14)

    update_marker()
    plt.show()

if __name__ == '__main__':
    create_globe()