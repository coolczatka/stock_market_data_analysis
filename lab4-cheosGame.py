import matplotlib.pyplot as plt
import random

def randomCorner(corners):
    return random.choice(corners)

def newPoint(point, corner):
    return (
        (point[0]+corner[0])/2,
        (point[1]+corner[1])/2,
    )

def chaosGame(config):

    points = [config['startPoint']]

    for i in range(config['epochs']):
        corner = randomCorner(config['corners'])
        point = newPoint(points[-1], corner)
        points.append(point)

    x, y = zip(*points)
    
    plt.figure()
    plt.title(f"{config['epochs']} iteracji")
    plt.scatter(x, y)
    plt.show()

config = {
    'startPoint': (0, 0),
    'corners': [(-1, -1), (1, -1), (0, 2)],
    'epochs': 10
}
chaosGame(config)

config['epochs'] = 100
chaosGame(config)
config['epochs'] = 1000
chaosGame(config)
config['epochs'] = 10000
chaosGame(config)
