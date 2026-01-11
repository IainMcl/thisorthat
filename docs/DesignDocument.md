# Design Document: This or That

## 1. Introduction

This project aims to develop a "This or That" application that allows uses
to choose between two options. The results of these comparisons will then
be used to help make decisions or understand preference trends.

An example use case which is the inspiration for this project is to be able
to decide which car to get when buying a new car. For this I don't know
what car I want, however, when I see cars I aesthetically know which ones
I like and don't like. This app will show images of cars and allow the user
to select which is better building up a knowledge base of preferences which
can then be used to inform a decision.

## 2. Project Goals

* Create an application that allows a user to choose between two options
presented to them.
* Store user choices to build a preference profile.
* Analyze the collected data to provide insights or recommendations based
on user preferences.
* Ensure the application is user-friendly and visually appealing.
* Treat this project as a coding exercise to practice software design and
development skills.

## 3. User Stories / Use Cases

*   **As a user**, I want to be presented with two distinct car options at
a time, so that I can easily make a choice between them.
*   **As a user**, I want to be able to select one of the two options to
indicate my preference.
*   **As a user**, I want my choices to be recorded, so that the application
can build a profile of my preferences over time.
*   **As a user**, I want to view a summary or analysis of my past choices,
so that I can understand the common characteristics of the cars I prefer.
*   **As a user**, I want to have the option to skip a choice if I don't
have a preference for either option presented.

## 4. Architecture Overview / Technical requirements

### MVP implementation

Use a data store of options (e.g., images of cars) and present two random
options
to the user. Capture the user's choice and store it in a simple database.

This will require a backend to serve options and record choices, and a
frontend to display the options and capture user input.

![MVP sequence
diagram](./assets/sequencediagrams/mvp_interactions/thisorthatmvp.png)

Source:
[code](./assets/sequencediagrams/mvp_interactions/001_initial_interaction.txt)

### Future enhancements

Define characteristics (metadata) for each option so that more nuanced
insights can be made. For example, if the options are cars, characteristics
could include size, colour, price, ...

Store these results in a graph database to allow for more complex queries and
analysis.

Add some form of machine learning to predict user preferences based on their
past choices.


### Architecture Diagram

## 5. Technical Stack

Most of these decisions will be made based on familiarity with tools and
practices that I want to develop.

### Data store

#### Requirements

* Store options (e.g., images of cars) along with their metadata.
* Store user choices and build a preference profile.

#### Decision

For this simple data storage a relational database like SQLite or PostgreSQL
would be sufficient. In future stages when thinking about more complex queries
and relationships a graph database like Neo4j could be considered. This
graph database could build off the relational database or replace it when
the complexity of the data and queries increases.

### Backend

#### Requirements

* Serve options to the frontend.
* Record user choices.
* Provide APIs for data retrieval and analysis.

#### Decision

A lightweight web framework would be sufficient. Since Python is highly
familiar then using FastAPI would be a good choice.

When building the API should remain functionally isolated from the web HTTP API
to allow for easier testing and potential reuse in other contexts.

### Frontend

#### Requirements

* Display two options to the user.
* Capture user input (choice between the two options).
* Provide a user-friendly and visually appealing interface.

#### Decision

A simple web frontend using HTML, CSS, and JavaScript would be
sufficient. However, to practice more framework orientated development using
React would be a good choice.

### Image storage

#### Requirements

* Store and serve images of options (e.g., cars).

#### Decision

For simplicity, images can be stored on the server's filesystem during
development. In a production environment, a cloud storage solution like
AWS S3 or Google Cloud Storage would be more appropriate.


## 6. Data Models

### User
*   id: Unique identifier for the user.
*   username: User's chosen username.

### Option
*   id: Unique identifier for the option.
*   name: Name or title of the option.
*   image_url: URL or path to the image representing the option.
*   metadata: Additional information about the option (e.g.,
characteristics). Blob or JSON field.

