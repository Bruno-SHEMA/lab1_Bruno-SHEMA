import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found. Please first run the bash file to create a grades.csv file. Use command `bash organizer.sh`")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
#        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        assignments = list(reader)

        if reader.fieldnames is None:
            print("grades.csv is empty.")
            print("Please enter assignment data...")

            assignments = []

            while True:
                assignment = input("Assignment name: ")
                group = input("Group (Formative/Summative): ")
                score = float(input("Score: "))
                weight = float(input("Weight: "))

                assignments.append({
                    "assignment": assignment,
                    "group": group,
                    "score": score,
                    "weight": weight
                })

                again = input("Do you want to record another assignment? (y/n): ").lower()

                if again != "y":
                    break
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["assignment", "group", "score", "weight"]
        )

        writer.writeheader()
        writer.writerows(assignments)

    return assignments

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    # Outputing report table
    if len(data) == 0:
        print("Error: CSV file is empty.")
        return
    print(
        f"{'Assignment':35}"
        f"{'Category':15}"
        f"{'Grade':10}"
        f"{'Weight':10}"
        f"{'Final Weight':10}"
        )
    for item in data:
        item['final_weight'] = (
        item['score'] * item['weight']
    ) / 100
    for item in data:
        print(
            f"{item['assignment']:35}  "
            f"{item['group']:10}"
            f"{item['score']:10}"
            f"{item['weight']:10}"
            f"{item['final_weight']:10}"
            )

    # TODO: a) Check if all scores are percentage based (0-100)
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(
                f"Invalid score found in {item['assignment']}: {item['score']}"
            )
        # else: 
            return
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = sum(item['weight'] for item in data)
    
    formative_weight = sum(
        item['weight']
        for item in data
        if item['group'].lower() == "formative"
                           )
    summative_weight = sum(
        item['weight']
        for item in data if item['group'].lower() == "summative"
    )
    if total_weight != 100:
        print("The total weight must be equal to 100")
        return
    if formative_weight != 60:
        print("Formative weight must be equal to 60, Please review it to proceed!")
        return
    if summative_weight != 40:
        print("Summartive weight must be equal to 40, Please review it to proceed!")
        return
    

    # TODO: c) Calculate the Final Grade and GPA
    formatives = sum(
        ((item['score'] * item['weight'])/100) 
        for item in data
        if item['group'].lower() == 'formative'
    )
    print(f"\n{'formatives(60)' :70} {formatives:.1f}")
    summatives = sum(
        ((item['score'] * item['weight']) /100) 
        for item in data
        if item['group'].lower() == 'summative'
    )
    print(f"{'Summartives(40)':70} {summatives: .1f}")

    total_grade = sum(
        (item['score']* item['weight'] /100)
        for item in data
    )
    gpa = (total_grade/100) *5.0
    # print(f"\n Total Grade: {total_grade}%")
    print(f" {'gpa':70}  {gpa}")
    
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    summative_grade = sum (
        (item['score']*item['weight'])/40 
        for item in data 
        if item['group'].lower()=='summative')
    formative_grade = sum (
        (item['score']*item['weight'])/60
        for item in data
        if item['group'].lower() == 'formative')
    if summative_grade>=50 and formative_grade >=50:
        print(f"\n {'Status':65} Passed")
    else:
        print(f"Status:       Failed")
    # TODO: e) Check for failed formative assignments (< 50%)
    failed_formative = [
        item for item in data
        if item['group'].lower()=='formative' and item['score'] < 50
    ]
    if failed_formative:
        highest_weight = max(item['weight'] for item in failed_formative)
        resubmit = [
            item for item in failed_formative
            if item['weight'] == highest_weight
        ]
    else:
        resubmit = []
    if resubmit:
        resubmit_assignment = []
        for item in resubmit:
            resubmit_assignment.append(item['assignment'])
            print(f"{'Available for resubmision':65} {item['assignment']}")
    else: print("No assignemnt available for resubmission!")
    
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    if summative_grade>=50 and formative_grade >=50:
        decision = 'Passed'
    else:
        decision = 'Failed'
    
    print(f"\n{'Final decision':65} {decision}")
    pass
    print("")
    if resubmit:
        resubmit_option = input("Do you want to resubmit? y/n")
        if resubmit_option == 'y':
            choosen = input(f"which one do you want to resubmit between: {resubmit_assignment}")
            if len(choosen) != 0:
                new_score = input(f"Enter New score for{choosen}")
        else:
            return
if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
