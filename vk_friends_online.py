import vk
import getpass
import vk_query


APP_ID = 3712852  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


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
    online_friends = api.execute(code=vk_query.get_online_friends)
    print(online_friends)
    return online_friends


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend)

if __name__ == '__main__':
    #print("Enter login")
    #login = get_user_login()
    #print("Enter password")
    #password = get_user_password()
    friends_online = get_online_friends("", "")
    print(friends_online)
#    output_friends_to_console(friends_online)
