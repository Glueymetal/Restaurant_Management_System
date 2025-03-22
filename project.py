import random
import sys
from PIL import Image

def main():
    try:
        print(
            "x-----------------------------------------------------------------------------------------------------x"
        )
        print(
            "                                          Jumbled Words                                                "
        )
        print(
            "x-----------------------------------------------------------------------------------------------------x"
        )
        print(
            "There are THREE difficulties and each difficulty will only have 5 QUESTIONS "
                    "And You can exit this program by entering x"
        )
        print("1.Easy\n2.Medium\n3.Hard\n4.Exit-(x)\n")
        print("Type 1 or 2 or 3 or x: ")
        mode = input("Mode:").lower()
        if verify_mode(mode):
            if mode == "1":
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print(
                    "                           It Seems like you have choosen EASY mode!                                     "
                )
                print(
                    "                           You have 5 chances to get the answer right                                  "
                )
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print("There are 2 categories you can choose from or you can exit by entering x")
                print("1.Colours\n2.Animals\n3.Exit-(x)\n")
                category = input("Enter 1 or 2 or x: ")
                score = easy(category)
                if score == None:
                    sys.exit("Error")
                progress("easy",score)

            elif mode == "2":
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print(
                    "                                It Seems like you have choosen MEDIUM mode!                                   "
                )
                print(
                    "                                You have 3 chances to get the answer right                                  "
                )
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print("There are 2 categories you can choose from or you can exit by entering x")
                print(
                    "1.Common Elements in the Periodic Table\n2.Iconic Dishes Around The World \n3.Exit-(x)\n"
                )
                category = input("Enter 1 or 2 or x: ")
                score = medium(category)
                if score == None:
                    sys.exit("Error")
                progress("medium",score)
            elif mode == "3":
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print(
                    "                            Seems like you have choosen/gotten to Hard mode!                                 "
                )
                print(
                    "         You have only 1 chance to get each answer right and if you get every answer right,        "
                )
                print(
                    "                                  You get a Special Prize!!                                         "
                )
                print(
                    "x-----------------------------------------------------------------------------------------------------x"
                )
                print("There are 2 categories you can choose from or you can exit by entering x")
                print("1.Countries of Asia\n2.Famous Sports\n3.Exit-(x)")
                category = input("Enter 1 or 2 or x: ")
                score = hard(category)
                if score == None:
                    sys.exit("Error")
                progress("hard",score)
            elif mode == "x":
                sys.exit("Thank You For Playing This Game")
    except ValueError:
        sys.exit("Please enter the Valid Input")
    except KeyboardInterrupt:
        print()
        print("Exiting...........")
        sys.exit("Thank You For Playing This Game")





def verify_mode(mode):
    if mode == "1" or mode == "2" or mode == "3" or mode == "x":
        return mode
    else:
        raise ValueError


