class AnonymousSurvey:
    """Collect anonymous answers to a asurvey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")

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

