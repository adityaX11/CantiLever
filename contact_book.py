# import json
# import os
# import tkinter as tk
# from tkinter import ttk, messagebox, simpledialog
# from datetime import datetime
# import re

# class Contact:
#     """Represents a contact with all necessary information."""
    
#     def __init__(self, name, phone, email="", address="", notes=""):
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address
#         self.notes = notes
#         self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     def to_dict(self):
#         """Convert contact to dictionary for JSON storage."""
#         return {
#             'name': self.name,
#             'phone': self.phone,
#             'email': self.email,
#             'address': self.address,
#             'notes': self.notes,
#             'created_date': self.created_date,
#             'last_modified': self.last_modified
#         }
    
#     @classmethod
#     def from_dict(cls, data):
#         """Create contact from dictionary."""
#         contact = cls(data['name'], data['phone'], data.get('email', ''), 
#                      data.get('address', ''), data.get('notes', ''))
#         contact.created_date = data.get('created_date', '')
#         contact.last_modified = data.get('last_modified', '')
#         return contact
    
#     def update(self, **kwargs):
#         """Update contact fields."""
#         for key, value in kwargs.items():
#             if hasattr(self, key):
#                 setattr(self, key, value)
#         self.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     def __str__(self):
#         return f"{self.name} - {self.phone}"

# class ContactBook:
#     """Main contact book class that manages contacts and file operations."""
    
#     def __init__(self, filename="contacts.json"):
#         self.filename = filename
#         self.contacts = []
#         self.load_contacts()
    
#     def add_contact(self, name, phone, email="", address="", notes=""):
#         """Add a new contact."""
#         # Validate input
#         if not name.strip() or not phone.strip():
#             raise ValueError("Name and phone number are required.")
        
#         # Check for duplicate phone numbers
#         if any(contact.phone == phone for contact in self.contacts):
#             raise ValueError("A contact with this phone number already exists.")
        
#         contact = Contact(name.strip(), phone.strip(), email.strip(), 
#                         address.strip(), notes.strip())
#         self.contacts.append(contact)
#         self.save_contacts()
#         return contact
    
#     # def get_contact_by_phone(self, phone):
#     #     """Get contact by phone number."""
#     #     for contact in self.contacts:
#     #         if contact.phone == phone:
#     #             return contact
#     #     return None
#     def get_contact_by_phone(self, phone):
#         """Get contact by phone number."""
#         phone = phone.strip()
#         for contact in self.contacts:
#            if contact.phone.strip() == phone:
#             return contact
#         return None

    
#     def search_contacts(self, query):
#         """Search contacts by name, phone, or email."""
#         query = query.lower()
#         results = []
#         for contact in self.contacts:
#             if (query in contact.name.lower() or 
#                 query in contact.phone or 
#                 (contact.email and query in contact.email.lower())):
#                 results.append(contact)
#         return results
    
#     def update_contact(self, phone, **kwargs):
#         """Update an existing contact. If phone is changed, update the phone field in the contact object."""
#         contact = self.get_contact_by_phone(phone)
#         if contact:
#             # If phone is being updated, update the contact's phone field
#             new_phone = kwargs.get('phone')
#             if new_phone and new_phone != contact.phone:
#                 # Check for duplicate phone
#                 if any(c.phone == new_phone for c in self.contacts):
#                     raise ValueError("A contact with this phone number already exists.")
#                 contact.phone = new_phone
#             # Update all other fields
#             contact.update(**kwargs)
#             self.save_contacts()
#             return contact
#         return None
    
#     def delete_contact(self, phone):
#         """Delete a contact by phone number."""
#         contact = self.get_contact_by_phone(phone)
#         if contact:
#             self.contacts.remove(contact)
#             self.save_contacts()
#             return True
#         return False
    
#     def get_all_contacts(self):
#         """Get all contacts sorted by name."""
#         return sorted(self.contacts, key=lambda x: x.name.lower())
    
#     def load_contacts(self):
#         """Load contacts from JSON file."""
#         try:
#             if os.path.exists(self.filename):
#                 with open(self.filename, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#                     self.contacts = [Contact.from_dict(contact_data) for contact_data in data]
#         except (json.JSONDecodeError, FileNotFoundError):
#             self.contacts = []
    
