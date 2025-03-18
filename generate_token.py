import tweepy

# Replace these with your API keys from api_keys_new.txt
api_key = "MISel9QhYlYpVuHM8UKes17cw"
api_secret = "CWRJFjcpDsSv83nGvkgBRfLdCykaNsQUiH4SlhwsjQVGoquKlN"

# Set up OAuth 1.0a handler
auth = tweepy.OAuthHandler(api_key, api_secret)

# Get the request token
try:
    redirect_url = auth.get_authorization_url()
    print("OAuth Token:", auth.request_token['oauth_token'])
    print("Visit this URL to authorize:", redirect_url)
    print("After authorizing on X, you’ll get a PIN code. Enter it here.")
    verifier = input("Enter the PIN code: ")
    auth.get_access_token(verifier)
    print("Access Token:", auth.access_token)
    print("Access Token Secret:", auth.access_token_secret)
    print("Verified X Handle:", "@" + auth.get_username())
except tweepy.TweepyException as e:
    print("Error:", e)
