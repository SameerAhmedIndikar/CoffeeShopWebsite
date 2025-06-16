# CoffeeShop

## Developed and Customized by
**Sameer Ahmed Indikar** – [GitHub @SameerAhmedIndikar](https://github.com/SameerAhmedIndikar)

---

## 📜 Credits
This project was adapted from an educational Django base. It has been extensively customized, refactored, and maintained by **Sameer Ahmed Indikar** to reflect original work and enhancements.

---

## Project Overview:
CoffeeShop is a Django web application that simulates an online coffee shop where users can browse a coffee menu and the detail page of each item in the menu, register, log in, add items to their cart, make online payments, like products, and leave ratings and reviews for products.

## Project Structure:
The project consists of 4 main applications:

1. **Users Application**  
   Handles authentication and registration using email. Includes email confirmation, OTP-based mobile confirmation, and profile creation via signals.

2. **Pages Application**  
   Displays all frontend views like index, about, admin dashboard, etc.

3. **Products Application**  
   Displays the coffee menu and product details. Includes features like search, like, rate, review, and add-to-cart (with quantity selection).

4. **Ecommerce Application**  
   Manages the cart and online payments. Includes order creation, cart quantity adjustments, checkout, and payment integration (e.g., Stripe).

## User Workflow:

- **Registration/Login**: Users register with email and password, confirm email, and can optionally enable 2FA via OTP.
- **Browsing**: Guests can view the coffee menu and product details.
- **Cart & Orders**: Authenticated users can add products to the cart, adjust quantities, and place orders.
- **Payment**: Online payment is processed via secure gateway.
- **Interaction**: Logged-in users can like, rate, and review products.

## Admin Panel:

- Add/edit/delete products
- View/manage users
- Track orders and update order statuses
- Admin dashboard includes dynamic charts and data tables

## Technology Stack:

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: PostgreSQL
- **Payment Gateway**: Stripe
- **Env Management**: `python-dotenv`

## Security Considerations:

- Use of `.env` files to store sensitive data
- Authentication and 2FA
- Input validation to avoid SQL injection and other vulnerabilities
- Dependency updates and patching

## Testing and Deployment:

- Unit testing and UAT recommended
- Production-ready setup via a secure server
- Git used for version control

## User Experience:

- Fully responsive UI for desktop and mobile
- User feedback incorporated via a "Contact Us" page

## Documentation:

Includes clear setup and usage instructions for developers to run locally and in production.

---

## System Architecture:
![coffeshop_project](https://github.com/mayals/CoffeeShop_django_v2/assets/48769543/43772f4f-d782-4cb2-bfcf-6573ba242832)

## ER Diagram:
![Coffeeshop_dbdiagram](https://github.com/mayals/CoffeeShop_django_v2/assets/48769543/15f0389e-011b-4676-b276-a001aed6de95)  
https://dbdiagram.io/d/Coffeeshop-6505b34302bd1c4a5eb1811a

---

## Getting Started:

To run CoffeeShop project locally:

1. Clone this repo  
   ```bash
   git clone https://github.com/SameerAhmedIndikar/CoffeeShopWebsite.git
