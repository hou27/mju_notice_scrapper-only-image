from notice import get_notice
from db import save_to_db

URL = 'https://www.mju.ac.kr/mjukr/257/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNDMlMkZhcnRjbExpc3QuZG8lM0ZiYnNDbFNlcSUzRCUyNmJic09wZW5XcmRTZXElM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZpc1ZpZXclM0R0cnVlJTI2c3JjaENvbHVtbiUzRHNqJTI2c3JjaFdyZCUzRCVFQyVBMCU4NCVFQSVCMyVCQyUyNg%3D%3D'
def main():
    notices = get_notice(URL)
    save_to_db(notices)
    
    return

if __name__ == "__main__":
    main()