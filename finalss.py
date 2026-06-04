import json
import tkinter as tk                #tkinter create the window,buttons,labels textbox
from tkinter import messagebox
import _json
import os



#folder from the driver
drivers = []

FILE_NAME = "drivers.json"

def load_data():
    global drivers
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                drivers = json.load(file)
        except:
            drivers = []
def save_data():
    global drivers
    with open(FILE_NAME, "w") as file:
        json.dump(drivers, file, indent=4)

def add_driver():                   #where the function or ano an gin dedefine hini dinhi like an drivers
    license_no = license_entry.get()
    name = name_entry.get()                         #didi asya kana didi makuha han information of the users
    age = age_entry.get()
    address = address_entry.get()
    contact_no = contact_entry.get()
    plate_no = plate_entry.get()
    gender = gender_entry.get()
    vehicle_no = vehicle_entry.get()


    if license_no == "" or name == "":
        messagebox.showerror("OPPS", "PLEASE FILL ALL FIELDS!")
        return

    driver = {"License": license_no, "Name": name, "Age": age, "Address": address, "Contact": contact_no, "Plate": plate_no, "Gender": gender, "Vehicle": vehicle_no}
    drivers.append(driver)
    save_data()
    messagebox.showinfo("Success", "Driver Added!")

    clear_fields()
    view_drivers()

def view_drivers():

    listbox.delete(0, tk.END)

# check every driver one by one
    for driver in drivers:
        display = (
            f"{driver['License']} | "       
            f"{driver['Name']} | "          
            f"{driver['Age']} | "
            f"{driver['Address']}|"
            f"{driver['Contact']} | "
            f"{driver['Plate']}|"
            f"{driver['Gender']}"
            f"{driver['Vehicle']}"
        )

        listbox.insert(tk.END, display)         #add the text to the list


def update_driver(index=None):

    selected = listbox.curselection()

    if not selected:
        drivers.pop(index)
        messagebox.showerror("OPPS", "PLEASE SELECT A DRIVER!")
        return
    index = selected[0]

    drivers[index]["License"] = license_entry.get()
    drivers[index]["Name"] = name_entry.get()
    drivers[index]["Age"] = age_entry.get()
    drivers[index]["Address"] = address_entry.get()
    drivers[index]["Contact"] = contact_entry.get()
    drivers[index]["Plate"] = plate_entry.get()
    drivers[index]["Gender"] = gender_entry.get()
    drivers[index]["Vehicle"] = vehicle_entry.get()

    messagebox.showinfo("Success", "Driver Updated!")

    clear_fields()
    view_drivers()


def delete_driver():

    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("OPPS", "PLEASE SELECT A DRIVER!")
        return

    index = selected[0]
    drivers.pop(index)
    messagebox.showinfo("Success", "Driver Deleted!")

    save_data()
    clear_fields()
    view_drivers()


def clear_fields():

    license_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    plate_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    vehicle_entry.delete(0, tk.END)

    save_data()

def select_driver(event):

    selected = listbox.curselection()

    if selected:
        index = selected[0]                                    #select a driver and
        clear_fields()

        license_entry.insert(0, drivers[index]["License"])
        name_entry.insert(0, drivers[index]["Name"])
        age_entry.insert(0, drivers[index]["Age"])
        address_entry.insert(0, drivers[index]["Address"])
        contact_entry.insert(0, drivers[index]["Contact"])
        plate_entry.insert(0, drivers[index]["Plate"])
        gender_entry.insert(0, drivers[index]["Gender"])
        vehicle_entry.insert(0, drivers[index]["Plate"])

root = tk.Tk()                      #create main window
root.title("Driver Information System")
root.geometry("700x500")
root.configure(bg="maroon")

title = tk.Label(
    root,
    text="DRIVER INFORMATION SYSTEM",
    font=("Arial", 18, "bold"),
    bg="yellow",
    fg="black"
)
title.pack(fill="x")

frame = tk.Frame(root, bg="maroon")                #frame of box
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="maroon", fg="white").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Age", bg="maroon", fg="white").grid(row=1, column=0)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1)

tk.Label(frame, text="Gender", bg="maroon", fg="white").grid(row=2, column=0)
gender_entry = tk.Entry(frame)
gender_entry.grid(row=2, column=1)

tk.Label(frame, text="Address", bg="maroon", fg="white").grid(row=3, column=0)
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1)

tk.Label(frame, text="License Number", bg="maroon", fg="white").grid(row=4, column=0)
license_entry = tk.Entry(frame)
license_entry.grid(row=4, column=1)

tk.Label(frame, text="Contact Number", bg="maroon", fg="white").grid(row=5, column=0)
contact_entry = tk.Entry(frame)
contact_entry.grid(row=5, column=1)

tk.Label(frame, text="Plate Number", bg="maroon", fg="white").grid(row=6, column=0)
plate_entry = tk.Entry(frame)
plate_entry.grid(row=6, column=1)

tk.Label(frame, text="Vehicle Type", bg="maroon", fg="white").grid(row=7, column=0)
vehicle_entry = tk.Entry(frame)
vehicle_entry.grid(row=7, column=1)


button_frame = tk.Frame(root, bg="maroon")
button_frame.pack(pady=10)

tk.Button(button_frame,
          text="ADD",
          bg="green",
          fg="white",
          width=12,
          command=add_driver).grid(row=0, column=0, padx=5)

tk.Button(button_frame,
          text="UPDATE",
          bg="orange",
          fg="white",
          width=12,
          command=update_driver).grid(row=0, column=1, padx=5)

tk.Button(button_frame,
          text="DELETE",
          bg="red",
          fg="white",
          width=12,
          command=delete_driver).grid(row=0, column=2, padx=5)

tk.Button(button_frame,
          text="CLEAR",
          bg="blue",
          fg="white",
          width=12,
          command=clear_fields).grid(row=0, column=3, padx=5)


listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)

load_data()
view_drivers()
listbox.bind("<<ListboxSelect>>", select_driver)

root.mainloop()

