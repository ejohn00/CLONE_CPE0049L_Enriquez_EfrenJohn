ENRIQUEZ, EFREN JOHN 08/07/2026 AI USAGE LOG

# AI_USAGE_LOG.md

# AI Usage Log

**Student:** Efren John Enriquez  
**Course:** CPE0049L – Software Design Final Examination

---

## AI Tool Used

- ChatGPT (OpenAI)

---

# Interaction 1

### Prompt

Generate a C4 Level 2 Container Diagram for my Python MVC project.

### AI Output

Generated a C4 Level 2 Container Diagram based on the project structure, including the MVC application, authentication module, library system, math operations, and testing components. Also generated a Mermaid diagram and container descriptions.

### Manual Verification / Corrections

- Compared the generated diagram with the actual project structure.
- Verified that all containers matched the repository files.
- Updated the diagram description to reflect the project's architecture.

---

# Interaction 2

### Prompt

Explain how to migrate the monolithic application into a microservice architecture using the Factory Pattern and Strategy Pattern.

### AI Output

Explained the concepts of monolithic architecture, microservices, Factory Pattern, and Strategy Pattern. Suggested separating the Authentication, Library, and Math components into independent services.

### Manual Verification / Corrections

- Adapted the proposed architecture to fit the existing project.
- Updated folder and file names to match the repository.
- Reviewed the design before including it in the migration report.

---

# Interaction 3

### Prompt

Help implement JWT authentication for Task 2.

### AI Output

Generated example code for creating and verifying JSON Web Tokens using the PyJWT library.

### Manual Verification / Corrections

- Added the generated code to `auth_profile.py`.
- Verified token generation and token validation.
- Installed the required PyJWT package.
- Confirmed that the code executed successfully.

---

# Interaction 4

### Prompt

Help create unit tests for `auth_profile.py` to improve code coverage.

### AI Output

Generated unit tests for the `generate_token()` and `verify_token()` functions.

### Manual Verification / Corrections

- Corrected the test file to match the actual function names.
- Removed incorrect references to a non-existent `login()` function.
- Executed `pytest --cov=.` to verify the tests.
- Confirmed an overall code coverage of 95%.

---

# Interaction 5

### Prompt

Help create a GitHub Actions CI/CD workflow with flake8, Bandit, and pytest.

### AI Output

Generated a GitHub Actions workflow (`main.yml`) that:
- Checks out the repository
- Sets up Python
- Installs dependencies
- Runs flake8
- Runs Bandit
- Executes pytest with an 85% coverage requirement

### Manual Verification / Corrections

- Added the workflow file to `.github/workflows/`.
- Installed all required dependencies.
- Executed the workflow locally where possible.
- Fixed code style issues reported by flake8.
- Verified that unit tests passed with the required coverage.

---

# Interaction 6

### Prompt

Help create `SECURITY.md` and explain dependency pinning and JWT authentication.

### AI Output

Generated a security report describing:
- Dependency pinning
- Mock vulnerability findings
- Security recommendations
- JWT authentication process

### Manual Verification / Corrections

- Verified package versions in `requirements.txt`.
- Reviewed the recommendations before adding them to the report.
- Updated the report to match the implemented authentication service.

---

# Summary

ChatGPT was used as a development assistant for architecture planning, documentation, code examples, unit testing, and CI/CD configuration. All generated output was manually reviewed, tested, and modified where necessary before being incorporated into the final submission.