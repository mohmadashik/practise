-- Search Argument Able - Sargable
-- Tips to write Sargable Queries
    -- Avoid using functions or calculations on indexed columns in WHERE clause
    -- Use direct comparisons whenever possible, instead of wrapping the column in a function
    -- if we need to use a function on a column, consider creating a computed column or a function-based index, if the database supports it
    
