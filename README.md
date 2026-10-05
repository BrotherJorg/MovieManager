# MovieOwl - A Simple Movie Manager

## Description

MovieOwl is a desktop application built using Python, SQLite, and PyQt which provides a simplified, intuitive and simple movie management system.

Personal management of a movie collection gets harder the bigger it grows. This is true in our digital age where movies can be scattered on different platforms. It can be hard to know what you own in and keep track of movies and their watch status, their reviews, their ratings and your personal notes especially with online services or manual writing.

MovieOwl solves this problem by packaging a movie record, recommendation, note and review systems all in one desktop application.

## Objectives
- To develop a single centralized desktop application for managing personal movie collections.
- To provide users a way to record the movies in their collection.
- To provide users the tools for creating, editing, and searching for movies.
- To allow users the ability to organize their movies through collections and favorites.
- To create a system for managing movie ratings, movie reviews and movie notes.
- To implement a movie recommendation system through random or score based selection.
- To display a simple dashboard for global movie collection statistics.
- To apply clean modular architecture, object oriented programming, database application and clean code practice in the development of the project.

## Features

### Dashboard
Display current database records and simple statistics in a neat, readable format.
- Allows the user to see the total number of movies, number of watched, watching, unwatched movies.
- Displays number of movies per genre and the average rating in the whole collection.
- Display dashboard at the start of application.
  
### Movie Management
Display table of movies.
- Allows adding, editing, viewing details, deleting of movie records.
- Allows user keyword searching, filtering by genres, by watch status.

### Watch status
Allows tracking of movie watch status.
- Allows tagging movie as watched.
- Allows tagging movie as watching
- Newly added movies tagged as unwatched as default.

### Review
Allows writing personal opinion on a movie entry
- Allows users to rate a movie.
- Allows writing a review.
- Allows writing a note.
- Save each movie review persistently per movie.

### Recommendation
Allows recommendation in two ways, a random movie or through a score.
- Allows selection of a random movie and displays it’s details.
- Allows ranked recommendations on recommendation page. 
- Selects unwatched and highly rated movies in database.

### User Collection
Allows user created collections/playlists of movies.
- Allows creation of custom named collection.
- Allows adding of movies to one or more collection.
- A default collection called favorites exits and movie added to favorites are automatically added on it.




## Technologies used
  #### Programming Language
  - Python 3.14
  
  #### GUI Framework / Library
  - PyQt6 6.11.0.
  - Qt Style Sheets (QSS) for application styling
  
  #### Database
  - SQLite3

  #### Libraries, Other Tools and Resources
  - Python Standard Library.
  - Git for version control.
  - GitHub for source-code management and repository hosting.
  - VSCode for development environment.
  - Manrope font for the application interface.
  - SVG icons for the graphical interface.

## Project Structure
    MovieOwl/
    ├── Assets/
    │   ├── fonts/
    │   └── icons/
    ├── Styles/
    ├── db/
    │   └── database.py
    ├── features/
    │   ├── collections/
    │   │   ├── repository.py
    │   │   ├── service.py
    │   │   └── view.py
    │   ├── dashboard/
    │   ├── favorites/
    │   ├── main_Window/
    │   ├── manage_movies/
    │   ├── movie_picker/
    │   ├── recommendations/
    │   └── review_notes/
    ├── .env.example
    ├── .gitignore
    ├── main.py
    ├── Movies.db
    └── README.md

Feature module pattern
Each folder in features/ is organized the same way:
repository.py: 
service.py: 
view.py:
model.py:

Feature folders
dashboard/:
manage_movies/: 
review_notes/:
recommendations/: 
movie_picker/: 
collections/:
favorites/:
main_Window/:



## Installation and setup
  #### Requirements
  - Python 3.14 or later
  - Git
  - PyQt6
  - Internet connection

  
  #### Installation
  
## Installation and Setup

### Requirements
- Python 3.14
- Git
- PyQt6 (installed in step 4)

### Installation

1. Clone the repository:

```powershell
   git clone https://github.com/BrotherJorg/MovieOwl.git
   cd MovieOwl
```

2. Create a virtual environment:

```powershell
   python -m venv .venv
```

3. Activate the virtual environment.

   Windows PowerShell:

```powershell
   .\.venv\Scripts\Activate.ps1
```

   macOS / Linux:

```bash
   source .venv/bin/activate
```

4. Install the required dependency:

```powershell
   pip install PyQt6
```

5. Run the application:

```powershell
   python main.py
```

When setup is successful, the application window opens on the Dashboard.

 ## How to Use the Application

1. **Launch the application.** Run `python main.py`. The Dashboard opens first and shows the collection statistics.

2. **Navigate between screens.** Use the sidebar to open Dashboard, Manage Movies, Movie Picker, Recommendations, Collections, and Favorites.

3. **Add a movie.** Open Manage Movies, choose the add option, fill in the movie details, and save. The new movie appears in the table with the watch status Unwatched.

4. **View, edit, or delete a movie.** Select a movie in the table to see its details, then edit or delete it.

5. **Search and filter.** Type a keyword in the search box to find movies. Use the filters to narrow the table by genre or watch status.

6. **Change the watch status.** Set a movie to Unwatched, Watching, or Watched.

7. **Rate and review a movie.** Open a movie's review screen to give it a rating, write a review, and add a personal note. Each movie keeps its own review and notes.

8. **Mark a favorite.** Toggle a movie as a favorite. It is added to the default Favorites collection, and you can browse it on the Favorites screen.

9. **Create a collection.** Open Collections, create a collection with a custom name, and add movies to it. A movie can belong to more than one collection.

10. **Pick a movie to watch.** Open Movie Picker to get a random movie and its details. Open Recommendations to see a ranked list of unwatched, highly rated movies.

11. **Read the Dashboard.** Return to the Dashboard to see the total number of movies, how many are Watched, Watching, and Unwatched, the number of movies per genre, and the average rating.


  
