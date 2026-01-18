import tkinter as tk
root = tk.Tk()
root.title("drawing pad")
root.geometry("800x600")

controls = tk.Frame(root)
controls.grid(row=0, column=0, stick="ew", padx=8, pady=8)
canvas = tk.Canvas(root, bg="white", width= 760, height=480)
canvas.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
 
current_color = "black"
pen_size = 5
last_x, last_y = None,None

def start_draw(event):
    global last_x, last_y
    last_x,laxt_y = event.x, event.y

def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill=current_color, width=pen_size,
                           capstyle=tk.ROUND)
    last_x, last_y = event.x, event.y

def end_draw(event):
    global last_x, last_y
    last_x, last_y = None, None

canvas.bind("<Button-1>, start_draw")
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", end_draw)

def set_black():
    global current_color
    current_color = "black"
def set_red():
    global current_color
    current_color = "red"
def set_blue():
    global current_color
    current_color = "blue"
def set_green():
    global current_color
    current_color = "green"
btn_black = tk.Button(controls, text="black", command=set_black)
btn_black.grid(row=0, column=0, padx=2)
btn_black = tk.Button(controls, text="red", command=set_red)
btn_black.grid(row=0, column=1, padx=2)
btn_black = tk.Button(controls, text="blue", command=set_blue)
btn_black.grid(row=0, column=2, padx=2)
btn_black = tk.Button(controls, text="green", command=set_green)
btn_black.grid(row=0, column=3, padx=2)

def change_size(value):
    global pen_size
    pen_size =int(value)
size_label = tk.Label(controls, text="pen size:")
size_label.grid(row=0,column=4, padx=6)
size_scale = tk.Scale(controls, from_=1, to=99,
                      orient="horizontal",
                      command=change_size)
size_scale.set(5)
size_scale.grid(row=0, column=5)

def clear_canvas():
    canvas.delete("all")
clear_btn = tk.Button(controls, text="clear", command=clear_canvas)
clear_btn.grid(row=0, column=6, padx=6)




root.mainloop()