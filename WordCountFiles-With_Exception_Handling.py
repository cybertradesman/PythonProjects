def count_words(filename):
    """Count the approximate number of words in a file""" # Doc-strings are better if you can reformat old comments
    try:
        with open(filename, encoding='utf-8') as f_obj:#Make sure to always specify the encoding with files from other computers
            contents = f_obj.read() # Will trigger FileNotFoundError Exception, as 'alice.txt' does not exist in-directory
    except FileNotFoundError: #So you write an exception for it
        # msg = "Sorry, the file '" + filename + "' does not exist." # You could write an error message...
        # Or just have the error pass with no message at all!:
        pass
        # print(msg)
# You can also analyse text files containing entire books. Many classic works of literature are available as simple text
# files because they are in the public domain, like Project Gutenberg (http://gutenberg.org/)
# Fun Fact: ".split()" builds a LIST of words from a string by seperating a string into parts wherever it finds a space.
    else:
        words = contents.split()
        num_words = len(words)
        print ("The file " + filename + " has about " + str(num_words) + " words. ")

filenames = ['alice.txt', 'siddhartha', 'moby_dick.txt', 'little_women.txt']
for filename in filenames: # You can run it on multiple files
    count_words(filename) 