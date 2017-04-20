######################

# YOUR CODE GOES HERE

# Import the modules you'll need for this assignment (json, requests)
import requests 
import json 

######################

# This is a working API key for the ProPublica Congress API. Don't change it.
API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'

def get_votes_by_date(chamber, start_date, end_date):
    '''
    Return all votes from a given day. You will be provided four input variables here:
    chamber: Denotes the chamber (Senate or House)
    start_date: The beginning of the time window you'd like to search for votes
    end_date: The end of the time window
    Construct the URL by plugging them into the correct places. The ProPublica docs
    don't do a good job of explaining this with start/end dates, but the correct URL
    will look like:
    https://api.propublica.org/congress/v1/{chamber}/votes/{year}/{month}.json
    The URL should be stored in a variable called url.
    You should then process the resulting data using the json module and return it in
    a variable called data.
    '''

    ###################

    # YOUR CODE GOES HERE

    # Define the proper URL here. It should use the chamber, start_date and end_date arguments
    # provided by the function.
    
    dateObject = start_date.split("-") #[year,month,day]

    url = 'https://api.propublica.org/congress/v1/'+chamber+'/votes/'+dateObject[0]+'/'+dateObject[1]+'.json'

    ###################

    response = requests.get(url, headers={"X-API-Key": API_KEY}).content

    ###################

    # YOUR CODE GOES HERE

    # Define the data variable here and use it to process the response into Python objects.

    data = json.loads(response) # Replace this with whatever the data variable should be

    ###################

    return data


def format_nomination_votes(data):
    '''
    Your next task is to take the results of the API response, extract several of the most
    important pieces of information, and put them into a list. We do this at the Times to
    ultimately save the data into a database, but you could also use it to produce a CSV
    for analysis.
    Specifically, the information you'll need to extract from each result is:
    
    - Vote date
    - Vote question
    - Vote description
    - Vote result
    - Total number of votes for each "yes," "no," "present," and "not voting"
    The output of this function, which should be stored in the variable called output,
    should be a list of lists. Each list should contain the aforementioned pieces of
    information for each result you get back.
    For example (whitespace added to make this more clear):
    output = [
      ['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting'],
      ['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']
    ]
    Hint: You'll have to use a loop. Remember that you can add items to a list using the
    "append" method. So if you want to add a new record to output, you could do something
    like output.append(record)
    '''
    output = [['date', 'question', 'description', 'result', 'yes', 'no', 'present', 'not_voting']]

    ###################

    # YOUR CODE GOES HERE
    
    votes = data['results']['votes']
    for i in range(0,len(votes)-1):
        vote = votes[i]
        list = [];
        list.append(vote["date"])
        list.append(vote["question"])
        list.append(vote["description"])
        list.append(vote["result"])
        list.append(vote["total"]["yes"])
        list.append(vote["total"]["no"])
        list.append(vote["total"]["present"])
        list.append(vote["total"]["not_voting"])
        output.append[list]
    

    # Process each result from the input data (stored in the variable called "data") and 
    # store just the relevant information in a list. Append that list to the output list.

    ###################

    return output


########## YOU CAN IGNORE THIS ##########

if __name__ == '__main__':
    votes = get_votes_by_date('senate', '2017-04-06', '2017-04-06')

    if votes == None:
        print "Looks like you haven't finished implementing the get_votes_by_date method ..."
        exit()
    elif type(votes) != dict:
        print "Something's wrong. You might still need to process the data using the json module."
        exit()
    elif type(votes) == dict:
        print 'Your data looks ok!'
        print votes

    formatted = format_nomination_votes(votes)

    if len(formatted) <= 1:
        print 'You only seem to have one item in your output. Did you append records for the others?'
        exit()

    print 'Output:'
    print formatted