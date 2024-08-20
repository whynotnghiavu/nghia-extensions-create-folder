import os


def create_folder(folder_path):
    for i in range(START,END):
        print(i)
        # Tạo folder con f"KhoaHoc{i}"


folder_path = r"input-nghia-extensions-create-folder"

START = 1
END = 10 









if not os.path.exists(folder_path):
    print(f"Không có thư mục {folder_path}")
    # os.mkdir(folder_path)


create_folder(folder_path)
