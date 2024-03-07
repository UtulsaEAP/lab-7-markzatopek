def get_letter_grade(grade:float):
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    return "F"


def courseGrade():
    file = input()
    loaded_file = open(file, "r")
    lines = loaded_file.readlines()
    loaded_file.close()
    
    grade_info = []
    for line in lines:
        grade_info.append(line.split("\t"))
    
    midterm1_avg = 0
    midterm2_avg = 0
    final_avg = 0
    
    for student in grade_info:
        student.append(get_letter_grade((student[2]+student[3]+student[4])/3))
        midterm1_avg += student[2]
        midterm2_avg += student[3]
        final_avg += student[4]
    
    midterm1_avg = round(midterm1_avg / len(grade_info), 2)
    midterm2_avg = round(midterm2_avg / len(grade_info), 2)
    final_avg = round(final_avg / len(grade_info), 2)
    
    report = open("report.txt", "w")
    for student in grade_info:
        report.write("\t".join(student))
    report.write(f"Averages: midterm1 {midterm1_avg}, midterm2 {midterm2_avg}, final {final_avg}")
    report.close()
    
    return

if __name__ == "__main__":
    courseGrade()
    
    