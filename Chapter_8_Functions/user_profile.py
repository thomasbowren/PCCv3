def main():
    user_profile = build_profile('thomas', 'bowren', middle='lee', city='searcy', state='ar', field='computer science')
    for profile, attribute in user_profile.items():
        print(f"{profile.title()}: {attribute.title()}")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

if __name__ == "__main__":
    main()