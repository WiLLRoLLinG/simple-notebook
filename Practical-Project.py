import os, time, random

# Class representing a Note with body, tag, and unique ID (UID)
class Note:
    def __init__(self, body, tag, uid):
        self.body = body  # The content of the note
        self.tag = tag    # A label to categorize the note
        self.uid = uid    # Unique identifier for the note

    # Method to display the note's details
    def display(self):
        return f'UID: {self.uid}\nNote: {self.body}\nTag: {self.tag}\n'

# Class representing a node in a linked list
class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node (a Note object)
        self.next = None  # Pointer to the next node in the linked list

# Class representing a Notebook to manage notes
class NoteBook:
    def __init__(self):
        self.head = None  # The first node in the linked list of notes

    # Adds a new note to the notebook
    def add(self, newdata, tag):
        uid = self.generate_uid()  # Generate a unique ID for the new note
        n = Node(Note(newdata, tag, uid))  # Create a new node with the note
        if self.head is None:  # If the list is empty, set the new note as the head
            self.head = n
            print(f"Generated UID for the note: {uid}") 
            return
        t = self.head
        while t.next:  # Traverse to the end of the list
            t = t.next
        t.next = n  # Add the new node at the end of the list
        print(f"Generated UID for the note: {uid}") 

    # Deletes a note by its UID
    def delete_by_id(self, uid):
        t = self.head
        p = None
        if t and t.data.uid == uid:  # If the first note is the one to delete
            self.head = t.next  # Move the head to the next note
            t = None  # Remove the reference to the deleted note
            return f'Note with UID {uid} was the first note and deleted'
        while t and t.data.uid != uid:  # Traverse to find the note with the given UID
            p = t
            t = t.next
        if t is None:  # If the note was not found
            return f'There is no note with UID {uid}'
        p.next = t.next  # Bypass the note to delete it
        t = None  # Remove the reference to the deleted note
        return f'Note with UID {uid} deleted successfully'

    # Deletes notes by their tag
    def delete_by_tag(self, tag):
        t = self.head
        p = None
        while t:  # Traverse through the list
            if t.data.tag == tag:  # If the tag matches
                if t == self.head:  # If the note is the head
                    self.head = t.next  # Move the head to the next note
                    t = None  # Remove the reference to the deleted note
                    return f'Note with tag {tag} deleted'
                else:  # If the note is not the head
                    p.next = t.next  # Bypass the note to delete it
                    t = None  # Remove the reference to the deleted note
                    return f'Note with tag {tag} deleted'
            p = t  # Move to the next note
            t = t.next
        return f'No note with tag {tag} found' 

    # Displays all notes in the notebook
    def show_all(self):
        if self.head is None: 
            print('The Notebook is empty')
            return
        now = self.head
        while now:
            print(now.data.display())
            now = now.next

    # Finds a note by its UID and displays its details
    def find_by_id(self, uid):
        now = self.head
        while now: 
            if now.data.uid == uid: 
                return now.data.display() 
            now = now.next
        return 'Note not found' 

    # Finds notes by their tag and returns their details
    def find_by_tag(self, tag):
        now = self.head
        found_notes = [] 
        while now: 
            if now.data.tag == tag: 
                found_notes.append(now.data.display())  # Add note to the list for display
            now = now.next
        if not found_notes: 
            return 'No notes with this tag'
        return "\n".join(found_notes) 

    # Generates a random unique ID for a new note
    def generate_uid(self):
        uid = random.randint(1, 99999) 
        while self.is_uid_taken(uid):
            uid = random.randint(1, 99999)
        return uid

    # Checks if a UID is already taken
    def is_uid_taken(self, uid):
        now = self.head
        while now: 
            if now.data.uid == uid: 
                return True  # UID is taken
            now = now.next
        return False  # UID is available

# Main function to run the notebook application
def main():
    notebook = NoteBook()  # Create a new notebook
    
    while True:
        print("\n--- Notebook Menu ---")
        print("1. Add a new note")
        print("2. Show all notes")
        print("3. Find note by ID")
        print("4. Find notes by tag")
        print("5. Delete note by ID")
        print("6. Delete note by tag")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        # Process user choice
        if choice == '1': 
            body = input("Enter the note: ") 
            tag = input("Enter the tag: ") 
            notebook.add(body, tag) 
            print("Note added successfully!")
            time.sleep(3)    
            os.system('cls')   
            
        elif choice == '2':  # Show all notes
            os.system('cls')   
            notebook.show_all()
        
        elif choice == '3':  # Find note by ID
            uid = int(input("Enter the UID to find: "))
            result = notebook.find_by_id(uid) 
            os.system('cls')   
            print(result)   
        
        elif choice == '4':  # Find notes by tag
            tag = input("Enter the tag to find: ") 
            result = notebook.find_by_tag(tag)
            os.system('cls')   
            print(result)   
        
        elif choice == '5':  # Delete note by ID
            uid = int(input("Enter the UID to delete: "))
            result = notebook.delete_by_id(uid) 
            os.system('cls')   
            print(result)   
        
        elif choice == '6':  # Delete note by tag
            tag = input("Enter the tag to delete: ") 
            result = notebook.delete_by_tag(tag)
            os.system('cls')   
            print(result)   
        
        elif choice == '7':  # Exit the program
            os.system('cls')   
            print("Exiting the notebook. Goodbye!") 
            time.sleep(2)    
            break
        
        else:  # Invalid choice
            os.system('cls')
            print("Invalid choice, please try again.")    
            time.sleep(2)    
            os.system('cls')

# Run the main function
if __name__ == "__main__":
    main()