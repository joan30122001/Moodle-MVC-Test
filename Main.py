from APIController import APIController
from ConsoleView import ConsoleView
import argparse

def main():
#     controller = APIController()
    
#     # Example for retrieving courses
#     token = 'd39ecf70f0e8370ff238bd8cdfcfd014'
#     courses_response = controller.get_courses(token)
#     ConsoleView.display(courses_response)
    
#     # Example for creating a course
#     # new_course_response = controller.create_course(
#     #     token=token,
#     #     fullname='Mon Nouveau Cours',
#     #     shortname='MNC',
#     #     categoryid=2
#     # )
#     # ConsoleView.display(new_course_response)

# if __name__ == "__main__":
#     main()
    parser = argparse.ArgumentParser(description="Test the Moodle API functionalities")
    parser.add_argument('--action', choices=['get_courses', 'create_course', 'get_user', 'create_category'], help='Specify the action to perform')
    args = parser.parse_args()
    
    controller = APIController()
    # token = 'd39ecf70f0e8370ff238bd8cdfcfd014'
    token = '6b56aecb50603a843ff19b06b792755a'

    if args.action == 'get_courses':
        courses_response = controller.get_courses(token)
        ConsoleView.display(courses_response)
    elif args.action == 'create_course':
        new_course_response = controller.create_course(
            token=token,
            fullname='Mekalfone',
            shortname='M',
            categoryid=7
        )
        ConsoleView.display(new_course_response)
    elif args.action == 'get_user':
        user_response = controller.get_user(
            token=token,
            username = "mekalfone"
        )
        ConsoleView.display(user_response)
    elif args.action == 'create_category':
        new_category_response = controller.create_category(
            token=token,
            category_name = "mekalfone"
        )
        ConsoleView.display(new_category_response)

if __name__ == "__main__":
    main()