# Lifenest Hospitals 🏥

### Hospital Appointment and Patient Registration System

## 📌 Project Overview

Lifenest Hospitals is a desktop-based hospital management application developed using Python. It provides a simple graphical interface for patient registration, patient record management and appointment booking.

The application uses SQLite to store patient and appointment details.

## 🎯 Objectives

- To simplify patient registration.
- To maintain patient records.
- To make appointment booking easier.
- To allow searching and managing patient information.
- To store information in a database.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Tkinter** – Graphical User Interface
- **SQLite3** – Database management
- **ttk** – Styled GUI components
- **tkcalendar** – Calendar widget for date selection

## 🧩 Components Used

- Label
- Entry
- Button
- Combobox
- LabelFrame
- Treeview
- Scrollbar
- DateEntry
- Messagebox

## ✨ Main Features

1. **Patient Registration** – Register patients with their personal details.
2. **Patient Records** – Display registered patient information.
3. **Patient Search** – Search patients using patient ID or name.
4. **Appointment Booking** – Book appointments by selecting a doctor, department, date and time.
5. **Appointment Management** – View appointment details.
6. **Appointment Cancellation** – Cancel booked appointments.

## 🗄️ Database Design

The project uses SQLite with two tables:

### Patients
- Patient ID
- Name
- Age
- Gender
- Phone Number

### Appointments
- Appointment ID
- Patient ID
- Doctor
- Department
- Date
- Time

## ▶️ How to Run the Project

1. Install Python.
2. Install the required calendar package:

   ```bash
   pip install tkcalendar
   ```

3. Open the project folder in VS Code.
4. Run the Python file:

   ```bash
   python hospital_appointment.py
   ```

## 🔮 Future Enhancements

- Doctor login and authentication.
- Patient medical history.
- Online appointment booking.
- Billing and payment management.

## 👩‍💻 Developed Using

**Python | Tkinter | SQLite**
