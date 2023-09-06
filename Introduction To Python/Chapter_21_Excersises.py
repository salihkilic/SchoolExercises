# Things to do, chapter 21
# https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch21.html#idm45794962624488

import geopandas
import matplotlib.pyplot as plt

# 21.1 Install geopandas and run Example 21-1. Try modifying things like colors and marker sizes.
print("\n------ 20.1 ------")

world_file = geopandas.datasets.get_path('naturalearth_lowres')
world = geopandas.read_file(world_file)
cities_file = geopandas.datasets.get_path('naturalearth_cities')
cities = geopandas.read_file(cities_file)
base = world.plot(color='red')
cities.plot(ax=base, color='blue', markersize=4)

print("Changed land colour to red, dots to blue and increased marker size to 4")

plt.show()
