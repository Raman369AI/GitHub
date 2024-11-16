import streamlit as st
import requests

# Title of the web app
st.title("Mushroom Predictor")

# Create input fields for each feature
cap_diameter = st.number_input("Cap Diameter (numeric)", format="%.2f")
cap_shape = st.text_input("Cap Shape")
cap_surface = st.text_input("Cap Surface")
cap_color = st.text_input("Cap Color")
does_bruise_or_bleed = st.text_input("Does Bruise or Bleed")
gill_attachment = st.text_input("Gill Attachment")
gill_spacing = st.text_input("Gill Spacing")
gill_color = st.text_input("Gill Color")
stem_height = st.number_input("Stem Height (numeric)", format="%.2f")
stem_width = st.number_input("Stem Width (numeric)", format="%.2f")
stem_root = st.text_input("Stem Root")
stem_surface = st.text_input("Stem Surface")
stem_color = st.text_input("Stem Color")
veil_type = st.text_input("Veil Type")
veil_color = st.text_input("Veil Color")
has_ring = st.text_input("Has Ring")
ring_type = st.text_input("Ring Type")
spore_print_color = st.text_input("Spore Print Color")
habitat = st.text_input("Habitat")
season = st.text_input("Season")
prediction_placeholder = st.empty()

# Button to trigger prediction
if st.button("Submit"):
    # Prepare the data to send to the API
    input_data = {
        "cap-diameter": cap_diameter,
        "cap-shape": cap_shape,
        "cap-surface": cap_surface,
        "cap-color": cap_color,
        "does-bruise-or-bleed": does_bruise_or_bleed,
        "gill-attachment": gill_attachment,
        "gill-spacing": gill_spacing,
        "gill-color": gill_color,
        "stem-height": stem_height,
        "stem-width": stem_width,
        "stem-root": stem_root,
        "stem-surface": stem_surface,
        "stem-color": stem_color,
        "veil-type": veil_type,
        "veil-color": veil_color,
        "has-ring": has_ring,
        "ring-type": ring_type,
        "spore-print-color": spore_print_color,
        "habitat": habitat,
        "season": season
    }

    # Send the request to the FastAPI prediction endpoint
    try:
        response = requests.post("https://raman12345-bzg7bhdkfbh4beft.centralindia-01.azurewebsites.net/predict", json=input_data)
        response.raise_for_status()  # Raise an error for bad responses

        # Get the prediction from the response
        prediction = response.json().get("prediction")
        prediction_placeholder.markdown(f"<h1 style='text-align: center; color: green;'>{prediction}</h1>", unsafe_allow_html=True)

        #st.success(f"Prediction: {prediction}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error("An unexpected error occurred.")
#http://127.0.0.1:8000/predict