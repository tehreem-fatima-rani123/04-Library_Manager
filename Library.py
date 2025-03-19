import streamlit as st
import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

# Custom CSS for styling
st.markdown("""
    <style>
    /* Gradient background for the header */
    .header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Card styling */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s, box-shadow 0.2s;
        text-align: center;
        margin: 1rem 0;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    /* Icon styling */
    .icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: #1e3c72;
    }
    /* Button styling */
    .stButton button {
        background: #1e3c72;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
        transition: background 0.3s;
    }
    .stButton button:hover {
        background: #2a5298;
    }
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .header {
            background: linear-gradient(135deg, #0f2027 0%, #203a43 100%);
        }
        .card {
            background: #2c3e50;
            color: white;
        }
        .icon {
            color: #3498db;
        }
        .stButton button {
            background: #3498db;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Homepage Header

st.markdown("""
    <div class="header">
        <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">📚 Personal Library Manager</h1>
        <p style="font-size: 1.2rem;">Your one-stop solution to manage your book collection with ease and style!</p>
    </div>
    """, unsafe_allow_html=True)

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <div class="icon">📖</div>
            <h3>Add a Book</h3>
            <p>Easily add new books to your library with all the details.</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <div class="icon">🔍</div>
            <h3>Search Books</h3>
            <p>Find books by title, author, genre, or year.</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <div class="icon">📊</div>
            <h3>View Stats</h3>
            <p>Track your reading progress with detailed statistics.</p>
        </div>
        """, unsafe_allow_html=True)

# Call to Action
st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <h2>Ready to get started?</h2>
        <p>Use the sidebar to navigate and manage your library.</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar menu
import streamlit as st

# Custom CSS for sidebar styling
st.markdown(
    """
    <style>
        .sidebar-title {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            color: white;
            padding: 15px;
            border-radius: 10px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Displaying the title in the sidebar
st.sidebar.markdown('<div class="sidebar-title">📚 Library Manager | Made with ❤️ by Tehreem Fatima</div>', unsafe_allow_html=True)


menu = st.sidebar.selectbox("Menu", ["Home", "Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])

# Add a Book

if menu == "Add a Book":
    st.subheader("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read")
    
    if st.button("Add Book"):
        if title and author:
            new_book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read": read_status
            }
            library.append(new_book)
            save_library(library)
            st.success("Book added successfully! 🎉")
            st.snow()  # Confetti animation
        else:
            st.warning("Title and Author are required!")

# Remove a Book
elif menu == "Remove a Book":
    st.subheader("Remove a Book")
    if library:
        book_titles = [book["title"] for book in library]
        title_to_remove = st.selectbox("Select Book to Remove", book_titles)
        
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != title_to_remove]
            save_library(library)
            st.success("Book removed successfully! 🗑️")
    else:
        st.warning("No books available to remove.")

# Search for a Book
elif menu == "Search for a Book":
    st.subheader("Search for a Book")
    search_query = st.text_input("Enter search term (title, author, genre, or year)")
    
    if st.button("Search"):
        results = [
            book for book in library
            if (search_query.lower() in book["title"].lower() or
                search_query.lower() in book["author"].lower() or
                search_query.lower() in book["genre"].lower() or
                search_query.lower() in str(book["year"]))
        ]
        
        if results:
            st.write("### Matching Books")
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

# Display All Books
elif menu == "Display All Books":
    st.subheader("Your Library")
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.info("Your library is empty.")

# Display Statistics
elif menu == "Statistics":
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books else 0
    
    st.write(f"📚 Total books: {total_books}")
    st.write(f"✅ Percentage read: {percentage_read:.2f}%")
    
    # Genre distribution (text-based)
    if library:
        genres = [book["genre"] for book in library]
        genre_counts = {genre: genres.count(genre) for genre in set(genres)}
        
        st.write("### Books by Genre")
        for genre, count in genre_counts.items():
            st.write(f"- **{genre}**: {count} books")

# Save library on exit
st.sidebar.markdown("---")
if st.sidebar.button("Exit"):
    save_library(library)
    st.sidebar.success("Library saved to file. Goodbye! 👋")
