HOST = 'imap.googlemail.com'
PORT = 993
SSL = True

OLD_DATA_DIR = 'old_data'
NEW_DATA_DIR = 'new_data'
ALL_FOLDERS_FI = 'all_folders.json'
FOLDER_DATA_FI = 'folder_data.json'

GMAIL_ID_FIELD = 'X-GM-MSGID'
FLAGS_FIELD = 'FLAGS'
FULL_MSG_FIELD = 'RFC822'
MSG_ID_FIELD = 'BODY.PEEK[HEADER.FIELDS (MESSAGE-ID)]'
MSG_ID_KEY = 'BODY[HEADER.FIELDS (MESSAGE-ID)]'
SUBJECT_FIELD = 'BODY.PEEK[HEADER.FIELDS (Subject)]'
SUBJECT_KEY = 'BODY[HEADER.FIELDS (SUBJECT)]'