#     def save_contacts(self):
#         """Save contacts to JSON file."""
#         try:
#             with open(self.filename, 'w', encoding='utf-8') as file:
#                 json.dump([contact.to_dict() for contact in self.contacts], 
#                          file, indent=2, ensure_ascii=False)
#         except Exception as e:
#             raise Exception(f"Error saving contacts: {e}")
    
#     def get_statistics(self):
#         """Get contact book statistics."""
#         total_contacts = len(self.contacts)
#         contacts_with_email = len([c for c in self.contacts if c.email])
#         contacts_with_address = len([c for c in self.contacts if c.address])
#         return {
#             'total_contacts': total_contacts,
#             'contacts_with_email': contacts_with_email,
#             'contacts_with_address': contacts_with_address
#         }

# class ContactBookGUI:
#     """GUI interface for the contact book using Tkinter."""
    
#     def __init__(self, contact_book):
#         self.contact_book = contact_book
#         self.root = tk.Tk()
#         self.root.title("Contact Book")
#         self.root.geometry("800x600")
#         self.root.configure(bg='#f0f0f0')
        
#         # Style configuration
#         style = ttk.Style()
#         style.theme_use('clam')
        
#         self.setup_ui()
#         self.refresh_contact_list()
    
#     def setup_ui(self):
#         """Setup the user interface."""
#         # Main frame
#         main_frame = ttk.Frame(self.root, padding="10")
#         main_frame.grid(row=0, column=0, sticky="nsew")
        
#         # --- GUI Responsiveness Fixes ---
#         # Ensure all columns and rows expand as window resizes
#         self.root.columnconfigure(0, weight=1)
#         self.root.rowconfigure(0, weight=1)
#         main_frame.columnconfigure(0, weight=0)  # Buttons column
#         main_frame.columnconfigure(1, weight=1)  # List column
#         main_frame.rowconfigure(0, weight=0)     # Title row
#         main_frame.rowconfigure(1, weight=1)     # Main content row
#         main_frame.rowconfigure(2, weight=0)     # Search row

#         # For search_frame
#         search_frame = ttk.Frame(main_frame)
#         search_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="we")
#         search_frame.columnconfigure(0, weight=0)
#         search_frame.columnconfigure(1, weight=1)

#         # For list_frame
#         list_frame = ttk.Frame(main_frame)
#         list_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))
#         list_frame.columnconfigure(0, weight=1)
#         list_frame.rowconfigure(0, weight=1)
        
#         # Treeview for contacts
#         columns = ('Name', 'Phone', 'Email', 'Address')
#         self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
#         # Configure columns
#         for col in columns:
#             self.tree.heading(col, text=col)
#             self.tree.column(col, width=150)
        
#         # Scrollbar
#         scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
        
#         self.tree.grid(row=0, column=0, sticky="nsew")
#         scrollbar.grid(row=0, column=1, sticky="ns")
        
#         # Title
#         title_label = ttk.Label(main_frame, text="Contact Book", 
#                                font=('Arial', 16, 'bold'))
#         title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
#         # Buttons frame
#         buttons_frame = ttk.Frame(main_frame)
#         buttons_frame.grid(row=1, column=0, sticky="nw", padx=(0, 10))
        
#         # Buttons
#         ttk.Button(buttons_frame, text="Add Contact", 
#                   command=self.add_contact_dialog).grid(row=0, column=0, pady=5, sticky=tk.W)
#         ttk.Button(buttons_frame, text="Edit Contact", 
#                   command=self.edit_contact_dialog).grid(row=1, column=0, pady=5, sticky=tk.W)
#         ttk.Button(buttons_frame, text="Delete Contact", 
#                   command=self.delete_contact_dialog).grid(row=2, column=0, pady=5, sticky=tk.W)
#         ttk.Button(buttons_frame, text="Search", 
#                   command=self.search_dialog).grid(row=3, column=0, pady=5, sticky=tk.W)
#         ttk.Button(buttons_frame, text="View Statistics", 
#                   command=self.show_statistics).grid(row=4, column=0, pady=5, sticky=tk.W)
        
#         # Search entry
#         ttk.Label(search_frame, text="Quick Search:").grid(row=0, column=0, padx=(0, 5))
#         self.search_var = tk.StringVar()
#         self.search_var.trace('w', self.on_search_change)
#         search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=40)
#         search_entry.grid(row=0, column=1, sticky="we")
        
