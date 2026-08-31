import requests


# ==========================================
# 1. ENTER USERNAMES HERE
# ==========================================

usernames = [
    "ujjwalgupta_2007",
    "instagram",
    "cristiano",
    "nasa"
]


# ==========================================
# 2. SEARCH FUNCTION
# ==========================================

def search_user(username):

    url = f"https://www.instagram.com/{username}/"

    print("\n================================")
    print("Searching:", username)
    print("================================")

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        # ----------------------------------
        # Check website response
        # ----------------------------------

        if response.status_code == 200:

            print("Profile found!")
            print("Username :", username)
            print("URL      :", url)

            return {
                "username": username,
                "url": url,
                "status": "Found"
            }

        elif response.status_code == 404:

            print("Profile not found.")

            return {
                "username": username,
                "url": url,
                "status": "Not Found"
            }

        else:

            print(
                "Instagram returned status:",
                response.status_code
            )

            return {
                "username": username,
                "url": url,
                "status": "Unknown"
            }

    except requests.exceptions.RequestException as error:

        print("Connection error:", error)

        return {
            "username": username,
            "url": url,
            "status": "Error"
        }


# ==========================================
# 3. SEARCH ALL USERNAMES
# ==========================================

results = []

for username in usernames:

    result = search_user(username)

    results.append(result)


# ==========================================
# 4. SHOW FINAL RESULTS
# ==========================================

print("\n\n================================")
print("          FINAL RESULTS")
print("================================")

for result in results:

    print("\nUsername:", result["username"])
    print("URL     :", result["url"])
    print("Status  :", result["status"])
    
    
