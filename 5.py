import math
class CelestialBody:
    def __init__(self, name, mass, pos ,vel):
        self.name = name
        self.mass = mass
        self.pos = list(pos)
        self.vel = list(vel)
    def distance_to(self, other):
        dx = self.pos[0] - other.pos[0]
        dy = self.pos[1] - other.pos[1]
        return math.sqrt(dx**2 + dy**2)
    def gravity_accel(self, other):
        dx = self.pos[0] - other.pos[0]
        dy = self.pos[1] - other.pos[1]
        dist = self.distance_to(other)
        force = (self.mass * other.mass) / (dist**2)
        ax = force * dx / (dist * self.mass)
        ay = force * dy / (dist * self.mass)
        return (ax,ay)
    def update(self, dt):
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
    def __str__(self):
        return f"[{self.name}]位置:{self.pos[0]:.2f},{self.pos[1]:.2f}"
sun = CelestialBody("太阳", 10000, (0,0), (0,0))
earth = CelestialBody("地球", 1, (10,0), (0,0.5))
dt = 0.1
for step in range(10):
    ax,ay = earth.gravity_accel(sun)
    earth.vel[0] += ax * dt
    earth.vel[1] += ay * dt
    earth.update(dt)
    print(f"{step+1:2d}步: {earth}")
print("\n模拟完成。")