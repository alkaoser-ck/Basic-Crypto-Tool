import customtkinter as ctk


class InputDialog:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Your Plain Text")
        self.root.geometry("400x350")

        self.result = None
        self.select = None
        self.key_value = None

        # error label (hidden initially)
        self.error_label = ctk.CTkLabel(self.root, text="", text_color="red")

        # key input (hidden initially)
        self.key_label = ctk.CTkLabel(self.root, text="Key:")

        self.key_entry = ctk.CTkEntry(
            self.root,
            width=200,
            placeholder_text="Integer Only",
            fg_color="white",
            text_color="#000000",
            placeholder_text_color="#000000",
        )
        self.key_entry.bind(
            "<Return>", lambda event: self.after_key()
        )  # Pressing Enter in key_entry moves focus to textbox

        # textbox
        self.textbox = ctk.CTkTextbox(self.root, width=380, height=150)
        self.textbox.bind("<Return>", self.on_enter)
        self.textbox.bind("<Shift-Return>", self.newline)

        # dropdown menu
        self.options = [
            "Caesar Cipher",
            "Base64",
            "Vigenere Cipher(dCode)",
            "Morse Code",
            "Reverse",
            "ROT",
            "Bifid",
        ]
        self.options_var = ctk.StringVar(value=self.options[3])
        self.dropdown = ctk.CTkOptionMenu(
            self.root,
            values=self.options,
            variable=self.options_var,
            command=self.on_option_change,
        )
        self.dropdown.pack(pady=10)

        self.textbox.pack(padx=10, pady=(10, 10))
        self.textbox.focus()  # Set initial focus to the textbox

        self.root.mainloop()

    # show/hide key input
    def on_option_change(self, value):
        # hide error message
        self.error_label.pack_forget()

        if value in ["Caesar Cipher", "ROT"]:
            # show key input
            self.key_label.configure(text="Key (Integer Only):")
            self.key_entry.configure(placeholder_text="Integer Only")
            self.set_numeric_validation()
            self.key_label.pack(padx=10, pady=(10, 0), anchor="w")
            self.key_entry.pack(padx=10, pady=(0, 10), anchor="w")
            self.key_entry.focus()  # focus on key entry

        elif value == "Vigenere Cipher(dCode)":
            self.key_label.configure(text="Key (2+ letters):")
            self.key_entry.configure(placeholder_text="Letters Only")
            self.set_alpha_validation()
            self.key_label.pack(padx=10, pady=(10, 0), anchor="w")
            self.key_entry.pack(padx=10, pady=(0, 10), anchor="w")
            self.key_entry.focus()

        elif value == "Bifid":
            self.key_label.configure(text="Key (unique letters):")
            self.key_entry.configure(placeholder_text="Letters Only")
            self.set_alpha_validation()
            self.key_label.pack(padx=10, pady=(10, 0), anchor="w")
            self.key_entry.pack(padx=10, pady=(0, 10), anchor="w")
            self.key_entry.focus()

        else:
            # hide key input
            self.key_label.pack_forget()
            self.key_entry.pack_forget()
            self.error_label.pack_forget()
            # self.textbox.bind("<Return>", self.after_key)
            self.textbox.focus()  # focus main text box

    # numeric key validation
    def set_numeric_validation(self):
        vcmd = (self.root.register(self.validate_numeric), "%P")
        self.key_entry.configure(validate="key", validatecommand=vcmd)

    def validate_numeric(self, val):
        return val.isdigit() or val == ""

    # alpha key validation
    def set_alpha_validation(self):
        vcmd = (self.root.register(self.validate_alpha), "%P")
        self.key_entry.configure(validate="key", validatecommand=vcmd)

    def validate_alpha(self, val):
        return val.isalpha() or val == ""

    # show error in UI
    def show_error(self, msg):
        self.error_label.configure(text=msg)
        self.error_label.pack()

    # after enting the key focus on text area
    def after_key(self):
        self.textbox.focus()

    # enter pressed
    def on_enter(self, event):
        option = self.options_var.get()

        # Bifid key must be unique
        if option == "Bifid":
            key_text = self.key_entry.get()
            if len(key_text) < 1:
                self.show_error("Key cannot be empty")
                return "break"
            if len(key_text) != len(set(key_text)):
                self.show_error("All letters in the key must be unique!")
                return "break"

        # vigenere minimum 2 letters
        if option == "Vigenere Cipher(dCode)":
            key_text = self.key_entry.get()
            if len(key_text) < 2:
                self.show_error("Key must be at least 2 letters!")
                return "break"

        # save result
        self.result = self.textbox.get("0.0", "end").rstrip()
        # is there a key and is the key option empty or not
        if self.key_entry.winfo_ismapped() and self.key_entry.get() != "":
            self.key_value = self.key_entry.get()

        self.select = option
        self.root.destroy()
        return "break"

    def newline(self, event):
        self.textbox.insert("insert", "\n")
        return "break"
