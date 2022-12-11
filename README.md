This is a project that has the intention of automating the match creation for BJJ tournaments. It is simple, but also effective and flexible. It creates a stack of objects that is useful for more and more complex tournaments. The stack from simple to more complex goes as follows:
- Belt #Implemented!
- Fighter #Implemented!
- Match #Implemented!
- Category #Implemented!
- Tournament #Not implemented
This project is used for studies and also to test the limits of my knowledge in pure python programming. Feel free to use it for whatever means.

This readme will be updated along with the project.

Here we will list the objects that compose our system (They will be listed and explained in an order of simplicity/deepness in stack):

Belt: Nothing but a support object that represents the belt of a fighter.
It can be initiated with a simple argument, and int of 0 to 4, representing the belt of the fighter:
- 0 : White
- 1 : Blue
- 2 : Purple
- 3 : Brown
- 4 : Black
It's only purpose is to be a more safe way of determining belt, being intiated with a set number of options and returning a pre determined string when needed. The previous design choice was to accept any string as argument, which seemed very unsafe code.

Fighter: It's data type created with the intention of representing Fighter data in memory, that way we can use it on our Category and Tournament objects. It's arguments are very specific and essential for the accurate representation of our fighters. To be even more precise in our representation, a UID is used as a primary key for each fighter. This UID can be create when a fighter object is initialized or it can be put in initialization as an argument.
Arguments:
- name=Full name of the fighter | string
- weight=Weight of the fighter in kilograms | float
- belt_number=Number used to initialize the Belt object that will represents the fighters belt | int
- age=Fighter's age | int
- sex=Fighter's sex, will be used to separate fighter in male and female category, can be represented only by a uppercase "M" or an uppercase "F", everything else will be discarded and raise an error | string
- uid=Optional argument (default=None), to be used only if the fighter is being pulled from the database and already has a determined uid, if this argument isnt established, the Fighter object will create a random uid for the fighter | UUID object

Match: Data type created to receive one or two Fighter objects, that will be used as the simply named attributes fighter1 and fighter2. after receiving 2 fighters, the match will be ready (checked with method .is_ready()) and can now be resolved. A object can be created with only 1 fighter, so you might need to add another fighter later, which can be used with the add_fighter() method. To resolve a match, call the method .resolve_match() and use as argument the int 1 or 2, representing the winner as fighter1 or fighter2. After that, you can check that the match is resolved using the method .is_resolved(), and it should represent the two fighter + winner if you print the object.
Arguments:
- fighter1=First fighter on the match | Fighter object
- fighter2=Second fighter on the match | Fighter object
Methods:
- return_fighters: returns a tuple of the present fighters in the object.
- is_ready: returns a boolean that says if the match is ready, that is, if both fighters are present.
- add_fighter: adds a fighter to a match that is not ready yet.
- resolve_match: resolves match, the winner is decided by the argument received. 1 = fighter1 wins, 2 = fighter2 wins.
- return_winner: return fighter object of the match winner
- return_loder: return fighter object of the match loser
- is_resolved: return boolean that indicates if the match is resolved, that is, if the match has a winner.
Use:
{
    match_object = Match(fighter1, fighter2)
    match_object.resolve_match(2)
}

Category: This class is made to represent a category (like flyweight, heavyweight, or even openweight). It will receives a list of fighter objects, then it creates matches based on those fighter objects, then it resolve those matches and create new ones based on the previous ones winners. This process continues until we have only one match with one winner, and this fighter object will represent the winner of this category.
Arguments: 
- fighter_list=List of fighters that will be part of this particular category. All Fighters here present will be used to create future matches. | list[Fighter]
Methods:
- add_fighter: Used to add fighter objects to the initial fighter list. Can be one or many (uses *args)
- return_fighters: Used to return the list of fighter objects that are part of this Category object.
- create_matches: Method that uses the fighter list present in the category object to create matches. Can also be forced to use a specific fighter list (useful when advancing the category).
- matches_are_ready: returns a boolean that indicates the category have created matches.
- return_matches: return a list of all the matches that were created, but only if matches are ready.
- resolve_category: responsible for resolving all matches currently in this category. Receives a number of arguments equal to the number of unsolved matches. In cases of uneven number of fighters, one must remember that the loser of the second to last match fights the fighter that should be alone on the last match.
- advance_category: Method responsible for taking the winners of the resolved matches and creating a new phase with new matches.
- check_for_winner: A method that checks if there is only one match, that it is resolved with one winner. That fighter will be the winner of the category.
- is_resolved: A method that returns a boolean that checks if the category is done and has a winner.
Use:
{
    example_category = Category(fighter_list) # instantiate object
    example_category.create_matches() # create matches
    {
        # loop until finished
        example_category.resolve_category(winners_numbers)
        example_category.advance_category()
    }
}

