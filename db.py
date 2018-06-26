# Imports
import psycopg2

# DB Connection
db = psycopg2.connect("dbname=news")

# Create a cursor, use this to perform queries
cursor = db.cursor()


def reportArticles():
    # Get top 3 articles
    print "|----------------------| START"
    print "Top 3 Articles by Views:"

    # Query to execute
    topArticlesQuery = """
    SELECT a.title, COUNT(l.path) AS views
    FROM articles a
    JOIN log l ON l.path LIKE '%' || a.slug || '%'
    GROUP BY a.title
    ORDER BY views DESC
    LIMIT 3
    """
    cursor.execute(topArticlesQuery)  # Execute the query
    topArticles = cursor.fetchall()  # Fetch all results into variable
    colnames = [desc[0] for desc in cursor.description]
    print colnames
    for a in topArticles:
        # For each result, print a line of text to report the number of views.
        print "Article \"" + a[0] + "\" reached: " + str(a[1]) + " views."

    print "|----------------------| END"

    def reportAuthors():
        # Get top 3 articles
        print "|----------------------| START"
        print "Top 3 Authors by Views:"

        # Query to execute
        topAuthorsQuery = """
        SELECT au.name, count(ar.slug) as views
        FROM authors au
        LEFT JOIN articles ar ON au.id = ar.author
        JOIN log l ON l.path LIKE '%' || ar.slug || '%'
        GROUP BY au.name
        ORDER BY views DESC
        LIMIT 3
        """
        cursor.execute(topAuthorsQuery)  # Execute the query
        topAuthors = cursor.fetchall()  # Fetch all results into variable
        colnames = [desc[0] for desc in cursor.description]
        print colnames
        for a in topAuthors:
            # For each result, print a line of text.
            print "Author \"" + a[0] + "\" reached " + str(a[1]) + " views."

        print "|----------------------| END"


def reportLogErrors():
    # Get Log
    logQuery = """
    SELECT *
    FROM log
    WHERE status != '200 OK'
    """
    cursor.execute(logQuery)
    logs = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print colnames
    for log in logs:
        print log

# reportArticles()
# reportAuthors()
reportLogErrors()

# close DB Connection once program has run.
cursor.close()
db.close()
