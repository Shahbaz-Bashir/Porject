 **Student Performance Tracker** ka code Object-Oriented Programming (OOP) ka use karke likha gaya hai. Iss mein different classes aur methods ka use kiya gaya hai jo system ko organize aur functionality ko modular banata hai. Ab main aapko step-by-step samjhaunga kay yeh project kaise bana aur code kya kaam karta hai:

---

### 1. **Project Ka Objective**
Is project ka maqsad:
- Students ki performance ko track karna.
- Unka average score nikalna.
- Yeh check karna ke student pass hai ya fail.
- Class ka overall average score nikalna.

Yeh sab cheezain OOP concepts jaise **classes**, **methods**, **loops**, aur **data structures** (jaise dictionaries aur lists) ka use karke achieve ki gayi hain.

---

### 2. **Classes Ka Role**

**a) `Student` Class:**
- **Purpose:** Har student ka data (naam aur scores) store karna aur uski performance calculate karna.
- **Attributes:**
  - `name`: Student ka naam store karta hai.
  - `scores`: Ek dictionary hai jo subjects aur unke scores store karta hai. Example: `{ "Math": 90, "Science": 80 }`
- **Methods:**
  1. `add_score(subject, score)`:
      - Is method ka kaam ek subject aur uska score add karna hai.
      - **Example:**
        ```python
        student.add_score("Math", 90)
        ```
  2. `calculate_average()`:
      - Total scores ka average calculate karta hai.
      - Agar scores empty hain to average `0` return karega.
      - **Example Output:** `85.0` (agar scores hain: `80, 90`)
  3. `get_status(passing_score=50)`:
      - Yeh check karta hai kay student ne saare subjects mein passing marks liye hain ya nahi.
      - **Example Output:** `True` (agar har score >= 50 hai).

---

**b) `PerformanceTracker` Class:**
- **Purpose:** Multiple students ka data manage karna aur class ka summary calculate karna.
- **Attributes:**
  - `students`: Ek list jo saare `Student` objects store karti hai.
- **Methods:**
  1. `add_student(student)`:
      - Ek student object tracker mein add karta hai.
      - **Example:**
        ```python
        tracker.add_student(student)
        ```
  2. `get_class_average()`:
      - Saare students ka average score calculate karta hai.
      - **Example Output:** `78.5`
  3. `display_summary()`:
      - Saare students ka summary display karta hai:
        - Student ka naam
        - Average score
        - Status (Passing ya Failing)
      - **Example Output:**
        ```
        Student: Ali, Average Score: 85.00, Status: Passing
        ```

---

### 3. **Code Ka Flow**

**Step 1: Data Input**
- Function `input_student_data(tracker)` teacher se student ka naam aur subjects ke scores input karta hai.
- Jab teacher 'done' likhta hai, tab student ka data tracker mein add hota hai.
- Yeh loop tab tak chalta hai jab tak teacher 'exit' nahi likhta.

**Step 2: Data Processing**
- Har student ka average aur status calculate hota hai using `calculate_average()` aur `get_status()` methods.
- Class ka overall average nikalta hai using `get_class_average()`.

**Step 3: Display Results**
- Function `display_tracker_summary(tracker)` summary ko print karta hai:
  - Har student ka naam, average, aur status.
  - Puri class ka average score.

---

### 4. **Code Explanation**
Yeh code kaise kaam karta hai, samjhte hain:

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}  # Har student ke subjects aur unke scores ko store karta hai.
```
- Jab new student object banate hain, uska naam aur scores ka empty dictionary initialize hota hai.

```python
    def add_score(self, subject, score):
        self.scores[subject] = score
```
- Yeh method ek subject ka naam aur uska score `scores` dictionary mein add karta hai.

```python
    def calculate_average(self):
        total_score = sum(self.scores.values())
        num_subjects = len(self.scores)
        return total_score / num_subjects if num_subjects > 0 else 0
```
- Yeh function:
  1. Saare scores ko sum karta hai.
  2. Subjects ka count leta hai.
  3. Average return karta hai.

```python
    def get_status(self, passing_score=50):
        return all(score >= passing_score for score in self.scores.values())
```
- Yeh function:
  - Har subject ka score check karta hai.
  - Agar saare scores passing hain to `True` return karta hai, warna `False`.

---

```python
class PerformanceTracker:
    def __init__(self):
        self.students = []
```
- Tracker ka kaam multiple students ka data manage karna hai.

```python
    def add_student(self, student):
        self.students.append(student)
```
- Yeh method tracker mein ek new student add karta hai.

```python
    def get_class_average(self):
        total_scores = [student.calculate_average() for student in self.students]
        return sum(total_scores) / len(total_scores) if total_scores else 0
```
- Class ka average calculate karta hai:
  1. Har student ka average calculate karta hai.
  2. Uska total le kar divide karta hai.

```python
    def display_summary(self):
        for student in self.students:
            avg_score = student.calculate_average()
            status = "Passing" if student.get_status() else "Failing"
            print(f"Student: {student.name}, Average Score: {avg_score:.2f}, Status: {status}")
```
- Yeh method har student ka naam, average, aur status print karta hai.

---

### 5. **Code Run Karne Ka Tarika**
- `main()` function run karein:
  1. Student data input karein.
  2. Class ka summary dekhein.

---

### 6. **Error Handling**
- Agar user invalid input deta hai (e.g., non-numeric scores), code crash hone ke bajaye input wapas maangta hai.

---

Aapka code kaafi organized aur robust hai. Ismein saare OOP concepts (classes, attributes, methods) ka sahi use kiya gaya hai. Agar aapko aur clarification chahiye ho to zarur puchhein!