#         # Bind double-click event
#         self.tree.bind('<Double-1>', self.on_contact_double_click)
    
#     def refresh_contact_list(self, contacts=None):
#         """Refresh the contact list display and keep Treeview in sync with backend.
#         Always clear selection after refresh to avoid stale selection issues when phone numbers change."""
#         # Clear existing items
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         # Add contacts
#         if contacts is None:
#             contacts = self.contact_book.get_all_contacts()
#         for contact in contacts:
#             self.tree.insert('', 'end', values=(
#                 contact.name,
#                 contact.phone,
#                 contact.email,
#                 contact.address
#             ))
#         # Always clear selection after refresh
#         self.tree.selection_remove(self.tree.selection())
    
#     def on_search_change(self, *args):
#         """Handle search input changes."""
#         query = self.search_var.get().strip()
#         if query:
#             results = self.contact_book.search_contacts(query)
#             self.refresh_contact_list(results)
#         else:
#             self.refresh_contact_list()
    
#     # def get_selected_contact(self):
#     #     """Get the currently selected contact. Returns None and shows a warning if nothing is selected or if the contact is not found."""
#     #     selection = self.tree.selection()
#     #     if not selection:
#     #         messagebox.showwarning("No Selection", "Please select a contact first.")
#     #         return None
#     #     item = self.tree.item(selection[0])
#     #     if not item or not item.get('values') or len(item['values']) < 2:
#     #         messagebox.showwarning("Selection Error", "Could not retrieve contact details from selection.")
#     #         return None
#     #     phone = item['values'][1]  # Phone is in the second column
#     #     contact = self.contact_book.get_contact_by_phone(phone)
#     #     if not contact:
#     #         messagebox.showwarning("Not Found", "Selected contact could not be found.")
#     #     return contact

#     def get_selected_contact(self):
#         """Get the currently selected contact. Returns None and shows a warning if nothing is selected or if the contact is not found."""
#         selection = self.tree.selection()
#         if not selection:
#             messagebox.showwarning("No Selection", "Please select a contact first.")
#             return None
#         item = self.tree.item(selection[0])
#         if not item or not item.get('values') or len(item['values']) < 2:
#             messagebox.showwarning("Selection Error", "Could not retrieve contact details from selection.")
#             return None
#         phone = str(item['values'][1]).strip()  # FIXED: Strip to ensure matching
#         contact = self.contact_book.get_contact_by_phone(phone)
#         if not contact:
#             messagebox.showwarning("Not Found", "Selected contact could not be found.")
#         return contact


#     def add_contact_dialog(self):
#         """Show dialog to add a new contact."""
#         dialog = ContactDialog(self.root, "Add New Contact")
#         self.root.wait_window(dialog.dialog)  # Wait for dialog to close
#         if dialog.result:
#             try:
#                 self.contact_book.add_contact(**dialog.result)
#                 self.refresh_contact_list()
#                 self.tree.selection_remove(self.tree.selection())  # Clear selection
#                 messagebox.showinfo("Success", "Contact added successfully!")
#             except ValueError as e:
#                 messagebox.showerror("Error", str(e))
    
#     def edit_contact_dialog(self):
#         """Show dialog to edit selected contact."""
#         contact = self.get_selected_contact()
#         if not contact:
#             return  # Feedback already given in get_selected_contact
#         dialog = ContactDialog(self.root, "Edit Contact", contact)
#         self.root.wait_window(dialog.dialog)  # Wait for dialog to close
#         if dialog.result:
#             try:
#                 # Use the original phone to update, but allow phone to change
#                 self.contact_book.update_contact(contact.phone, **dialog.result)
#                 self.refresh_contact_list()
#                 self.tree.selection_remove(self.tree.selection())  # Clear selection after edit
#                 messagebox.showinfo("Success", "Contact updated successfully!")
#             except ValueError as e:
#                 messagebox.showerror("Error", str(e))
    
#     def delete_contact_dialog(self):
#         """Show dialog to delete selected contact."""
#         contact = self.get_selected_contact()
#         if not contact:
#             return  # Feedback already given in get_selected_contact
#         if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {contact.name}?"):
#             self.contact_book.delete_contact(contact.phone)
#             self.refresh_contact_list()
#             self.tree.selection_remove(self.tree.selection())  # Clear selection after delete
#             messagebox.showinfo("Success", "Contact deleted successfully!")
    
