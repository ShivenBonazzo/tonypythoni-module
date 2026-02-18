import sys
import math

def create_position(x: int, y: int, z: int) -> tuple:
	return (x, y, z)


def calculate_distance(p1: tuple, p2: tuple) -> float:
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinate(coord_str: str) -> tuple:
	parts = coord_str.split(",")
	return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
	print("=== Game Coordinate System ===")
	pos = create_position(10, 20, 5)
	print(f"Position created: {pos}")
	origin = (0, 0, 0)
	dist = calculate_distance(origin, pos)
	print(f"Distance between {origin} and {pos}: {round(dist, 2)}")
	print()
	valid_str = "3,4,0"
	print(f'Parsing coordinates: "{valid_str}"')
	try:
		parsed = parse_coordinate(valid_str)
		print(f"Parsed position: {parsed}")
		dist2 = calculate_distance(origin, parsed)
		print(f"Distance between {origin} and {parsed}: {dist2}")
	except ValueError as e:
		print(f"Error parsing coordinates: {e}")
	print()
	invalid_str = "abc,def,ghi"
	print(f'Parsing invalid coordinates: "{invalid_str}"')
	try:
		parsed_invalid = parse_coordinate(invalid_str)
		print(f"Parsed position: {parsed_invalid}")
	except ValueError as e:
		print(f"Error parsing coordinates: {e}")
		print(f"Error details - Type: ValueError, Args: {e.args}")
	print()
	x, y, z = parsed
	print("Unpacking demonstration:")
	print(f"Player at x={x}, y={y}, z={z}")
	print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
	main()
