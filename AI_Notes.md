# AI Usage Notes

## AI Tools Used

- ChatGPT (OpenAI)
- GitHub Copilot / Codex

## 1. AI-generated vs. manually written code

ChatGPT was used to:
- Explain FastAPI concepts and project architecture.
- Guide the implementation of the API endpoints.
- Help design the project structure.
- Explain Pydantic models and JSON file storage.
- Help write automated tests.
- Help prepare the README and this AI_NOTES document.

GitHub Codex was used to:
- Review the completed project like a pull request.
- Suggest improvements related to code quality, validation, testing, and API documentation.

I manually integrated the suggestions that improved the project while keeping the implementation simple and appropriate for the assignment.

## 2. Validation and changes made

I manually:
- Tested every API endpoint using Swagger UI.
- Ran the automated test suite using pytest.
- Improved the storage layer to safely handle missing or empty JSON files.
- Improved request validation by trimming whitespace from string inputs.
- Added response models to improve the generated OpenAPI documentation.
- Improved the test suite by using a temporary JSON file for test isolation.
- Added additional tests for invalid input and missing resources.

## 3. AI suggestions not adopted

Some AI suggestions were intentionally not implemented because they would make the project unnecessarily complex for this assignment. Examples include:
- Replacing JSON storage with a database.
- Converting the application to an asynchronous architecture.
- Introducing advanced design patterns or additional frameworks.

The goal was to keep the project simple, readable, and aligned with the assignment requirements.