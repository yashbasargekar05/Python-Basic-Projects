questions = [
            ["Who is Shah Rukh Khan ?", "WWE Wrestler", "Actor", "Astronaut", "plumber",2],
            ["What is the capital of France?", "Paris", "London", "Berlin", "Rome", 1],
            ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
            ["What is the chemical symbol for water?", "H2O", "CO2", "O2", "NaCl", 1],
            ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
            ["What is the tallest mountain in the world?", "Mount Everest", "K2", "Kangchenjunga", "Lhotse", 1],
            ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
            ["Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Mark Twain", "Charles Dickens", 1],
            ["What is the smallest prime number?", "0", "1", "2", "3", 3],
            ["What is the currency of Japan?", "Yen", "Dollar", "Euro", "Pound", 1]
             ]

prizes = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]
i = 0

for question in questions:
    print(question[0])
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])
    
    try:
        a = int(input("Enter the number corresponding to your answer: "))
        if (a == question[5]):
            print("Correct!")
        else:
            print("Wrong! The correct answer is:", question[question[5]])
            break
    except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            break
    
    print(f"You won {prizes[i]}RS")
    i += 1