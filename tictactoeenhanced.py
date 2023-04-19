"""
Tic Tac Toe with Memory

Dies ist eine erweiterte Version des klassischen Tic Tac Toe Spiels.
In dieser Version hat jedes Feld auf dem Spielfeld zwei Eigenschaften: ein Symbol (X oder O) und ein Ereignis.
Die Ereignisse können verschiedene Aktionen auslösen, wie zum Beispiel das Löschen eines zufälligen Symbols, das erneute Ziehen eines Spielers oder das Verschieben aller Symbole um eine Zeile nach unten.

Das Besondere an diesem Spiel ist, dass die Ereignisse bei jedem Spiel zufällig verteilt werden. Das bedeutet, dass jedes Spiel eine neue Herausforderung ist, da die Spieler nicht wissen, welche Ereignisse auf welchen Feldern liegen.

Das Spiel wird von zwei Spielern gespielt. Die Spieler setzen abwechselnd ihr Symbol (X oder O) auf ein freies Feld auf dem Spielfeld.
Wenn ein Spieler drei seiner Symbole in einer Reihe (horizontal, vertikal oder diagonal) hat, gewinnt er das Spiel.
Wenn alle Felder auf dem Spielfeld besetzt sind und kein Spieler gewonnen hat, endet das Spiel unentschieden.
"""
import pygame

# pygame initialisieren und ein Fenster erstellen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tic Tac Toe with Memory")

# Das Spielfeld als eine zweidimensionale Liste definieren
# Jede Zelle enthält zwei Elemente: das Symbol (X oder O) und das Ereignis (hidden oder etwas anderes)
board = [
    ["X", "nothing", "O", "delete random symbol", "X", "nothing"],
    ["O", "move again", "X", "nothing", "O", "rotate symbol"],
    ["X", "nothing", "O", "delete opponent symbol", "X", "nothing"]
]

# Einige Farben definieren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Eine Schriftart definieren
font = pygame.font.SysFont("Arial", 64)

# Die Größe und den Abstand jeder Zelle definieren
field_size = 100
field_margin = 10
board_x = 100
board_y = 100

# Eine Funktion definieren, die das Spielfeld auf dem Bildschirm zeichnet
def draw_board():
    for row in range(3):
        for col in range(3):
            if col * 2 >= len(board[row]):
                print(f"Ungültiger Index: {row=}, {col=}")
            else:
                symbol = board[row][col * 2]
            # Die Position und Größe jeder Zelle berechnen
            x = board_x + col * (field_size + field_margin)
            y = board_y + row * (field_size + field_margin)
            width = field_size
            height = field_size

            # Ein Rechteck für jede Zelle zeichnen
            pygame.draw.rect(screen, WHITE, [x, y, width, height])

            # Das Symbol und das Ereignis für jede Zelle bekommen
            symbol = board[row][col * 2] # Den Index mit col * 2 berechnen, um das erste Element zu bekommen
            event = board[row][col * 2 + 1] # Den Index mit col * 2 + 1 berechnen, um das zweite Element zu bekommen

            # Das Symbol auf der Zelle zeichnen
            text = font.render(symbol, True, BLACK)
            text_rect = text.get_rect()
            text_rect.centerx = x + width / 2
            text_rect.centery = y + height / 2
            screen.blit(text, text_rect)

            # Das Ereignis auf der Zelle zeichnen, wenn es aufgedeckt ist
            if event != "hidden":
                text = font.render(event, True, RED)
                text_rect = text.get_rect()
                text_rect.centerx = x + width / 2
                text_rect.centery = y + height / 4 # Die Position etwas nach oben verschieben, um Platz für das Symbol zu lassen
                screen.blit(text, text_rect)

# Eine Variable definieren, die angibt, ob das Spiel läuft oder nicht
running = True

# Eine Hauptschleife definieren, die das Spiel laufen lässt und auf Ereignisse reagiert
while running:
    # Durch alle Ereignisse iterieren, die pygame empfängt
    for event in pygame.event.get():
        # Wenn der Benutzer das Fenster schließt, dann beende das Spiel
        if event.type == pygame.QUIT:
            running = False
        
        # Wenn der Benutzer die Maus klickt, dann verarbeite den Zug
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Die Position der Maus bekommen
            pos = pygame.mouse.get_pos()

            # Die Position der Maus in eine Reihe und Spalte des Spielfelds umrechnen
            row = (pos[1] - board_y) // (field_size + field_margin)
            col = (pos[0] - board_x) // (field_size + field_margin)

            # Prüfen, ob die Reihe und Spalte gültig sind (innerhalb des Spielfelds) und ob die Zelle noch nicht aufgedeckt ist
            if row >= 0 and row < 4 and col >= 0 and col < 4 and board[row][col * 2 + 1] == "hidden":
                # Das Ereignis der Zelle von hidden auf etwas anderes ändern (z.B. nothing), um es aufzudecken
                board[row][col * 2 + 1] = "nothing" # Hier kannst du das Ereignis anpassen, je nachdem, was du für dein Spiel haben möchtest

                # Hier kannst du die Spiellogik implementieren, z.B. prüfen, ob das Ereignis einen Einfluss auf das Spiel hat, ob ein Spieler gewonnen hat, ob das Spiel unentschieden ist, usw.

    # Den Bildschirm mit Schwarz füllen
    screen.fill(BLACK)

    # Das Spielfeld zeichnen
    draw_board()

    # Den Bildschirm aktualisieren
    pygame.display.flip()
