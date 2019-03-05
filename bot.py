import tweepy, requests
import config

# Getting keys and secrets
consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_key = config.ACCESS_KEY
access_secret = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def fetch_address(msg):
    """ To fetch address from a tweet
    """
    address = ''
    message = msg.split(' ')
    for i in range(len(message)):
        word = message[i]
        if len(word) > 2:
            if word[0] == '0' and word[1] == 'x':
                address = word
                break
    return address

def send_eth(address):
    """ To send eth to someone using faucet
    """
    response = requests.post('http://localhost:3001/faucet', data = {"address": address, "agent": "twitter"})
    return response

def replyToUser(response, msg_id, requestor):
    """ Reply to user according to reposne
    """ 
    if response == 200:
        reply = '@' + str(requestor) + ' x tokens have been transferred to your account'
    elif response == 503:
        reply = '@' + str(requestor) + ' you’ve already requested for tokens in the last 24 hrs' + ' Only one transfer in 24 hours is allowed'
    elif response == 404:
        reply = '@' + str(requestor) + ' something went wrong and we couldn’t transfer tokens to your wallet address.' +  ' Please check address provided and try again later'

    api.update_status(reply, msg_id)

def main():
    # Last 5 mentions
    timeline = api.mentions_timeline(count = 5)
    for i in range(len(timeline)):
        message = timeline[i].text
        requestor = timeline[i].user.screen_name
        msg_id = timeline[i].id
        address = fetch_address(message)
        # print(requestor)
        response = send_eth(address)
        replyToUser(response, msg_id, requestor)

if __name__ == '__main__':
    main()