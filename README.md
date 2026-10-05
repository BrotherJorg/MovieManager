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
  	
- Allows the user to see total number of movies, number of watched, watching, unwatched movies.
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
-  Save each movie review persistently per movie.

### Recommendation
Allows recommendation in two ways, a random movie or through a score.
- Provide selection of a random movie and displays it’s details.
- Provide consistent recommendations on recommendation page. 
- Selects unwatched and highly rated movies.

### User Collection
Allows user created collections/playlists of movies.
- Allows creation of custom named collection.
- Allows adding of movies to one or more collection.
- A default collection called favorites exits and movie added to favorites are automatically added on it.




## Technologies used
  #### Programming Language
  - Python 3.14
  
  #### GUI Framework / Library
  - PyQt6
  - Qt Style Sheets (QSS) for application styling
  
  #### Database
  - SQLite
    
  #### Libraries
  - Python Standard Library
  - sqlite3 for SQLite database integration
  
    ##### Other Tools and Resources
    - Git for version control
    - GitHub for source-code management and repository hosting
    - VSCodium for development
    - Manrope font for the application interface
    - SVG icons for the graphical interface

## Project Structure

## Installation and setup
  #### Requirements
  - Python 3.14 or later
  - Git
  - PyQt6
    
  #### Installation
  
  1. Clone the repository:
  git clone <repository-url>
  cd MovieOwl

  2. Create a virtual environment:
  python -m venv .venv
  
  3. Activate the virtual environment.

     in Windows PowerShell:

     .\.venv\Scripts\Activate.ps1
  
  4. Install the required dependency:

      pip install PyQt6
  
  7. Run the application:
     
      python main.py

 ## How to use the application


  
