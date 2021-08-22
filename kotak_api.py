from ks_api_client import ks_api


def initial():
    ip = '127.0.0.1'
    client = ks_api.KSTradeApi(access_token, user_id, consumer_key, ip, app_id)

    login = client.login(password)
    try:
        global otp
        if otp:
            pass
    except Exception as e:
        print('access code is send to your registered mobile no and email id')
        otp=input('enter your access_code(otp)')
        with open('api_data.py','a') as file:
            file.write(f'otp="{otp}"\n')
    session = client.session_2fa(otp)
    print('Response : ',login['Success']['message'])
    return client


try:
    with open('api_data.py', 'x') as file:
        file.write(f'access_token="{input("enter your access_token")}"\n')
        file.write(f'user_id="{input("enter your user_id")}"\n')
        file.write(f'app_id="{input("enter your app_id")}"\n')
        file.write(f'consumer_key="{input("enter your consumer_key")}"\n')
        file.write(f'password="{input("enter your login_password")}"\n')
except:
    from api_data import *
finally:
    from api_data import *


if __name__ == '__main__':
    client=initial()
