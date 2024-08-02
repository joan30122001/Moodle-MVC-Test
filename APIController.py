from MoodleAPI import MoodleAPI

class APIController:
    def request_moodle(self, **params):
        query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
        url = f"http://digitalschool.freehostia.com/webservice/rest/server.php?{query_string}"
        php_code = f"""
        <?php
        $curl = curl_init();
        curl_setopt_array($curl, array(
          CURLOPT_URL => '{url}',
          CURLOPT_RETURNTRANSFER => true,
          CURLOPT_ENCODING => '',
          CURLOPT_MAXREDIRS => 10,
          CURLOPT_TIMEOUT => 0,
          CURLOPT_FOLLOWLOCATION => true,
          CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
          CURLOPT_CUSTOMREQUEST => 'GET',
          CURLOPT_HTTPHEADER => array(
            'Content-Type: application/x-www-form-urlencoded',
            'Authorization: Basic bWVrYWxmb25lOg==',
            'Cookie: MoodleSession=qeca1cvcnu4fnb8v3b168frhlr'
          ),
        ));
        $response = curl_exec($curl);
        curl_close($curl);
        echo $response;
        ?>
        """
        return MoodleAPI.execute_php(php_code)

    def get_courses(self, token):
        return self.request_moodle(wstoken=token, wsfunction='core_course_get_courses_by_field', moodlewsrestformat='json')

    def create_course(self, token, fullname, shortname, categoryid):
        return self.request_moodle(
            wstoken=token,
            wsfunction='core_course_create_courses',
            moodlewsrestformat='json',
            **{f'courses[0][{key}]': value for key, value in {'fullname': fullname, 'shortname': shortname, 'categoryid': categoryid}.items()}
        ) 
    def get_user(self, token, username):
        return self.request_moodle(
            wstoken=token,
            wsfunction='core_user_get_users_by_field',
            moodlewsrestformat='json',
            field='username',
            **{'values[0]': username}
        )
    def create_category(self, token, category_name):
        return self.request_moodle(
            wstoken=token,
            wsfunction='core_course_create_categories',
            moodlewsrestformat='json',
            **{'categories[0][name]': category_name}
        )
    def update_user(self, token, userid, email, firstname):
        return self.request_moodle(
        wstoken=token,
        wsfunction='core_user_update_users',
        moodlewsrestformat='json',
        **{f'users[0][{key}]': value for key, value in {'id': userid, 'email': email, 'firstname': firstname}.items()}
    )