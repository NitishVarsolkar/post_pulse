import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
from database_utils import send_data_to_astra
from pandastable import Table

def load_excel(file_path):
    try:
        data = pd.read_excel(file_path, sheet_name=None)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error loading Excel file: {e}")
        return None

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        file_name_var.set(file_path.split("/")[-1])
        return file_path
    return None

def upload_file():
    global data
    file_path = browse_file()
    if file_path:
        data = load_excel(file_path)
        if data:
            sheet_name_var.set("")
            sheet_name_menu["menu"].delete(0, "end")
            for sheet in data.keys():
                sheet_name_menu["menu"].add_command(label=sheet, command=tk._setit(sheet_name_var, sheet))
            messagebox.showinfo("Success", "Excel file loaded successfully.")

def send_to_database():
    if not data:
        messagebox.showerror("Error", "No data loaded to send to the database.")
        return
    try:
        if send_data_to_astra(data):
            messagebox.showinfo("Success", "Data sent to the database successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending data to the database: {e}")

def display_data(sheet_name):
    if not data:
        messagebox.showerror("Error", "No data loaded. Please upload an Excel file first.")
        return
    if sheet_name not in data:
        messagebox.showerror("Error", f"Sheet '{sheet_name}' not found in the data.")
        return
    for widget in table_frame.winfo_children():
        widget.destroy()
    table = Table(table_frame, dataframe=data[sheet_name], showtoolbar=False, showstatusbar=False, editable=False)
    table.show()

root = tk.Tk()
root.title("Excel Viewer")
root.state('zoomed')

data = None
sheet_name_var = tk.StringVar()
file_name_var = tk.StringVar(value="No file selected")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=10, font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TOptionMenu", font=("Arial", 12))

top_frame = tk.Frame(root, bg="#f4f4f4", height=50)
top_frame.pack(fill=tk.X)

file_label = tk.Label(top_frame, textvariable=file_name_var, bg="#f4f4f4", fg="#333", font=("Arial", 12, "bold"))
file_label.pack(side=tk.LEFT, padx=20, pady=10)

upload_button = ttk.Button(top_frame, text="Upload Excel File", command=upload_file)
upload_button.pack(side=tk.RIGHT, padx=20, pady=10)

table_frame = tk.Frame(root, bg="#ffffff")
table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

bottom_frame = tk.Frame(root, bg="#f4f4f4", height=50)
bottom_frame.pack(fill=tk.X)

sheet_name_label = ttk.Label(bottom_frame, text="Select Sheet:")
sheet_name_label.pack(side=tk.LEFT, padx=10, pady=10)

sheet_name_menu = ttk.OptionMenu(bottom_frame, sheet_name_var, "")
sheet_name_menu.pack(side=tk.LEFT, padx=10, pady=10)

view_button = ttk.Button(bottom_frame, text="View Sheet", command=lambda: display_data(sheet_name_var.get()))
view_button.pack(side=tk.LEFT, padx=10, pady=10)

send_button = ttk.Button(bottom_frame, text="Send to Database", command=send_to_database)
send_button.pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
