import unittest
from robot import Terrain

class TestRobotMovement(unittest.TestCase):

    def test_robot_creation_and_movement(self):
        terrain = Terrain(5, 5)
        terrain.create_robot(1)
        terrain.create_robot(2)

        terrain.move_robot(1, "E2")
        terrain.move_robot(1, "S1")
        self.assertEqual(terrain.get_robot_position(1), (1, 2))

        terrain.move_robot(2, "E2")
        terrain.move_robot(2, "S1") 
        self.assertEqual(terrain.get_robot_position(2), (0, 2))

    def test_robot_boundary(self):
        terrain = Terrain(3, 3)
        terrain.create_robot(3)
        terrain.move_robot(3, "N1") 
        self.assertEqual(terrain.get_robot_position(3), (0, 0))

if __name__ == '__main__':
    unittest.main()
