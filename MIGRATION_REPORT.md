ENRIQUEZ, EFREN JOHN 08/07/2026 MIGRATION REPORT

# MIGRATION REPORT

## 1. Legacy Architecture

The original project was a monolithic Python MVC application. The controller directly interacted with the authentication module, library system, and math operations module.

## 2. Code Smells Identified

1. Tight Coupling
   - The controller directly instantiated other modules.

2. God Controller
   - The controller handled multiple responsibilities.

3. Limited Modularity
   - Business logic was spread across different files without clear service boundaries.

## 3. Migration to Microservices

The application was reorganized into service-based modules:

- Authentication Service
- Library Service
- Math Service

A Factory Pattern was introduced to dynamically provide the required service.

The Math Service uses the Strategy Pattern to switch between Encryption and Compression algorithms.

## 4. AI Assistance

AI was used to:

- Generate the initial Factory Pattern.
- Generate the initial Strategy Pattern.
- Suggest the C4 Level 2 Container Diagram.
- Suggest the microservice architecture.

## 5. Manual Corrections

The following corrections were made manually after reviewing the AI-generated output:

- Updated import statements to match the project's folder structure.
- Renamed classes to follow the project's naming conventions.
- Corrected method names that did not exist in the project.
- Fixed syntax errors in the generated code.
- Removed unused variables and imports.
- Verified that the project compiled and all tests passed.
- Adjusted the Factory implementation to work with the existing MVC controller.

## 6. Verification

The application was tested successfully.

- Unit tests executed using pytest.
- Strategy Pattern processed the required dataset.
- Factory Pattern correctly instantiated services.
- Application executed without runtime errors.

## Manual Corrections

ChatGPT generated an initial version of the C4 Level 2 Container Diagram and example implementations of the Factory and Strategy patterns.

The following manual changes were made:

- Adapted the generated design to match my project's actual folder structure.
- Updated import paths to match the repository.
- Renamed service classes to fit the existing codebase.
- Verified that all generated code ran correctly with the project.
- Tested the application and corrected minor syntax and logic issues where necessary.

## JWT Authentication Process

1. The client sends a username and password to the authentication service.
2. The server verifies the credentials.
3. If valid, the server creates a signed JWT using the HS256 algorithm and a secret key.
4. The token is returned to the client.
5. The client includes the JWT in the Authorization header for future requests.
6. The server verifies the token's signature before granting access to protected resources.
7. If the signature is invalid or the token has expired, access is denied.