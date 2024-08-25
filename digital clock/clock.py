import customtkinter as ctk
from time import strftime

# Initialize the main window
root = ctk.CTk()
root.title("Digital Clock Adit")

def time():
    # Change time format to 12-hour format with AM/PM
    string = strftime('%I:%M:%S %p \n %D ')
    label.configure(text=string)
    label.after(1000, time)

# Configure the appearance and colors
ctk.set_appearance_mode("light")  # Modes: "System" (default), "Light", "Dark"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# Create a custom label with customtkinter
label = ctk.CTkLabel(root, text="", font=('New Times Roman', 60, 'bold'), text_color='black')
label.pack(anchor='center', pady=20, padx=20)

# Call the time function to update the clock
time()

# Start the main loop
root.mainloop()
