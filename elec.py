import streamlit as st

# ---------- CLASS DEFINITIONS ----------
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting."


class Car(Vehicle):
    def play_music(self):
        return f"{self.brand} {self.model} is playing music."


class ElectricCar(Car):
    def charge(self):
        return f"{self.brand} {self.model} is charging."


class SmartDevice:
    def connect_wifi(self):
        return "Connecting to WiFi..."


class SmartCar(Car, SmartDevice):
    def auto_drive(self):
        return f"{self.brand} {self.model} is driving automatically."


class Bike(Vehicle):
    def kick_start(self):
        return f"{self.brand} {self.model} is kick-started."


class ElectricSmartCar(SmartCar, ElectricCar):
    def autopilot_mode(self):
        return f"{self.brand} {self.model} is in autopilot mode."


# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Vehicle System", page_icon="🚗")
st.title("🚗 Smart Electric Vehicle System")

# Session state
if "vehicle" not  in st.session_state:
+    st.session_state.vehicle = None

# Sidebar menu
menu = st.sidebar.radio("📋 Menu", ["Create Vehicle", "Vehicle Actions"])

# ---------- CREATE VEHICLE ----------

if menu == "Create Vehicle":
    st.header("🆕 Create Your Vehicle")

    brand = st.text_input("Enter vehicle brand:")
    model = st.text_input("Enter vehicle model:")
    vehicle_type = st.selectbox(
        "Select Vehicle Type",
        ["Car", "Bike", "Electric Car", "Smart Car", "Electric Smart Car"]
    )

    if st.button("Create Vehicle"):
        if not brand.strip() or not model.strip():
            st.warning("Please enter both brand and model.")
        else:
            if vehicle_type == "Car":
                st.session_state.vehicle = Car(brand, model)
            elif vehicle_type == "Bike":
                st.session_state.vehicle = Bike(brand, model)
            elif vehicle_type == "Electric Car":
                st.session_state.vehicle = ElectricCar(brand, model)
            elif vehicle_type == "Smart Car":
                st.session_state.vehicle = SmartCar(brand, model)
            elif vehicle_type == "Electric Smart Car":
                st.session_state.vehicle = ElectricSmartCar(brand, model)

            st.success(f"✅ {vehicle_type} '{brand} {model}' created successfully!")

# ---------- VEHICLE ACTIONS ----------
elif menu == "Vehicle Actions":
    st.header("⚙️ Vehicle Actions")

    if st.session_state.vehicle is None:
        st.warning("Please create a vehicle first.")
    else:
        v = st.session_state.vehicle
        actions = []

        # Dynamically show actions available for that vehicle
        if hasattr(v, "start"): actions.append("Start Vehicle")
        if hasattr(v, "play_music"): actions.append("Play Music")
        if hasattr(v, "charge"): actions.append("Charge Vehicle")
        if hasattr(v, "connect_wifi"): actions.append("Connect WiFi")
        if hasattr(v, "auto_drive"): actions.append("Auto Drive")
        if hasattr(v, "kick_start"): actions.append("Kick Start")
        if hasattr(v, "autopilot_mode"): actions.append("Autopilot Mode")

        action = st.radio("Choose an action", actions)

        if st.button("Run Action"):
            if action == "Start Vehicle":
                st.success(v.start())
            elif action == "Play Music":
                st.info(v.play_music())
            elif action == "Charge Vehicle":
                st.info(v.charge())
            elif action == "Connect WiFi":
                st.info(v.connect_wifi())
            elif action == "Auto Drive":
                st.info(v.auto_drive())
            elif action == "Kick Start":
                st.info(v.kick_start())
            elif action == "Autopilot Mode":
                st.info(v.autopilot_mode())

