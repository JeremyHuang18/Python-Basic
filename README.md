# Online Examination System

### 1. Roles

#### Base Class: `User`
- **Attributes**:
  - `username`: The username of the user.
- **Methods**:
  - `get_role()`: Returns the string `"User"`.
  - `__str__()`: Returns a formatted string: `"Username: {username}, Role: {role}"`, where `{role}` is obtained using the `get_role()` method.

#### Derived Class: `Student`
- **Inherits from `User`**, with additional functionality:
  - **Attributes**:
    - `student_id`: A unique identifier for the student.
  - **Methods**:
    - Overrides `get_role()`: Returns the string `"Student"`.
    - `submit_exam(exam_name)`: Accepts the name of an exam as a parameter and prints a formatted message: `"{username} has submitted the exam: {exam_name}"`.

---

### 2. Functional Requirements
a. Implement the `User` and `Student` classes as described.  
b. Test the system by:
   - Creating a `Student` object with a username and student ID.
   - Calling the `__str__()` method to display the student’s information.
   - Calling the `submit_exam()` method with an exam name to simulate the student submitting an exam.

---

# Virtual Banking System

### 1. Class Design

#### Base Class: `Account`
- **Attributes**:
  - `account_number`: A unique identifier for each account, automatically assigned with an incrementing number starting from 1000.
  - `balance`: The current account balance.
- **Methods**:
  - `deposit(amount)`: Increases the account balance. Raises a `ValueError` if the deposit amount is less than or equal to 0, with the message `"Deposit amount must be positive."`
  - `withdraw(amount)`: Decreases the account balance. Raises a `ValueError` if the withdrawal amount is greater than the current balance or less than or equal to 0, with appropriate error messages: `"Insufficient balance"` or `"Withdraw amount must be positive."`
  - `__str__()`: Returns a formatted string: `"Account Number: {account_number}, Balance: {balance:.2f}."`
- **Class Attribute**:
  - `next_account_number`: A static attribute that stores the next available account number.
- **Static Method**:
  - `validate_amount(amount)`: Validates whether the given amount is positive. Raises a `ValueError` if the amount is invalid.

#### Derived Class: `SavingsAccount`
- **Inherits from `Account`**, with additional functionality:
  - **Attributes**:
    - `interest_rate`: The interest rate for the savings account, defaulting to 3% (`0.03`).
  - **Methods**:
    - `apply_interest()`: Applies the interest rate to the account balance, increasing it accordingly.
    - Overrides `__str__()`: Extends the string representation to include the interest rate: `"Account Number: {account_number}, Balance: {balance:.2f}, Interest Rate: {interest_rate:.2%}."`

---

### 2. Functional Requirements
a. Implement the above classes and their functionalities.  
b. Test the system by:
   - Creating two `Account` objects, performing deposit and withdrawal operations, and printing their details.
   - Creating a `SavingsAccount` object, performing deposit operations, applying interest, and printing its details.
   - Testing invalid deposit and withdrawal scenarios (e.g., negative or excessive amounts) and handling exceptions with meaningful error messages.