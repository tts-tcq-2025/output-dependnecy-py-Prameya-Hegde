def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append((i * 5 + j, major, minor))
    return color_map

def print_color_map(color_map):
    for number, major, minor in color_map:
        print(f'{number:2} | {major:6} | {minor:6}')

if __name__ == "__main__":
    color_map = generate_color_map()
    assert len(color_map) == 25
    print_color_map(color_map)
    print("All is well (maybe!)")
