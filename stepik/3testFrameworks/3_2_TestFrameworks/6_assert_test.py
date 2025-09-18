# assert example
import self

assert abs(-42) == 42, "Should be absolute value of a number"

# print the text with .format
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# print the text with f-strings
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# assert example with descriotion text
catalog_text = "каталог" # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"