import requests

param = {
    "amount": 10,
    "type": "boolean"
}

res = requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean')
res.raise_for_status()
data = res.json()
question_data = (data["results"])


# question_data = [
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The Cold War ended with Joseph Stalin&#039;s death.",
#         "correct_answer": "False"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The Tiananmen Square protests of 1989 were held in Hong Kong.",
#         "correct_answer": "False"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The United States Department of Homeland Security was formed in response to the September 11th attacks.",
#         "correct_answer": "True"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Former United States Presidents John Adams and Thomas Jefferson died within hours of each other.",
#         "correct_answer": "True"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In World War ll, Great Britian used inflatable tanks on the ports of Great Britain to divert Hitler away from Normandy\/D-day landing.",
#         "correct_answer": "True"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Adolf Hitler was tried at the Nuremberg trials.",
#         "correct_answer": "False"

#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Kublai Khan is the grandchild of Genghis Khan?",
#         "correct_answer": "True"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War.",
#         "correct_answer": "True"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The United States of America was the first country to launch a man into space.",
#         "correct_answer": "False"
#     },
#     {
#         "category": "History",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Thomas Crapper was a plumber who invented the flushing toilet.",
#         "correct_answer": "False"
#     }
# ]