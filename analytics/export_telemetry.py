import fastf1

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

telemetry = lap.get_car_data().add_distance()

telemetry.to_csv(
    r'E:\F1_Virtual_ECU_Project\data\ver_monza_telemetry.csv',
    index=False
)

print("Telemetry exported.")