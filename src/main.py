"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã.

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        Danh sách sinh viên khớp với từ khóa
    """
    results = []
    keyword_lower = keyword.lower()

    for student in students:
        if keyword_lower in student.name.lower() or keyword_lower in student.student_id.lower():
            results.append(student)

    if results:
        print(f"🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for student in results:
            print(f"  {student}")
    else:
        print(f"❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")

    return results


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

    # Tìm kiếm sinh viên
    print("\n--- Tìm kiếm ---")
    search_student(students, "Van")


if __name__ == "__main__":
    main()
