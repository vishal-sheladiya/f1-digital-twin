import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache(
    r'E:\F1_Virtual_ECU_Project\cache'
)

session = fastf1.get_session(2025, 'Monza', 'Q')
session.load()

ver = session.laps.pick_drivers('VER').pick_fastest()
lec = session.laps.pick_drivers('LEC').pick_fastest()

ver_tel = ver.get_car_data().add_distance()
lec_tel = lec.get_car_data().add_distance()

plt.figure(figsize=(12,6))

plt.plot(
    ver_tel['Distance'],
    ver_tel['Speed'],
    label='Verstappen'
)

plt.plot(
    lec_tel['Distance'],
    lec_tel['Speed'],
    label='Leclerc'
)

plt.xlabel("Distance [m]")
plt.ylabel("Speed [km/h]")
plt.title("Verstappen vs Leclerc - Monza 2025 Qualifying")
plt.legend()
plt.grid()

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\driver_comparison.png'
)

plt.show()

print("Verstappen Lap Time:", ver['LapTime'])
print("Leclerc Lap Time:", lec['LapTime'])

plt.show()