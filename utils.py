# Libraries
import imapclient

# Local imports
import constants


def login_to_server(username, password):
  server = imapclient.IMAPClient(constants.HOST, port=constants.PORT,
                                 ssl=constants.SSL, use_uid=True)
  server.login(username, password)
  return server
