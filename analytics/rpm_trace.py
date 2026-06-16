import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache(
    r'E:\F1_Virtual_ECU_Project\cache'
)

session = fastf1.get_session(2025, 'Monza', 'Q')
session.load()

lap = session.laps.pick_fastest()
telemetry = lap.get_car_data().add_distance()

plt.figure(figsize=(12,5))

plt.plot(
    telemetry['Distance'],
    telemetry['RPM'],
    label='RPM'
)

plt.xlabel("Distance [m]")
plt.ylabel("RPM")
plt.title("Engine RPM - Monza 2025")
plt.legend()
plt.grid()

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\rpm_trace.png'
)

plt.show()