import requests
import argparse

def view_activity(user_name):
  
  r = requests.get(f'https://api.github.com/users/{user_name}/events')

  response = r.json()
  
  if type(response) == dict and response.get('status') == '404':
    print('User not found')
    return

  commits_count = 0

  for resp in reversed(response):

    if resp.get('type') == 'CreateEvent':
      print(f'- User CREATED {resp.get('payload').get('ref_type')} {resp.get('repo').get('name')}')
      if resp.get('payload').get('ref_type') == 'branch':
        print(f'  - User PUSH {commits_count} commits to {resp.get('repo').get('name')}')
        commits_count = 0

    if resp.get('type') == 'PushEvent':
      print(f'- User PUSH {len(resp.get('payload').get('commits'))} commits to {resp.get('repo').get('name')}')

    if resp.get('type') == 'WatchEvent':
      print(f'- User STARRED {resp.get('repo').get('name')}')
      
      
if __name__ == '__main__':
  
  parser = argparse.ArgumentParser()

  parser.add_argument('user_name')

  args = parser.parse_args()

  view_activity(args.user_name)


