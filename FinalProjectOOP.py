import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class PatientRecord:
    def __init__(self, name, appointment_date, age, condition, gender, dob):
        self.name = name
        self.appointment_date = appointment_date
        self.age = age
        self.condition = condition
        self.gender = gender
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, Appointment Date: {self.appointment_date}, Age: {self.age}, " \
               f"Condition: {self.condition}, Gender: {self.gender}, Date of Birth: {self.dob}"


# Sorting functions
def bubble_sort_by_name(records):
    n = len(records)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if records[j].name > records[j + 1].name:
                records[j], records[j + 1] = records[j + 1], records[j]


def selection_sort_by_dob(records):
    n = len(records)
    for i in range(n):
        max_index = i  # Change from min_index to max_index
        for j in range(i + 1, n):
            if records[j].dob > records[max_index].dob:  # Sort in descending order (most recent first)
                max_index = j
        records[i], records[max_index] = records[max_index], records[i]


def insertion_sort_by_appointment_date(records):
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        # Compare and place the key record in descending order of appointment date
        while j >= 0 and records[j].appointment_date < key.appointment_date:  # Changed the '<' to '>'
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key


# Main Application
class PatientRecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Records Management System")

        self.root.geometry("610x600")
        self.root.config(bg="#F4F6F7")

        # List to hold patient records
        self.records = []

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title label with a color
        self.title_label = tk.Label(self.root, text="Patient Records Management", font=("Arial", 20, "bold"),
                                    fg="#333333", bg="#F4F6F7")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20, padx=10)

        # Buttons
        self.create_button("Add Patient Record", self.add_patient_record, 1, 0, bg="#4CAF50")
        self.create_button("View Records", self.view_records, 1, 1, bg="#2196F3")
        self.create_button("Update Patient Record", self.update_patient_record, 2, 0, bg="#FF5722")
        self.create_button("Search by Name", self.search_by_name, 2, 1, bg="#FF9800")
        self.create_button("Search by Appointment Date", self.search_by_appointment_date, 3, 0, bg="#8BC34A")
        self.create_button("Exit", self.exit_program, 3, 1, bg="#F44336")

    def create_button(self, text, command, row, col, bg):
        btn = tk.Button(self.root, text=text, width=25, height=3, font=("Arial", 14),
                        command=command, bg=bg, fg="white", activebackground="#388E3C", relief="solid", bd=2)
        btn.grid(row=row, column=col, pady=10, padx=10, sticky="ew")

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        position_top = (screen_height // 2) - (height // 2)
        position_right = (screen_width // 2) - (width // 2)
        window.geometry(f'{width}x{height}+{position_right}+{position_top}')

    def add_patient_record(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Patient Record")
        add_window.geometry("300x500")

        self.center_window(add_window, 300, 500)

        # Labels and entry fields
        tk.Label(add_window, text="Enter Name (Surname, Firstname MI):").pack(pady=5)
        name_entry = tk.Entry(add_window, width=30)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Appointment Date (MM-DD-YYYY):").pack(pady=5)
        appointment_entry = tk.Entry(add_window, width=30)
        appointment_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Age:").pack(pady=5)
        age_entry = tk.Entry(add_window, width=30)
        age_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Condition/Diagnosis:").pack(pady=5)
        condition_entry = tk.Entry(add_window, width=30)
        condition_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Gender (F/M):").pack(pady=5)
        gender_entry = tk.Entry(add_window, width=30)
        gender_entry.pack(pady=5)

        tk.Label(add_window, text="Enter Date of Birth (MM-DD-YYYY):").pack(pady=5)
        dob_entry = tk.Entry(add_window, width=30)
        dob_entry.pack(pady=5)

        def submit():
            name = name_entry.get()
            appointment_date = appointment_entry.get()
            age = age_entry.get()
            condition = condition_entry.get()
            gender = gender_entry.get()
            dob = dob_entry.get()

            if not all([name, appointment_date, age, condition, gender, dob]):
                messagebox.showwarning("Input Error", "Please fill all fields.", parent=add_window)
                return

            # Add the record to the list
            self.records.append(PatientRecord(name, appointment_date, int(age), condition, gender, dob))
            messagebox.showinfo("Success", "Patient record added.", parent=add_window)
            add_window.destroy()

        submit_btn = tk.Button(add_window, text="Submit", command=submit)
        submit_btn.pack(pady=20)

    def view_records(self):
        if not self.records:
            messagebox.showinfo("No Records", "No records available.", parent=self.root)
            return

        # Ask user for sorting option
        sort_choice = simpledialog.askinteger("Sort Options",
                                              "Choose sorting option:\n1. Sort by Name (A-Z)\n2. Sort by Date of Birth\n3. Sort by Appointment Date\nEnter 1, 2, or 3:",
                                              parent=self.root)

        if sort_choice == 1:
            bubble_sort_by_name(self.records)
            messagebox.showinfo("Sorted", "Sorted by Name (A-Z).", parent=self.root)
        elif sort_choice == 2:
            selection_sort_by_dob(self.records)
            messagebox.showinfo("Sorted", "Sorted by Date of Birth (Most Recent First).", parent=self.root)
        elif sort_choice == 3:
            insertion_sort_by_appointment_date(self.records)
            messagebox.showinfo("Sorted", "Sorted by Appointment Date (Most Recent First).", parent=self.root)
        else:
            messagebox.showwarning("Invalid Choice", "Invalid choice. Returning to main menu.", parent=self.root)
            return

        # Display sorted records in a message box
        records_str = "\n\n".join(str(record) for record in self.records)
        messagebox.showinfo("Patient Records", records_str, parent=self.root)

    def update_patient_record(self):
        if not self.records:
            messagebox.showinfo("No Records", "No records available to update.", parent=self.root)
            return

        # Ask the user to select a record to update
        record_choices = [record.name for record in self.records]
        selected_name = simpledialog.askstring("Select Patient",
                                               "Choose a patient by name to update:\n" + "\n".join(record_choices),
                                               parent=self.root)

        # Find the selected record
        selected_record = None
        for record in self.records:
            if selected_name.lower() in record.name.lower():
                selected_record = record
                break

        if not selected_record:
            messagebox.showinfo("Not Found", "No record found for the name.", parent=self.root)
            return

        # Create a new top-level window to modify the record
        update_window = tk.Toplevel(self.root)
        update_window.title(f"Update {selected_record.name}")
        update_window.geometry("400x500")

        self.center_window(update_window, 400, 500)

        # Labels and entry fields to edit the selected record
        tk.Label(update_window, text="Enter Name (Surname, Firstname MI):").pack(pady=5)
        name_entry = tk.Entry(update_window, width=30)
        name_entry.insert(0, selected_record.name)
        name_entry.pack(pady=5)

        tk.Label(update_window, text="Enter Appointment Date (MM-DD-YYYY):").pack(pady=5)
        appointment_entry = tk.Entry(update_window, width=30)
        appointment_entry.insert(0, selected_record.appointment_date)
        appointment_entry.pack(pady=5)

        tk.Label(update_window, text="Enter Age:").pack(pady=5)
        age_entry = tk.Entry(update_window, width=30)
        age_entry.insert(0, selected_record.age)
        age_entry.pack(pady=5)

        tk.Label(update_window, text="Enter Condition/Diagnosis:").pack(pady=5)
        condition_entry = tk.Entry(update_window, width=30)
        condition_entry.insert(0, selected_record.condition)
        condition_entry.pack(pady=5)

        tk.Label(update_window, text="Enter Gender (F/M):").pack(pady=5)
        gender_entry = tk.Entry(update_window, width=30)
        gender_entry.insert(0, selected_record.gender)
        gender_entry.pack(pady=5)

        tk.Label(update_window, text="Enter Date of Birth (MM-DD-YYYY):").pack(pady=5)
        dob_entry = tk.Entry(update_window, width=30)
        dob_entry.insert(0, selected_record.dob)
        dob_entry.pack(pady=5)

        # Submit button to save changes
        def submit():
            selected_record.name = name_entry.get()
            selected_record.appointment_date = appointment_entry.get()
            selected_record.age = age_entry.get()
            selected_record.condition = condition_entry.get()
            selected_record.gender = gender_entry.get()
            selected_record.dob = dob_entry.get()

            messagebox.showinfo("Success", "Patient record updated.", parent=update_window)
            update_window.destroy()

        submit_btn = tk.Button(update_window, text="Update", command=submit)
        submit_btn.pack(pady=20)

    def search_by_name(self):
        name = simpledialog.askstring("Search by Name", "Enter the patient's name to search:", parent=self.root)
        if not name:
            return

        found_records = [record for record in self.records if name.lower() in record.name.lower()]
        if found_records:
            records_str = "\n\n".join(str(record) for record in found_records)
            messagebox.showinfo("Search Results", records_str, parent=self.root)
        else:
            messagebox.showinfo("No Results", "No records found for the given name.", parent=self.root)

    def search_by_appointment_date(self):
        appointment_date = simpledialog.askstring("Search by Appointment Date",
                                                  "Enter the appointment date (MM-DD-YYYY):", parent=self.root)
        if not appointment_date:
            return

        found_records = [record for record in self.records if appointment_date in record.appointment_date]
        if found_records:
            records_str = "\n\n".join(str(record) for record in found_records)
            messagebox.showinfo("Search Results", records_str, parent=self.root)
        else:
            messagebox.showinfo("No Results", "No records found for the given appointment date.", parent=self.root)

    def exit_program(self):
        self.root.quit()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PatientRecordsApp(root)
    root.mainloop()

