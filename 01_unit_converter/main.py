import streamlit as st  # Import Streamlit for creating the web-based UI

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
    }

    key = f"{unit_from}_{unit_to}"
    
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    elif unit_from == unit_to:
        return value  
    else:
        return None

# Streamlit UI setup
st.title("🌟 Smart Unit Converter")  
st.write("Convert between different units effortlessly!")

# User input
value = st.number_input("🔢 Enter value:", min_value=1.0, step=1.0)

# Dropdowns for unit selection
units = ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"]
unit_from = st.selectbox("📌 Convert from:", units)
unit_to = st.selectbox("🎯 Convert to:", units)

# Convert button
if st.button("🔄 Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if result is not None:
        st.success(f"✅ Converted Value: {round(result, 4)} {unit_to}")
    else:
        st.error("❌ Conversion not supported. Please select valid units.")