#     def search_dialog(self):
#         """Show advanced search dialog."""
#         query = simpledialog.askstring("Search Contacts", 
#                                      "Enter search term (name, phone, or email):")
#         if query:
#             results = self.contact_book.search_contacts(query)
#             if results:
#                 self.refresh_contact_list(results)
#                 messagebox.showinfo("Search Results", f"Found {len(results)} contact(s)")
#             else:
#                 messagebox.showinfo("Search Results", "No contacts found.")
    
#     def show_statistics(self):
#         """Show contact book statistics."""
#         stats = self.contact_book.get_statistics()
#         message = f"""Contact Book Statistics:
        
# Total Contacts: {stats['total_contacts']}
# Contacts with Email: {stats['contacts_with_email']}
# Contacts with Address: {stats['contacts_with_address']}"""
        
#         messagebox.showinfo("Statistics", message)
    
#     def on_contact_double_click(self, event):
#         """Handle double-click on contact to view details."""
#         contact = self.get_selected_contact()
#         if contact:
#             self.show_contact_details(contact)
    
#     def show_contact_details(self, contact):
#         """Show detailed view of a contact."""
#         details_window = tk.Toplevel(self.root)
#         details_window.title(f"Contact Details - {contact.name}")
#         details_window.geometry("400x300")
#         details_window.configure(bg='#f0f0f0')
        
#         # Center the window
#         details_window.transient(self.root)
#         details_window.grab_set()
        
#         # Details frame
#         frame = ttk.Frame(details_window, padding="20")
#         frame.grid(row=0, column=0, sticky="nsew")
        
#         details_window.columnconfigure(0, weight=1)
#         details_window.rowconfigure(0, weight=1)
#         frame.columnconfigure(1, weight=1)
        
#         # Contact details
#         ttk.Label(frame, text="Name:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.name).grid(row=0, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Phone:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.phone).grid(row=1, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Email:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.email or "N/A").grid(row=2, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Address:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.address or "N/A").grid(row=3, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Notes:", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.notes or "N/A").grid(row=4, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Created:", font=('Arial', 10, 'bold')).grid(row=5, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.created_date).grid(row=5, column=1, sticky=tk.W, pady=2)
        
#         ttk.Label(frame, text="Modified:", font=('Arial', 10, 'bold')).grid(row=6, column=0, sticky=tk.W, pady=2)
#         ttk.Label(frame, text=contact.last_modified).grid(row=6, column=1, sticky=tk.W, pady=2)
        
#         # Close button
#         ttk.Button(frame, text="Close", command=details_window.destroy).grid(row=7, column=0, columnspan=2, pady=20)
    
#     def run(self):
#         """Start the GUI application."""
#         self.root.mainloop()

# class ContactDialog:
#     """Dialog for adding/editing contacts."""
    
#     def __init__(self, parent, title, contact=None):
#         self.result = None
        
#         # Create dialog window
#         self.dialog = tk.Toplevel(parent)
#         self.dialog.title(title)
#         self.dialog.geometry("400x350")
#         self.dialog.configure(bg='#f0f0f0')
        
#         # Center the window
#         self.dialog.transient(parent)
#         self.dialog.grab_set()
        
#         # Variables
#         self.name_var = tk.StringVar(value=contact.name if contact else "")
#         self.phone_var = tk.StringVar(value=contact.phone if contact else "")
#         self.email_var = tk.StringVar(value=contact.email if contact else "")
#         self.address_var = tk.StringVar(value=contact.address if contact else "")
#         self.notes_var = tk.StringVar(value=contact.notes if contact else "")
        
#         self.setup_ui()
    
#     def setup_ui(self):
#         """Setup the dialog UI."""
#         frame = ttk.Frame(self.dialog, padding="20")
#         frame.grid(row=0, column=0, sticky="nsew")
        
#         self.dialog.columnconfigure(0, weight=1)
#         self.dialog.rowconfigure(0, weight=1)
#         frame.columnconfigure(1, weight=1)
        
