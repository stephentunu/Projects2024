import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
from colorama import init, Fore
import tkinter as tk
import PSReadLine
from tkinter import messagebox

init()

def device_location(phone_number):
    # ... (your existing device_location function)

def get_lat_lng(location):
    try:
        key = "YOUR-API-KEY"  # Replace with your actual API key
        geocoder_instance = OpenCageGeocode(key)
        results = geocoder_instance.geocode(location)
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    except Exception:
        return None, None

def show_exact_location_on_map(latitude, longitude, location):
    # ... (your existing show_exact_location_on_map function)
    pass

def login():
    # Create a login window
    login_window = tk.Tk()
    login_window.title("Phone Tracking App Login")

    # Add widgets (labels, entry fields, buttons, etc.) to the login window
    label = tk.Label(login_window, text="Enter your phone number: ")
    label.pack()

    phone_entry = tk.Entry(login_window)
    phone_entry.pack()

    def handle_login():
        phone_number = phone_entry.get()
        location, service_provider = device_location(phone_number)

        if location and service_provider:
            messagebox.showinfo("Login Successful", f"Location: {location}\nService Provider: {service_provider}")
            lat, lng = get_lat_lng(location)
            if lat and lng:
                show_exact_location_on_map(lat, lng, location)
                print(f"Map saved as Location.html")
            else:
                print(f"{Fore.RED}Error fetching latitude and longitude.{Fore.RESET}")
        else:
            messagebox.showerror("Login Failed", "Invalid phone number.")

    login_button = tk.Button(login_window, text="Login", command=handle_login)
    login_button.pack()

    login_window.mainloop()

if __name__ == "__main__":
    login()import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode
from colorama import init, Fore
import tkinter as tk
from tkinter import messagebox

init()

def device_location(phone_number):
    # ... (your existing device_location function)
    pass

def get_lat_lng(location):
    try:
        key = "YOUR-API-KEY"  # Replace with your actual API key
        geocoder_instance = OpenCageGeocode(key)
        results = geocoder_instance.geocode(location)
        latitude = results[0]['geometry']['lat']
        longitude = results[0]['geometry']['lng']
        return latitude, longitude
    except Exception:
        return None, None

def show_exact_location_on_map(latitude, longitude, location):
    # ... (your existing show_exact_location_on_map function)
    pass

def login():
    # Create a login window
    login_window = tk.Tk()
    login_window.title("Phone Tracking App Login")

    # Add widgets (labels, entry fields, buttons, etc.) to the login window
    label = tk.Label(login_window, text="Enter your phone number: ")
    label.pack()

    phone_entry = tk.Entry(login_window)
    phone_entry.pack()

    def handle_login():
        phone_number = phone_entry.get()
        location, service_provider = device_location(phone_number)

        if location and service_provider:
            messagebox.showinfo("Login Successful", f"Location: {location}\nService Provider: {service_provider}")
            lat, lng = get_lat_lng(location)
            if lat and lng:
                show_exact_location_on_map(lat, lng, location)
                print(f"Map saved as Location.html")
            else:
                print(f"{Fore.RED}Error fetching latitude and longitude.{Fore.RESET}")
        else:
            messagebox.showerror("Login Failed", "Invalid phone number.")

    login_button = tk.Button(login_window, text="Login", command=handle_login)
    login_button.pack()

    login_window.mainloop()

if __name__ == "__main__":
    login()