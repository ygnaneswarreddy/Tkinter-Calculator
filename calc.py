import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        # Fixed geometry setting and restricted resizing for a clean look
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        
        # Colors for a modern "Dark Mode" look
        self.colors = {
            "bg": "#202020",
            "display_bg": "#323232",
            "btn_num": "#3B3B3B",
            "btn_op": "#323232",
            "btn_eq": "#4CC2FF",
            "text": "#FFFFFF"
        }
        
        self.root.configure(bg=self.colors["bg"])
        self.expression = ""
        self.input_text = tk.StringVar()
        
        self.create_display()
        self.create_buttons()

    def create_display(self):
        # Increased padding and better font for the display
        display_frame = tk.Frame(self.root, bg=self.colors["bg"], pady=20)
        display_frame.pack(expand=True, fill="both")

        entry = tk.Entry(
            display_frame, 
            textvariable=self.input_text, 
            font=("Segoe UI", 32, "bold"), 
            justify="right", 
            bd=0, 
            bg=self.colors["bg"], 
            fg=self.colors["text"],
            insertbackground="white" # cursor color
        )
        entry.pack(expand=True, fill="both", padx=20)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.colors["bg"])
        button_frame.pack(expand=True, fill="both")

        # Configured grid weights so buttons expand evenly
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)

        # Realistic layout including 'C' for clear
        buttons = [
            ('C', 0, 0), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0, 2), ('.', 4, 2), ('=', 4, 3) # '0' spans 2 columns
        ]

        for btn_data in buttons:
            # Handle the optional columnspan for the '0' button
            text, row, col = btn_data[0], btn_data[1], btn_data[2]
            c_span = btn_data[3] if len(btn_data) > 3 else 1
            
            # Choose color based on type of button
            bg_color = self.colors["btn_num"]
            if text in ['/', '*', '-', '+']: bg_color = self.colors["btn_op"]
            if text == '=': bg_color = self.colors["btn_eq"]
            if text == 'C': bg_color = "#9e2a2b"

            btn = tk.Button(
                button_frame, text=text, font=("Segoe UI", 14),
                bg=bg_color, fg=self.colors["text"], bd=0,
                activebackground="#505050", activeforeground="white",
                command=lambda t=text: self.on_click(t)
            )
            btn.grid(row=row, column=col, columnspan=c_span, sticky="nsew", padx=1, pady=1)

    def on_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        else:
            self.press(char)

    def press(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            # Use format to avoid long trailing decimals (floating point math)
            result = eval(self.expression)
            if isinstance(result, float):
                result = round(result, 8)
            
            self.expression = str(result)
            self.input_text.set(self.expression)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()