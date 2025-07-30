# Swag Labs Automation Project

This project contains automated end-to-end tests for the Swag Labs demo e-commerce website, built using Playwright.

## Automated Scenarios Covered
The current automation suite covers the following key user flows:

* **User Login:** Successful login with valid credentials.

* **Product Management:**
    * Adding a single item to the cart.
    * Adding multiple items to the cart.

* **Complete Checkout Process:**
    * Proceeding from cart to checkout.
    * Filling in user information.
    * Verifying order overview.
    * Completing the purchase.

## Technologies Used
* **Automation Framework:** Playwright
* **Language:** Python

## How to Run Tests
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pricilla123-34/shopping-cart-playwright.git](https://github.com/pricilla123-34/shopping-cart-playwright.git)
    cd shopping-cart-playwright
    ```
2.  **Install dependencies:**
    * **Python:**
        ```bash
        pip install -r requirements.txt
        playwright install
        ```
    *(Note: Ensure you have a `requirements.txt` file in your project root with `playwright`, `pytest`, and `pytest-playwright` listed, as discussed earlier.)*

3.  **Execute tests:**
    * **Python:**
        ```bash
        pytest
        ```
