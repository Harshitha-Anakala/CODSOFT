import tkinter as tk
from tkinter import messagebox
class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)
        self.tasks = []
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)
        self.task_text = tk.Text(self.task_frame, width=50, height=10)
        self.task_text.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_text.config(yscrollcommand=self.scrollbar.set)
        self.task_text.config(state=tk.DISABLED)
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)
        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)
        self.complete_button = tk.Button(self.button_frame, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.get_selected_task_index()
        if selected_task_index is not None:
            del self.tasks[selected_task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def mark_complete(self):
        selected_task_index = self.get_selected_task_index()
        if selected_task_index is not None:
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = f"{task} ✔️"
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")

    def update_task_list(self):
        self.task_text.config(state=tk.NORMAL)
        self.task_text.delete(1.0, tk.END)
        for task in self.tasks:
            self.task_text.insert(tk.END, f"• {task}\n")
        self.task_text.config(state=tk.DISABLED)

    def get_selected_task_index(self):
        try:
            index = int(self.task_text.index(tk.SEL_FIRST).split('.')[0]) - 1
            return index
        except tk.TclError:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()