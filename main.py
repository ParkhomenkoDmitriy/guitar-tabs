import os
import pygame
from tab_extraction import extract_images_from_docx

def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            img_path = os.path.join(directory, filename)
            images.append(pygame.image.load(img_path))
    return images

def main():
    # Укажите путь к вашему файлу .docx
    docx_path = r"D:\Tabs\Exodus\Исход 1.docx"
    output_dir = "output_directory"

    # Проверьте, существует ли файл по указанному пути
    if not os.path.exists(docx_path):
        print(f"The file {docx_path} does not exist.")
        return

    # Извлечение изображений из документа
    extract_images_from_docx(docx_path, output_dir)
    print("Images extracted successfully.")

    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Guitar Tabs Viewer")
    clock = pygame.time.Clock()

    # Загрузка изображений
    images = load_images_from_directory(output_dir)
    if not images:
        print("No images found in the output directory.")
        return

    # Основной игровой цикл
    running = True
    image_index = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    image_index = (image_index + 1) % len(images)
                elif event.key == pygame.K_LEFT:
                    image_index = (image_index - 1) % len(images)

        # Очистка экрана
        screen.fill((255, 255, 255))

        # Отображение текущего изображения
        image = images[image_index]
        image_rect = image.get_rect(center=(400, 300))
        screen.blit(image, image_rect)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
