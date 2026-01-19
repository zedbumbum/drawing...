import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("950x650")

# --- Setup for Saving (The "Invisible" Canvas) ---
cv_width, cv_height = 800, 500
image_data = Image.new("RGB", (cv_width, cv_height), "white")
draw_buffer = ImageDraw.Draw(image_data)

current_color = "black"
pen_size = 5
last_x, last_y = None, None

# --- Functions ---
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        # Draw on visible screen
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill=current_color, width=pen_size,
                           capstyle=tk.ROUND, smooth=True)
        # Draw on the file we will save
        draw_buffer.line([last_x, last_y, event.x, event.y], 
                         fill=current_color, width=pen_size)
    last_x, last_y = event.x, event.y

def end_draw(event):
    global last_x, last_y
    last_x, last_y = None, None

def set_color(new_color):
    global current_color
    current_color = new_color

def use_eraser():
    global current_color
    current_color = "white"

def clear_canvas():
    canvas.delete("all")
    draw_buffer.rectangle([0, 0, cv_width, cv_height], fill="white")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if file_path:
        image_data.save(file_path)
        messagebox.showinfo("Drawing Pad", "Image Saved!")

# --- UI Layout (Using GRID) ---
controls = tk.Frame(root)
controls.grid(row=0, column=0, sticky="ew", padx=8, pady=8)

canvas = tk.Canvas(root, bg="white", width=cv_width, height=cv_height, cursor="pencil")
canvas.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# 1. Color Palette Buttons
colors = ["black", "red", "blue", "green", "orange", "purple", "yellow"]
for i, color in enumerate(colors):
    btn = tk.Button(controls, bg=color, width=3, command=lambda c=color: set_color(c))
    btn.grid(row=0, column=i, padx=2)

# 2. Eraser (Placed after the colors)
eraser_btn = tk.Button(controls, text="Eraser", command=use_eraser)
eraser_btn.grid(row=0, column=7, padx=5)

# 3. Pen Size Scale
size_scale = tk.Scale(controls, from_=1, to=50, orient="horizontal", 
                      command=lambda v: globals().update(pen_size=int(v)))
size_scale.set(5)
size_scale.grid(row=0, column=8, padx=10)

# 4. Action Buttons
tk.Button(controls, text="Clear", command=clear_canvas).grid(row=0, column=9, padx=5)
tk.Button(controls, text="Save Image", fg="darkgreen", command=save_file).grid(row=0, column=10, padx=5)

# Canvas Bindings
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", end_draw)

root.mainloop()
