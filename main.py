import os
from notice import get_notice
from db import save_to_db
from dotenv import load_dotenv

load_dotenv(verbose=True)

URL = os.getenv('URL')
def main():
    notices = get_notice(URL)
    save_to_db(notices)
    
    return

if __name__ == "__main__":
    main()