#         # Title
#         ttk.Label(frame, text="Contact Information", 
#                  font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
#         # Form fields
#         ttk.Label(frame, text="Name *:").grid(row=1, column=0, sticky=tk.W, pady=2)
#         ttk.Entry(frame, textvariable=self.name_var, width=30).grid(row=1, column=1, sticky="we", pady=2)
        
#         ttk.Label(frame, text="Phone *:").grid(row=2, column=0, sticky=tk.W, pady=2)
#         ttk.Entry(frame, textvariable=self.phone_var, width=30).grid(row=2, column=1, sticky="we", pady=2)
        
#         ttk.Label(frame, text="Email:").grid(row=3, column=0, sticky=tk.W, pady=2)
#         ttk.Entry(frame, textvariable=self.email_var, width=30).grid(row=3, column=1, sticky="we", pady=2)
        
#         ttk.Label(frame, text="Address:").grid(row=4, column=0, sticky=tk.W, pady=2)
#         ttk.Entry(frame, textvariable=self.address_var, width=30).grid(row=4, column=1, sticky="we", pady=2)
        
#         ttk.Label(frame, text="Notes:").grid(row=5, column=0, sticky=tk.W, pady=2)
#         notes_entry = ttk.Entry(frame, textvariable=self.notes_var, width=30)
#         notes_entry.grid(row=5, column=1, sticky="we", pady=2)
        
#         # Buttons
#         button_frame = ttk.Frame(frame)
#         button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
#         ttk.Button(button_frame, text="Save", command=self.save).grid(row=0, column=0, padx=5)
#         ttk.Button(button_frame, text="Cancel", command=self.cancel).grid(row=0, column=1, padx=5)
        
#         # Focus on name field
#         frame.focus_set()
    
#     def save(self):
#         """Save the contact information."""
#         name = self.name_var.get().strip()
#         phone = self.phone_var.get().strip()
        
#         if not name or not phone:
#             messagebox.showerror("Error", "Name and phone number are required.")
#             return
        
#         self.result = {
#             'name': name,
#             'phone': phone,
#             'email': self.email_var.get().strip(),
#             'address': self.address_var.get().strip(),
#             'notes': self.notes_var.get().strip()
#         }
        
#         self.dialog.destroy()
    
#     def cancel(self):
#         """Cancel the dialog."""
#         self.dialog.destroy()

# def console_interface():
#     """Console-based interface for the contact book."""
#     contact_book = ContactBook()
    
#     def print_menu():
#         print("\n" + "="*50)
#         print("           CONTACT BOOK MENU")
#         print("="*50)
#         print("1. Add Contact")
#         print("2. View All Contacts")
#         print("3. Search Contacts")
#         print("4. Edit Contact")
#         print("5. Delete Contact")
#         print("6. View Statistics")
#         print("7. Exit")
#         print("="*50)
    
#     def get_contact_info():
#         """Get contact information from user input."""
#         name = input("Enter name: ").strip()
#         phone = input("Enter phone number: ").strip()
#         email = input("Enter email (optional): ").strip()
#         address = input("Enter address (optional): ").strip()
#         notes = input("Enter notes (optional): ").strip()
#         return name, phone, email, address, notes
    
#     def display_contact(contact):
#         """Display a single contact."""
#         print(f"\nName: {contact.name}")
#         print(f"Phone: {contact.phone}")
#         print(f"Email: {contact.email or 'N/A'}")
#         print(f"Address: {contact.address or 'N/A'}")
#         print(f"Notes: {contact.notes or 'N/A'}")
#         print(f"Created: {contact.created_date}")
#         print(f"Modified: {contact.last_modified}")
#         print("-" * 30)
    
#     while True:
#         print_menu()
#         choice = input("Enter your choice (1-7): ").strip()
        
#         if choice == '1':
#             print("\n--- ADD NEW CONTACT ---")
#             try:
#                 name, phone, email, address, notes = get_contact_info()
#                 contact_book.add_contact(name, phone, email, address, notes)
#                 print("Contact added successfully!")
#             except ValueError as e:
#                 print(f"Error: {e}")
        
#         elif choice == '2':
#             print("\n--- ALL CONTACTS ---")
#             contacts = contact_book.get_all_contacts()
#             if contacts:
#                 for contact in contacts:
#                     display_contact(contact)
#             else:
#                 print("No contacts found.")
        
