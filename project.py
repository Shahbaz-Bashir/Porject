class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}  # Dictionary to store subject: score pairs

    def add_score(self, subject, score):
        """Adds a score for a specific subject."""
        self.scores[subject] = score

    def calculate_average(self):
        """Calculates and returns the average score across all subjects."""
        total_score = sum(self.scores.values())
        num_subjects = len(self.scores)
        return total_score / num_subjects if num_subjects > 0 else 0

    def get_status(self, passing_score=50):
        """Determines if the student is passing all subjects."""
        return all(score >= passing_score for score in self.scores.values())

class PerformanceTracker:
    def __init__(self):
        self.students = []  # List to store all Student objects

    def add_student(self, student):
        """Adds a Student object to the tracker."""
        self.students.append(student)

    def get_class_average(self):
        """Calculates and returns the class average score across all students."""
        total_scores = [student.calculate_average() for student in self.students]
        return sum(total_scores) / len(total_scores) if total_scores else 0

    def display_summary(self):
        """Displays a summary of each student's performance."""
        for student in self.students:
            avg_score = student.calculate_average()
            status = "Passing" if student.get_status() else "Failing"
            print(f"Student: {student.name}, Average Score: {avg_score:.2f}, Status: {status}")
def input_student_data(tracker):
    """Takes input from the teacher to add student data to the tracker."""
    while True:
        name = input("Enter student name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        student = Student(name)
        while True:
            subject = input(f"Enter subject for {name} (or type 'done' to finish subjects): ")
            if subject.lower() == 'done':
                break
            score = float(input(f"Enter score for {subject}: "))
            student.add_score(subject, score)
        tracker.add_student(student)
    print("Data entry complete.\n")

def display_tracker_summary(tracker):
    """Displays a summary of all student performance."""
    print("\nClass Summary:")
    tracker.display_summary()
    print(f"\nClass Average Score: {tracker.get_class_average():.2f}")

def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker\n")
    input_student_data(tracker)
    display_tracker_summary(tracker)

