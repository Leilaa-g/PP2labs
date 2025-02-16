yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.date())
print("Today:", current_date.date())
print("Tomorrow:", tomorrow.date())

