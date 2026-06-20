import streamlit as st
import fastf1
import matplotlib.pyplot as plt


fastf1.Cache.enable_cache(
    r'E:\F1_Virtual_ECU_Project\cache'
)


st.set_page_config(
    page_title="F1 Digital Twin",
    page_icon="🏎️",
    layout="wide"
)


st.title("🏎️ F1 Digital Twin Dashboard")


st.sidebar.title("Controls")


driver = st.sidebar.selectbox(
    "Driver",
    ["VER", "LEC", "NOR", "PIA", "HAM"]
)

comparison_driver = st.sidebar.selectbox(
    "Comparison Driver",
    ["VER", "LEC", "NOR", "PIA", "HAM"],
    index=1
)

if driver == comparison_driver:
    st.warning(
        "Choose two different drivers for comparison."
    )
    st.stop()

track = st.sidebar.selectbox(
    "Track",
    [
        "Monza",
        "Silverstone",
        "Spa",
        "Monaco"
    ]
)

st.sidebar.success(
    f"{driver} vs {comparison_driver}"
)

st.sidebar.write(
    f"Track: {track}"
)


@st.cache_resource
def load_session(track):
    session = fastf1.get_session(
        2025,
        track,
        'Q'
    )
    session.load()
    return session


with st.spinner("Loading telemetry..."):
    session = load_session(track)


lap = session.laps.pick_drivers(
    driver
).pick_fastest()

comparison_lap = session.laps.pick_drivers(
    comparison_driver
).pick_fastest()

comparison_tel = comparison_lap.get_car_data().add_distance()

lap_diff = (
    comparison_lap['LapTime'].total_seconds()
    - lap['LapTime'].total_seconds()
)

telemetry = lap.get_car_data().add_distance()


st.write("Loaded:", driver)


st.info(
    f"Track: {track} | Driver: {driver}"
)


st.write(
    "Formula 1 inspired vehicle digital twin project."
)


st.header("Telemetry Analytics")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        label="Fastest Lap",
        value=str(lap['LapTime'])[10:22]
    )


with col2:
    st.metric(
        label="Top Speed",
        value=f"{telemetry['Speed'].max():.0f} km/h"
    )


with col3:
    st.metric(
        label="Driver Gap",
        value=f"{lap['LapTime'].total_seconds():.3f} s"
    )


st.header("Telemetry Plots")

fig, ax = plt.subplots(figsize=(10,5))

ax.plot(
    telemetry['Distance'],
    telemetry['Speed']
)

ax.set_title(
    f"{driver} Speed Trace"
)

ax.set_xlabel(
    "Distance [m]"
)

ax.set_ylabel(
    "Speed [km/h]"
)

ax.grid()

st.pyplot(fig)

fig2, ax2 = plt.subplots(figsize=(10,5))

ax2.plot(
    telemetry['Distance'],
    telemetry['Throttle'],
    label='Throttle'
)

ax2.plot(
    telemetry['Distance'],
    telemetry['Brake'] * 100,
    label='Brake'
)

ax2.set_title(
    f"{driver} Driver Inputs"
)

ax2.set_xlabel(
    "Distance [m]"
)

ax2.set_ylabel(
    "Input [%]"
)

ax2.legend()

ax2.grid()

st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.plot(
    telemetry['Distance'],
    telemetry['nGear']
)

ax3.set_title(
    f"{driver} Gear Trace"
)

ax3.set_xlabel(
    "Distance [m]"
)

ax3.set_ylabel(
    "Gear"
)

ax3.grid()

st.pyplot(fig3)

st.header("Driver Comparison")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Driver A",
        driver
    )

with col2:
    st.metric(
        "Driver B",
        comparison_driver
    )

with col3:
    st.metric(
        "Lap Difference",
        f"{lap_diff:.3f} s"
    )

fig4, ax4 = plt.subplots(figsize=(12,6))

ax4.plot(
    telemetry['Distance'],
    telemetry['Speed'],
    label=driver
)

ax4.plot(
    comparison_tel['Distance'],
    comparison_tel['Speed'],
    label=comparison_driver
)

ax4.set_title(
    f"{driver} vs {comparison_driver}"
)

ax4.set_xlabel(
    "Distance [m]"
)

ax4.set_ylabel(
    "Speed [km/h]"
)

ax4.legend()

ax4.grid()

st.pyplot(fig4)

lap_diff = (
    comparison_lap['LapTime'].total_seconds()
    - lap['LapTime'].total_seconds()
)

