# AI-Grade-Predictor
# 🎓 Student Success AI: More than just a Grade Predictor!

##  why i made this project
Being a student at **VIT Bhopal**, I always wonder—if i study one extra hour today, will it actually help my CGPA?? We all have these doubts. Most online calculators are just simple math, but i wanted to build something smarter. This project uses a **Random Forest ML model** to answer that. Its basically a "Smart Academic Counselor" that helps find your perfect balance—showing that good quality study is way better than just sitting with books for 10 hours and getting tired.



---

## features
* **Smart-Study Logic:** Unlike basic code, this AI knows that **4 to 5 hours** of daily study is the "Sweet Spot" for getting 9+ GPA. 
* **Advice that actually makes sense:** If your Internals are already full (45+/50), the AI wont nag you to "get more marks." Instead, it tells you to keep your consistency or focus on final exams.
* **Pro UI:** A clean, "Midnight Slate" dark theme built with **Tkinter**. I used high-contrast buttons so its easy to see where to click.
* **Predictive Analytics:** Uses **Random Forest Regression** to understand how attendance and habits actually affect grades in real life.





##  whats inside the folder?
* `app_tk.py`: The main app you run to see the GUI.
* `model.py`: The script that trains the AI brain.
* `grade_model.pkl`: The saved model (dont delete this or app wont work!).
* `student_data.csv`: Sample of the 1500 records used to train the AI.
* `requirements.txt`: List of libraries you need to install.

---

##  how to run it

### 1. Install stuff
First, make sure you have python, then install these:
pip install -r requirements.txt

### 2. Train the Brain

Run the trainer to sync the "Smart-Study" logic:
python3 model.py

### 3. Open the App
Launch the dashboard:
python3 app_tk.py

### Tech Stuff
Most predictors use Linear Regression, but that’s too simple for real life. Academic success isn’t a straight line. By using Random Forest, this project "remembers" rules like—how 75% attendance is different from 90%. It makes the prediction feel much more real .

## ⚡ Tips for Best Use
* **Don’t blindly follow the AI** – use it as a guide.  
* **Keep your input realistic** – if you say you study 12 hours a day but actually sleep through half of it, the prediction won’t match reality 
* **Use the “Sweet Spot” study hours** (4–5 hours) consistently to see best results.  
* **Track your progress** – save your results in a notebook to see improvements over time.

---

## Note
This project is **not 100% accurate** – grades depend on many things, including your own effort, focus, and exam strategy. Think of it as a smart friend giving advice, not a magic calculator.

---

##  Created By
**Name:** Drishti Singh  
**Registration No.:** 25BCE11005  
**College:** VIT Bhopal University
