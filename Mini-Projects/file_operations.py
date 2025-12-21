import os
import datetime
from datetime import datetime

# File Interaction Manager
# A CLI-based program for creating, reading, writing, searching, and deleting files and content.
# Provides an interactive interface for common file operations with user confirmations for destructive actions.

# Notable features:
#   - Object-oriented design using File class to encapsulate file metadata
#   - os.walk() for recursive directory traversal when searching for files across folder structures
#   - Context managers (with open()) for safe file handling with automatic resource cleanup
#   - Case-sensitive and case-insensitive search capabilities for flexible text matching
#   - File metadata tracking (name, content, size) synchronized with disk operations
#   - Interactive operation menu with single-character command shortcuts
#   - Confirmation prompts before executing destructive operations (overwrites, deletions)

# Necessary Improvements / Known Limitations
#
# The following items document immediate technical limitations identified during development. These are intentionally noted
# as part of the learning process and reflect areas that require correction for full correctness or robustness.
#
# - File Deletion Logic:
#   The delete operation is currently bound to the active File object rather than resolving the filename explicitly provided
#   by the user. This may result in unintended file deletion and should be corrected to ensure user-specified targets are used.
#
# - File Existence Handling:
#   The program assumes the target file exists during File object initialization. Attempting to open a non-existent file will
#   raise an exception. A validation check should precede file access to handle this case safely.
#
# - Recursive Menu Flow:
#   User re-prompting is handled through recursive function calls. While functional for limited use, this approach is not ideal 
#   for long-running programs and should be replaced with an iterative loop-based control structure.
#
# - Stale File State:
#   File metadata (content and size) is cached at initialization and may become outdated following write or append operations.
#   A refresh mechanism should be implemented to resync the object state with the filesystem.
#
# These limitations are acknowledged intentionally to document learning progression rather than 
# to present a fully polished implementation.


# Possible improvements:
#   - Implement specific exception handling (FileNotFoundError, PermissionError) instead of bare except blocks
#   - Add input validation for file names (empty strings, invalid characters, path traversal prevention)
#   - Extract confirmation logic into a reusable helper function to reduce code duplication
#   - Replace magic strings ('c', 'r', 'w') with named constants or enums for better maintainability
#   - Add base case protection for recursive operation() calls to prevent stack overflow
#   - Refactor File class to use properties that read fresh data from disk rather than caching potentially stale values
#   - Implement proper logging instead of print statements for better debugging and monitoring
#   - Add support for relative and absolute file path handling using pathlib module
#   - Consider separating concerns: File class for data model, separate functions for I/O operations, and UI logic in operation()

class File():

    def __init__(self, name, content, size):
        self.name: str = name
        self.content: str = content
        self.size: int = size
    
def create(file_name, content):
    try:
        with open(file_name, 'x') as file:
            file.write(f"Created at {datetime.now()} \n\n {content}")
    except:
        return f"We were not able to create the file {file_name} at this time. \n"

    return f"The creation of the file '{file_name}' was successful. \n"

def read(file): return file.content

def searchPhrase(file, item, sensitive):
    if not sensitive:
        file.content = file.content.lower()
        item = item.lower()
    
    if len(item) <= 1:
        chars = file.content

        for index, char in enumerate(chars):
            if char == item:
                return f"Found '{char}' at index {index} \n"
    else:
        phrases = file.content.split()

        for index, phrase in enumerate(phrases):
            if phrase == item:
                return f"Found '{phrase}' at index {index} \n"
        
    
    return f"'{item}' was not found in the file \n"

def searchFile(file_name):
    for root, dirs, files in os.walk('.'):  # os.walk returns 3 values: root, directories, files
        if file_name in files:
            return os.path.join(root, file_name)
    
    return None

def iterations(file, item, sensitive):
    count = 0

    if not sensitive:
        file.content = file.content.lower()
        item = item.lower()

    if len(item) <= 1:
        chars = file.content

        for char in chars:
            if char == item:
                count += 1
    else:
        phrases = file.content.split()

        for phrase in phrases:
            if phrase == item:
                count += 1
            
    return count

