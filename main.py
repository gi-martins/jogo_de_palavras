import random


def choose_menu() -> str:
    print("Escolha sua dificuldade")
    print("1 - nível fácil")
    print("2 - nível médio")
    print("3 - nível difícil")
    print("0 - sair do jogo")
    return input("Dificuldade: ")


def set_level(config: str) -> dict: 
    if config == "1":
        return {"lifes": 15, "level": "nivel_facil.txt"}
    elif config == "2":
        return {"lifes": 10, "level": "nivel_medio.txt"}
    elif config == "3":
        return {"lifes": 5, "level": "nivel_dificil.txt"}


def set_secret_word(lvl: str) -> str:
    with open(lvl, "r", encoding="utf-8") as database:
        words = database.read().split()
    return words[random.randint(0, len(words)-1)]


def run_game(secret_word: str, lifes: int) -> None: 
    valid_letters = []
    
    while True:
        gessed_word = ""

        letter_attempt = input("Digite uma letra: ")

        if len(letter_attempt) > 1 or letter_attempt.isspace() or not letter_attempt.isalpha(): 
            print("Digite apenas uma letra válida")
            continue

        if letter_attempt in secret_word:
            valid_letters.append(letter_attempt)
        else:
            lifes -= 1

        for letter in secret_word:    
        
            if letter in valid_letters:
                gessed_word += letter
            
            else:
                gessed_word += "*"         

        print(gessed_word)

        if lifes <= 0:
            print("Você perdeu!")
            break

        if gessed_word == secret_word:
            print("Palavra secreta está certa")
            break


if __name__ == "__main__":
    
    print("Jogo descubra a palavra")
    
    while True:
        
        difficulty = choose_menu()

        if difficulty == "0":
            print("Tchau, até a próxima")
            break
        if difficulty not in ("1", "2", "3"):
            print("\n**** Digite 1, 2 ou 3 ****\n")
            continue

        game_config = set_level(difficulty) # dicionario --> level == dicionario

        secret_word = set_secret_word(game_config["level"])

        run_game(secret_word, game_config["lifes"])
