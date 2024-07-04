# from APIController import APIController
# from ConsoleView import ConsoleView
# import argparse

# def main():
# #     controller = APIController()
    
# #     # Example for retrieving courses
# #     token = 'd39ecf70f0e8370ff238bd8cdfcfd014'
# #     courses_response = controller.get_courses(token)
# #     ConsoleView.display(courses_response)
    
# #     # Example for creating a course
# #     # new_course_response = controller.create_course(
# #     #     token=token,
# #     #     fullname='Mon Nouveau Cours',
# #     #     shortname='MNC',
# #     #     categoryid=2
# #     # )
# #     # ConsoleView.display(new_course_response)

# # if __name__ == "__main__":
# #     main()
#     parser = argparse.ArgumentParser(description="Test the Moodle API functionalities")
#     parser.add_argument('--action', choices=['get_courses', 'create_course', 'get_user', 'create_category'], help='Specify the action to perform')
#     args = parser.parse_args()
    
#     controller = APIController()
#     # token = 'd39ecf70f0e8370ff238bd8cdfcfd014'
#     token = '6b56aecb50603a843ff19b06b792755a'

#     if args.action == 'get_courses':
#         courses_response = controller.get_courses(token)
#         ConsoleView.display(courses_response)
#     elif args.action == 'create_course':
#         new_course_response = controller.create_course(
#             token=token,
#             fullname='Mekalfone',
#             shortname='M',
#             categoryid=7
#         )
#         ConsoleView.display(new_course_response)
#     elif args.action == 'get_user':
#         user_response = controller.get_user(
#             token=token,
#             username = "mekalfone"
#         )
#         ConsoleView.display(user_response)
#     elif args.action == 'create_category':
#         new_category_response = controller.create_category(
#             token=token,
#             category_name = "mekalfone"
#         )
#         ConsoleView.display(new_category_response)

# if __name__ == "__main__":
#     main()



# import pytest
# from APIController import APIController
# from ConsoleView import ConsoleView

# # Fixture to provide API Controller
# @pytest.fixture
# def controller():
#     return APIController()

# # Fixture to provide token
# @pytest.fixture
# def token():
#     return '6b56aecb50603a843ff19b06b792755a'

# # Mock ConsoleView.display to not perform any actual console output during tests
# @pytest.fixture(autouse=True)
# def mock_display(mocker):
#     mocker.patch.object(ConsoleView, 'display')

# # Test getting courses
# def test_get_courses(controller, token, mocker):
#     mocker.patch.object(APIController, 'get_courses', return_value={'status': 'success', 'data': []})
#     response = controller.get_courses(token)
#     assert response['status'] == 'success'
#     ConsoleView.display(response)  # Ensure ConsoleView.display is called

# # Test creating a course
# def test_create_course(controller, token, mocker):
#     expected_response = {'status': 'success', 'course_id': 101}
#     mocker.patch.object(APIController, 'create_course', return_value=expected_response)
#     response = controller.create_course(token, 'Mekalfone', 'M', 7)
#     assert response == expected_response
#     ConsoleView.display(response)

# # Test getting a user
# def test_get_user(controller, token, mocker):
#     expected_response = {'status': 'success', 'user_id': '1001'}
#     mocker.patch.object(APIController, 'get_user', return_value=expected_response)
#     response = controller.get_user(token, 'mekalfone')
#     assert response == expected_response
#     ConsoleView.display(response)

# # Test creating a category
# def test_create_category(controller, token, mocker):
#     expected_response = {'status': 'success', 'category_id': 500}
#     mocker.patch.object(APIController, 'create_category', return_value=expected_response)
#     response = controller.create_category(token, 'mekalfone')
#     assert response == expected_response
#     ConsoleView.display(response)






# import pytest
# from APIController import APIController
# from ConsoleView import ConsoleView

# @pytest.fixture
# def controller():
#     return APIController()

# @pytest.fixture
# def token():
#     return '6b56aecb50603a843ff19b06b792755a'

# # Since ConsoleView.display is critical to output, you don't need to mock it. Instead, check what it prints.
# # Test getting courses
# def test_get_courses(controller, token, capsys):
#     # Setup a known return value for the controller method
#     controller.get_courses = lambda t: {'status': 'success', 'data': []}
#     response = controller.get_courses(token)
#     # Assuming ConsoleView.display prints the response
#     ConsoleView.display(response)
#     captured = capsys.readouterr()
#     assert 'success' in captured.out
#     # assert 'Course1' in captured.out
#     # assert 'Course2' in captured.out

