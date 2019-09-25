free_storage_and_users = list(map(int, input().split()))
free_storage = free_storage_and_users[0]
number_of_users = free_storage_and_users[1]
users = []
for i in range(1, number_of_users + 1):
    user = int(input())
    users.append(user)
users = sorted(users)
users_storage = []
for user in users:
    if (sum(users_storage) + user) <= free_storage:
        users_storage.append(user)
    else:
        break
print(len(users_storage))
