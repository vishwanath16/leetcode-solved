import sqlite3
from datetime import datetime
import os


def filename():
    problem_name = input("Enter the problem name: ").strip()
    
    folder_prompt = (
        "In which folder you want to save?\n"
        "1.  1-D Dynamic Programming\n"
        "2.  2-D Dynamic Programming\n"
        "3.  Advanced Graphs\n"
        "4.  Arrays & Hashing\n"
        "5.  Backtracking\n"
        "6.  Binary Search\n"
        "7.  Bit Manipulation\n"
        "8.  Graphs\n"
        "9.  Greedy\n"
        "10. Heap | Priority Queue\n"
        "11. Intervals\n"
        "12. Linked List\n"
        "13. Math & Geometry\n"
        "14. Sliding Window\n"
        "15. Stack\n"
        "16. Trees\n"
        "17. Tries\n"
        "18. Two Pointers\n"
        "→ Enter number (1-18): "
    )
    
    folder = input(folder_prompt).strip()
    
    folder_names = {
        "1": "1-D Dynamic Programming",
        "2": "2-D Dynamic Programming",
        "3": "Advanced Graphs",
        "4": "Arrays & Hashing",
        "5": "Backtracking",
        "6": "Binary Search",
        "7": "Bit Manipulation",
        "8": "Graphs",
        "9": "Greedy",
        "10": "Heap | Priority Queue",
        "11": "Intervals",
        "12": "Linked List",
        "13": "Math & Geometry",
        "14": "Sliding Window",
        "15": "Stack",
        "16": "Trees",
        "17": "Tries",
        "18": "Two Pointers"
    }
    
    selected_folder = folder_names.get(folder)
    if selected_folder is None:
        print("Invalid folder selection. Exiting.")
        exit(1)
    
    filename_safe = problem_name.replace(" ", "_") + ".py"
    
    base_dir = "/Volumes/Files/Programs/Python/LeetCode/"
    file_path = os.path.join(base_dir, selected_folder, filename_safe)
    
    return file_path, problem_name


def add_to_database(problem_name, level, category):
    today = datetime.now().strftime("%d-%m-%Y")
    conn = sqlite3.connect('problems.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO problems (problem_name, level, category, date)
        VALUES (?, ?, ?, ?)
    ''', (problem_name, level, category, today))
    
    conn.commit()
    conn.close()
    print(f"→ Added to database: {problem_name} ({level}) - {today}")


def main():
    print("LeetCode file & database helper\n")
    
    file_path, problem_name = filename()
    
    print("\n" + "-"*50)
    print(f"File will be created/updated: {file_path}")
    print(f"Problem name: {problem_name}")
    print("-"*50 + "\n")
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    link = problem_name.lower().replace(" ", "-").replace("'", '')
    
    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) == 0:
            file.write(f"# Link: https://leetcode.com/problems/{link}/\n\n")
    
    level_prompt = (
        "Enter the difficulty level:\n"
        "1. Easy\n"
        "2. Medium\n"
        "3. Hard\n"
        "→ Choose (1-3): "
    )
    level_choice = input(level_prompt).strip()
    
    levels = {"1": "Easy", "2": "Medium", "3": "Hard"}
    selected_level = levels.get(level_choice, "Unknown")
    
    category = os.path.basename(os.path.dirname(file_path))

    add_to_database(problem_name, selected_level, category)
    
    print("\nDone! File ready at:", file_path)


if __name__ == "__main__":
    main()