#         elif choice == '3':
#             print("\n--- SEARCH CONTACTS ---")
#             query = input("Enter search term: ").strip()
#             if query:
#                 results = contact_book.search_contacts(query)
#                 if results:
#                     print(f"\nFound {len(results)} contact(s):")
#                     for contact in results:
#                         display_contact(contact)
#                 else:
#                     print("No contacts found.")
#             else:
#                 print("Please enter a search term.")
        
#         elif choice == '4':
#             print("\n--- EDIT CONTACT ---")
#             original_phone = input("Enter phone number of contact to edit: ").strip()
#             contact = contact_book.get_contact_by_phone(original_phone)
#             if contact:
#                 print(f"Editing contact: {contact.name}")
#                 name, new_phone, email, address, notes = get_contact_info()
#                 try:
#                     contact_book.update_contact(original_phone, name=name, phones=new_phone, 
#                                              email=email, address=address, notes=notes)
#                     print("Contact updated successfully!")
#                 except ValueError as e:
#                     print(f"Error: {e}")
#             else:
#                 print("Contact not found.")
        
#         elif choice == '5':
#             print("\n--- DELETE CONTACT ---")
#             phone = input("Enter phone number of contact to delete: ").strip()
#             if contact_book.delete_contact(phone):
#                 print("Contact deleted successfully!")
#             else:
#                 print("Contact not found.")
        
#         elif choice == '6':
#             print("\n--- STATISTICS ---")
#             stats = contact_book.get_statistics()
#             print(f"Total Contacts: {stats['total_contacts']}")
#             print(f"Contacts with Email: {stats['contacts_with_email']}")
#             print(f"Contacts with Address: {stats['contacts_with_address']}")
        
#         elif choice == '7':
#             print("Goodbye!")
#             break
        
#         else:
#             print("Invalid choice. Please try again.")

# def main():
#     """Main function to run the application."""
#     print("Welcome to Contact Book Application!")
#     print("Choose your interface:")
#     print("1. Console Interface")
#     print("2. GUI Interface")
    
#     while True:
#         choice = input("Enter your choice (1 or 2): ").strip()
        
#         if choice == '1':
#             console_interface()
#             break
#         elif choice == '2':
#             contact_book = ContactBook()
#             gui = ContactBookGUI(contact_book)
#             gui.run()
#             break
#         else:
#             print("Invalid choice. Please enter 1 or 2.")

# if __name__ == "__main__":
#     main() 


# -----------------------------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Contact:
    """A class to represent a single contact."""
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactBook:
    """A class to manage the contact book."""
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        """Add a new contact to the contact book."""
        self.contacts.append(contact)

    def delete_contact(self, contact):
        """Delete a contact from the contact book."""
        if contact in self.contacts:
            self.contacts.remove(contact)

    def edit_contact(self, old_contact, new_contact):
        """Edit a contact in the contact book."""
        for i, contact in enumerate(self.contacts):
            if contact == old_contact:
                self.contacts[i] = new_contact
                return

    def search_contacts(self, keyword):
        """Search contacts by name, phone, email, or address."""
        return [c for c in self.contacts if keyword.lower() in str(c).lower()]

    def get_contact_by_phone(self, phone):
        """Get contact by phone number."""
        phone = phone.strip()
        for contact in self.contacts:
            if contact.phone.strip() == phone:
                return contact
        return None


