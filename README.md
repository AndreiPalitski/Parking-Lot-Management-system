# Parking Lot Management System

## Overview
This is a simple Python-based Parking Lot Management System that allows users to:
- Add cars to the parking lot
- Remove cars from the parking lot
- Check parking prices
- Administrator parking settings (price per hour, capacity, clear parking lot, etc.)
- Save parking data to a CSV file
- Calculate parking fees based on time parked

## Features
- **Car Management:** Add, remove, and find cars by number.
- **Pricing System:** Set and update parking prices per hour.
- **Admin Panel:** Change lot capacity, clear parking data, and view statistics.
- **Time-Based Billing:** Calculates total hours parked and corresponding fee.
- **Persistent Storage:** Saves parking data in a CSV file.

## Requirements
- Python 3.x

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/parking-lot-system.git
   cd parking-lot-system
   ```
2. Run the script:
   ```sh
   python parking.py
   ```

## Usage
### Menu Options:
1. **Enter a Car** - Add a new car to the parking lot.
2. **Remove a Car** - Remove a car using its car number.
3. **Show Parking Price** - Display the current price per hour.
4. **Admin Panel** - Access admin features (requires login: `admin/admin`).
5. **Exit** - Quit the program.

### Admin Panel Options:
1. Change price per hour
2. Change maximum capacity
3. Clear parking lot
4. Show all parked cars
5. Show cars parked for more than 24 hours
6. Exit

## Data Storage
- **Parking data is saved in `Parking_Data.csv`**, containing:
  - Car Number
  - Phone Number
  - Arrival Time

## Future Improvements
- Implement a GUI for better user experience
- Integrate database storage instead of CSV files
- Add real-time notifications for cars parked over 24 hours

---

Enjoy using the Parking Lot Management System! 🚗

