import random
ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.


class Board:

    def __init__(self):
        self.ALL_SPACES = list('123456789')
        self.board = {}
        self.move = None
        self.currentPlayer = random.choice([X, O])
        if self.currentPlayer==X:
            self.nextPlayer = O
        else:
            self.nextPlayer = X

        for space in ALL_SPACES:
            self.board[space] = BLANK  # Wszystkie pola na początku są puste.

    def __str__(self):
        return f'''
                    {self.board['1']}|{self.board['2']}|{self.board['3']} 1 2 3 
                    -+-+- 
                    {self.board['4']}|{self.board['5']}|{self.board['6']} 4 5 6 
                    -+-+- 
                    {self.board['7']}|{self.board['8']}|{self.board['9']} 7 8 9'''

    def update(self):
        self.board[self.move] = self.currentPlayer


    def isValidSpace(self):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if self.move is None:
            return False
        return self.move in ALL_SPACES or self.board[self.move] == BLANK

    def play(self):
        self.move = None
        while not self.isValidSpace():
            print(f'Jaki jest ruch gracza {self.currentPlayer}? (1-9)')
            self.move = input()
        self.update()

    def switchPlayers(self):
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer


    def isWinner(self):
        b, p = self.board, self.currentPlayer  # Krótsze nazwy jako "składniowy cukier".
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or  # poziomo na górze
                (b['4'] == b['5'] == b['6'] == p) or  # poziomo w środku
                (b['7'] == b['8'] == b['9'] == p) or  # poziomo u dołu
                (b['1'] == b['4'] == b['7'] == p) or  # pionowo z lewej
                (b['2'] == b['5'] == b['8'] == p) or  # pionowo w środku
                (b['3'] == b['6'] == b['9'] == p) or  # pionowo z prawej
                (b['3'] == b['5'] == b['7'] == p) or  # przekątna 1
                (b['1'] == b['5'] == b['9'] == p))  # przekątna 2

    def isBoardFull(self):
        for space in ALL_SPACES:
            if self.board[space] == BLANK:
                return False  # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True  # Nie ma wolnych pól, zatem zwróć True.

def main():
    """Rozgrywka w kółko i krzyżyk."""
    print('Witaj w grze kółko i krzyżyk!')
    gameBoard = Board()
    while True:
        print(gameBoard)

        # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
        move = None
        gameBoard.play()
        if gameBoard.isWinner():
            print(gameBoard.currentPlayer + ' wygrał grę!')
            break
        elif gameBoard.isBoardFull():  # Sprawdzenie remisu.
            gameBoard.print()
            print('Gra zakończyła się remisem!')
            break
          # Zmiana gracza.
        gameBoard.switchPlayers()
    print('Dziękuję za grę!')




if __name__ == '__main__':
    main()  # Wywołaj main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.
