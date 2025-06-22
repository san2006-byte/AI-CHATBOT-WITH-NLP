# AI-CHATBOT-WITH-NLP

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : SANDHYA M

*INTERN ID* : CT04DG1363

*DOMAIN* : Python Programming

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH

  I was tasked with creating an interactive chatbot in Python utilising Natural Language Processing (NLP) techniques. The chatbot needed to be able to conversely respond to user enquiries, particularly those pertaining to basic Python programming. This chatbot had to mimic actual human interaction by intelligently responding to user messages based on their content, in contrast to standard command-line programmes that only return outputs.
  I chose to use NLTK (Natural Language Toolkit), a Python NLP library that is frequently used in both academic and commercial NLP projects, to finish this task. Even though I had heard of natural language processing (NLP), this was the first time I had actually used it to create a working chatbot. The chance to study how machines understand human language and react contextually—a feature utilised in voice assistants, help desks, and AI customer support systems nowadays excited me.
  
  Making a plan for the chatbot's behaviour was the first step. I made a file called intents.json that served as the knowledge base for the chatbot. It contained frequently asked user questions organised into categories (or "intents") such as hellos, Python lists, loops, functions, and farewells. Each intent included a set of pre-written responses along with sample input phrases. The chatbot was able to match user input with pre-existing topics thanks to this JSON structure.  
  In terms of code, I created a script named chatbot.py that reads the intent file, analyses user input, and determines the intent that matches the user the best. I accomplished this by reducing words to their most basic form using a straightforward NLP technique known as stemming, more especially the PorterStemmer from NLTK. This made it easier for the chatbot to comprehend that the terms "functions," "functioning," and "function" all refer to the same fundamental idea.

  The chatbot preprocessed the text before comparing the user's input to the JSON file's patterns. It selected a pertinent response and printed it in the terminal if it discovered a match. The chatbot encouraged the user to try again by politely stating that it didn't understand if there was no match. Because of this method, the chatbot was lightweight and simple to add more questions to.
  Formatting the user experience was one of the most fascinating aspects of this task. I wanted the chatbot to feel interactive, friendly, and responsive even though it operates in the terminal. I included fallback messages for input that was not recognised and paid close attention to the input/output flow. The chatbot felt more realistic and approachable because of this attention to detail.

  After everything was functioning properly, I used Visual Studio Code's built-in terminal to launch the chatbot. It answered correctly when I tested it using a variety of questions, including "What is a loop?" "Hello," "Bye," and "What is a function in Python?" The chatbot felt like a real assistant that could teach someone the fundamentals of programming; it did more than just work.
  Ultimately, I stored the functional files in a project folder as intents.json and chatbot.py. Through this task, I was able to learn about the fundamentals of conversational AI systems, how logic can be guided by structured data like intents, and how even minor NLP techniques like stemming can have a significant impact on language comprehension.    
  
  All in all, I learned more than just how to write code from this project. It demonstrated to me how chatbots can be developed step-by-step, how machines can be made to understand human communication, and how crucial it is to combine data, logic, and user experience when creating intelligent systems. I'm now more comfortable using Python for real-world AI applications as well as scripting.

  *OUTPUT*:
  
