# SauceDemo QA Automation Project

Automated end-to-end UI testing project built with **Python, Playwright, and Pytest** using the SauceDemo e-commerce application.

This project demonstrates automated testing of common user workflows including authentication, inventory validation, product sorting, shopping cart functionality, checkout, form validation, and logout.

## Technologies Used

- Python
- Playwright
- Pytest
- pytest-playwright
- Git / GitHub
- VS Code

## Test Coverage

The automated regression suite contains **12 tests** covering:

- Valid user login
- Invalid login
- Locked-out user validation
- Inventory validation
- Product details validation
- Product sorting: low to high
- Product sorting: high to low
- Adding multiple products to the cart
- Removing an item from the cart
- Complete checkout workflow
- Checkout form validation
- User logout

## Project Structure

```text
playwright-python-qa-portfolio/
├── SauceDemo/
│   └── tests/
│       ├── conftest.py
│       ├── test_cart_count.py
│       ├── test_checkout.py
│       ├── test_checkout_validation.py
│       ├── test_invalid_login.py
│       ├── test_inventory.py
│       ├── test_locked_user.py
│       ├── test_login.py
│       ├── test_logout.py
│       ├── test_product_details.py
│       ├── test_remove_item.py
│       ├── test_sort_high_to_low.py
│       └── test_sort_low_to_high.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Pytest Fixtures

A reusable Pytest fixture is defined in `conftest.py` to handle common login setup for tests that require an authenticated user.

This reduces duplicated code and makes the test suite easier to maintain.

## Installation

Clone the repository and create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser binaries:

```bash
playwright install
```

## Running the Tests

Run the complete regression suite:

```bash
pytest SauceDemo/tests -v
```

Run tests with the browser visible:

```bash
pytest SauceDemo/tests -v --headed
```

Run an individual test:

```bash
pytest SauceDemo/tests/test_checkout.py -v
```

## Automation Scenarios

The suite validates both positive and negative scenarios, including successful user workflows and expected application behavior when invalid or incomplete information is provided.

Examples include verifying product prices are correctly sorted, confirming cart item counts, validating required checkout information, and confirming successful order completion.

## Future Improvements

Planned improvements include:

- Page Object Model (POM)
- GitHub Actions CI/CD
- API test automation
- Additional test data and parameterization
- Cross-browser testing

## Author

**Dominique Derosena**

QA / Software Test Automation Portfolio