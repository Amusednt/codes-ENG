import PyPDF2
import os

def extract_pdf_content(pdf_path, output_txt):
    """
    Reads a PDF file and saves its text content into a text file.
    :param pdf_path: Path to the source PDF.
    :param output_txt: Name of the resulting text file.
    """
    if not os.path.exists(pdf_path):
        print("❌ Error: Source file not found.")
        return

    try:
        with open(pdf_path, 'rb') as pdf_file:
            # Initialize the PDF reader object
            reader = PyPDF2.PdfReader(pdf_file)
            full_text = []

            print(f"📄 Processing {len(reader.pages)} pages...")

            # Iterate through all pages and extract text
            for page in reader.pages:
                full_text.append(page.extract_text())

            # Save the combined text to a file
            with open(output_txt, 'w', encoding='utf-8') as f:
                f.write("\n".join(full_text))
            
            print(f"✅ Success! Content saved to {output_txt}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage:
# extract_pdf_content("report.pdf", "report_summary.txt")
