#!/usr/bin/env python3
"""
Test script for the Contact Book application.
This script tests all major functionality and error handling.
"""

import os
import tempfile
from contact_book import ContactBook, Contact

def test_contact_class():
    """Test the Contact class functionality."""
    print("Testing Contact class...")
    
    # Test contact creation
    contact = Contact("Test User", "123-456-7890", "test@email.com", "123 Test St", "Test notes")
    assert contact.name == "Test User"
    assert contact.phone == "123-456-7890"
    assert contact.email == "test@email.com"
    assert contact.address == "123 Test St"
    assert contact.notes == "Test notes"
    print("✓ Contact creation works")
    
    # Test contact update
    contact.update(name="Updated User", email="updated@email.com")
    assert contact.name == "Updated User"
    assert contact.email == "updated@email.com"
    print("✓ Contact update works")
    
    # Test to_dict and from_dict
    contact_dict = contact.to_dict()
    new_contact = Contact.from_dict(contact_dict)
    assert new_contact.name == contact.name
    assert new_contact.phone == contact.phone
    print("✓ Contact serialization works")
    
    print("✓ All Contact class tests passed!\n")

def test_contact_book_basic():
    """Test basic ContactBook functionality."""
    print("Testing ContactBook basic functionality...")
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.close()
    
    try:
        contact_book = ContactBook(temp_file.name)
        
        # Add contacts
        contact1 = contact_book.add_contact("Alice", "111-111-1111", "alice@test.com")
        contact2 = contact_book.add_contact("Bob", "222-222-2222", "bob@test.com")
        
        assert len(contact_book.contacts) == 2
        print("✓ Adding contacts works")
        
        # Get all contacts
        all_contacts = contact_book.get_all_contacts()
        assert len(all_contacts) == 2
        assert all_contacts[0].name == "Alice"
        print("✓ Getting all contacts works")
        
        # Search contacts
        results = contact_book.search_contacts("alice")
        assert len(results) == 1
        assert results[0].name == "Alice"
        print("✓ Search functionality works")
        
        # Update contact
        contact_book.update_contact("111-111-1111", name="Alice Updated")
        contact = contact_book.get_contact_by_phone("111-111-1111")
        assert contact is not None and contact.name == "Alice Updated"
        print("✓ Contact update works")
        
        # Delete contact
        deleted = contact_book.delete_contact("222-222-2222")
        assert deleted
        assert len(contact_book.contacts) == 1
        print("✓ Contact deletion works")
        
        # Statistics
        stats = contact_book.get_statistics()
        assert stats['total_contacts'] == 1
        print("✓ Statistics work")
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    
    print("✓ All basic ContactBook tests passed!\n")

def test_contact_book_validation():
    """Test ContactBook validation and error handling."""
    print("Testing ContactBook validation...")
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.close()
    
    try:
        contact_book = ContactBook(temp_file.name)
        
        # Empty name
        try:
            contact_book.add_contact("", "123-456-7890")
            assert False, "Should have raised ValueError"
        except ValueError:
            print("✓ Empty name validation works")
        
        # Empty phone
        try:
            contact_book.add_contact("Test User", "")
            assert False, "Should have raised ValueError"
        except ValueError:
            print("✓ Empty phone validation works")
        
        # Duplicate phone
        contact_book.add_contact("User 1", "123-456-7890")
        try:
            contact_book.add_contact("User 2", "123-456-7890")
            assert False, "Should have raised ValueError for duplicate phone"
        except ValueError:
            print("✓ Duplicate phone validation works")
        
        # Non-existent get
        contact = contact_book.get_contact_by_phone("999-999-9999")
        assert contact is None
        print("✓ Non-existent contact handling works")
        
        # Non-existent update
        try:
            contact_book.update_contact("999-999-9999", name="Test")
            assert False, "Should have raised ValueError for non-existent contact"
        except ValueError as e:
            assert str(e) == "Contact not found."
            print("✓ Non-existent contact update handling works")
        
        # Non-existent delete
        deleted = contact_book.delete_contact("999-999-9999")
        assert not deleted
        print("✓ Non-existent contact deletion handling works")
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    
    print("✓ All validation tests passed!\n")

def test_file_operations():
    """Test file I/O operations."""
    print("Testing file operations...")
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.close()
    
    try:
        contact_book1 = ContactBook(temp_file.name)
        contact_book1.add_contact("Test User", "123-456-7890", "test@email.com")
        
        contact_book2 = ContactBook(temp_file.name)
        assert len(contact_book2.contacts) == 1
        assert contact_book2.contacts[0].name == "Test User"
        print("✓ File save/load works")
        
        non_existent_file = "/non/existent/path/contacts.json"
        contact_book3 = ContactBook(non_existent_file)
        assert len(contact_book3.contacts) == 0
        print("✓ Non-existent file handling works")
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    
    print("✓ All file operation tests passed!\n")

def test_search_functionality():
    """Test search functionality thoroughly."""
    print("Testing search functionality...")
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.close()
    
    try:
        contact_book = ContactBook(temp_file.name)
        
        contact_book.add_contact("John Doe", "111-111-1111", "john@test.com", "123 Main St")
        contact_book.add_contact("Jane Smith", "222-222-2222", "jane@test.com", "456 Oak Ave")
        contact_book.add_contact("Bob Johnson", "333-333-3333", "bob@test.com", "789 Pine Rd")
        
        # Name search
        results = contact_book.search_contacts("john")
        assert any(r.name == "John Doe" for r in results)
        print("✓ Name search works")
        
        # Phone search
        results = contact_book.search_contacts("222")
        assert len(results) == 1
        assert results[0].name == "Jane Smith"
        print("✓ Phone search works")
        
        # Email search
        results = contact_book.search_contacts("bob@test.com")
        assert len(results) == 1
        assert results[0].name == "Bob Johnson"
        print("✓ Email search works")
        
        # No results
        results = contact_book.search_contacts("nonexistent")
        assert len(results) == 0
        print("✓ No results search works")
        
        # Empty search returns all
        results = contact_book.search_contacts("")
        assert len(results) == 3
        print("✓ Empty search returns all contacts")
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    
    print("✓ All search tests passed!\n")

def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("           RUNNING CONTACT BOOK TESTS")
    print("=" * 60)
    
    try:
        test_contact_class()
        test_contact_book_basic()
        test_contact_book_validation()
        test_file_operations()
        test_search_functionality()
        
        print("=" * 60)
        print("           ALL TESTS PASSED! ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        raise

if __name__ == "__main__":
    run_all_tests()
