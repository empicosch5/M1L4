import telebot

bot = telebot.TeleBot('')

questions = [
    {"question": "What's the most popular Roblox game right now?", "answer": "grow a garden"},
    {"question": "How many continents are there?", "answer": "7"},
    {"question": "What is 3 times 7?", "answer": "21"}
]

user_question_index = {}

@bot.message_handler(commands=['victorina'])
def start_quiz(message):
    user_question_index[message.chat.id] = 0
    bot.send_message(message.chat.id, questions[0]["question"])

@bot.message_handler(func=lambda message: message.chat.id in user_question_index)
def quiz_handler(message):
    idx = user_question_index[message.chat.id]
    correct_answer = questions[idx]["answer"]
    if message.text.strip().lower() == correct_answer.lower():
        bot.reply_to(message, "Correct!")
    else:
        bot.reply_to(message, f"Wrong! The correct answer is: {correct_answer}")
    idx += 1
    if idx < len(questions):
        user_question_index[message.chat.id] = idx
        bot.send_message(message.chat.id, questions[idx]["question"])
    else:
        bot.send_message(message.chat.id, "Quiz finished!")
        del user_question_index[message.chat.id]

bot.polling()
