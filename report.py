#!/usr/bin/env python

# Imports
import psycopg2
import datetime

# DB Connection
db = psycopg2.connect("dbname=news")

# Create a cursor, use this to perform queries
cursor = db.cursor()
file = open("log.txt", "w")
time = datetime.datetime.now()
file.write("--- New Report: " + str(time) + " ---")


def reportArticles():
    print "Getting top 3 Articles..."

    file.write("\nTop 3 Articles by Views:\n")

    # Query to execute
    topArticlesQuery = """
    SELECT a.title, COUNT(*) AS views
    FROM articles a
    JOIN log l ON l.path LIKE '%' || a.slug || '%'
    GROUP BY a.title
    ORDER BY views DESC
    LIMIT 3
    """
    cursor.execute(topArticlesQuery)  # Execute the query
    topArticles = cursor.fetchall()  # Fetch all results into variable
    for a in topArticles:
        # A line of text for each result
        file.write("Article \"" + a[0] + "\": " + str(a[1]) + " views.\n")
    print "Done."


def reportAuthors():
    print "Getting top 4 authors..."

    file.write("\nTop 4 Authors by Views:\n")

    # Query to execute
    topAuthorsQuery = """
    SELECT au.name, count(*) as views
    FROM authors au
    LEFT JOIN articles ar ON au.id = ar.author
    JOIN log l ON l.path LIKE '%' || ar.slug || '%'
    GROUP BY au.name
    ORDER BY views DESC
    LIMIT 4
    """
    cursor.execute(topAuthorsQuery)  # Execute the query
    topAuthors = cursor.fetchall()  # Fetch all results into variable
    for a in topAuthors:
        # For each result, print a line of text.
        file.write("Author \"" + a[0] + "\": " + str(a[1]) + " views.\n")
    print "Done."


def reportLogErrors():
    print "Getting error logs..."

    file.write("\nDays on which more than 1 percent of requests had errors:\n")

    # Get Log
    logQuery = """
    SELECT cast(l.time as date) AS day,
    COUNT(*) AS total,
    l2.errors AS errors,
    ROUND((l2.errors * 100) / COUNT(*)::numeric, 3) AS error_perc
    FROM log l
    LEFT JOIN (
        SELECT COUNT(l2.status) AS errors,
        date_trunc('day', l2.time) AS error_day
        FROM log l2
        WHERE l2.status NOT LIKE '%200%'
        GROUP BY error_day
        ) l2 ON date_trunc('day', l.time) = l2.error_day
    GROUP BY day, l2.errors
    HAVING ROUND((l2.errors * 100) / COUNT(*), 3) >= 1
    """
    cursor.execute(logQuery)
    logs = cursor.fetchall()
    if len(logs) > 0:
        for log in logs:
            file.write(str(log[0]) + ": " + str(log[3]) + "%\n")
    else:
        file.write("No days had more than 1 percent errors")
    print "Done."

reportArticles()
reportAuthors()
reportLogErrors()

print "Done, see log.txt in \"./\" directory"

# close DB Connection once program has run.
cursor.close()
db.close()
file.close()
