
import requests ,json
from api_data import *
from ks_api_client import ks_api



client = ks_api.KSTradeApi(access_token, user_id, consumer_key, ip, app_id)


def login(client,consumer_key,access_token,app_id,user_id,password):
    headers={'accept':'application/json','consumerKey':consumer_key,'ip':'127.0.0.1','appId':app_id,'Content-Type':'application/json','Authorization':"Bearer "+access_token}
    data=json.dumps({'userid':user_id,'password':password})
    response= requests.post("https://tradeapi.kotaksecurities.com/apim/session/1.0/session/login/userid",headers=headers,data=data).json()
    url = "https://tradeapi.kotaksecurities.com/apim/session/1.0/session/2FA/oneTimeToken"
    headers["oneTimeToken"] = response['Success']['oneTimeToken']
    client.one_time_token=headers['oneTimeToken']
    data = json.dumps({"userid":user_id})
    resp = requests.post(url, headers=headers, data=data).json()
    client.session_token=resp['success']['sessionToken']
    print("Session Token ",client.session_token)
    print("Loged In  Successfully")
    return client

def get_margin(client):
    headers={'accept':'application/json','consumerKey':f"{client.consumer_key}",'Authorization':"Bearer "+client.access_token,"sessionToken":f"{client.session_token}"}
    api_response= requests.get("https://tradeapi.kotaksecurities.com/apim/margin/1.0/margin",headers=headers).text
    print(api_response)
    return api_response

login(client,consumer_key,access_token,app_id,user_id,password)
get_margin(client)