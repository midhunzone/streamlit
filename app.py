
import streamlit as st

# Constants
DENSITY_OF_STEEL = 7850  # kg/m^3
MM_TO_METERS = 0.001  # Conversion factor from mm to meters
COST_PER_KG = {
    'Mild Steel Plate': 61,
    'Round Plate': 70,
    'Channel': 60,
    'Angle': 60,
    'Flat': 60,
    'Round Plate with Bore': 75,
    'CR Sheet': 75,
    'Round Pipe': 140,
    'Square Tube': 80
}
TAX_RATE = 0.18  # 18% tax

# Function to calculate weight and cost
def calculate_weight_and_cost(member_type, length, breadth=0, thickness=0, diameter=0, inner_diameter=0, height=0, flange_width=0, flange_thickness=0, web_thickness=0, leg1=0, leg2=0, side=0):
    length = length * MM_TO_METERS
    volume = 0
    dimensions = ""

    if member_type in ['Mild Steel Plate', 'Flat', 'CR Sheet']:
        breadth = breadth * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        volume = length * breadth * thickness
        dimensions = f"{length*1000:.0f} x {breadth*1000:.0f} x {thickness*1000:.0f} mm"
    elif member_type == 'Round Plate':
        diameter = diameter * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        radius = diameter / 2
        volume = 3.1416 * radius ** 2 * thickness
        dimensions = f"{diameter*1000:.0f} x {thickness*1000:.0f} mm"
    elif member_type == 'Round Plate with Bore':
        diameter = diameter * MM_TO_METERS
        inner_diameter = inner_diameter * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        outer_radius = diameter / 2
        inner_radius = inner_diameter / 2
        volume = 3.1416 * (outer_radius ** 2 - inner_radius ** 2) * thickness
        dimensions = f"{diameter*1000:.0f} x {thickness*1000:.0f} mm, Inner Diameter: {inner_diameter*1000:.0f} mm"
    elif member_type == 'Round Pipe':
        diameter = diameter * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        outer_radius = diameter / 2
        inner_radius = outer_radius - thickness
        volume = 3.1416 * (outer_radius ** 2 - inner_radius ** 2) * length
        dimensions = f"{diameter*1000:.0f} x {thickness*1000:.0f} mm"
    elif member_type == 'Square Tube':
        side = side * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        outer_side = side
        inner_side = side - 2 * thickness
        volume = (outer_side ** 2 - inner_side ** 2) * length
        dimensions = f"{side*1000:.0f} x {thickness*1000:.0f} mm"
    elif member_type == 'Channel':
        height = height * MM_TO_METERS
        flange_width = flange_width * MM_TO_METERS
        flange_thickness = flange_thickness * MM_TO_METERS
        web_thickness = web_thickness * MM_TO_METERS
        volume = length * ((2 * flange_width * flange_thickness) + (height - 2 * flange_thickness) * web_thickness)
        dimensions = f"{height*1000:.0f} x {flange_width*1000:.0f} x {flange_thickness*1000:.0f} x {web_thickness*1000:.0f} mm"
    elif member_type == 'Angle':
        leg1 = leg1 * MM_TO_METERS
        leg2 = leg2 * MM_TO_METERS
        thickness = thickness * MM_TO_METERS
        volume = length * (leg1 + leg2 - thickness) * thickness
        dimensions = f"{leg1*1000:.0f} x {leg2*1000:.0f} x {thickness*1000:.0f} mm"

    weight = volume * DENSITY_OF_STEEL
    cost = weight * COST_PER_KG[member_type]
    total_cost = cost + (cost * TAX_RATE)
    return dimensions, weight, total_cost

# Streamlit app layout
st.title("Steel Member Weight and Cost Calculator")

member_type = st.selectbox("Select the type of steel member", ['Mild Steel Plate', 'Round Plate', 'Channel', 'Angle', 'Flat', 'Round Plate with Bore', 'CR Sheet', 'Round Pipe', 'Square Tube'])

length = st.number_input("Length (mm)", min_value=0)
if member_type in ['Mild Steel Plate', 'Flat', 'CR Sheet']:
    breadth = st.number_input("Breadth (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)
elif member_type == 'Round Plate':
    diameter = st.number_input("Diameter (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)
elif member_type == 'Round Plate with Bore':
    diameter = st.number_input("Diameter (mm)", min_value=0)
    inner_diameter = st.number_input("Inner Diameter (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)
elif member_type == 'Round Pipe':
    diameter = st.number_input("Diameter (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)
elif member_type == 'Square Tube':
    side = st.number_input("Side Length (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)
elif member_type == 'Channel':
    height = st.number_input("Height (mm)", min_value=0)
    flange_width = st.number_input("Flange Width (mm)", min_value=0)
    flange_thickness = st.number_input("Flange Thickness (mm)", min_value=0)
    web_thickness = st.number_input("Web Thickness (mm)", min_value=0)
elif member_type == 'Angle':
    leg1 = st.number_input("Leg1 Width (mm)", min_value=0)
    leg2 = st.number_input("Leg2 Width (mm)", min_value=0)
    thickness = st.number_input("Thickness (mm)", min_value=0)

if st.button("Calculate Weight and Cost"):
    if member_type in ['Mild Steel Plate', 'Flat', 'CR Sheet']:
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, breadth, thickness)
    elif member_type == 'Round Plate':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, thickness=thickness, diameter=diameter)
    elif member_type == 'Round Plate with Bore':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, thickness=thickness, diameter=diameter, inner_diameter=inner_diameter)
    elif member_type == 'Round Pipe':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, thickness=thickness, diameter=diameter)
    elif member_type == 'Square Tube':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, thickness=thickness, side=side)
    elif member_type == 'Channel':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, height=height, flange_width=flange_width, flange_thickness=flange_thickness, web_thickness=web_thickness)
    elif member_type == 'Angle':
        dimensions, weight, total_cost = calculate_weight_and_cost(member_type, length, leg1=leg1, leg2=leg2, thickness=thickness)

    st.write(f"**Type**: {member_type}")
    st.write(f"**Dimensions**: {dimensions}")
    st.write(f"**Weight**: {weight:.2f} Kg")
    st.write(f"**Total Cost**: Rs {total_cost:.2f}")
