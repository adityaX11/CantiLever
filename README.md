<!-- # Contact Book Application

A comprehensive Python Contact Book application that allows users to manage their contacts with both console and GUI interfaces.

## Features

### Core Functionality
- **Add Contacts**: Add new contacts with name, phone, email, address, and notes
- **View Contacts**: Display all contacts in a sorted list
- **Search Contacts**: Search by name, phone number, or email
- **Edit Contacts**: Update existing contact information
- **Delete Contacts**: Remove contacts from the address book
- **Contact Statistics**: View summary statistics about your contacts

### Data Management
- **Persistent Storage**: All contacts are saved to a JSON file (`contacts.json`)
- **Data Validation**: Ensures required fields are provided and prevents duplicate phone numbers
- **Automatic Timestamps**: Tracks when contacts are created and last modified

### User Interfaces
- **Console Interface**: Text-based interface for command-line users
- **GUI Interface**: Modern graphical interface using Tkinter
  - Clean, intuitive design
  - Quick search functionality
  - Contact details view
  - Confirmation dialogs for destructive actions

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Setup
1. Clone or download the project files
2. Ensure you have Python installed on your system
3. No additional installation steps required

## Usage

### Running the Application

```bash
python contact_book.py
```

When you run the application, you'll be prompted to choose your preferred interface:

1. **Console Interface** - Text-based menu system
2. **GUI Interface** - Graphical user interface

### Console Interface

The console interface provides a menu-driven experience:

```
==================================================
           CONTACT BOOK MENU
==================================================
1. Add Contact
2. View All Contacts
3. Search Contacts
4. Edit Contact
5. Delete Contact
6. View Statistics
7. Exit
==================================================
```

### GUI Interface

The GUI interface offers:

- **Main Window**: Displays all contacts in a table format
- **Quick Search**: Real-time search as you type
- **Add Contact**: Button to add new contacts
- **Edit Contact**: Select a contact and click edit
- **Delete Contact**: Select a contact and click delete
- **View Details**: Double-click any contact to see full details
- **Statistics**: View contact book statistics

### Data Storage

All contacts are automatically saved to `contacts.json` in the same directory as the application. The file is created automatically when you add your first contact.

## File Structure

```
ContactBook/
├── contact_book.py      # Main application file
├── requirements.txt     # Dependencies (none required)
├── README.md          # This file
└── contacts.json      # Contact data (created automatically)
```

## Features in Detail

### Contact Information
Each contact stores:
- **Name** (required)
- **Phone Number** (required, must be unique)
- **Email Address** (optional)
- **Physical Address** (optional)
- **Notes** (optional)
- **Creation Date** (automatic)
- **Last Modified Date** (automatic)

### Search Functionality
- Search by name (partial matches)
- Search by phone number (exact or partial)
- Search by email address (partial matches)
- Case-insensitive search

### Data Validation
- Name and phone number are required
- Phone numbers must be unique
- Email addresses are optional but validated if provided
- All fields are trimmed of leading/trailing whitespace

### Error Handling
- Graceful handling of file I/O errors
- User-friendly error messages
- Data validation with clear feedback
- Confirmation dialogs for destructive actions

## Technical Details

### Architecture
- **Contact Class**: Represents individual contacts with all properties
- **ContactBook Class**: Manages the collection of contacts and file operations
- **ContactBookGUI Class**: Handles the graphical user interface
- **ContactDialog Class**: Manages contact input/editing dialogs
- **Console Interface**: Text-based interaction system

### Data Format
Contacts are stored in JSON format for easy reading and debugging:

```json
[
  {
    "name": "John Doe",
    "phone": "123-456-7890",
    "email": "john@example.com",
    "address": "123 Main St",
    "notes": "Work contact",
    "created_date": "2024-01-15 10:30:00",
    "last_modified": "2024-01-15 10:30:00"
  }
]
```

## Contributing

This is a learning project, but suggestions and improvements are welcome! The code is well-documented and follows Python best practices.

## License

This project is open source and available under the MIT License.

## Future Enhancements

Potential improvements could include:
- Contact categories/tags
- Contact import/export (CSV, vCard)
- Contact photos
- Birthday reminders
- Contact sharing
- Cloud synchronization
- Advanced search filters
- Contact backup/restore

---

**Enjoy managing your contacts with this simple yet powerful Contact Book application!**  -->

# Contact Book (Tkinter GUI)

A minimal & aesthetic Contact Book desktop app built with **Python** and **Tkinter**. Easily manage your contacts in style — add, edit, delete, search, and view with a modern UI.

---

## Features

 -Add, edit, delete contacts
 -Real-time search by name, phone, email, or address
 -See total contact count (stats)
 -Soft pastel-themed GUI with modern fonts
 -Double-click to view contact details

## Getting Started

Run the app
  -> python contact_book.py
Tech Used
  Python — backend logic
  Tkinter — desktop GUI
  TTK Styling — for a clean aesthetic

Future Ideas
  Export to CSV
  Import from file
  Dark mode
  Contact avatars
  Birthday notifications
  AI integration (for Recomendation purpose).
-> I am still working on this feature ,for this my project look like productive.

Author
  Aditya Kumar
     Student & Python dev
    [adix110086@gmail.com] (optional)

License
MIT — use it freely, remix it proudly.
