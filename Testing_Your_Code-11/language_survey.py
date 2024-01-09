from surveys import AnonymousSurvey

def main():
    # Define a question, and make a survey.
    question = "What language did you firsrt learn to speak?"
    language_survey = AnonymousSurvey(question)

    # Show the question, and store responses to the question.
    language_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input("Language: ")
        if response.lower() == 'q':
            break
        language_survey.store_response(response)
    
    # Show the survey results.
    print("\nThank you to everyone who participated in the survey!")
    language_survey.show_results()

if __name__ == "__main__":
    main()