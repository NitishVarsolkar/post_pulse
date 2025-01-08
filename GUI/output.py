import tkinter as tk
from tkinter import ttk

def create_header(parent):
    """Create the header section."""
    header_frame = tk.Frame(parent, bg="#f25c54", height=80)
    header_frame.pack(fill="x", side="top")

    header_label = tk.Label(
        header_frame,
        text="Post Pulse",
        bg="#f25c54",
        fg="white",
        font=("Helvetica", 22, "bold"),
    )
    header_label.pack(pady=20)

    return header_frame


def create_ai_review_section(parent):
    """Create the AI Review section."""
    frame = tk.Frame(parent, bg="white", pady=20)
    frame.pack(fill="x", padx=20, pady=10)

    title_label = tk.Label(
        frame, text="AI Review", bg="white", font=("Helvetica", 16, "bold")
    )
    title_label.pack(anchor="w")

    # Create a placeholder text box for AI review
    text_box = tk.Text(frame, height=6, wrap="word", font=("Helvetica", 12), padx=10, pady=10, bd=0, relief="flat", bg="#f9f9f9")
    text_box.insert("1.0", "Awaiting AI Review...")
    text_box.pack(fill="x", pady=5)

    return frame


def create_engagement_rate_section(parent):
    """Create the Engagement Rate section."""
    frame = tk.Frame(parent, bg="white", pady=20)
    frame.pack(fill="x", padx=20, pady=10)

    title_label = tk.Label(
        frame, text="Engagement Rate", bg="white", font=("Helvetica", 16, "bold")
    )
    title_label.pack(anchor="w")

    # Create an entry box for engagement rate
    entry_box = tk.Entry(frame, font=("Helvetica", 14), bg="#f9f9f9", bd=1, relief="solid")
    entry_box.insert(0, "Awaiting Calculation...")
    entry_box.pack(fill="x", pady=5)

    return frame


def create_table_section(parent):
    """Create the Table section."""
    frame = tk.Frame(parent, bg="white", pady=20)
    frame.pack(fill="both", expand=True, padx=20, pady=10)

    title_label = tk.Label(
        frame, text="Table", bg="white", font=("Helvetica", 16, "bold")
    )
    title_label.pack(anchor="w")

    # Placeholder for the table
    table_placeholder = tk.Label(frame, text="No data to display yet.", bg="white", font=("Helvetica", 12), fg="#888")
    table_placeholder.pack(pady=10)

    return frame


def create_gui():
    """Create the main GUI."""
    root = tk.Tk()
    root.title("Post Pulse")
    root.geometry("900x750")
    root.configure(bg="white")

    # Create sections
    create_header(root)
    create_ai_review_section(root)
    create_engagement_rate_section(root)
    create_table_section(root)

    # Run the GUI
    root.mainloop()


if __name__ == "__main__":
    create_gui()
