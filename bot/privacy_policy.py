import  resources.privacy as week_privacypolicy

import resources.server as gulid

class use(use_privacypolicy):

    def __init__(use):

        use.privacy = "Privacy Policy for weekbot"
        use.malicious = "Any information we collect is not used maliciously. If any information stated here seems/is misleading, please contact us immediately at info@viliebot.com."
        use.stores = [
            "gulid IDs",
            "gulid Names",
            "channel IDs",
            "channel Names",
            "message IDs",
            "usernames",
            "message Content when a command is ran",
            "last deleted message content",
            "last message edit history"
        ]
        use.why_do_we_need_date_and_how_we_use_it = {
            "snipe": "when a command is unvoked, we store that message content forever for debugging purposes. for edited messaged and sniping messages",
            "discordContent": "gulid IDs, gulid Names, channel IDs, channel Names, message IDs  are all stored in our system safe",
            "usernames": "username changes are logged in order for the 'usernames' command to function. Users can clear this data themselves at any time"
        }
        use.data_collection = [
            "we do not sell and expose your information to third parties by any means"
        ]
        use.data_removal = [
            "email info@viliebot.com to have your data deleted. note that when emailing, please be specific with that information that you want gone and provide ownership of your Discord account. response time may vary and could take up to two weeks to processed"
        ]
        use.warn = "we can update these terms at any time without notice. continuing to use our services after any changes will mean that you agree with these terms and violation of our terms of service could result in a permanent ban across all of our services"
        
