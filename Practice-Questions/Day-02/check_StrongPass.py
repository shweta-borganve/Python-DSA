def is_strong_Password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        return False
    return True 

print(is_strong_Password("StrongPass1!"))  # True
print(is_strong_Password("weakpass"))      # False 
