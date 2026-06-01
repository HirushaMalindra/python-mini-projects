import fitz
import os

def pdf_to_img(pdf_path, output_folder):
    """Convert each page of the PDF to an image and saves them."""
    os.makedirs(output_folder, exist_ok=True)

    pdf_document = fitz.open(pdf_path)
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        output_path = f"{output_folder}/page_{page_number + 1}.png"
        pix.save(output_path)
        print(f"saved: {output_path}")

    pdf_document.close()

  if __name__ == "__main__":
# you can give any PDF file path and output folder path here
    pdf_path = r"E:\Users\User\Downloads\Example.pdf" # just a example path, change it to your actual PDF file path
    output_folder = r"E:\Users\User\Pictures\output_images" # just a example path, change it to your desired output folder path

    if os.path.exists(pdf_path):
        pdf_to_img(pdf_path, output_folder)  
    else:
        print(f"Error: The file {pdf_path} does not exist. Please check the path and try again.")      
