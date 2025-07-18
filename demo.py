#!/usr/bin/env python3
"""
Demo script for the Contact Book application.
This script demonstrates how to use the ContactBook class programmatically.
"""

from contact_book import ContactBook, Contact

def demo_contact_book():
    """Demonstrate the Contact Book functionality."""
    
    print("=" * 60)
    print("           CONTACT BOOK DEMO")
    print("=" * 60)
    
    # Create a new contact book
    contact_book = ContactBook("demo_contacts.json")
    
    # Add some sample contacts
    print("\n1. Adding sample contacts...")
    
    try:
        # Add first contact
        contact1 = contact_book.add_contact(
            name="John Doe",
            phone="555-123-4567",
            email="john.doe@email.com",
            address="123 Main Street, City, State 12345",
            notes="Work colleague"
        )
        print(f"✓ Added: {contact1}")
        
        # Add second contact
        contact2 = contact_book.add_contact(
            name="Jane Smith",
            phone="555-987-6543",
            email="jane.smith@email.com",
            address="456 Oak Avenue, Town, State 67890",
            notes="Friend from college"
        )
        print(f"✓ Added: {contact2}")
        
        # Add third contact
        contact3 = contact_book.add_contact(
            name="Bob Johnson",
            phone="555-555-5555",
            email="bob.johnson@email.com",
            address="789 Pine Road, Village, State 11111",
            notes="Neighbor"
        )
        print(f"✓ Added: {contact3}")
        
    except ValueError as e:
        print(f"Error adding contact: {e}")
    
    # Display all contacts
    print("\n2. All contacts:")
    contacts = contact_book.get_all_contacts()
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact.name} - {contact.phone}")
        print(f"   Email: {contact.email}")
        print(f"   Address: {contact.address}")
        print(f"   Notes: {contact.notes}")
        print()
    
    # Search functionality
    print("3. Search functionality:")
    
    # Search by name
    print("\n   Searching for 'john':")
    results = contact_book.search_contacts("john")
    for contact in results:
        print(f"   - {contact.name} ({contact.phone})")
    
    # Search by phone
    print("\n   Searching for '555':")
    results = contact_book.search_contacts("555")
    for contact in results:
        print(f"   - {contact.name} ({contact.phone})")
    
    # Update a contact
    print("\n4. Updating contact...")
    updated_contact = contact_book.update_contact(
        "555-123-4567",
        email="john.doe.updated@email.com",
        notes="Work colleague - Updated"
    )
    if updated_contact:
        print(f"✓ Updated: {updated_contact.name}")
        print(f"  New email: {updated_contact.email}")
        print(f"  New notes: {updated_contact.notes}")
    
    # Show statistics
    print("\n5. Contact book statistics:")
    stats = contact_book.get_statistics()
    print(f"   Total contacts: {stats['total_contacts']}")
    print(f"   Contacts with email: {stats['contacts_with_email']}")
    print(f"   Contacts with address: {stats['contacts_with_address']}")
    
    # Demonstrate contact retrieval
    print("\n6. Getting specific contact:")
    contact = contact_book.get_contact_by_phone("555-987-6543")
    if contact:
        print(f"   Found: {contact.name}")
        print(f"   Phone: {contact.phone}")
        print(f"   Email: {contact.email}")
        print(f"   Created: {contact.created_date}")
        print(f"   Modified: {contact.last_modified}")
    
    print("\n" + "=" * 60)
    print("Demo completed! Check 'demo_contacts.json' for the saved data.")
    print("=" * 60)

def demo_contact_class():
    """Demonstrate the Contact class functionality."""
    
    print("\n" + "=" * 60)
    print("           CONTACT CLASS DEMO")
    print("=" * 60)
    
    # Create a contact
    contact = Contact(
        name="Alice Brown",
        phone="555-111-2222",
        email="alice@example.com",
        address="321 Elm Street",
        notes="Test contact"
    )
    
    print(f"Created contact: {contact}")
    print(f"Contact details:")
    print(f"  Name: {contact.name}")
    print(f"  Phone: {contact.phone}")
    print(f"  Email: {contact.email}")
    print(f"  Address: {contact.address}")
    print(f"  Notes: {contact.notes}")
    print(f"  Created: {contact.created_date}")
    print(f"  Modified: {contact.last_modified}")
    
    # Update the contact
    print(f"\nUpdating contact...")
    contact.update(
        email="alice.updated@example.com",
        notes="Updated test contact"
    )
    print(f"Updated contact:")
    print(f"  Email: {contact.email}")
    print(f"  Notes: {contact.notes}")
    print(f"  Modified: {contact.last_modified}")
    
    # Convert to dictionary
    contact_dict = contact.to_dict()
    print(f"\nContact as dictionary:")
    for key, value in contact_dict.items():
        print(f"  {key}: {value}")
    
    # Create from dictionary
    new_contact = Contact.from_dict(contact_dict)
    print(f"\nRecreated contact: {new_contact}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Run the demos
    demo_contact_book()
    demo_contact_class()
    
    print("\nTo run the full application with GUI or console interface:")
    print("python contact_book.py") 