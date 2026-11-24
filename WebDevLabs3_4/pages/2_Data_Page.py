# Lab 3: API data page
# TODO: Rename this file to fit your page. Keep the number at the front, since it sets the
#       page's order in the sidebar (for example, 2_Pokedex.py).
#
# This page shows data from your API, processed with your own Python code. No AI on this page.
# It should have:
#   - at least 2 meaningful user inputs (for example st.selectbox, st.text_input, st.slider)
#   - at least 2 dynamic visuals that change based on the user's input: charts, displays of
#     images, or other visualizations (see the example website for examples!)

import requests
import streamlit as st
import pandas as pd
import plotly.express as px

url = "https://atlanta.data.socrata.com/resource/jmke-icfi.json"
response = requests.get(url, timeout=10)
data = response.json()
print(data)

# Separating my data!
# Bar Graph Data
totals = {}
for payment in data:
    vendor = payment["vendor_name"]
    amount = float(payment["amount"])
    if vendor in totals:
        totals[vendor] += amount
    else:
        totals[vendor] = amount
# Bar Graph
st.header("Vendor Payment Comparison")
vendor_names = list(totals.keys())
selected = st.multiselect("Choose vendors to compare", vendor_names, default = vendor_names[:5])

chosen_labels = []
chosen_values = []
for vendor, total in totals.items():
    if vendor in selected:
        chosen_labels.append(vendor)
        chosen_values.append(total)

fig2 = px.bar(x=chosen_labels, y=chosen_values, labels={"x": "Vendor", "y": "Amount $"})
st.plotly_chart(fig2)

# Pie Chart

