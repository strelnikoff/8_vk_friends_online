import vk
import getpass


APP_ID = 3712852


def get_user_login():
    return input()


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api = vk.API(session)
    online_friends = api.execute(code=vk_query.get_online_friends,v="5.60")
    return online_friends


if __name__ == '__main__':
    print("Enter login")
    login = get_user_login()
    print("Enter password")
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print(friends_online)
