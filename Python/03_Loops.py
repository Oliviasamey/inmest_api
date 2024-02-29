users = [
    {
        "name": "Ben",
        "email": "ben@safety.com",
        "mobille_number": "+2544344343325",
        "lat": 4.24544535465,
        "long":-3.354546545,
        "last_in_distress": "24/01/2024",
        "in_distress": False
        },
    {
        "name": "Suad",
        "email": "suad@safety.com",
        "mobille_number": "+2334344343324",
        "lat": 4.24544535465,
        "long":-3.354546545,
        "last_in_distress": "01/12/2023",
        "in_distress": True
    },
    {
        "name": "Paulo",
        "email": "Paulo@safety.com",
        "mobille_number": "+2334344343324",
        "lat": 4.24544535465,
        "long":-3.354546545,
        "last_in_distress": "24/01/2024",
        "in_distress": False
    }
]

for user in users:
    # print(f"Name: {user.get('name')}, Email: {user.get('email')}")
    if user.get("in_distress") == True:
        print(f"Contacting community for {user.get('name')}...")
        
        
        #closest_users = []
        closest_user = list(filter(
            lambda c_user: c_user.get("lat")== user.get("lat")
            and c_user.get("long")== user.get("long") 
            and c_user.get("email") != user.get("email"),
            users))

        for closest_user in closest_user:
            print(f"Hello {closest_user.get('name')}, you are closer to {user.get('name')}, {user.get('name')} need your help, kindly go and save her")
            print(closest_user)

        #find all users who have the lat and long as user.get("lat") as
        # user.get("lat") and user.get("long")

        #write a for loop to broadcast a message in closest_users.