import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1
# Return all the columns for planets that have 0 moons.
df_no_moons = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
    """,
    conn1
)

# STEP 2
# Return the name and mass of each planet that has a name with exactly 7 letters.
df_name_seven = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
    """,
    conn1
)

##### Part 2: Advanced Filtering #####

# STEP 3
# Return the name and mass for each planet that has a mass <= 1.00.
df_mass = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
    """,
    conn1
)

# STEP 4
# Return all columns for planets that have at least one moon and mass < 1.00.
df_mass_moon = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
    """,
    conn1
)

# STEP 5
# Return the name and color of planets that have a color containing the string "blue".
df_blue = pd.read_sql(
    """
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
    """,
    conn1
)

##### Part 3: Ordering and Limiting #####

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Return name, age, breed of hungry dogs (hungry=1), sorted youngest to oldest.
df_hungry = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
    """,
    conn2
)

# STEP 7
# Return name, age, hungry for hungry dogs between ages 2 and 7, sorted A-Z by name.
df_hungry_ages = pd.read_sql(
    """
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
    """,
    conn2
)

# STEP 8
# Return name, age, breed for the 4 oldest dogs
df_4_oldest = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, breed ASC
    LIMIT 4;
    """,
    conn2
)

##### Part 4: Aggregation #####

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Return the total number of years that Babe Ruth played professional baseball.
df_ruth_years = pd.read_sql(
    """
    SELECT COUNT(DISTINCT year) AS total_years
    FROM babe_ruth_stats;
    """,
    conn3
)

# STEP 10
# Return the total number of home runs hit by Babe Ruth during his career.
df_hr_total = pd.read_sql(
    """
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
    """,
    conn3
)

##### Part 5: Grouping and Aggregation #####

# STEP 11
# For each team, return team and number of years played (aliased as number_years).
df_teams_years = pd.read_sql(
    """
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
    """,
    conn3
)

# STEP 12
# For each team Babe Ruth played on and averaged over 200 at-bats with,
# return team and average at_bats (aliased as average_at_bats).
df_at_bats = pd.read_sql(
    """
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200;
    """,
    conn3
)

conn1.close()
conn2.close()
conn3.close()
