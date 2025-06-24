import streamlit as st
import requests

API_KEY = "f465ede8166380b820d669ea15f5609d"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

st.set_page_config(page_title="Weather Checker 🌦️")
st.title("🌦️ Weather Checker App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city:
        data = get_weather(city)
        if data.get("cod") != 200:
            st.error(f"City not found: {city}")
        else:
            st.success(f"Weather for {city.title()}:")
            st.metric("🌡️ Temperature", f"{data['main']['temp']}°C")
            st.write(f"**☁️ Description**: {data['weather'][0]['description'].title()}")
            st.write(f"**💧 Humidity**: {data['main']['humidity']}%")
            st.write(f"**🌬️ Wind Speed**: {data['wind']['speed']} m/s")
    else:
        st.warning("Please enter a city name.")
