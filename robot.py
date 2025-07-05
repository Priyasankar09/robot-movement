class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)

class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.robots = {}  
        self.occupied_positions = set()

    def create_robot(self, robot_id):
        if robot_id in self.robots:
            print("Robot with this ID already exists.")
        else:
            robot = Robot(robot_id)
            self.robots[robot_id] = robot
            self.occupied_positions.add((0, 0))
            print(f"Robot {robot_id} created at position (0, 0).")

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            print("Robot ID not found.")
            return

        direction = command[0].upper()
        try:
            steps = int(command[1:])
        except ValueError:
            print("Invalid command format.")
            return

        robot = self.robots[robot_id]
        x, y = robot.position
        self.occupied_positions.discard(robot.position)

        for _ in range(steps):
            next_x, next_y = x, y
            if direction == 'N':
                next_x -= 1
            elif direction == 'S':
                next_x += 1
            elif direction == 'E':
                next_y += 1
            elif direction == 'W':
                next_y -= 1
            else:
                print("Invalid direction.")
                break

            if (next_x < 0 or next_y < 0 or
                next_x >= self.rows or next_y >= self.cols):
                print("Cannot move outside the terrain.")
                break

            if (next_x, next_y) in self.occupied_positions:
                print("Another robot is in the way. Stopped moving.")
                break

            x, y = next_x, next_y

        robot.position = (x, y)
        self.occupied_positions.add(robot.position)
        print(f"Robot {robot_id} moved to position {robot.position}.")

    def get_robot_position(self, robot_id):
        if robot_id in self.robots:
            return self.robots[robot_id].position
        else:
            return None
