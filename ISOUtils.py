import tkinter as tk
from tkinter import filedialog
import subprocess

def mount_udf():
    source = source_entry.get()
    mount_path = mount_entry.get()
    subprocess.call(["mdconfig", "-a", "-t", "vnode", "-f", source, "-u", "0"])
    subprocess.call(["mount", "-t", "udf", "/dev/md0", mount_path])

def unmount_udf():
    mount_path = mount_entry.get()
    subprocess.call(["umount", mount_path])
    subprocess.call(["mdconfig", "-d", "-u", "0"])

def browse_path():
    mount_path = filedialog.askdirectory()
    mount_entry.delete(0,tk.END)
    mount_entry.insert(0, mount_path)

root = tk.Tk()
root.title("UDF Mount Utility")

source_label = tk.Label(root, text="Source:")
source_label.grid(row=0, column=0)

source_entry = tk.Entry(root)
source_entry.grid(row=0, column=1)

browse_button = tk.Button(root, text="Browse", command=lambda: source_entry.insert(0, filedialog.askopenfilename()))
browse_button.grid(row=0, column=2)

mount_label = tk.Label(root, text="Mount Path:")
mount_label.grid(row=1, column=0)

mount_entry = tk.Entry(root)
mount_entry.grid(row=1, column=1)

browse_mount_path_button = tk.Button(root, text="Browse", command=browse_path)
browse_mount_path_button.grid(row=1, column=2)

mount_button = tk.Button(root, text="Mount", command=mount_udf)
mount_button.grid(row=2, column=0)

unmount_button = tk.Button(root, text="Unmount", command=unmount_udf)
unmount_button.grid(row=2, column=1)

root.mainloop()
