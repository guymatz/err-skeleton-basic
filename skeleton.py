# This is a stripped-down skeleton for Err plugins

from errbot import BotPlugin, botcmd
#from errbot.builtins.webserver import webhook


class Skeleton(BotPlugin):
	"""An Err plugin skeleton"""
	#min_err_version = '1.6.0' # Optional, but recommended
	#max_err_version = '2.0.0' # Optional, but recommended

	# Passing split_args_with=None will cause arguments to be split on any kind
	# of whitespace, just like Python's split() does
	@botcmd(split_args_with=None)
	def skeleton(self, mess, args):
		"""A command which simply returns 'Example'"""
		return "Example"

        """ Not currently used
	@webhook
	def example_webhook(self, incoming_request):
		"""A webhook which simply returns 'Example'"""
		return "Example"
        """
