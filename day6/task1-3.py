def check_password(criteria_type, min_length, password):
    if not isinstance(criteria_type, str):
        raise ValueError("Criteria type must be a string")

    if not isinstance(min_length, int) or min_length < 0:
        raise ValueError("Minimum length must be a non-negative integer")

    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    
    if criteria_type == "lower":
        lowercase_count = 0
        for char in password:
            if char.islower():
                lowercase_count += 1
        return lowercase_count >= min_length

    elif criteria_type == "special":
        special_characters = "!@#$%^&*()_+[]{}|;:,.<>?`~"
        special_count = 0
        for char in password:
            if char in special_characters:
                special_count += 1
        return special_count >= min_length

    else:
        raise ValueError("Invalid criteria type")  # Invalid criteria_type

result_lower = check_password("lower", "e", "mysecretpassword")
result_special = check_password("special", 2, "mysecretpassword")

print(f"Password meets lowercase criteria: {result_lower}")
print(f"Password meets special character criteria: {result_special}")
print(ValueError)
