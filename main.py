from robot import Terrain

terrain = Terrain(5, 5)
terrain.create_robot(1)
terrain.create_robot(2)
terrain.move_robot(1, "E2")
terrain.move_robot(1, "S1")
terrain.move_robot(2, "E2")
terrain.move_robot(2, "S1")
print("Robot 1 is at:", terrain.get_robot_position(1))
print("Robot 2 is at:", terrain.get_robot_position(2))
