import fitz

file = fitz.open('dido_ivanchyk.pdf')

for pageNumber, page in enumerate(file.pages(), start=1):
    text = page.getText()

    print(f"Extracting text from page {pageNumber}")
    txt = open(f'report_page_{pageNumber}.txt', 'a')
    txt.writelines(text)
    txt.close


