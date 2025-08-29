
# import unittest
# from modules import get_main

# class NamesTestCase(unittest.TestCase):
#     def test_first_last(self):
#         formatted_name = get_main("janis", "joplin")
#         self.assertEqual(formatted_name, "Janis Joplin")

#     def test_first_last_middle(self):
#         formatted_name = get_main("janis", "joplin", "marie")
#         self.assertEqual(formatted_name, "Janis Marie Joplin")
# if __name__ == "__main__":
#     unittest.main()





# import unittest
# from modules import location

# class LocationTestCase(unittest.TestCase):
    
#     def test_city_country(self):
#         formatted_location = location("santiago", "chile")
#         self.assertEqual(formatted_location, "Santiago, Chile")
    
#     def test_city_country_population(self):
#         formatted_location = location("santiago", "chile", 5000000)
#         self.assertEqual(formatted_location, "Santiago, Chile - population 5000000")

# if __name__ == "__main__":
#     unittest.main()





import unittest
from modules import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")
        self.assertIn("English", my_survey.responses)
    
    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "French"]
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == "__main__":
    unittest.main()