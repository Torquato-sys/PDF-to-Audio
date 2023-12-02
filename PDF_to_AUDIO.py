import PyPDF2, pyttsx3

# Abre o ebook .pdf
path =open('Aula01-OqueEstatsticaeparaqueserve.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

# Percorre as páginas do ebook, extrai o texto e faz a leitura

for pages in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()