# # Test creating a course
# def test_create_course(controller, token, capsys):
#     controller.create_course = lambda token, fullname, shortname, categoryid: {'status': 'success', 'course_id': 101}
#     response = controller.create_course(token, 'Mekalfone', 'M', 7)
#     ConsoleView.display(response)
#     captured = capsys.readouterr()
#     assert 'success' in captured.out
#     assert '101' in captured.out

# # Test getting a user
# def test_get_user(controller, token, capsys):
#     controller.get_user = lambda token, username: {'status': 'success', 'user_id': '1001'}
#     response = controller.get_user(token, 'mekalfone')
#     ConsoleView.display(response)
#     captured = capsys.readouterr()
#     assert 'success' in captured.out
#     assert '1001' in captured.out

# # Test creating a category
# def test_create_category(controller, token, capsys):
#     controller.create_category = lambda token, category_name: {'status': 'success', 'category_id': 500}
#     response = controller.create_category(token, 'mekalfone')
#     ConsoleView.display(response)
#     captured = capsys.readouterr()
#     assert 'success' in captured.out
#     assert '500' in captured.out






























# import unittest
# from unittest.mock import MagicMock
# from APIController import APIController  
# from ConsoleView import ConsoleView 
# import json
# from HtmlTestRunner import HTMLTestRunner


# class CustomTestResult(unittest.TextTestResult):
#     def addSuccess(self, test):
#         super().addSuccess(test)
#         self.stream.write(f"SUCCESS: {test}\n")

#     def addError(self, test, err):
#         super().addError(test, err)
#         self.stream.write(f"ERROR: {test}, {err}\n")

#     def addFailure(self, test, err):
#         super().addFailure(test, err)
#         self.stream.write(f"FAILURE: {test}, {err}\n")

# class CustomTextTestRunner(unittest.TextTestRunner):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, resultclass=CustomTestResult, **kwargs)





# class TestAPIController(unittest.TestCase):
#     def setUp(self):
#         # Setup a mock APIController and ConsoleView
#         self.controller = APIController()
#         self.controller.get_courses = MagicMock()
#         self.controller.create_course = MagicMock()
#         self.controller.get_user = MagicMock()
#         self.controller.create_category = MagicMock()
        
#         # ConsoleView.display = MagicMock()
#         self.original_display = ConsoleView.display
#         ConsoleView.display = MagicMock(side_effect=self.print_display)

#         # Common token used for all tests
#         self.token = '6b56aecb50603a843ff19b06b792755a'

    

#     def print_display(self, data):
#         # Function to simulate display and print data
#         print("Display call with:", data)
#         self.original_display(data)  # Call the original method if necessary



#     def test_get_courses(self):
#         # Mock response for get_courses
#         self.controller.get_courses.return_value = {'status': 'success', 'data': ['Course1', 'Course2']}
#         # Simulate calling the actual functionality
#         courses_response = self.controller.get_courses(self.token)
#         # Verify results
#         ConsoleView.display(courses_response)
#         self.controller.get_courses.assert_called_once_with(self.token)
#         ConsoleView.display.assert_called_once_with({'status': 'success', 'data': ['Course1', 'Course2']})

#     def test_create_course(self):
#         # Mock response for create_course
#         self.controller.create_course.return_value = {'status': 'success', 'course_id': 101}
#         # Simulate calling the actual functionality
#         new_course_response = self.controller.create_course(
#             token=self.token,
#             fullname='Mekalfone',
#             shortname='M',
#             categoryid=7
#         )
#         # Verify results
#         ConsoleView.display(new_course_response)
#         self.controller.create_course.assert_called_once_with(
#             token=self.token,
#             fullname='Mekalfone',
#             shortname='M',
#             categoryid=7
#         )
#         ConsoleView.display.assert_called_once_with({'status': 'success', 'course_id': 101})

#     def test_get_user(self):
#         # Mock response for get_user
#         self.controller.get_user.return_value = {'status': 'success', 'username': 'mekalfone'}
#         # Simulate calling the actual functionality
#         user_response = self.controller.get_user(
#             token=self.token,
#             username="mekalfone"
#         )
#         # Verify results
#         ConsoleView.display(user_response)
#         self.controller.get_user.assert_called_once_with(
#             token=self.token,
#             username="mekalfone"
#         )
#         ConsoleView.display.assert_called_once_with({'status': 'success', 'username': 'mekalfone'})

#     def test_create_category(self):
#         # Mock response for create_category
#         self.controller.create_category.return_value = {'status': 'success', 'category_id': 3}
#         # Simulate calling the actual functionality
#         new_category_response = self.controller.create_category(
#             token=self.token,
#             category_name="mekalfone"
#         )
#         # Verify results
#         ConsoleView.display(new_category_response)
#         self.controller.create_category.assert_called_once_with(
#             token=self.token,
#             category_name="mekalfone"
#         )
#         ConsoleView.display.assert_called_once_with({'status': 'success', 'category_id': 3})

