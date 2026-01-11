# This or That: A Gemini Collaboration

This document outlines the development practices and conventions for the `thisorthat` project, a collaboration between a human developer and Gemini.

## 1. Project Overview

`thisorthat` is a tool designed to help users make decisions and discover their preferences by comparing two items at a time. The initial use case is for choosing a car within a specific price range. By presenting pairs of car images, the application will help the user either identify a specific "best" car or uncover common features and styles they prefer.

The long-term vision is for the application to be generic, allowing it to be adapted to compare anything, not just cars.

## 2. Development Workflow

We will follow a simple, iterative process for development:

1.  **Design:** For any new feature or significant change, we will first collaborate on and update the project's design document, located at `docs/DesignDocument.md`.
2.  **Implement:** Gemini will write the code based on the approved design.
3.  **Test:** Gemini will write and run automated tests to ensure the implementation is correct and robust.
4.  **Review:** The project owner will review the changes.

## 3. Technical Standards

*   **Primary Language(s):** To be determined during implementation (Python for backend, JavaScript/TypeScript for frontend).
*   **Code Style & Linting:** To be determined during implementation (e.g., Black/Ruff for Python, Prettier/ESLint for JavaScript/TypeScript).
*   **Testing Framework:** Backend: `pytest`. Frontend: Jest, React Testing Library, and Playwright.

## 4. Our Collaboration

*   **My (Gemini's) Role:** To act as an AI software engineering partner, assisting with design, coding, testing, and documentation.
*   **Your Role:** To act as the project owner, providing direction, making final decisions, and reviewing the work.
