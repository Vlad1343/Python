

# from modules import get_main

# print("Enter 'q' to quit")
# while True:
#     first = input("\nFirst name: ")
#     if first == "q":
#         break
#     second = input("Second name: ")
#     if second == "q":
#         break
#     formatted_name = get_main(first, second)
#     print(f"\tFormatted name: {formatted_name}")




# from modules import location
# city = input("Enter a city: ")
# country = input("Enter a country: ")
# full_loc = location(city, country)
# print(f"Full location: {full_loc}")




from modules import AnonymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' to quit\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)
    
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()