class ContactBookGUI:
    """The GUI for the contact book."""
    def __init__(self, root):
        self.root = root
        self.root.title("📒 Aesthetic Contact Book")
        self.root.geometry("800x600")
        self.root.configure(bg="#f9f5f0")

        # Initialize contact book
        self.contact_book = ContactBook()

        # Style setup
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background="#f9f5f0", foreground="#333", font=('Helvetica', 10))
        style.configure("TButton", padding=6, font=('Helvetica', 10, 'bold'), background="#a0c4ff", foreground="#333")
        style.map("TButton", background=[('active', '#89b4f7')])
        style.configure("Treeview", background="#fff", foreground="#000", font=('Helvetica', 10), rowheight=30, fieldbackground="#fff")
        style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), background="#bdb2ff")

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Search bar
        search_frame = ttk.Frame(self.root, padding="10")
        search_frame.pack(fill=tk.X, pady=10)
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(search_frame, text="Search", command=self.search_contacts).pack(side=tk.LEFT, padx=5)

        # Buttons
        buttons_frame = ttk.Frame(self.root, padding="10")
        buttons_frame.pack(fill=tk.X)
        ttk.Button(buttons_frame, text="Add Contact", command=self.add_contact_dialog).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Edit Contact", command=self.edit_contact_dialog).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Delete Contact", command=self.delete_contact).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(buttons_frame, text="Stats", command=self.show_stats).grid(row=0, column=3, padx=10, pady=5)

        # Treeview (contact list)
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show="headings", selectmode="browse")
        for col in ("Name", "Phone", "Email", "Address"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, width=150)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.tree.bind("<Double-1>", self.on_double_click)

    def refresh_contact_list(self, contacts=None):
        """Refresh the contact list display."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        contacts = contacts if contacts is not None else self.contact_book.contacts
        for contact in contacts:
            self.tree.insert('', tk.END, values=(contact.name, contact.phone, contact.email, contact.address))

    def add_contact_dialog(self):
        """Dialog to add a new contact."""
        dialog = ContactDialog(self.root, "Add Contact")
        if dialog.result:
            new_contact = Contact(*dialog.result)
            self.contact_book.add_contact(new_contact)
            self.refresh_contact_list()

    def get_selected_contact(self):
        """Get the currently selected contact."""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a contact first.")
            return None
        item = self.tree.item(selection[0])
        if not item or not item.get('values') or len(item['values']) < 2:
            messagebox.showwarning("Selection Error", "Could not retrieve contact details from selection.")
            return None
        phone = str(item['values'][1]).strip()
        contact = self.contact_book.get_contact_by_phone(phone)
        if not contact:
            messagebox.showwarning("Not Found", "Selected contact could not be found.")
        return contact

    def edit_contact_dialog(self):
        """Edit the selected contact."""
        contact = self.get_selected_contact()
        if not contact:
            return
        dialog = ContactDialog(self.root, "Edit Contact", contact)
        if dialog.result:
            new_contact = Contact(*dialog.result)
            self.contact_book.edit_contact(contact, new_contact)
            self.refresh_contact_list()

    def delete_contact(self):
        """Delete the selected contact."""
        contact = self.get_selected_contact()
        if not contact:
            return
        if messagebox.askyesno("Delete", f"Are you sure you want to delete {contact.name}?"):
            self.contact_book.delete_contact(contact)
            self.refresh_contact_list()

    def search_contacts(self):
        """Search contacts and update list."""
        keyword = self.search_var.get()
        results = self.contact_book.search_contacts(keyword)
        self.refresh_contact_list(results)

    def show_stats(self):
        """Show simple statistics."""
        total = len(self.contact_book.contacts)
        messagebox.showinfo("Stats", f"Total Contacts: {total}")

    def on_double_click(self, event):
        """Show contact details on double click."""
        contact = self.get_selected_contact()
        if contact:
            messagebox.showinfo("Contact Details", str(contact))


class ContactDialog:
    """Dialog for adding/editing a contact."""
    def __init__(self, parent, title, contact=None):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.grab_set()
        self.result = None
        self.dialog.configure(bg="#f9f5f0")

        frame = ttk.Frame(self.dialog, padding="20")
        frame.pack(padx=10, pady=10)

        ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar(value=getattr(contact, 'name', ''))
        ttk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.phone_var = tk.StringVar(value=getattr(contact, 'phone', ''))
        ttk.Entry(frame, textvariable=self.phone_var).grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar(value=getattr(contact, 'email', ''))
        ttk.Entry(frame, textvariable=self.email_var).grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Address:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.address_var = tk.StringVar(value=getattr(contact, 'address', ''))
        ttk.Entry(frame, textvariable=self.address_var).grid(row=3, column=1, pady=5)

        ttk.Button(frame, text="Save", command=self.on_save).grid(row=4, column=0, columnspan=2, pady=15)

        self.dialog.wait_window()

    def on_save(self):
        """Save contact info and close dialog."""
        self.result = (
            self.name_var.get().strip(),
            self.phone_var.get().strip(),
            self.email_var.get().strip(),
            self.address_var.get().strip()
        )
        self.dialog.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
