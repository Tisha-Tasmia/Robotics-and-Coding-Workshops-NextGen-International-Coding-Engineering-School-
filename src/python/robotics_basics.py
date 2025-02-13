import time
import random

class AI_Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move_forward(self, steps):
        self.position += steps
        print(f"{self.name} moved forward to position {self.position}")

    def scan_environment(self):
        obstacles = ["Clear Path", "Obstacle Detected"]
        scan_result = random.choice(obstacles)
        print(f"{self.name} Scan: {scan_result}")
        return scan_result

    def autonomous_navigation(self):
        for _ in range(5):
            if self.scan_environment() == "Clear Path":
                self.move_forward(2)
            else:
                print(f"{self.name} stopped due to an obstacle.")
                break
            time.sleep(1)

# Example usage
robot = AI_Robot("NextGenBot")
robot.autonomous_navigation()
