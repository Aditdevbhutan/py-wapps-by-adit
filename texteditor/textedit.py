import customtkinter as ctk
from tkinter import filedialog, messagebox, Menu  # Import Menu from tkinter

def new_file():
    text.delete(1.0, ctk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, ctk.END)
            text.insert(ctk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, ctk.END))
            messagebox.showinfo("Info", "File saved successfully in Adit Text Editor!!")

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Adit Text Editor")
root.geometry("800x600")

menu = Menu(root)  # Use standard Menu
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = ctk.CTkTextbox(root, wrap=ctk.WORD, font=("Helvetica", 12), fg_color="lightblue")
text.pack(expand=ctk.YES, fill=ctk.BOTH)

root.mainloop()
