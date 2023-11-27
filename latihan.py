import tkinter as tk
from tkinter import ttk, messagebox

class CompleteFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Isian Data")
        self.root.geometry("1366x768")
        self.root.configure(bg="#FFC0CB", padx= 500, pady=30)  # Warna pink

        # Mendapatkan lebar dan tinggi layar
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # # Mengatur ukuran jendela dan posisi di tengah layar
        # window_width = 1366
        # window_height = 768
        # x_position = (screen_width - window_width) // 2
        # y_position = (screen_height - window_height) // 2
        # self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Form Isian Data
        self.label_name = tk.Label(root, text="Nama:", bg="#FFC0CB")
        self.entry_name = tk.Entry(root)

        self.label_age = tk.Label(root, text="Usia:", bg="#FFC0CB")
        self.entry_age = tk.Entry(root)

        self.label_gender = tk.Label(root, text="Jenis Kelamin:", bg="#FFC0CB")
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(root, textvariable=self.gender_var, values=["Pria", "Wanita"])

        self.label_education = tk.Label(root, text="Pendidikan:", bg="#FFC0CB")
        self.education_var = tk.StringVar()
        self.education_combobox = ttk.Combobox(root, textvariable=self.education_var, values=["SD", "SMP", "SMA", "S1", "S2", "S3"])

        self.label_status = tk.Label(root, text="Status:", bg="#FFC0CB")
        self.status_var = tk.StringVar()
        self.status_radio1 = tk.Radiobutton(root, text="Belum Menikah", variable=self.status_var, value="Belum Menikah", bg="#FFC0CB")
        self.status_radio2 = tk.Radiobutton(root, text="Menikah", variable=self.status_var, value="Menikah", bg="#FFC0CB")

        self.label_hobbies = tk.Label(root, text="Hobi:", bg="#FFC0CB")
        self.hobby_var1 = tk.BooleanVar()
        self.hobby_checkbox1 = tk.Checkbutton(root, text="Membaca Buku", variable=self.hobby_var1, bg="#FFC0CB")
        self.hobby_var2 = tk.BooleanVar()
        self.hobby_checkbox2 = tk.Checkbutton(root, text="Olahraga", variable=self.hobby_var2, bg="#FFC0CB")

        # Tombol untuk Menampilkan Data
        self.btn_show_data = tk.Button(root, text="Tampilkan Data", command=self.show_data, bg="#FF69B4")  # Warna pink muda

        # Layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_age.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_age.grid(row=1, column=1, padx=10, pady=5)

        self.label_gender.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.gender_combobox.grid(row=2, column=1, padx=10, pady=5)

        self.label_education.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.education_combobox.grid(row=3, column=1, padx=10, pady=5)

        self.label_status.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        self.status_radio1.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        self.status_radio2.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)

        self.label_hobbies.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.hobby_checkbox1.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
        self.hobby_checkbox2.grid(row=5, column=2, padx=10, pady=5, sticky=tk.W)

        self.btn_show_data.grid(row=6, column=1, pady=10)

    def show_data(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        education = self.education_var.get()
        status = self.status_var.get()
        hobbies = []

        if self.hobby_var1.get():
            hobbies.append("Membaca Buku")
        if self.hobby_var2.get():
            hobbies.append("Olahraga")

        # Menampilkan data di jendela pesan
        data_text = f"Nama: {name}\nUsia: {age}\nJenis Kelamin: {gender}\nPendidikan: {education}\nStatus: {status}\nHobi: {', '.join(hobbies)}"
        messagebox.showinfo("Data", data_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CompleteFormApp(root)
    root.mainloop()
