import tkinter as tk
from tkinter import ttk, messagebox


def on_submit():
    input_text = input_entry.get().strip()

    if not input_text:
        messagebox.showerror("Error", "Please enter some text!")
        return

    messagebox.showinfo("Success", "Data Fetched Successfully")


root = tk.Tk()
root.title("Post Pulse")

window_width = 560
window_height = 312

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.configure(bg="#F5F5F5")

style = ttk.Style(root)
style.theme_use("clam")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

header_frame = tk.Frame(root, bg="#1E88E5")
header_frame.grid(row=0, column=0, sticky="ew")
header_frame.columnconfigure(0, weight=1)

header_label = tk.Label(
    header_frame,
    text="Post Pulse",
    bg="#1E88E5",
    fg="white",
    font=("Helvetica", 20, "bold"),
)
header_label.grid(row=0, column=0, pady=20, padx=10)

input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

input_frame.columnconfigure(1, weight=1)

input_label = tk.Label(
    input_frame, text="Enter Account Link:", bg="#F5F5F5", font=("Arial", 14, "bold")
)
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

input_entry = ttk.Entry(input_frame, font=("Arial", 14))
input_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.grid(row=2, column=0, sticky="ew", pady=10)
button_frame.columnconfigure(0, weight=1)

submit_button = ttk.Button(button_frame, text="Submit", command=on_submit)
submit_button.grid(row=0, column=0, padx=20, pady=10, ipadx=15, ipady=5)

root.mainloop()
