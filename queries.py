import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
  host="containers-us-west-190.railway.app",
    database="railway",
    user="postgres",
    password="u1npW6SnjJz3BHDi2Whx",
    port="7259"
)

# Create a cursor to execute SQL queries
cur = conn.cursor()

# Example query: Monthly sales trends over the years
cur.execute("""
    SELECT month, year, SUM(sales) AS total_sales
    FROM monthly_sales
    GROUP BY month, year
    ORDER BY year, month
""")
monthly_sales_trends = cur.fetchall()
print("Monthly Sales Trends:")
for row in monthly_sales_trends:
    print(f"Month: {row[0]}, Year: {row[1]}, Total Sales: {row[2]}")

# Example query: Top-selling products in a given month and year
target_month = 12
target_year = 2022
cur.execute("""
    SELECT month, year, product_name, sales
    FROM monthly_sales
    WHERE month = %s AND year = %s
    ORDER BY sales DESC
    LIMIT 5
""", (target_month, target_year))
top_selling_products = cur.fetchall()
print("\nTop-selling Products:")
for row in top_selling_products:
    print(f"Month: {row[0]}, Year: {row[1]}, Product Name: {row[2]}, Sales: {row[3]}")

# Example query: Top-selling product categories overall
cur.execute("""
    SELECT category, SUM(sales) AS total_sales
    FROM top_category_sales
    GROUP BY category
    ORDER BY total_sales DESC
    LIMIT 5
""")
top_selling_categories = cur.fetchall()
print("\nTop-selling Categories:")
for row in top_selling_categories:
    print(f"Category: {row[0]}, Total Sales: {row[1]}")

# Close the cursor and connection
cur.close()
conn.close()
