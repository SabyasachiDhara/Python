import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText
from PIL import Image  # for button icon
from threading import Thread
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ---------------- CONFIG ----------------
ROUTER_URL = "http://192.168.0.1/"
ROUTER_PASS = "admin"
HEADLESS = True
# ----------------------------------------

def log(msg, color="black"):
    text_area.config(state='normal')
    text_area.insert("end", f"{time.strftime('%b%d,%Y %I:%M:%S')} - {msg}\n", color)
    text_area.see("end")
    text_area.config(state='disabled')

def reboot_router():
    base_dir = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
    chrome_binary = os.path.join(base_dir, "chrome-portable", "chrome.exe")
    chromedriver_path = os.path.join(base_dir, "chromedriver.exe")

    options = Options()
    options.binary_location = chrome_binary
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(executable_path=chromedriver_path)
    try:
        log("[*] Starting...", "blue")
        driver = webdriver.Chrome(service=service, options=options)

        log(f"[*] Opening router CP...", "blue")
        driver.get(ROUTER_URL)
        time.sleep(1)

        try:
            pwd = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            pwd.clear()
            pwd.send_keys(ROUTER_PASS)
            pwd.send_keys(Keys.ENTER)
            log("[*] Logged in...", "green")
        except Exception as e:
            log("[!] ERROR,,,Pswd input NF: " + str(e), "red")
            driver.quit()
            return

        time.sleep(2)

        reboot_clicked = False
        for xp in ["//*[normalize-space(text())='Reboot']",
                   "//button[contains(text(),'Reboot')]",
                   "//span[contains(text(),'Reboot')]",
                   "//a[contains(text(),'Reboot')]"]:
            try:
                driver.find_element(By.XPATH, xp).click()
                log(f"[*] Reboot Section Opened...", "yellow")
                reboot_clicked = True
                break
            except:
                continue
        if not reboot_clicked:
            log("[!] ERROR,,,Reboot btn NF.", "red")
            driver.quit()
            return

        time.sleep(1)

        yes_clicked = False
        for xp in ["//*[normalize-space(text())='Yes']",
                   "//span[normalize-space(text())='Yes']",
                   "//div[normalize-space(text())='Yes']"]:
            try:
                driver.find_element(By.XPATH, xp).click()
                log("[*] Router reboot triggered!!!", "yellow")
                yes_clicked = True
                break
            except:
                continue
        if not yes_clicked:
            log("[!] ERROR,,,Yes btn NF.", "red")

        time.sleep(2)
        driver.quit()
        log("[*] DONE!!!", "green")

    except Exception as e:
        log("[!] Error: " + str(e), "red")

def start_reboot():
    Thread(target=reboot_router).start()

# ---------------- GUI ----------------
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("TP-Link Router Rebooter")
root.geometry("500x400")

# Header
header = ctk.CTkLabel(root, text="বেতার 🔄 192.168.0.1\n───── ⋆⋅☆⋅⋆ ─────", font=("Arial", 18, "bold"))
header.pack(pady=10)

# Load router icon for button
icon_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "router.png")
if os.path.exists(icon_path):
    router_icon = ctk.CTkImage(Image.open(icon_path), size=(24, 24))
else:
    router_icon = None

# Rounded button with icon and hover
btn = ctk.CTkButton(root, text="Reboot Router", corner_radius=20, fg_color="#4CAF50",
                    hover_color="#45a049", font=("Arial", 14, "bold"),
                    command=start_reboot, image=router_icon, compound="left")
btn.pack(pady=15, ipadx=10, ipady=5)

# Status panel
text_area = ScrolledText(root, state='disabled', width=60, height=15, bg="#2e2e3e", fg="#ffffff", font=("Consolas", 10))
text_area.pack(padx=10, pady=10)

# Footer
footer = ctk.CTkLabel(root, text="Developed by Sabyasachi Dhara", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

# Colored log tags
text_area.tag_configure("red", foreground="red")
text_area.tag_configure("green", foreground="lime")
text_area.tag_configure("blue", foreground="cyan")
text_area.tag_configure("yellow", foreground="yellow")

root.mainloop()
