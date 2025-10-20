# 01_NguyenThiPhuongThao.py

student_list = []

def add_student(name, year_of_birth, address):
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for student in student_list:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")

def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    found_students = [s for s in student_list if search_name.lower() in s['name'].lower()]
    if not found_students:
        print("Khong tim thay sinh vien nao.")
    else:
        for student in found_students:
            print(f" - Ten: {student['name']}, Nam sinh: {student['year_of_birth']}, Dia chi: {student['address']}")

if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")

    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    print("\n2. In danh sach sinh vien:")
    print_student_list()

    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")

    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")
if __name__ == "__main__":
    print("Chương trình quản lý sinh viên đang chạy...")
