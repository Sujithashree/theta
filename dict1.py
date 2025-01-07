students = {
    1:{"name":"google","age":21},
    2:{"name":"aaa","age":22},
    3:{"name":"bbb","age":23},
    4:{"name":"cat","age":24},
    5:{"name":"dog","age":25},
}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']},Age: {details['age']}")