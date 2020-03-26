from errbot import BotPlugin, botcmd

import tweepy


class TweeBot(BotPlugin):
    """Updates twitter status"""

    @botcmd
    def tweet(self, msg, args):
        """Send tweet to the world"""
        auth = tweepy.OAuthHandler(self.config['consumer_key'], self.config['consumer_secret'])
        auth.set_access_token(self.config['access_token'], self.config['access_token_secret'])
        api = tweepy.API(auth)

        try:
            status = api.update_status(args)
            return "Twitter status updated."
        except tweepy.error.TweepError as error:
            return error.response.text

    def get_configuration_template(self):
            return {'consumer_key': 'change me',
                    'consumer_secret': 'change me',
                    'access_token': 'change me',
                    'access_token_secret': 'change me',
                    }
