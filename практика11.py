import tkinter as tk
from tkinter import ttk, messagebox, filedialog


root = tk.Tk()
root.title("Касимов Глеб Евгеньевич")   
root.geometry("500x350")

#создание вкладки
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')


#вкладка1(калькулятор)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

#поля для чисел
num1_entry = ttk.Entry(tab1)
num2_entry = ttk.Entry(tab1)

num1_entry.pack(pady=10)
num2_entry.pack(pady=10)

#операции
operation = ttk.Combobox(tab1, values=["+", "-", "*", "/"], state="readonly")
operation.current(0)
operation.pack(pady=10)

#вычисления
def calculate():
    try:
        a = float(num1_entry.get())
        b = float(num2_entry.get())
        op = operation.get()

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("Ошибка", "Деление на ноль!")
                return
            result = a / b

        messagebox.showinfo("Результат", f"Ответ: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

#кнопка "Вычислить"
btn_calc = ttk.Button(tab1, text="Вычислить", command=calculate)
btn_calc.pack(pady=10)



#вкладка2(чекбоксы)
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Выбор")

chk1_var = tk.BooleanVar()
chk2_var = tk.BooleanVar()
chk3_var = tk.BooleanVar()

chk1 = ttk.Checkbutton(tab2, text="Первый", variable=chk1_var)
chk2 = ttk.Checkbutton(tab2, text="Второй", variable=chk2_var)
chk3 = ttk.Checkbutton(tab2, text="Третий", variable=chk3_var)

chk1.pack(pady=5)
chk2.pack(pady=5)
chk3.pack(pady=5)

def show_choice():
    if chk1_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали первый вариант.")
    elif chk2_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали второй вариант.")
    elif chk3_var.get():
        messagebox.showinfo("Выбор", "Вы выбрали третий вариант.")
    else:
        messagebox.showwarning("Нет выбора", "Ничего не выбрано!")

btn_choice = ttk.Button(tab2, text="Показать выбор", command=show_choice)
btn_choice.pack(pady=10)



#вкладка3(работа с текстом)
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текст")

text_box = tk.Text(tab3, wrap="word")
text_box.pack(expand=True, fill="both", padx=10, pady=10)

#загрузки файла
def load_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, content)


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть текстовый файл", command=load_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

root.mainloop()
