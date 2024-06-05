from midiutil import MIDIFile
import pygame.midi

def tab_to_midi(tab_text, output_midi):
    # Здесь нужно преобразовать текст табулатур в формат, удобный для MIDI
    # Пример - добавление одной ноты
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)
    midi.addNote(0, 0, 60, 0, 1, 100)  # Канал 0, нота C4

    with open(output_midi, 'wb') as output_file:
        midi.writeFile(output_file)

def play_midi(file_path):
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)

    pygame.midi.quit()
