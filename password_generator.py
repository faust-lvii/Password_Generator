import customtkinter as ctk
import string
import random

class PasswordGenerator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Modern Şifre Oluşturucu")
        self.root.geometry("500x650")
        
        # Set the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Şifre Oluşturucu",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)

        # Şifre Uzunluğu
        self.length_frame = ctk.CTkFrame(self.main_frame)
        self.length_frame.pack(fill="x", padx=20, pady=10)
        
        self.length_label = ctk.CTkLabel(
            self.length_frame,
            text="Şifre Uzunluğu:",
            font=ctk.CTkFont(size=14)
        )
        self.length_label.pack(side="left", padx=10)
        
        self.length_var = ctk.StringVar(value="12")
        self.length_entry = ctk.CTkEntry(
            self.length_frame,
            textvariable=self.length_var,
            width=100
        )
        self.length_entry.pack(side="right", padx=10)

        # Özel Karakterler
        self.special_frame = ctk.CTkFrame(self.main_frame)
        self.special_frame.pack(fill="x", padx=20, pady=10)
        
        self.special_label = ctk.CTkLabel(
            self.special_frame,
            text="Özel Karakterler:",
            font=ctk.CTkFont(size=14)
        )
        self.special_label.pack(side="left", padx=10)
        
        self.special_chars_var = ctk.StringVar(value="!@#$%^&*")
        self.special_chars_entry = ctk.CTkEntry(
            self.special_frame,
            textvariable=self.special_chars_var,
            width=200
        )
        self.special_chars_entry.pack(side="right", padx=10)

        # Karmaşıklık Seviyesi
        self.complexity_frame = ctk.CTkFrame(self.main_frame)
        self.complexity_frame.pack(fill="x", padx=20, pady=20)
        
        self.complexity_label = ctk.CTkLabel(
            self.complexity_frame,
            text="Karmaşıklık Seviyesi:",
            font=ctk.CTkFont(size=14)
        )
        self.complexity_label.pack(pady=10)

        self.complexity = ctk.StringVar(value="normal")
        
        # Radio buttons for complexity
        self.radio_frame = ctk.CTkFrame(self.complexity_frame)
        self.radio_frame.pack(pady=10)
        
        self.radio_basic = ctk.CTkRadioButton(
            self.radio_frame,
            text="Basit",
            variable=self.complexity,
            value="basit"
        )
        self.radio_basic.pack(side="left", padx=20)
        
        self.radio_normal = ctk.CTkRadioButton(
            self.radio_frame,
            text="Normal",
            variable=self.complexity,
            value="normal"
        )
        self.radio_normal.pack(side="left", padx=20)
        
        self.radio_high = ctk.CTkRadioButton(
            self.radio_frame,
            text="Yüksek",
            variable=self.complexity,
            value="yuksek"
        )
        self.radio_high.pack(side="left", padx=20)

        # Generate Button
        self.generate_button = ctk.CTkButton(
            self.main_frame,
            text="Şifre Oluştur",
            command=self.generate_password,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.generate_button.pack(pady=30)

        # Password Display Frame
        self.password_display_frame = ctk.CTkFrame(self.main_frame)
        self.password_display_frame.pack(fill="x", padx=20, pady=10)
        
        self.password_label = ctk.CTkLabel(
            self.password_display_frame,
            text="Oluşturulan Şifre:",
            font=ctk.CTkFont(size=14)
        )
        self.password_label.pack(pady=10)
        
        self.password_var = ctk.StringVar()
        self.password_display = ctk.CTkEntry(
            self.password_display_frame,
            textvariable=self.password_var,
            width=300,
            height=40,
            font=ctk.CTkFont(size=16),
            justify="center"
        )
        self.password_display.pack(pady=10)

        # Copy Button
        self.copy_button = ctk.CTkButton(
            self.password_display_frame,
            text="Kopyala",
            command=self.copy_password,
            width=100,
            height=30
        )
        self.copy_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            special_chars = self.special_chars_var.get()
            complexity = self.complexity.get()

            # Base character sets
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits

            if complexity == "basit":
                chars = lowercase + digits
            elif complexity == "normal":
                chars = lowercase + uppercase + digits
            else:  # yuksek
                chars = lowercase + uppercase + digits + special_chars

            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            
            # Ensure at least one character from each required set based on complexity
            if complexity == "normal":
                password = (random.choice(lowercase) + 
                          random.choice(uppercase) + 
                          random.choice(digits) +
                          ''.join(random.choice(chars) for _ in range(length-3)))
            elif complexity == "yuksek":
                password = (random.choice(lowercase) + 
                          random.choice(uppercase) + 
                          random.choice(digits) +
                          random.choice(special_chars) +
                          ''.join(random.choice(chars) for _ in range(length-4)))
            
            # Shuffle the password
            password_list = list(password)
            random.shuffle(password_list)
            password = ''.join(password_list)

            self.password_var.set(password)
        except ValueError:
            self.password_var.set("Geçersiz şifre uzunluğu!")

    def copy_password(self):
        password = self.password_var.get()
        if password and password != "Geçersiz şifre uzunluğu!":
            self.root.clipboard_clear()
            self.root.clipboard_append(password)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()
