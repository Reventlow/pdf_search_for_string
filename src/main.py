# import packages
from decouple import config
import os
import PyPDF2
import re


folder_path = "pdf_folder" #config("FILE_PATH") # replace with the path to your folder

def find_pdf_files_in_folder(pdf_folder_path: str) -> list:
    print(folder_path)
    pdf_files = [f for f in os.listdir(pdf_folder_path) if os.path.isfile(os.path.join(pdf_folder_path, f)) and f.endswith(".pdf")]
    return pdf_files

def search_for_string_in_pdf(file_name: str, search_for_string: str) -> bool:
    # open the pdf file
    reader = PyPDF2.PdfReader(folder_path + "/" + file_name)

    # get number of pages
    num_pages = len(reader.pages)

    # extract text and do the search
    for page in reader.pages:
        text = page.extract_text()
        res_search = re.search(search_for_string, text)
        if not res_search:
            return False
        return True
def main():
    pdf_files = find_pdf_files_in_folder(folder_path)
    for file_name in pdf_files:
        parts = file_name.split("_")
        try:
            result = parts[1]
            is_file_correct = search_for_string_in_pdf(file_name, result)
            if not is_file_correct:
                print(f"File {file_name} is not correct")

        except IndexError:
            pass


if __name__ == '__main__':
    main()