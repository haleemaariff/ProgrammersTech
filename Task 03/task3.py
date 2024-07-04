import tkinter as tk
from tkinter import messagebox

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Initialize variables
        self.student_list = []

        # Create UI elements
        self.label_title = tk.Label(root, text="Student Management System", font=("Arial", 18))
        self.label_title.grid(row=0, column=0, columnspan=4, pady=10)

        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.grid(row=1, column=1, columnspan=3, pady=5)

        self.label_age = tk.Label(root, text="Age:")
        self.label_age.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_age = tk.Entry(root, width=10)
        self.entry_age.grid(row=2, column=1, pady=5)

        self.label_course = tk.Label(root, text="Course:")
        self.label_course.grid(row=2, column=2, pady=5, sticky=tk.E)
        self.entry_course = tk.Entry(root, width=20)
        self.entry_course.grid(row=2, column=3, pady=5)

        self.button_add = tk.Button(root, text="Add Student", command=self.add_student)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_update = tk.Button(root, text="Update Student", command=self.update_student)
        self.button_update.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        self.button_delete = tk.Button(root, text="Delete Student", command=self.delete_student)
        self.button_delete.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.button_view = tk.Button(root, text="View Students", command=self.view_students)
        self.button_view.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

        self.listbox_students = tk.Listbox(root, height=10, width=60)
        self.listbox_students.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        self.refresh_listbox()

    def add_student(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        course = self.entry_course.get()

        if name and age and course:
            self.student_list.append({"Name": name, "Age": age, "Course": course})
            self.refresh_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Student added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def update_student(self):
        selected_index = self.listbox_students.curselection()
        if selected_index:
            index = selected_index[0]
            updated_name = self.entry_name.get()
            updated_age = self.entry_age.get()
            updated_course = self.entry_course.get()

            if updated_name and updated_age and updated_course:
                self.student_list[index] = {"Name": updated_name, "Age": updated_age, "Course": updated_course}
                self.refresh_listbox()
                self.clear_entries()
                messagebox.showinfo("Success", "Student updated successfully.")
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Please select a student to update.")

    def delete_student(self):
        selected_index = self.listbox_students.curselection()
        if selected_index:
            index = selected_index[0]
            del self.student_list[index]
            self.refresh_listbox()
            self.clear_entries()
            messagebox.showinfo("Success", "Student deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a student to delete.")

    def view_students(self):
        self.listbox_students.delete(0, tk.END)
        for student in self.student_list:
            self.listbox_students.insert(tk.END, f"Name: {student['Name']}, Age: {student['Age']}, Course: {student['Course']}")

    def refresh_listbox(self):
        self.view_students()

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_course.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
