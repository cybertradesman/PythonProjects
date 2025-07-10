filename = 'prrogramming.txt' # In the future, Write an input statement to ask the name of the file to write to

with open(filename, 'w') as file_object: # open() automatically creates the file if it doesn't already exist
    file_object.write("I love programming.\n") # In the future, use input statements to enter whatever it is you want to write to a file from this one
    file_object.write("I love creating new games.\n")
    # Including new lines in your write() statements makes each string appear on its own line

    # To Add Content to a file instead of overwriting it, you simply open the file in APPEND MODE.
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


