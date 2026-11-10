import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)

    efficiency = volume / surface_area
    return efficiency

def main():
    print("Can Storage Efficiency")

    # First can 
    radius = 6.83
    height = 10.16

    efficiency = compute_storage_efficiency(radius, height)
    print("#1 Picnic", round(efficiency, 2))

    # Second can
    radius = 7.78
    height = 11.91

    efficiency = compute_storage_efficiency(radius, height)
    print("#1 Tall", round(efficiency, 2))

    # Third can
    radius = 8.73
    height = 11.59

    efficiency = compute_storage_efficiency(radius, height)
    print("#2", round(efficiency, 2))

    # Fourth can
    radius = 10.32
    height = 11.91

    efficiency = compute_storage_efficiency(radius, height)
    print("#2.5", round(efficiency, 2))

    # Fifth can
    radius = 10.79
    height = 17.78

    efficiency = compute_storage_efficiency(radius, height)
    print("#3 Cylinder", round(efficiency, 2))

    # Sixth can
    radius = 13.02
    height = 14.29
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#5", round(efficiency, 2))

    # Seventh can
    radius = 5.40
    height = 8.89
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#6Z", round(efficiency, 2))

    # Eighth can
    radius = 6.83
    height = 7.62
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#8Z Short", round(efficiency, 2))

    # Ninth can
    radius = 15.72
    height = 17.78
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#10", round(efficiency, 2))

    # Tenth can
    radius = 6.83
    height = 12.38
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#211", round(efficiency, 2))

    # Eleventh can
    radius = 7.62
    height = 11.27
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#300", round(efficiency, 2))

    # Twelfth can
    radius = 8.10
    height = 11.11
    
    efficiency = compute_storage_efficiency(radius, height)
    print("#303", round(efficiency, 2))


if __name__ == "__main__":
    main()