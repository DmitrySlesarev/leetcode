import pprint

print = pprint.pprint

user_data = {
    "id": 10293,
    "profile": {"name": "Alex", "role": "Admin", "verified": True},
    "activity_log": ["login", "update_profile", "logout"],
    "preferences": {"theme": "dark", "notifications": {"email": True, "sms": False}}
}

print(user_data)