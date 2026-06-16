import fastf1
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache(
    r'E:\F1_Virtual_ECU_Project\cache'
)

session = fastf1.get_session(2025, 'Monza', 'Q')
session.load()

lap = session.laps.pick_fastest()
telemetry = lap.get_car_data().add_distance()

plt.figure(figsize=(12,6))

plt.plot(
    telemetry['Distance'],
    telemetry['Throttle'],
    label='Throttle [%]'
)

plt.plot(
    telemetry['Distance'],
    telemetry['Brake'] * 100,
    label='Brake [%]'
)

plt.xlabel("Distance [m]")
plt.ylabel("Input [%]")
plt.title("Driver Inputs - Monza 2025")
plt.legend()
plt.grid()

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\driver_inputs.png'
)

plt.show()

plt.figure(figsize=(12,5))

plt.plot(
    telemetry['Distance'],
    telemetry['nGear'],
    label='Gear'
)

plt.legend()

plt.xlabel("Distance [m]")
plt.ylabel("Gear")
plt.title("Gear Trace - Monza 2025")
plt.grid()

plt.savefig(
    r'E:\F1_Virtual_ECU_Project\plots\gear_trace.png'
)

plt.show()
