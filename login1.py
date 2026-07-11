import datetime
logs = [
    'User login: Saif = SUCCESS',
    'User login: hacker = FAILED',
    'File access: admin = SUCCESS',
    'User login: unknown = FAILED'
    ]
print("=== SECURITY AUDIT REPORT ===")
print ("DATE: ", datetime.datetime.now())
for log in logs:
    status = 'ALERT' if 'FAILED' in log else 'OK'
    print(f'{status} -> {log}