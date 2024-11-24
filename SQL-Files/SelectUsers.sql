SELECT *, salt::text, password_hash::text FROM api_users
ORDER BY userid ASC 
