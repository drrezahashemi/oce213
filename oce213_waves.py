import numpy as np
import matplotlib.pyplot as plt

def wave_properties(T, H):
    """
    Calculate wave angular frequency (omega) and amplitude (a).
    
    Parameters:
        T (float): Wave period (seconds)
        H (float): Wave height (meters)
    
    Returns:
        omega (float): Angular frequency (rad/s)
        a (float): Amplitude (meters)
    """
    omega = 2 * np.pi / T
    a = H / 2
    return omega, a


def shallow_water_wavelength(T, h, g=9.81):
    """
    Calculate wavelength in shallow water approximation.
    
    Parameters:
        T (float): Wave period (seconds)
        h (float): Water depth (meters)
        g (float): Acceleration due to gravity (m/s²)
    
    Returns:
        L (float): Wavelength (meters)
    """
    L = T * np.sqrt(g * h)
    k = 2 * np.pi / L
    return L,k


def deep_water_wavelength(T, g=9.81):
    """
    Calculate wavelength and wave number using deep water approximation.
    
    Parameters:
        T (float): Wave period (seconds)
        g (float): Acceleration due to gravity (m/s²)
    
    Returns:
        L (float): Wavelength (meters)
        k (float): Wave number (1/m)
    """
    omega = 2 * np.pi / T
    L = g * T**2 / (2 * np.pi)
    k = 2 * np.pi / L
    return L, k


def plot_wave(H, L):
    """
    Plot a sinusoidal wave over 2 wavelengths.
    
    Parameters:
        H (float): Wave height (meters)
        L (float): Wavelength (meters)
    """
    a = H / 2
    x = np.linspace(0, 2 * L, 1000)
    y = a * np.cos(2 * np.pi * x / L)

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, label='Wave Profile')
    plt.axhline(0, color='gray', linestyle='--')
    plt.title('Wave Profile Over 2 Wavelengths')
    plt.xlabel('Distance (m)')
    plt.ylabel('Water Surface Elevation (m)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