# if __name__ == '__main__':
#     # unittest.main()
#     # unittest.main(testRunner=HTMLTestRunner(output='test_reports'))
#     unittest.main(testRunner=CustomTextTestRunner())





























# class TestAPIControllerIntegration(unittest.TestCase):
#     def setUp(self):
#         # Initialize the APIController
#         self.controller = APIController()
#         self.token = '6b56aecb50603a843ff19b06b792755a'  # This token should be valid for your test environment

#         # Assuming ConsoleView.display just prints the output, we don't need to mock it for integration tests
#         # If it does more complex operations, consider what needs to be verified about its behavior

#     def test_get_courses(self):
#         # Assuming get_courses returns a list of courses from the database
#         courses_response = self.controller.get_courses(self.token)
#         # Assert based on expected test data in the database
#         self.assertIn('Course1', courses_response['data'])  # Validate that 'Course1' is part of the response
#         self.assertIn('Course2', courses_response['data'])  # Validate that 'Course2' is part of the response
#         self.assertEqual(courses_response['status'], 'success')

#     def test_create_course(self):
#         # Assuming create_course adds a new course to the database
#         new_course_response = self.controller.create_course(
#             token=self.token,
#             fullname='New Course',
#             shortname='NC',
#             categoryid=1
#         )
#         self.assertEqual(new_course_response['status'], 'success')
#         self.assertTrue('course_id' in new_course_response)  # Check if the course_id is returned

#     def test_get_user(self):
#         # Fetch the user 'mekalfone' from the test database
#         user_response = self.controller.get_user(
#             token=self.token,
#             username="mekalfone"
#         )
#         self.assertEqual(user_response, {'status': 'success', 'username': 'mekalfone'})

#     def test_create_category(self):
#         # Assuming create_category adds a new category to the database
#         new_category_response = self.controller.create_category(
#             token=self.token,
#             category_name="New Category"
#         )
#         self.assertEqual(new_category_response['status'], 'success')
#         self.assertTrue('category_id' in new_category_response)  # Check if the category_id is returned

#     def test_create_category(self):
#         try:
#             new_category_response = self.controller.create_category(
#                 token=self.token,
#                 category_name="New Category"
#             )
#             if new_category_response is None:
#                 self.fail("API returned None. Possible connection issue or server error.")
#             elif not isinstance(new_category_response, dict):
#                 # Log actual response to see what's being returned
#                 self.fail(f"Unexpected response type: {type(new_category_response)}. Response: {new_category_response}")

#             self.assertEqual(new_category_response.get('status'), 'success', f"API call failed, response: {new_category_response}")
#             self.assertIn('category_id', new_category_response, "Response does not contain category_id.")

#         except Exception as e:
#             # Log the exception message
#             self.fail(f"An exception occurred: {e}")

#     def tearDown(self):
#         # Cleanup logic here if necessary
#         # e.g., delete any data added by tests if not handled by transactions
#         pass

# if __name__ == '__main__':
#     unittest.main()



import unittest
from APIController import APIController  
from ConsoleView import ConsoleView 

class TestAPIController(unittest.TestCase):
    def setUp(self):
        # Initialize APIController
        self.controller = APIController()
        
        # Common token used for all tests, ensure this token is valid for live testing
        self.token = '6b56aecb50603a843ff19b06b792755a'
        self.tokens = 'd39ecf70f0e8370ff238bd8cdfcfd014'

    def test_get_courses(self):
        # Call the actual functionality
        courses_response = self.controller.get_courses(self.tokens)
        # Display results
        ConsoleView.display(courses_response)
        # Here, you could assert expected values if known, for example:
        # self.assertIn('Course1', courses_response['data'])

    def test_create_course(self):
        # Call the actual functionality
        new_course_response = self.controller.create_course(
            token=self.token,
            fullname='Mekalfone',
            shortname='MKS',
            categoryid=10
        )
        # Display results
        ConsoleView.display(new_course_response)
        # Assert expected results
        # self.assertEqual(new_course_response['status'], 'success')

    def test_get_user(self):
        # Call the actual functionality
        user_response = self.controller.get_user(
            token=self.token,
            username="mekalfone"
        )
        # Display results
        ConsoleView.display(user_response)
        # Assert expected results
        # self.assertEqual(user_response['status'], 'success')

    def test_create_category(self):
        # Call the actual functionality
        new_category_response = self.controller.create_category(
            token=self.token,
            category_name="mekalfone"
        )
        # Display results
        ConsoleView.display(new_category_response)
        # Assert expected results
        # self.assertEqual(new_category_response['status'], 'success')

if __name__ == '__main__':
    unittest.main()
