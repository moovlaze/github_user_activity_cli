import requests

r = requests.get('https://api.github.com/users/moovlaze/events')

response = r.json()

for resp in reversed(response):

  if resp.get('type') == 'CreateEvent':
    # events_dict.setdefault(resp.get('type'), []).append(
    # {
    #   "ref_type": resp.get('payload').get('ref_type'),
    #   "repo": resp.get('repo').get('name'),
    #   "ref": resp.get('payload').get('ref'),
    #   "created_at": resp.get('created_at')
    # })
    print(f'- User CREATED {resp.get('payload').get('ref_type')} {resp.get('repo').get('name')}')

  if resp.get('type') == 'PushEvent':
    # events_dict.setdefault(resp.get('type'), [])

    # events_dict[resp.get('type')].append({
    #   "repo": resp.get('repo').get('name'),
    #   "commits": len(resp.get('payload').get('commits'))
    # })
    # repo_name = resp.get('repo').get('name')
    # commit_count = 0

    # if resp.get('repo').get('name') == repo_name:
    #   commit_count += 1
    # else:
    #    repo_name = resp.get('repo').get('name')

    print(f'- User PUSH {len(resp.get('payload').get('commits'))} commits to {resp.get('repo').get('name')}')

  if resp.get('type') == 'WatchEvent':
    print(f'- User STARRED {resp.get('repo').get('name')}')

    
# print(events_dict)

# for item in events_dict['CreateEvent']:
  
#   if item['ref_type'] == 'repository':
#     print(f'- Создал репозиторий  {item['repo']} в {item['created_at']}')

#   if item['ref_type'] == 'branch':
#     print(f'\t- Создал ветку  {item['ref']} в {item['created_at']} \n')

# for item in events_dict['PushEvent']:

#   print(item)