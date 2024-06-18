import subprocess
import os
import json

class MoodleAPI:
    # @staticmethod
    # def execute_php(php_code):
    #     with open('temp.php', 'w') as f:
    #         f.write(php_code)
    #     try:
    #         output = subprocess.run(['php', 'temp.php'], capture_output=True, text=True)
    #         return json.loads(output.stdout)
    #     finally:
    #         os.remove('temp.php')


    @staticmethod
    def execute_php(php_code):
        with open('temp.php', 'w') as f:
            f.write(php_code)
        try:
            output = subprocess.run(['php', 'temp.php'], capture_output=True, text=True)
            # Debugging line
            # print("PHP Output:", output.stdout)  
            return json.loads(output.stdout)
        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)
            print("PHP Output causing error:", output.stdout)  # Output that caused the error
            return None  # Return None or handle as appropriate
        finally:
            os.remove('temp.php')