def easy(category):
    if category == "1":
        try:
            print("x-----------Easy Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                chances = 0
                colours = [
                    "Red",
                    "Blue",
                    "Green",
                    "Yellow",
                    "Purple",
                    "Orange",
                    "Pink",
                    "Brown",
                    "Gray",
                    "Black",
                    "White",
                ]
                word = random.choice(colours)
                while word in prev:
                    word = random.choice(colours)
                prev.add(word)
                sentence = list(word)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        chances += 1
                        if chances == 5:
                            count += 1
                            print(f"Sorry, the correct answer was {word}.")
                            break
            return score
        except:
            print("Try Again!!")
    elif category == "2":
        try:
            print("x-----------Easy Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                chances = 0
                animals = [
                    "Aardvark",
                    "Elephant",
                    "Lion",
                    "Penguin",
                    "Tortoise",
                    "Dog",
                    "Bee",
                    "Monkey",
                    "Alligator",
                    "Wolf",
                    "Dolphin",
                    "Octopus",
                    "Whale",
                    "Cat",
                    "Shark",
                ]
                word = random.choice(animals)
                while word in prev:
                    word = random.choice(animals)
                prev.add(word)
                sentence = list(word)
                # print(sentence)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        chances += 1
                        if chances == 5:
                            count += 1
                            print(f"Sorry, the correct answer was {word}.")
                            break
            return score
        except:
            print("Try Again!!")
    elif category == "x":
        sys.exit("Thank You for Playing!!")
    else:
        sys.exit("Thank You for Playing!!")


def medium(category):
    if category == "1":
        try:
            print("x-----------Medium Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                chances = 0
                elements = [
                    "Hydrogen",
                    "Helium",
                    "Lithium",
                    "Beryllium",
                    "Boron",
                    "Carbon",
                    "Nitrogen",
                    "Oxygen",
                    "Fluorine",
                    "Neon",
                    "Sodium",
                    "Magnesium",
                    "Aluminium",
                    "Silicon",
                ]
                word = random.choice(elements)
                while word in prev:
                    word = random.choice(elements)
                prev.add(word)
                sentence = list(word)
                # print(sentence)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        chances += 1
                        if chances == 3:
                            count += 1
                            print(f"Sorry, the correct answer was {word}.")
                            break
            return score
        except:
            print("Try Again!!")
    elif category == "2":
        try:
            print("x-----------Medium Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                chances = 0
                dishes = [
                    "Pizza",
                    "Sushi",
                    "Hummus",
                    "Tacos",
                    "Curry",
                    "FriedRice",
                    "HotDogs",
                    "Croissant",
                    "PadThai",
                    "Samosa",
                    "Goulash",
                    "Baklava",
                    "Sashimi",
                    "Poutine",
                    "Ceviche",
                    "Kimchi",
                    "Paella",
                ]

                word = random.choice(dishes)
                while word in prev:
                    word = random.choice(dishes)
                sentence = list(word)
                prev.add(word)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        chances += 1
                        if chances == 3:
                            count += 1
                            print(f"Sorry, the correct answer was {word}.")
                            break
            return score
        except:
            print("Try Again!!")
    elif category == "x":
        sys.exit("Thank You for Playing!!")
    else:
        sys.exit("Thank You for Playing!!")


def hard(category):
    if category == "1":
        try:
            print("x-----------Hard Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                countries = [
                    "India",
                    "China",
                    "Indonesia",
                    "Pakistan",
                    "Bangladesh",
                    "Japan",
                    "Philippines",
                    "Vietnam",
                    "Iran",
                    "Turkey",
                    "Thailand",
                    "Myanmar",
                    "SouthKorea",
                    "Iraq",
                    "Afghanistan",
                    "SaudiArabia",
                    "Uzbekistan",
                    "Yemen",
                    "Malaysia",
                    "Nepal",
                    "NorthKorea",
                    "Syria",
                    "SriLanka",
                    "Kazakhstan",
                    "Cambodia",
                    "Jordan",
                    "Azerbaijan",
                    "Tajikistan",
                    "UnitedArabEmirates",
                    "Israel",
                    "Laos",
                    "Kyrgyzstan",
                    "Turkmenistan",
                    "Singapore",
                    "Palestine",
                    "Lebanon",
                    "Oman",
                    "Kuwait",
                    "Georgia",
                    "Mongolia",
                    "Armenia",
                    "Qatar",
                    "Bahrain",
                    "Timor-Leste",
                    "Cyprus",
                    "Bhutan",
                    "Maldives",
                    "Brunei",
                ]
                word = random.choice(countries)
                while word in prev:
                    word = random.choice(countries)
                prev.add(word)
                sentence = list(word)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        print(f"Sorry, the correct answer was {word}.")
                        count += 1
                        break
            return score
        except(ValueError):
            print("Try Again")
    elif category == "2":
        try:
            print("x-----------Hard Mode-----------x")
            print(f"You have chosen category {category}")
            prev = set()
            count = 0
            score = 0
            while count < 5:
                sports = [
                    "Football",
                    "Cricket",
                    "Hockey",
                    "Tennis",
                    "Volleyball",
                    "TableTennis",
                    "Basketball",
                    "Baseball",
                    "Rugby",
                    "Golf",
                    "Badminton",
                    "Boxing",
                    "Cycling",
                    "Gymnastics",
                    "Wrestling",
                    "Archery",
                    "Sailing",
                ]
                word = random.choice(sports)
                while word in prev:
                    word = random.choice(sports)
                prev.add(word)
                sentence = list(word)
                random.shuffle(sentence)
                new_word = "".join(sentence)
                while new_word == word:
                    random.shuffle(sentence)
                    new_word = "".join(sentence)
                print(f"{count+1}. The word to be rearranged: {new_word}")
                while True:
                    you = input("Enter guess: ")
                    if you.lower() == word.lower():
                        print("Correct")
                        score += 1
                        count += 1
                        break
                    else:
                        print(f"Sorry, the correct answer was {word}.")
                        count += 1
                        break
            return score
        except ValueError:
            print("Try Again!!")
    elif category == "x":
        sys.exit("Thank You for Playing!!")
    else:
        sys.exit("Thank You for Playing!!")


def show_scores(mode, score):
    if (mode == "easy" or mode == "medium") and score == 5:
        return "Impressive! You rearranged every word correctly!"
    elif (mode == "hard") and score == 5:
        return "Impressive! You rearranged every word correctly in HARD Mode!"
    elif (mode == "easy" or mode == "medium" or mode == "hard") and (
        score == 3 or score == 4
    ):
        return "Good! You got most of them right"
    elif (mode == "easy" or mode == "medium" or mode == "hard") and (
        score == 2 or score == 1
    ):
        return "Not bad! You're making progress."
    else:
        return "Keep practicing - you'll improve!"

def progress(mode,score):
        if mode == "easy":
                    if score == 5:
                            print(f"Score:{score}/5")
                            print(show_scores(mode,score))
                            print(
                                "x-----------------------------------------------------------------------------------------------------x"
                            )
                            print(
                                "                         Congratulations!! You have cleared Easy Mode!                "
                            )
                            print(
                                "                            !!You have progressed to Medium Mode!!                       "
                            )
                            print(
                                "                         You have 3 chances to get the answer right                                  "
                            )
                            print(
                                "x-----------------------------------------------------------------------------------------------------x"
                            )
                            print("There are 2 categories you can choose from")
                            print("Or you can exit the program by entering \"x\"")
                            print(
                                "1.Common Elements in the Periodic Table\n2.Iconic Dishes Around The World\n3.Exit-(x)"
                            )
                            category = input("Enter 1 or 2 or x: ")
                            score = medium(category)
                            if score == None:
                                sys.exit("Error")
                            progress("medium",score)
                    else:
                            print(f"Score:{score}/5")
                            print(show_scores(mode,score))
                            print("Seems like you are stuck in Easy Mode!!!")
                            print("There are 2 categories you can choose from or you can exit by entering \"x\"")
                            print("1.Colours\n2.Animals\n3.Exit-(x)")
                            category = input("Enter 1 or 2 or x:")
                            score = easy(category)
                            if score == None:
                                sys.exit("Error")
                            progress("easy",score)
        elif mode == "medium":
                if score == 5:
                    print(f"Score:{score}/5")
                    print(show_scores(mode,score))
                    print(
                        "x-----------------------------------------------------------------------------------------------------x"
                    )
                    print(
                                "                       Congratulations!! You have cleared Medium Mode!                "
                            )
                    print(
                                  "                         !!You have progressed to HARD Mode !!                   "
                    )
                    print(
                        "               You have only 1 chances to get each answer right and if you get every answer right,        "
                    )
                    print(
                        "                                       You get a Special Prize!!                                         "
                    )
                    print(
                        "x-----------------------------------------------------------------------------------------------------x"
                    )
                    print("There are 2 categories you can choose from or you can exit the program by entering x")
                    print("1.Countries of Asia\n2.Famous Sports\n3.Exit-(x)\n")
                    category = input("Enter 1 or 2 or x: ")
                    score = hard(category)
                    if score == None:
                            sys.exit("Error")
                    progress("hard",score)
                else:
                    print(f"Score:{score}/5")
                    print(show_scores(mode,score))
                    print("Seems like you are stuck in Medium Mode!!!")
                    print("There are 2 categories you can choose from or you can exit the program by entering x")
                    print(
                        "1.Common Elements in the Periodic Table\n2.Iconic Dishes Around The World\n3.Exit-(x)\n"
                    )
                    category = input("Enter 1 or 2 or x:")
                    score = medium(category)
                    if score == None:
                        sys.exit("Error")
                    progress("medium",score)
        elif mode == "hard":
            if score == 5:
                print("Game Over!")
                print(f"Score:{score}/5")
                print("!!Here's Your Reward!!")
                im = Image.open("download.png")
                im.show()
                print(show_scores(mode,score))
                print("To continue playing the game,enter 1")
                print("Or,to exit,enter 2")
                option = input("Enter 1 or 2: ")
                while option != "1" and option != "2":
                    option = input("Enter 1 or 2: ")
                if option == "1":
                    restart(True)
                elif option == "2":
                    restart(False)
            else:
                print(f"Score:{score}/5")
                print(show_scores(mode,score))
                print("Seems like you are stuck in Hard Mode!!!")
                print("There are 2 categories you can choose from or you can exit the program by entering x")
                print("1.Countries of Asia\n2.Famous Sports\n3.Exit-(x)")
                category = input("Enter 1 or 2 or x: ")
                score = hard(category)
                if score == None:
                    sys.exit("Error")
                progress("hard",score)

def restart(option):
    if option == True:
        main()
    elif option == False:
        sys.exit("!!!Thank You For Playing This Game!!!")





if __name__ == "__main__":
    main()
