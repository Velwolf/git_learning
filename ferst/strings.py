def recursive(value):
    print(value)
    if value < 4:
        recursive(value + 1)

recursive(1)
