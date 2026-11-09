
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkcalendar import DateEntry
from datetime import date

# ---------- DATABASE ----------
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor TEXT NOT NULL,
    department TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL
)
""")

conn.commit()

# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("LIFENEST HOSPITALS")
root.geometry("1100x850")
root.minsize(900, 700)
root.configure(bg="#edf4f8")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    rowheight=27,
    font=("Arial", 10),
    background="white",
    fieldbackground="white"
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold"),
    background="#d5e8f2"
)

# ---------- HEADER ----------
header = tk.Frame(root, bg="#176b87", pady=15)
header.pack(fill="x")

tk.Label(
    header,
    text="LIFENEST HOSPITALS",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#176b87"
).pack()

tk.Label(
    header,
    text="Patient Registration and Appointment Management",
    font=("Arial", 11),
    fg="white",
    bg="#176b87"
).pack(pady=4)

content = tk.Frame(root, bg="#edf4f8", padx=15, pady=10)
content.pack(fill="both", expand=True)


# ---------- BUTTON STYLE ----------
def make_button(parent, text, command, color="#176b87"):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg="white",
        activebackground="#0f5269",
        activeforeground="white",
        font=("Arial", 10, "bold"),
        padx=10,
        pady=6,
        cursor="hand2",
        relief="flat"
    )


# ---------- TABLE CREATION ----------
def make_table(parent, columns, widths, height):
    frame = tk.Frame(parent, bg="white")
    frame.pack(fill="both", expand=True)

    table = ttk.Treeview(
        frame,
        columns=columns,
        show="headings",
        height=height
    )

    for col, width in zip(columns, widths):
        table.heading(col, text=col)
        table.column(col, width=width, anchor="center")

    scrollbar_y = ttk.Scrollbar(
        frame, orient="vertical", command=table.yview
    )

    scrollbar_x = ttk.Scrollbar(
        frame, orient="horizontal", command=table.xview
    )

    table.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    table.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    return table


# ---------- PATIENT REGISTRATION ----------
patient_form = tk.LabelFrame(
    content,
    text="Patient Registration",
    font=("Arial", 11, "bold"),
    bg="#edf4f8",
    padx=12,
    pady=10
)

patient_form.pack(fill="x", pady=6)

tk.Label(
    patient_form,
    text="Patient Name:",
    bg="#edf4f8"
).grid(row=0, column=0, padx=8, pady=6, sticky="w")

name_entry = tk.Entry(patient_form, width=25)
name_entry.grid(row=0, column=1, padx=8, pady=6)

tk.Label(
    patient_form,
    text="Age:",
    bg="#edf4f8"
).grid(row=0, column=2, padx=8, pady=6, sticky="w")

age_entry = tk.Entry(patient_form, width=12)
age_entry.grid(row=0, column=3, padx=8, pady=6)

tk.Label(
    patient_form,
    text="Gender:",
    bg="#edf4f8"
).grid(row=1, column=0, padx=8, pady=6, sticky="w")

gender_box = ttk.Combobox(
    patient_form,
    values=["Female", "Male", "Other"],
    state="readonly",
    width=22
)

gender_box.grid(row=1, column=1, padx=8, pady=6)
gender_box.set("Female")

tk.Label(
    patient_form,
    text="Phone Number:",
    bg="#edf4f8"
).grid(row=1, column=2, padx=8, pady=6, sticky="w")

phone_entry = tk.Entry(patient_form, width=25)
phone_entry.grid(row=1, column=3, padx=8, pady=6)


# ---------- PATIENT RECORDS ----------
patient_section = tk.LabelFrame(
    content,
    text="Registered Patients",
    font=("Arial", 11, "bold"),
    bg="#edf4f8",
    padx=10,
    pady=8
)

patient_section.pack(fill="both", expand=True, pady=6)

patient_table = make_table(
    patient_section,
    ("ID", "Name", "Age", "Gender", "Phone"),
    (70, 220, 70, 100, 150),
    4
)


# ---------- SEARCH PATIENTS ----------
search_frame = tk.Frame(content, bg="#edf4f8")
search_frame.pack(fill="x", pady=5)

tk.Label(
    search_frame,
    text="Search by patient ID or name:",
    bg="#edf4f8"
).pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, width=25)
search_entry.pack(side="left", padx=5)


# ---------- APPOINTMENT FORM ----------
appointment_form = tk.LabelFrame(
    content,
    text="Book Appointment",
    font=("Arial", 11, "bold"),
    bg="#edf4f8",
    padx=12,
    pady=10
)

appointment_form.pack(fill="x", pady=6)

tk.Label(
    appointment_form,
    text="Patient ID:",
    bg="#edf4f8"
).grid(row=0, column=0, padx=6, pady=6, sticky="w")

appointment_patient_id = tk.Entry(
    appointment_form, width=12
)
appointment_patient_id.grid(
    row=0, column=1, padx=6, pady=6
)

tk.Label(
    appointment_form,
    text="Doctor:",
    bg="#edf4f8"
).grid(row=0, column=2, padx=6, pady=6, sticky="w")

doctor_box = ttk.Combobox(
    appointment_form,
    values=[
        "Dr. Tarun",
        "Dr. Akhil",
        "Dr. Priya",
        "Dr. Ravi"
    ],
    state="readonly",
    width=18
)

doctor_box.grid(row=0, column=3, padx=6, pady=6)
doctor_box.set("Dr. Tarun")

tk.Label(
    appointment_form,
    text="Department:",
    bg="#edf4f8"
).grid(row=1, column=0, padx=6, pady=6, sticky="w")

department_box = ttk.Combobox(
    appointment_form,
    values=[
        "General Medicine",
        "Cardiology",
        "Dermatology"
    ],
    state="readonly",
    width=18
)

department_box.grid(row=1, column=1, padx=6, pady=6)
department_box.set("General Medicine")

tk.Label(
    appointment_form,
    text="Appointment Date:",
    bg="#edf4f8"
).grid(row=1, column=2, padx=6, pady=6, sticky="w")

date_entry = DateEntry(
    appointment_form,
    width=16,
    date_pattern="yyyy-mm-dd",
    mindate=date.today()
)

date_entry.grid(row=1, column=3, padx=6, pady=6)

tk.Label(
    appointment_form,
    text="Appointment Time:",
    bg="#edf4f8"
).grid(row=2, column=0, padx=6, pady=6, sticky="w")

time_box = ttk.Combobox(
    appointment_form,
    values=[
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM"
    ],
    state="readonly",
    width=18
)

time_box.grid(row=2, column=1, padx=6, pady=6)
time_box.set("10:00 AM")


# ---------- APPOINTMENT RECORDS ----------
appointment_section = tk.LabelFrame(
    content,
    text="Appointment Records",
    font=("Arial", 11, "bold"),
    bg="#edf4f8",
    padx=10,
    pady=8
)

appointment_section.pack(fill="both", expand=True, pady=6)

appointment_table = make_table(
    appointment_section,
    (
        "Appointment ID",
        "Patient ID",
        "Doctor",
        "Department",
        "Date",
        "Time"
    ),
    (110, 90, 140, 160, 120, 110),
    4
)


# ---------- VIEW PATIENTS ----------
def view_patients(search=""):
    for item in patient_table.get_children():
        patient_table.delete(item)

    cursor.execute("""
        SELECT * FROM patients
        WHERE CAST(patient_id AS TEXT) LIKE ?
        OR name LIKE ?
        ORDER BY patient_id
    """, (f"%{search}%", f"%{search}%"))

    for record in cursor.fetchall():
        patient_table.insert("", tk.END, values=record)


# ---------- SEARCH PATIENT ----------
def search_patient():
    view_patients(search_entry.get().strip())


# ---------- SHOW ALL PATIENTS ----------
def show_all_patients():
    search_entry.delete(0, tk.END)
    view_patients()


# ---------- REGISTER PATIENT ----------
def register_patient():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    gender = gender_box.get()
    phone = phone_entry.get().strip()

    if not name or not age or not phone:
        messagebox.showerror(
            "Error",
            "Please fill in all patient fields."
        )
        return

    if not age.isdigit() or not 1 <= int(age) <= 120:
        messagebox.showerror(
            "Error",
            "Enter an age between 1 and 120."
        )
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror(
            "Error",
            "Enter a 10-digit phone number."
        )
        return

    cursor.execute("""
        INSERT INTO patients (name, age, gender, phone)
        VALUES (?, ?, ?, ?)
    """, (name, int(age), gender, phone))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Patient registered successfully!"
    )

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    gender_box.set("Female")

    view_patients()


# ---------- REMOVE PATIENT ----------
def remove_patient():
    selected = patient_table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a patient from the table."
        )
        return

    record = patient_table.item(
        selected[0], "values"
    )

    patient_id = record[0]
    patient_name = record[1]

    confirm = messagebox.askyesno(
        "Confirm Removal",
        f"Remove patient {patient_name} (ID: {patient_id})?\n"
        "Their appointments will also be deleted."
    )

    if confirm:
        cursor.execute(
            "DELETE FROM appointments WHERE patient_id = ?",
            (patient_id,)
        )

        cursor.execute(
            "DELETE FROM patients WHERE patient_id = ?",
            (patient_id,)
        )

        conn.commit()

        view_patients(search_entry.get().strip())
        view_appointments()

        messagebox.showinfo(
            "Success",
            "Patient removed successfully!"
        )


# ---------- VIEW APPOINTMENTS ----------
def view_appointments():
    for item in appointment_table.get_children():
        appointment_table.delete(item)

    cursor.execute("""
        SELECT * FROM appointments
        ORDER BY appointment_id
    """)

    for record in cursor.fetchall():
        appointment_table.insert("", tk.END, values=record)


# ---------- BOOK APPOINTMENT ----------
def book_appointment():
    patient_id = appointment_patient_id.get().strip()
    doctor = doctor_box.get()
    department = department_box.get()
    appointment_date = date_entry.get_date().strftime("%Y-%m-%d")
    appointment_time = time_box.get()

    if not patient_id.isdigit():
        messagebox.showerror(
            "Error",
            "Enter a valid patient ID."
        )
        return

    cursor.execute(
        "SELECT patient_id FROM patients WHERE patient_id = ?",
        (int(patient_id),)
    )

    if cursor.fetchone() is None:
        messagebox.showerror(
            "Error",
            "Patient ID not found. Register the patient first."
        )
        return

    cursor.execute("""
        INSERT INTO appointments
        (patient_id, doctor, department, date, time)
        VALUES (?, ?, ?, ?, ?)
    """, (
        int(patient_id),
        doctor,
        department,
        appointment_date,
        appointment_time
    ))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Appointment booked successfully!"
    )

    appointment_patient_id.delete(0, tk.END)
    view_appointments()


# ---------- CANCEL APPOINTMENT ----------
def cancel_appointment():
    selected = appointment_table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Appointment",
            "Select an appointment from the table."
        )
        return

    record = appointment_table.item(
        selected[0], "values"
    )

    appointment_id = record[0]

    confirm = messagebox.askyesno(
        "Confirm Cancellation",
        "Are you sure you want to cancel this appointment?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM appointments WHERE appointment_id = ?",
            (appointment_id,)
        )

        conn.commit()
        view_appointments()

        messagebox.showinfo(
            "Cancelled",
            "Appointment cancelled successfully."
        )


# ---------- PATIENT BUTTONS ----------
make_button(
    patient_form,
    "Register Patient",
    register_patient
).grid(
    row=2, column=0, columnspan=2, pady=8
)

make_button(
    patient_form,
    "Remove Patient",
    remove_patient,
    color="#b43c46"
).grid(
    row=2, column=2, columnspan=2, pady=8
)


# ---------- SEARCH BUTTONS ----------
make_button(
    search_frame,
    "Search",
    search_patient
).pack(side="left", padx=4)

make_button(
    search_frame,
    "Show All",
    show_all_patients,
    color="#53758a"
).pack(side="left", padx=4)


# ---------- APPOINTMENT BUTTONS ----------
make_button(
    appointment_form,
    "Book Appointment",
    book_appointment
).grid(
    row=2, column=3, padx=6, pady=8
)

make_button(
    content,
    "Cancel Selected Appointment",
    cancel_appointment,
    color="#b43c46"
).pack(pady=8)


# ---------- CLOSE APPLICATION ----------
def close_application():
    conn.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_application)

# Load saved records when the application starts
view_patients()
view_appointments()

root.mainloop()
