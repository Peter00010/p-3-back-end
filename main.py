from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = {
    1: {
        "question": "What is the smallest country in the world?",
        "choices": [ "Vatican City","Monaco", "San Marino"],
        "answer": "Vatican City"
    },
    2: {
        "question": "In which year did World War II end?",
        "choices": ["1945","1943" , "1947"],
        "answer": "1945"
    },
    3: {
        "question": "Who wrote the novel 'Pride and Prejudice'?",
        "choices": [ "Charlotte Bronte", "Emily Bronte","Jane Austen"],
        "answer": "Jane Austen"
    },
    4: {
        "question": "What is the largest mammal in the world?",
        "choices": ["Blue whale","Elephant", "Giraffe"],
        "answer": "Blue whale"
    },
    5: {
        "question": "Which city is known as the 'City of Love'?",
        "choices": ["Venice", "Rome","Paris"],
        "answer": "Paris"
    },
    6: {
        "question": "Who was the first person to step on the moon?",
        "choices": [ "Buzz Aldrin","Neil Armstrong", "Michael Collins"],
        "answer": "Neil Armstrong"
    },
    7: {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    8: {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "choices": ["China", "Japan", "South Korea"],
        "answer": "Japan"
    },
    9: {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "choices": ["Michelangelo","Leonardo da Vinci", "Raphael"],
        "answer": "Michelangelo"
    },
    10: {
        "question": "What is the largest organ in the human body?",
        "choices": ["Liver", "Heart", "Skin"],
        "answer": "Skin"
    },
    11: {
        "question": "What is the capital of Australia?",
        "choices": ["Sydney", "Melbourne", "Canberra"],
        "answer": "Canberra"
    },
    12: {
        "question": "Who is often called the 'Father of Computers'?",
        "choices": ["Charles Babbage", "Alan Turing", "Ada Lovelace"],
        "answer": "Charles Babbage"
    },
    13: {
        "question": "What is the main ingredient in guacamole?",
        "choices": [ "Tomato","Avocado", "Onion"],
        "answer": "Avocado"
    },
    14: {
        "question": "Which planet is known as the 'Red Planet'?",
        "choices": ["Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    15: {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Au", "Ag", "Fe"],
        "answer": "Au"
    },
    16: {
        "question": "Which famous artist cut off part of his ear?",
        "choices": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci"],
        "answer": "Vincent van Gogh"
    },
    17: {
        "question": "What is the largest living species of lizard?",
        "choices": ["Monitor lizard", "Gila monster","Komodo dragon"],
        "answer": "Komodo dragon"
    },
    18: {
        "question": "Which country is known as the 'Pearl of Africa'?",
        "choices": ["Uganda", "Tanzania", "Kenya"],
        "answer": "Uganda"
    },
    19: {
        "question": "Who is the author of 'The Great Gatsby'?",
        "choices": ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck"],
        "answer": "F. Scott Fitzgerald"
    },
    20: {
        "question": "What is the largest species of shark?",
        "choices": ["Great white shark", "Whale shark", "Hammerhead shark"],
        "answer": "Whale shark"
    },
     21: {
        "question": "What is the world's largest desert?",
        "choices": ["Sahara Desert", "Arctic Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    22: {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "answer": "Leonardo da Vinci"
    },
    23: {
        "question": "What is the most widely spoken language in the world?",
        "choices": ["English", "Mandarin Chinese", "Spanish"],
        "answer": "Mandarin Chinese"
    },
    24: {
        "question": "What is the capital of Canada?",
        "choices": ["Toronto", "Vancouver", "Ottawa"],
        "answer": "Ottawa"
    },
    25: {
        "question": "Who is known as the 'Father of Modern Physics'?",
        "choices": ["Albert Einstein", "Isaac Newton", "Galileo Galilei"],
        "answer": "Albert Einstein"
    },
    26: {
        "question": "What is the national flower of Japan?",
        "choices": ["Cherry blossom", "Rose", "Lotus"],
        "answer": "Cherry blossom"
    },
    27: {
        "question": "Which element is the most abundant in the Earth's atmosphere?",
        "choices": ["Oxygen", "Nitrogen", "Carbon dioxide"],
        "answer": "Nitrogen"
    },
    28: {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["William Shakespeare", "George Bernard Shaw", "Christopher Marlowe"],
        "answer": "William Shakespeare"
    },
    29: {
        "question": "What is the largest type of deer?",
        "choices": ["Elk", "Moose", "Reindeer"],
        "answer": "Moose"
    },
    30: {
        "question": "What is the longest river in Africa?",
        "choices": ["Nile River", "Congo River", "Zambezi River"],
        "answer": "Nile River"
    },
    31: {
        "question": "Who is the Greek god of war?",
        "choices": ["Ares", "Zeus", "Hades"],
        "answer": "Ares"
    },
    32: {
        "question": "What is the largest bird of prey in the world?",
        "choices": ["Golden eagle", "Bald eagle", "Andean condor"],
        "answer": "Andean condor"
    },
    33: {
        "question": "Who wrote the novel 'To Kill a Mockingbird'?",
        "choices": ["Harper Lee", "John Steinbeck", "F. Scott Fitzgerald"],
        "answer": "Harper Lee"
    },
    34: {
        "question": "What is the largest freshwater lake in the world by volume?",
        "choices": ["Lake Superior", "Lake Baikal", "Lake Victoria"],
        "answer": "Lake Baikal"
    },
    35: {
        "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
        "choices": ["Mercury", "Venus", "Mars"],
        "answer": "Venus"
    },
    36: {
        "question": "What is the capital of South Korea?",
        "choices": ["Seoul", "Busan", "Incheon"],
        "answer": "Seoul"
    },
    37: {
        "question": "Who is the author of 'The Catcher in the Rye'?",
        "choices": ["J.D. Salinger", "Ernest Hemingway", "F. Scott Fitzgerald"],
        "answer": "J.D. Salinger"
    },
    38: {
        "question": "What is the chemical symbol for silver?",
        "choices": ["Ag", "Au", "Pt"],
        "answer": "Ag"
    },
    39: {
        "question": "What is the tallest mountain in Africa?",
        "choices": ["Mount Kilimanjaro", "Mount Kenya", "Mount Elgon"],
        "answer": "Mount Kilimanjaro"
    },
    40: {
        "question": "Who painted 'The Starry Night'?",
        "choices": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"],
        "answer": "Vincent van Gogh"
    },
    41: {
        "question": "What is the largest species of bear?",
        "choices": ["Polar bear", "Grizzly bear", "Kodiak bear"],
        "answer": "Polar bear"
    },
    42: {
        "question": "Which country has the longest coastline in the world?",
        "choices": ["Canada", "Australia", "Norway"],
        "answer": "Canada"
    },
    43: {
        "question": "Who composed the 'Four Seasons'?",
        "choices": ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Antonio Vivaldi"],
        "answer": "Antonio Vivaldi"
    },
    44: {
        "question": "What is the largest species of penguin?",
        "choices": ["Emperor penguin", "King penguin", "Gentoo penguin"],
        "answer": "Emperor penguin"
    },
    45: {
        "question": "Who is known as the 'King of Pop'?",
        "choices": ["Elvis Presley", "Michael Jackson", "Prince"],
        "answer": "Michael Jackson"
    },
    46: {
        "question": "What is the capital of Brazil?",
        "choices": ["Rio de Janeiro", "Brasília", "São Paulo"],
        "answer": "Brasília"
    }
}

@app.get("/")
def index():
    return { "name": "First Data" } 

@app.get("/get-question/{question_id}")
def get_question(question_id: int ):
    random_question = random.choice(questions)
    return random_question

