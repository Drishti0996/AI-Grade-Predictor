import tkinter as tk
from tkinter import messagebox
import joblib

class VITSmarterAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Academic Insight Pro")
        self.root.geometry("520x750")
        self.root.configure(bg="#1C2128")

        try:
            self.model = joblib.load('grade_model.pkl')
        except:
            messagebox.showerror("Error", "Run model.py first!")
            root.destroy()

        # Header
        self.header = tk.Frame(root, bg="#22272E", pady=30)
        self.header.pack(fill="x")
        tk.Label(self.header, text="GPA ANALYTICS ENGINE", font=("Segoe UI", 16, "bold"), 
                 bg="#22272E", fg="#F0F6FC").pack()

        # Input Area
        self.container = tk.Frame(root, bg="#1C2128", padx=60)
        self.container.pack(fill="both", expand=True)

        self.inputs = {}
        fields = [("Attendance (75-100%)", "att"), ("Study Hours (Daily)", "study"),
                  ("Previous CGPA", "prev"), ("Internals (0-50)", "int"), ("GPA Goal", "goal")]

        for label_text, key in fields:
            tk.Label(self.container, text=label_text, font=("Segoe UI", 10, "bold"), 
                     bg="#1C2128", fg="#768390").pack(anchor="w", pady=(15, 2))
            ent = tk.Entry(self.container, font=("Segoe UI", 12), bg="#22272E", fg="#F0F6FC", 
                           insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#444C56")
            ent.pack(fill="x", ipady=8)
            self.inputs[key] = ent

        # Button: BLACK TEXT ON GREEN
        self.btn = tk.Button(root, text="GENERATE PREDICTION", command=self.calculate,
                             bg="#238636", fg="black", font=("Segoe UI", 11, "bold"), 
                             activebackground="#2EA44F", cursor="hand2", bd=0, pady=12)
        self.btn.pack(pady=40, padx=60, fill="x")

        self.res_label = tk.Label(root, text="PREDICTED GPA: --", font=("Segoe UI", 18, "bold"), bg="#1C2128", fg="#F0F6FC")
        self.res_label.pack()

        self.advice = tk.Label(root, text="Enter details for AI feedback.", font=("Segoe UI", 9, "italic"), 
                               bg="#1C2128", fg="#768390", wraplength=400)
        self.advice.pack(pady=20)

    def calculate(self):
        try:
            att, study, prev, internals = float(self.inputs['att'].get()), float(self.inputs['study'].get()), float(self.inputs['prev'].get()), float(self.inputs['int'].get())
            pred = max(0, min(10, self.model.predict([[att, study, prev, internals]])[0]))
            self.res_label.config(text=f"PREDICTED GPA: {pred:.2f} / 10")
            
            if internals >= 45:
                msg = "✨ Internals are perfect. Maintain study hours for 9+ GPA."
            elif study >= 4.5:
                msg = "🌟 High Efficiency: You've reached the study sweet spot!"
            else:
                msg = "💡 Advice: Increase study to 5 hours for maximum GPA growth."
            self.advice.config(text=msg)
        except:
            messagebox.showwarning("Error", "Fill all boxes with numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VITSmarterAI(root)
    root.mainloop()