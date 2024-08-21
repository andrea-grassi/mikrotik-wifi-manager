import paramiko
import tkinter as tk
from tkinter import font
from tkinter import ttk

# Configuration
router_ip = "router-ip-address"
username = "username"
password = "password"

# Send commands via SSH to MikroTik router
def send_command(command):
    try:
        # SSHClient instance
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(router_ip, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()
        
        ssh.close()
        
        if error:
            show_message("Error", f"Error: {error}", "error")
        else:
            if "enable" in command:
                show_message("Success", "WiFi has been enabled 🍺", "success")
            else:
                show_message("Success", "WiFi has been disabled 🍺", "success")
    except Exception as e:
        show_message("Error", f"Error on SSH connection: {e} 😵", "error")

def show_message(title, message, message_type):
    msg_icon = {
        "success": "✅",
        "error": "❌"
    }.get(message_type, "")
    
    top = tk.Toplevel(root)
    top.title(title)

    window_width = 400
    window_height = 100
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    top.geometry(f"{window_width}x{window_height}+{x}+{y}")
    top.resizable(False, False)
    
    lbl_msg = tk.Label(top, text=f"{msg_icon} {message}", font=('Arial', 12), pady=10)
    lbl_msg.pack()

    btn_ok = tk.Button(top, text="OK", command=top.destroy, width=10)
    btn_ok.pack(pady=5)

# Turn WiFi on
def wifi_on():
    send_command("/interface wireless enable wlan1")

# Turn WiFi off
def wifi_off():
    send_command("/interface wireless disable wlan1")

# Main window
root = tk.Tk()
root.title("MikroTik WiFi")
root.geometry("300x150")

window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

button_font = font.Font(family='Arial', size=12, weight='bold')

btn_on = ttk.Button(root, text="Turn WiFi On", command=wifi_on, width=20)
btn_on['style'] = 'TButton'
btn_on.pack(pady=10)

btn_off = ttk.Button(root, text="Turn WiFi Off", command=wifi_off, width=20)
btn_off['style'] = 'TButton'
btn_off.pack(pady=10)

style = ttk.Style()
style.configure('TButton', font=button_font, padding=10)

# Start GUI
root.mainloop()