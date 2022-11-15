import tkinter as tk
import requests
import json


def change_zip(label, zip, root):
    try:
        api_request = requests.get(
            f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip}&distance=5&API_KEY=D16ACBFC-403F-43AF-8505-4D23CE913338")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]
        color = "#ffffff"

        match category:
            case "Good": color = "#0C0"
            case "Moderate": color = "#FFFF00"
            case "Unhealthy for Sensitive Groups": color = "#ff9900"
            case "Unhealthy": color = "#ff0000"
            case "Very Unhealthy": color = "990066"
            case "Hazardous": color = "#660000"
            case _: color = "#ffffff"

        root.configure(bg=color)
        label.config(text=f"{city} Air Quality {quality} {category}", font=(
            "Helvetica", 20), bg=color)
    except Exception as _:
        root.configure(bg="white")
        label.config(text="Not Found", font=(
            "Helvetica", 20), bg="white")


def main():
    root = tk.Tk()
    root.title("Quality Air App")
    root.iconbitmap("cloudy.ico")
    root.resizable(False, False)

    label = tk.Label(root, text="TEST")
    label.grid(row=0, column=0, columnspan=2)
    change_zip(label, "70801", root)

    zip_entry = tk.Entry(root, text="Enter zip code")
    zip_entry.grid(row=1, column=0, sticky=tk.E, padx=5)

    zip_button = tk.Button(root, text="Check quality", command=lambda: change_zip(
        label, zip_entry.get(), root))
    zip_button.grid(row=1, column=1, sticky=tk.W, pady=5)

    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error in program:")
        print(e)
        exit(-1)
