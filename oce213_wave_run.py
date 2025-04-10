# Example script that uses the wave module

# Import the functions
from oce213_waves import wave_properties, shallow_water_wavelength, deep_water_wavelength, plot_wave

# --- Input parameters ---
T = 8.0      # wave period in seconds
H = 2.5      # wave height in meters
h = 5.0      # water depth in meters

# --- Compute wave properties ---
omega, a = wave_properties(T, H)
print("Angular frequency (omega): %.3f rad/s" % omega)
print("Amplitude (a): %.2f m" % a)

# --- Compute shallow water wavelength ---
L_shallow = shallow_water_wavelength(T, h)
print("Shallow water wavelength: %.2f m" % L_shallow)

# --- Compute deep water wavelength and wave number ---
L_deep, k = deep_water_wavelength(T)
print("Deep water wavelength: %.2f m" % L_deep)
print("Wave number (k): %.3f 1/m" % k)

# --- Plot the wave using deep water wavelength ---
plot
