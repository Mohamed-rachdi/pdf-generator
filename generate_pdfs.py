from faker import Faker
from fpdf import FPDF
import random
import string

# Initialiser Faker
fake = Faker()

# Fonction pour générer un texte aléatoire
def generate_random_text(length=5000):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=length))

# Fonction pour créer un PDF avec du texte aléatoire
def create_pdf(file_path, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(file_path)

# Générer 10 PDF avec 5000 caractères aléatoires chacun
for i in range(10):
    random_text = generate_random_text()
    file_name = f"random_text_{i + 1}.pdf"
    create_pdf(file_name, random_text)
    print(f"PDF créé : {file_name}")

print("Tous les fichiers PDF ont été créés avec succès.")