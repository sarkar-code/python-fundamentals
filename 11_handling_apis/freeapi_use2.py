# PRACTICE CODE FOR API HANDLING

import requests

def fetch_random_book_data():
    url = "https://api.freeapi.app/api/v1/public/books/39"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_data = data["data"]
        eTAG = book_data["etag"]
        version = book_data["volumeInfo"]["contentVersion"]
        view_ability = book_data["accessInfo"]["viewability"]
        return eTAG, version, view_ability
    else:
        raise Exception("Failed to fetch book data")
    

def main():
    try:
        eTAG, version, view_ability = fetch_random_book_data()
        print(f"eTAG: {eTAG} \nVersion: {version} \nView_possibility: {view_ability}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()