
class ExpertSystem:
    def __init__(self):
        # Initialize the knowledge base with diseases and their associated symptoms
        self.knowledge_base = {
            'Common Cold': {'fever', 'cough', 'sore throat', 'runny nose'},
            'Flu': {'fever', 'cough', 'body aches', 'fatigue'},
            'COVID-19': {'fever', 'dry cough', 'shortness of breath', 'loss of taste or smell'}
        }

        # Initialize the treatment base with diseases and their recommended treatments
        self.treatment_base = {
            'Common Cold': 'Rest, fluids, over-the-counter cold medication',
            'Flu': 'Antiviral medication, rest, fluids',
            'COVID-19': 'Isolation, rest, fluids, medical treatment if necessary'
        }

    def recommend_diagnosis(self, user_symptoms):
        # Initialize an empty list to store matching diagnoses
        matching_diseases = []

        # Loop through each disease and its associated symptoms in the knowledge base
        for disease, symptoms in self.knowledge_base.items():
            # Find common symptoms between user_symptoms and the current disease's symptoms
            common_symptoms = set(user_symptoms).intersection(symptoms)

            # If there are at least three common symptoms, consider this disease a match
            if len(common_symptoms) >= 3:
                matching_diseases.append(disease)

        # Return the list of matching diagnoses
        return matching_diseases

    def recommend_treatment(self, diagnosis):
        # Return the recommended treatment for a given diagnosis from the treatment base
        if diagnosis in self.treatment_base:
            return self.treatment_base[diagnosis]
        else:
            # If the diagnosis is not in the treatment base, return a default message
            return "No treatment recommendation available for this diagnosis."

# Main function to interact with the expert system
def main():
    # Instantiate the ExpertSystem class
    expert_system = ExpertSystem()

    print("Welcome to the Hospital Expert System!")

    # Prompt the user to enter their symptoms
    print("Please enter your symptoms (separated by commas):")
    user_input = input().strip().lower()  # Get user input and convert it to lowercase
    # Split the input into a list of individual symptoms and remove extra spaces
    user_symptoms = [symptom.strip() for symptom in user_input.split(',')]

    # Get recommended diagnoses based on the user's symptoms
    recommended_diagnoses = expert_system.recommend_diagnosis(user_symptoms)

    # If there are recommended diagnoses, display them
    if recommended_diagnoses:
        print("Based on your symptoms, the following diagnoses are recommended:")
        # Loop through each recommended diagnosis and print it
        for diagnosis in recommended_diagnoses:
            print("-", diagnosis)

        # Display recommended treatment(s) for each diagnosis
        print("\nRecommending treatment:")
        for diagnosis in recommended_diagnoses:
            treatment = expert_system.recommend_treatment(diagnosis)
            print(f"For {diagnosis}: {treatment}")
    else:
        # If no diagnoses were found, print a message
        print("No diagnoses found based on the symptoms provided.")


# Entry point for the script
if __name__ == "__main__":
    main()  # Run the main function

