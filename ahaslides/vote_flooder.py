import requests
import json
from threading import Thread

def send_action(num_threads_started, safety=None):
   print(num_threads_started, " started.")
   for i in range(num_loops):
    #    print(f"{str(i)}. run of Thread {str(num_threads_started)}")
        if choice == 1:
            requests.post(f"https://audience.ahaslides.com/api/slide-option/{option_id}/vote", data=body)
        elif choice == 2:
            requests.post(f"https://audience.ahaslides.com/api/slide-option/{option_id}/unvote", data=body)

def start_threads(num_threads):
    for t in range(num_threads):
        num_threads_started = str(int(t)+1)
        Thread(target=send_action, args=(num_threads_started,)).start()

choice = int(input("[1] Vote\n[2] Unvote\n"))

presentation_link = input("\nPresentation link: ")
presentation_id = presentation_link.split(sep="/")[3]

body = {
    "uniqueAccessCode":f"{presentation_id}",
    "numberOfVotes": 1
}

get_slide_id_link = f"https://audience.ahaslides.com/api/presentation/audience-data/{presentation_id}"
get_slide_id_request = json.loads(requests.get(get_slide_id_link).content)
slide_id = get_slide_id_request["activeSlide"]

list_options = json.loads(requests.get(f"https://audience.ahaslides.com/api/slide-option/list/?slideId={slide_id}").content)

print("\nChoose your option: \n")

for i in range(list_options["count"]):
    title = list_options["rows"][i]["title"]
    votes = list_options["rows"][i]["votesCount"]
    possible_option_id = list_options["rows"][i]["id"]
    print(f'{i+1}. ({votes} votes): {title}')

action_for = input("\nAction for item (number): ")
option_id = list_options["rows"][int(action_for)-1]["id"]

if choice == 1:
    number_of_votes = input("\nHow many Votes?: ")
    for i in range(20,0,-1):
        if int(number_of_votes)%i == 0:
            num_loops = int(int(number_of_votes)/i)
            print(f'\nStarting {i} Threads using {num_loops} loops. \nVoting [{list_options["rows"][int(action_for)-1]["title"]}] with id {option_id}, already having {list_options["rows"][int(action_for)-1]["votesCount"]} votes.')
            start_threads(i)
            break
        else:
            continue
elif choice == 2:
    number_of_unvotes = input("\nHow many Unvotes?: ")
    for i in range(20,0,-1):
        if int(number_of_unvotes)%i == 0:
            num_loops = int(int(number_of_unvotes)/i)
            print(
            f'\nStarting {i} Threads using {num_loops} loops. \nUnvoting [{list_options["rows"][int(action_for) - 1]["title"]}] with id {option_id}, already having {list_options["rows"][int(action_for) - 1]["votesCount"]} votes.')
            start_threads(i)
            break
        else:
            continue
