
# Robot Movement Simulation

This is a simple Python project that simulates robots moving in a grid using commands like `N2`, `E3`, `S1`, and `W2`.
 

--- 

Each robot:
- Starts at position  (0, 0)
- Moves step-by-step in a grid
- Stops before entering a cell that already has another robot

---

## 🔧 How to Set Up and Run the Project

### Step 1: Clone or Download the Code

**Using Git (recommended):**

```bash
git clone https://github.com/Priyasankar09/robot-movement.git
cd robot-movement
````

---

### Step 2: Run the Code Manually (main.py)

You can test robot movement manually using `main.py`.

To run it:

```bash
python main.py
```

**Expected output example:**

```
Robot 1 created at position (0, 0).
Robot 2 created at position (0, 0).
Robot 1 moved to position (0, 2).
Robot 1 moved to position (1, 2).
Robot 2 moved to position (0, 2).
Another robot is in the way. Stopped moving.
Robot 2 moved to position (0, 2).
Robot 1 is at: (1, 2)
Robot 2 is at: (0, 2)
```

---

### Step 3: Run the Unit Tests (test\_robot.py)

This will automatically check if your robot logic is working correctly.

To run the tests:

```bash
python test_robot.py
```

**Expected output:**

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

If you see `OK`, your code is correct!

---

## 📌 Command Format

Use 2-character commands to move the robots:

* **N** = North (up)
* **S** = South (down)
* **E** = East (right)
* **W** = West (left)

**Example commands:**

* `N3` → Move 3 steps up
* `E2` → Move 2 steps right
* `S1` → Move 1 step down

---

## 🧠 Rules to Remember

* All robots start at `(0, 0)`
* Robots cannot go outside the grid
* Robots stop before entering a cell already occupied by another robot
* The grid size is defined like:
  `terrain = Terrain(5, 5)` → 5 rows and 5 columns

---

## 🛠 Requirements

* Python 3.6 or higher
* No third-party packages required (only built-in modules)

--
