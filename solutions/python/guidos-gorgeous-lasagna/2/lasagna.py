EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_in_oven):
    """Return the remaining baking time in minutes."""
    return 40 - time_in_oven

def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time in minutes based on the number of layers."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total elapsed time in minutes."""
    return number_of_layers * 2 + elapsed_bake_time