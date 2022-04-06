# Presto
 Picks a restaurant based on your likes and dislikes if you cannot decide.

 ### Authors:
 Curtis Lin

 ### Date of Creation: 
 7/3/2020

 # Author Notes: 
 N/A

 ## Key Features:
 - Cost preferences: At runtime, the user will be asked if they want to spend less money. If yes, the user will have higher chances of getting a food choice that is less expensive. 

 - Distance preference: At runtime, the user will be asked if they are really hungry. If yes, the user will have higher chances of getting a food choice that is closer.

 - Adventurous perference: At runtime, the user will be asked if they are feeling Adventurous. If yes, the user will have higher chances of getting a food choice they have never been to. By default, there is slightly more bias towards food choices that the user has not been to. 

 - Unsatisfied choice: Once the user gets a restaurant choice, they will be asked if they are satisfied with their choice, if they aren't that food choice will be eliminated from the pool of possible restaurants that can be selected and the user will be given a new restaurant. 

 - Only Open Restaurants: The script has the ability to look at the current time and only give choices where the restaurant is actually open when the user arrives meaning it will give restaurants that are currently open and will still be open by the time the user arrives at the restaurant. 

 - Weekend Hours: The restaurants list textfile has the ability to store both weekday and weekend hours of a restaurant since some restaurants tend to have different hours. This is taken to account and the script deals with it.

 - Data logging: The script keeps a data log of everything at runtime in a separate text file called "randomRestaurantNameGeneratorLog.log". This is where you can see all of the restaurants that were added into the pool of possible choices, how many entries were given to each possible choice ,and all of the inputs recieved by the script. 

 ## How To Use:
  The input textfile is generated by hardcoding values onto the spreadsheet and copying all the values into a plain text file:
  https://docs.google.com/spreadsheets/d/1R47FkJCqLwFZHuWNRf7SFgiu41vsYzz7HqB7yJfqeGE/edit?usp=sharing

  See restaurantsList.txt for an example textfile that contains the user's tastes. 
  
  Once you have the input txtfile completed, change the input textfile that contains all of the user's perferred taste in restaurants in line 104:


## Packages Used:
 - Google Firebase
 - Yelp Fusion API
 - Next.JS - front end
 - FastAPI - back end

To run the front end:
```
yarn dev
```

To run the back end, open the venv in api:
```
uvicorn main:app --reload
```


