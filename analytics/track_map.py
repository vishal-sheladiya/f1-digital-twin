import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache(
    r'E:\F1_Virtual_ECU_Project\cache'
)

session = fastf1.get_session(
    2025,
    'Monza',
    'Q'
)

session.load()

lap = session.laps.pick_drivers(
    'VER'
).pick_fastest()

pos = lap.get_pos_data()

plt.figure(figsize=(8,8))

plt.plot(
    pos['X'],
    pos['Y']
)

plt.title(
    'Monza Track Map'
)

plt.axis('equal')

plt.grid()

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\track_map.png'
)

plt.show()