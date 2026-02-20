import random
import math

class ChaosObject:
    def __init__(self, x, y, mass=1):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = mass

    def apply_chaos_impulse(self, intensity=50):
        angle = random.uniform(0, 2 * math.pi)
        force = random.uniform(0, intensity)

        fx = math.cos(angle) * force
        fy = math.sin(angle) * force

        self.vx += fx / self.mass
        self.vy += fy / self.mass

    def update(self, dt=0.1):
        self.x += self.vx * dt
        self.y += self.vy * dt

if __name__ == "__main__":
    obj = ChaosObject(0, 0, mass=2)

    obj.apply_chaos_impulse(intensity=100)
    obj.update()

    print("Position:", obj.x, obj.y)
    print("Velocity:", obj.vx, obj.vy)
