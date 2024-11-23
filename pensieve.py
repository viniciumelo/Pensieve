import cv2
import pytesseract
import os

# Configuração do Tesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"

# Função para processar a imagem
def process_prescription(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)

    # Converter para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar binarização
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Realizar OCR
    text = pytesseract.image_to_string(binary_image, lang="eng")

    return text

# Testando o programa
if __name__ == "__main__":
    # Caminho da imagem de teste
    test_image = "data/sample_prescription.jpeg"  # Substitua pelo caminho real

    if os.path.exists(test_image):
        extracted_text = process_prescription(test_image)
        print("Texto extraído:")
        print(extracted_text)
    else:
        print(f"Imagem não encontrada: {test_image}")
