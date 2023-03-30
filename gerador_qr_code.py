import tkinter as tk
import qrcode
from PIL import ImageTk

class QRCode:
    def __init__(self, text):
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data(text)
        self.qr.make(fit=True)
    
    def get_qrcode_image(self):
        img = self.qr.make_image(fill_color="black", back_color="white")
        return img
    
    def save_qrcode_image(self, filename):
        img = self.get_qrcode_image()
        img.save(filename)

class QRCodeGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Gerador de QR Code")
        
        self.label = tk.Label(self.window, text="Texto:")
        self.label.grid(row=0, column=0, padx=5, pady=5)
        
        self.text_entry = tk.Entry(self.window, width=40)
        self.text_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.generate_button = tk.Button(self.window, text="Gerar", command=self.generate_qrcode)
        self.generate_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
        
        self.qrcode_label = tk.Label(self.window)
        self.qrcode_label.grid(row=2, column=0, padx=5, pady=5, columnspan=2)
    
    def generate_qrcode(self):
        text = self.text_entry.get()
        qrcode_generator = QRCode(text)
        img = qrcode_generator.get_qrcode_image()
        img = ImageTk.PhotoImage(img)
        self.qrcode_label.config(image=img)
        self.qrcode_label.image = img
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    qrcode_generator = QRCodeGenerator()
    qrcode_generator.run()