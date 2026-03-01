import tkinter as tk
from tkinter import filedialog, messagebox

# Create main window
window = tk.Tk()
window.title("Simple Text Editor")
window.geometry("700x500")
window.minsize(500, 300)

# ---------- FUNCTIONS ----------

def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())
        window.title(f"Text Editor - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))
        window.title(f"Text Editor - {filepath}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- LAYOUT ----------

button_frame = tk.Frame(window, padx=5, pady=5)
button_frame.pack(side="left", fill="y")

open_btn = tk.Button(button_frame, text="Open", command=open_file)
open_btn.pack(fill="x", pady=5)

save_btn = tk.Button(button_frame, text="Save As", command=save_file)
save_btn.pack(fill="x")

text = tk.Text(window, wrap="word")
text.pack(side="right", expand=True, fill="both")

# Start app
window.mainloop()