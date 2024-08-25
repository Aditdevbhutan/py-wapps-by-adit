import customtkinter as ctk

def clk(b):
    if b == "=":
        disp.insert(ctk.END, f"={eval(disp.get())}")
    elif b == "c":
        disp.delete(0, ctk.END)
    else:
        disp.insert(ctk.END, b)

# Initialize the app
app = ctk.CTk()
app.title("Calculator")

# Create the display entry widget
disp = ctk.CTkEntry(app, width=240)
disp.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
btns = ["7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", "c", "=", "+"]

# Create buttons using a loop
for i, b in enumerate(btns):
    ctk.CTkButton(app, text=b, command=lambda x=b: clk(x)) \
    .grid(row=i//4 + 1, column=i % 4, padx=5, pady=5)

# Run the app
app.mainloop()
