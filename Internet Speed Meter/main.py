import tkinter as tk
import psutil

def format_speed(bytes_per_sec):
    KB = bytes_per_sec/1024
    
    if KB < 1024 :
        return f"{KB:.1f} KB/s"
    else: 
        return f"{KB/1024:.2f} MB/s"

def update():
    global old_r , old_s
    new_r = psutil.net_io_counters().bytes_recv
    new_s = psutil.net_io_counters().bytes_sent
    
    down = new_r - old_r
    up = new_s - old_s
    
    old_r  = new_r
    old_s = new_s
    
    download_label.config(text=f"Download: {format_speed(down)}")
    upload_label.config(text=f"Upload: {format_speed(up)}")
    
    print(down, up)
    
    root.after(1000, update)

root = tk.Tk()
root.title("Internet Speed Meter")
root.geometry("280x80")
root.resizable(False, False)

old_r = psutil.net_io_counters().bytes_recv
old_s = psutil.net_io_counters().bytes_sent

download_label = tk.Label(root, text="Download: 0 KB/s", font=("Arial", 14))
download_label.pack(pady=5)

upload_label = tk.Label(root, text="Upload: 0 KB/s", font=("Arial", 14))
upload_label.pack(pady=5)


update()
root.mainloop()