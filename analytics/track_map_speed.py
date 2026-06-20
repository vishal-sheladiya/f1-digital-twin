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
car = lap.get_car_data()

plt.figure(figsize=(8,8))

min_len = min(
    len(pos),
    len(car)
)

scatter = plt.scatter(
    pos['X'][:min_len],
    pos['Y'][:min_len],
    c=car['Speed'][:min_len],
    s=8
)

plt.colorbar(
    scatter,
    label='Speed [km/h]'
)

plt.title(
    'Monza Speed Map'
)

plt.axis('equal')

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\track_speed_map.png'
)

plt.show()