from pathlib import Path
import json

def main():
    path = Path('username.json')
    contents = path.read_text()
    formatted_user = json.loads(contents)
    user = dict(formatted_user)
    greet_user(path, user)
    print("username.json contains the following user info:")
    print(path.read_text())

def greet_user(path, user):
    if path.exists():
        if user['name']:
            print(f"Hello, {user['name']}", end='')
        else:
            name = get_username()
            user['name'] = name
            print(f"Hello, {user['name']}", end='')
            path.write_text(user['name'])
        if user['age']:
            print(f"Congratulations on your {user['age']} years in life!", end='')
        else:
            age = get_age()
            user['age'] = age
            print(f"Congratulations on your {user['age']} years in life!", end='')
            path.write_text(user['age'])
        if user['occupation']:
            print(f"The world can always use more {user['occupation']} like you.", end='')
        else:
            occupation = get_occupation()
            user['occupation'] = occupation
            print(f"The world could always use more {user['occupation']} like you.", end='')
            path.write_text(user['occupation'])
    else:
        name = get_username()
        user['name'] = name
        age = get_age()
        user['age'] = age
        occupation = get_occupation()
        user['occupation'] = occupation
        path.write_text(str(user))
        print(f"Hello, {user['name']}. Congratulations on your {user['age']} years in life! The world could always use more {user['occupation']}s like you.")

def get_username():
    name = input("Username: ")
    formatted_name = json.dumps(name)
    return formatted_name

def get_age():
    age = input("Age: ")
    formatted_age = json.dumps(age)
    return formatted_age

def get_occupation():
    occupation = input("Occupation: ")
    formatted_occupation = json.dumps(occupation)
    return formatted_occupation

if __name__ == "__main__":
    main()