import time

class BankChatbot():
    def __init__(self):
        self.user_name = None
        self.user_age = None
        self.user_balance = None

    def greet(self):
        print("Hello, I'm your bank's virtual assistant. How can I assist you today?")
        time.sleep(1)

    def get_user_info(self):
        self.user_name = input("What's your name? ")
        print(f"Nice to meet you, {self.user_name}!")
        time.sleep(1)
        while True:
            try:
                self.user_age = int(input("How old are you? "))
                if self.user_age <= 0:
                    print("Please enter a valid age.")
                    continue
                break
            except ValueError:
                print("Please enter a valid age.")

        time.sleep(1)
        while True:
            try:
                self.user_balance = float(input("What's your current account balance? Rs"))
                if self.user_balance < 0:
                    print("Please enter a valid balance.")
                    continue
                break
            except ValueError:
                print("Please enter a valid balance.")
        time.sleep(1)

    def suggest_services(self):
        print("Based on your information, we recommend the following services:")
        if self.user_age >= 10 and self.user_age < 25:
            print("- You'll be able to open a student account as per your age.")
        if self.user_age >= 18:
            print("- Apply for a savings account to start saving for your future.")
        if self.user_balance >= 1000:
            print("- Consider opening a fixed deposit account for higher interest rates.")
        if self.user_age >= 25:
            print("- Explore investment options such as mutual funds or stocks.")
        time.sleep(1)

    def process_request(self):
        request = input("Is there anything specific you'd like assistance with? ").lower()
        if "balance" in request:
            print(f"Your current account balance is Rs{self.user_balance}.")
        elif "transaction" in request:
            print("You can perform various transactions through our online banking portal.")
        elif "loan" in request:
            print("To apply for a loan, please visit our nearest branch or apply online.")
        elif "fd" in request:
            print("Putting your money in an FD is a good option. Current interest rate for an FD is 6.75%.")
        elif "no" in request:
            print("OK. Have a great day!")
        else:
            print("I'm sorry, I couldn't understand your request.")

    def say_goodbye(self):
        print("Thank you for using our services. Have a great day!")

def main():
    bank_chatbot = BankChatbot()
    bank_chatbot.greet()
    bank_chatbot.get_user_info()
    bank_chatbot.suggest_services()
    bank_chatbot.process_request()
    bank_chatbot.say_goodbye()

if __name__ == "__main__":
    main()
