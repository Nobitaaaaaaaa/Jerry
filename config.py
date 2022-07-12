from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18005200"))
API_HASH = getenv("API_HASH", "ddc99b20d72ff77da2cbd576fbe31027")
BOT_TOKEN = getenv("BOT_TOKEN","5506903401:AAHlf0f-0gfjHXChYujK5y8jVhB1-7oq40o")
BOT_NAME = getenv("BOT_NAME","Tom")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
SESSION_NAME = getenv("SESSION_NAME", "BQCpe2WzN73ZVetMp_zf6Q9pVhpMgr12Pg17uVJz02-XAQrHOxeq8b4LmfzIj9gZkeL8tEhnk77Tl_2vWxkCRwznEtGiHSipu442evLZWghsgYn77I3OvnnXRHI0t7o0wSPzZTdcwWAILMHtyxuJF7mcRffyfEsTSZTksNfamInyw8E4McA4-_fK-bwzbzNwUQ_jHZrRi1qPW6KEMN8wH-o3Lb8La0kgi4OuxanW1ngF82xp_fIgOkWOGCKqvd88NNHcmXAMBfUl2fePLKsZejlNE7UyBIso6znQtuc1c_mXq7p2yLzmt_HnSj92KNQl3sp07ajPymAfhDYyvkNYLRmgAAAAAFEaDzwA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1504404866").split()))
