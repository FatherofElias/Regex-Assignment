# Question 1


# Task 1


import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = "exclude.com"

# Use a regex pattern to match email addresses, but exclude the specified domain
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)

# Filter out emails from the exclude_domain
filtered_emails = [email for email in emails if not email.endswith(f"@{exclude_domain}")]

print(filtered_emails)