def write(file, content):
    try:
        with open(file.name, 'w') as f:
                f.write(content)

        # Updates the fileobject's content and size
        file.content = content
        file.size = os.path.getsize(file.name)
    except:
        return print(f"{write.__name__.capitalize()} was unable to be performed at this time. \n")

    return "Your write was successful. \n"

def append(file, content):
    try:
        with open(file.name, 'a') as f:
                f.write(content)

        # Updates the fileobject's content and size
        file.content += content  # Append to existing content
        file.size = os.path.getsize(file.name)
    except:
        return f"{append.__name__.capitalize()} was unable to be performed at this time. \n"
    
    return "Your append was successful. \n"

def deleteItem(file, item):
    try:
        # str.replace() returns a new string, doesn't modify in-place
        file.content = file.content.replace(item, '')

        with open(file.name, 'w') as f:
                f.write(file.content)

        # Updates the fileobject's size
        file.size = os.path.getsize(file.name)
    except:
        return f"We were unable to delete '{item}' from '{file.name}' at this time. \n"
    
    return f"The deletion of '{item}' from '{file.name}' was successfull. \n"


def deleteFile(file):
    os.remove(file.name)

    return f"The deletion of file '{file.name}' was successful. \n"

def operation(file):
    action = input("What action would you like to perform? create('c'), read('r'), write('w'), append('a'), search('s'), iterations('i'), or delete('d')? \n")

    if action == 'c':
        file_name = input("What is the name of the file you'd like to create? \n")

        write_create = input("Would you like to write to the file during its creation? Y/n \n").lower()

        if write_create == 'y':
            content = input("What would you like write to the file? \n")

            result = create(file_name, content)
        else: result = create(file_name, '')    
    elif action == 'r':
        result = read(file)
    elif action == 'w':
        confirm = input("This action will overwrite the file you are currently accessing. Would you like to proceed with this request? Y/n \n").lower()
        if confirm == 'y':
            content = input("What would you like to write to the file? \n")

            result = file.write(file, content)
        else: result = operation(file)
    elif action == 'a':
        content = input("What would you like to write to the file? \n")

        result = append(file, content)
    elif action == 's':
        query = input("Are you searching for an item or a file? \n").lower()

        if query == 'file':
            file_name = input("What is the name of the file you are searching for? \n")

            result = f"The file '{file_name}' was found at '{searchFile(file_name)}'. \n"
        else:
            item = input("What item are you searching for? \n")

            # Asks the user if the searh is case sensitive
            if input("Is this search case sensitive? Y/n \n").lower() == 'y': sensitive = True 
            else: sensitive = False

            result = searchPhrase(file, item, sensitive)
    elif action == 'i':
        item = input("What item are you searching for? \n")

        # Asks the user if the searh is case sensitive
        if input("Is this search case sensitive? Y/n \n").lower() == 'y': sensitive = True 
        else: sensitive = False

        result = iterations(file, item, sensitive)
    elif action == 'd':
        object_type = input("What type of object would you like to delete? file('f') or phrase ('p') \n")

        if object_type == 'f':
            file_name = input("What is the name of the file you would like to delete? \n")

            confirmation = input(f"You are about to delete the file {file_name}. Are you sure? Y/n \n").lower()

            if confirmation == 'y':
                try:
                    result = deleteFile(file)
                except:
                    result = f"The deletion of file '{file_name}' was unsuccessful. \n"
            else:
                result = operation(file)  # Recursive call - capture its return value
        else:
            item = input("What phrase would you like to delete? \n")

            confirmation = input(f"You are about to delete '{item}' from the file. Are you sure? Y/n \n").lower()
            
            if confirmation == 'y':
                try:
                    result = deleteItem(file, item)
                except:
                    result = f"The deletion of item '{item}' was unsuccessful. \n"
            else:
                result = operation(file)  # Recursive call - capture its return value
    else:
        result = "We were unable to take that action at this time. \n"

    return result


def main():
    file_name = input("Enter the name of the file you'd like to interact with: ")

    file = File(file_name, open(file_name).read(), os.path.getsize(file_name))
    
    print(operation(file))

if __name__ == "__main__":
    main()