# ============
# 1. The Math
# ============
# Python’s math module provides functions for mathematical operations.

# 🔹 Common Math Functions
import math
print(math.sqrt(16))  # Output: 4.0
print(math.pow(2, 3))  # Output: 8.0
print(math.pi)  # Output: 3.141592653589793

# ===================
# 2. DateTime Module
# ===================
# Python’s datetime module helps in handling date and time.

# 🔹 Getting Current Date and Time
from datetime import datetime
now = datetime.now()
print(now)  # Output: 2025-03-15 12:45:30.123456

# 🔹 Formatting Date and Time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # Output: 2025-03-15 12:45:30

# ===================
# 3. Calendar Module
# ===================
# Used for working with dates and calendars.

# 🔹 Printing a Calendar
import calendar
print(calendar.month(2025, 3))  # Prints the calendar for March 2025
