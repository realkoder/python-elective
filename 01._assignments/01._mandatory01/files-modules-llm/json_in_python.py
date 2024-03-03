import os
import subprocess
import requests

# blackjack_hand = (8, "q")
# encoded_hand = json.dumps(blackjack_hand)
# decoded_hand = json.load(encoded_hand)


# response = requests.get("https://api.github.com/orgs/python-elective-kea/repos")
# if (response.ok):
#     python_repos = json.loads(response.text)
#     for repo in python_repos:
#         print(repo)


# Function to fetch clone URLs of repositories from GitHub API
def fetch_repo_clone_urls():
    url = 'https://api.github.com/orgs/python-elective-kea/repos'
    response = requests.get(url)
    data = response.json()
    clone_urls = [repo['clone_url'] for repo in data]
    return clone_urls

# Function to write clone URLs to a file
def write_clone_urls_to_file(clone_urls):
    with open('clone_urls.txt', 'w') as f:
        for url in clone_urls:
            f.write(url + '\n')
    print('Clone URLs written to clone_urls.txt')

# Function to create a folder for the repositories
def create_repo_folder():
    try:
        os.mkdir('python-elective-kea-repos')
        print('Repository folder created')
    except OSError as error:
        print('Error creating repository folder:', error)

# Function to clone repositories into the folder
def clone_repos(clone_urls):
    for url in clone_urls:
        command = f'git clone {url}'
        try:
            subprocess.run(command, cwd='python-elective-kea-repos', shell=True, check=True)
        except subprocess.CalledProcessError as error:
            print(f'Error cloning repository from {url}:', error)

# Main function to orchestrate the process
def main():
    clone_urls = fetch_repo_clone_urls()
    
    write_clone_urls_to_file(clone_urls)
        
    create_repo_folder()
    
    clone_repos(clone_urls)

# Run the main function
if __name__ == "__main__":
    main()