### UserChoice
*   id: Unique identifier for the choice event.
*   user_id: Identifier for the user who made the choice. (FK relationship
to User)
*   chosen_option_id: The single option chosen by the user from the presented
list. Can be null if the user skips. (FK relationship to Option)
*   timestamp: Date and time when the choice was made.

### PresentedChoice (Join Table)
*   id: Unique identifier for this entry.
*   user_choice_id: Identifier for the choice event. (FK relationship to
UserChoice)
*   option_id: Identifier for one of the options presented to the user. (FK
relationship to Option)

Although not required for MVP having a `User` model allows for future
expansion to
support multiple users and personalized preference profiles. For the MVP,
a full
user registration system will not be implemented. Instead, a unique session ID
will be generated for each visitor (stored in a cookie or local storage)
and this
will be used as the `user_id` to associate choices with a single, anonymous
user.

## 7. API Design

### HTTP Endpoints

*   **`GET /options`**: Retrieve two options for the user to choose from.
    *   **Success Response (`200 OK`):**
        ```json
        [
            {
                "id": 123,
                "name": "Ford Mustang",
                "image_url": "/images/mustang.jpg",
                "metadata": {"year": 2022, "color": "Red"}
            },
            {
                "id": 456,
                "name": "Chevrolet Camaro",
                "image_url": "/images/camaro.jpg",
                "metadata": {"year": 2023, "color": "Black"}
            }
        ]
        ```

*   **`POST /choices`**: Record the user's choice.
    *   **Request Body:**
        ```json
        {
          "user_id": "session_abc123",
          "presented_option_ids": [123, 456],
          "chosen_option_id": 456
        }
        ```
    *   **Success Response (`201 Created`):** Empty body.
    *   **Error Response (`400 Bad Request`):** Body contains error details
    if the input is malformed.

*   **`GET /preferences`**: Retrieve the user's preference profile based on
their choices. (Not required for MVP)

### Backend API

*   `get_random_options()`: Fetch two distinct options from the database
that the current user has seen the least. If there's a tie, select randomly
from that pool. This ensures a more even and unique distribution of options
presented to the user.
*   `record_user_choice(user_id, presented_option_ids, chosen_option_id)`:
Store the user's choice in the database. This involves creating a `UserChoice`
record and multiple `PresentedChoice` records.


## 8. User Interface (UI) / User Experience (UX) Considerations

*   **Workflow:**
    1.  The user visits the main page and is immediately presented with two
    car images side-by-side.
    2.  To indicate a preference, the user clicks on one of the images.
    3.  A "Skip" or "Neither" button will be available below the images for
    the user to bypass the choice.
    4.  Once a choice is made (or skipped), the application seamlessly loads
    the next pair of images.
    5.  A separate page or a dedicated section on the main page will be
    available to view a summary of the user's preferences.
*   **Visual Design:**
    *   The design should be clean, modern, and minimalist to ensure the
    primary focus remains on the images being compared.
    *   Generous use of white space and clear, legible typography will
    be employed.

## 9. Testing Strategy

*   **Unit Tests:** The backend's business logic (e.g., option selection,
choice recording) will be tested using a framework like `pytest`. The API
layer will be kept thin to maximize testable logic.
*   **Integration Tests:** API-level tests will be written to verify the
HTTP endpoints, ensuring correct request handling and response formatting.
*   **Frontend Tests:** Key React components will have unit tests using a
framework like Jest and React Testing Library. End-to-end user flows will
be tested using Playwright.

## 10. Future Considerations / Open Questions

*   **Data Sourcing:** How will the initial set of car images and data be
sourced and loaded into the database?
*   **Preference Analysis:** What is the initial strategy for analyzing user
preferences? (e.g., simple ranking by number of wins, analyzing metadata of
winning options).
*   **Authentication:** How do we handle user authentication and management
if the application is expanded to support multiple users?
*   **User Content:** Could we allow users to upload their own options to
compare in the future?

