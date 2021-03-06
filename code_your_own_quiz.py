''' Game Play Steps 
1 Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard .
2 Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
3 When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank .
4 When player guesses incorrectly, they are prompted to try again. '''

# The quiz list containing the qwestions as items for easy, medium, hard respectively

quiz = ['''Eleven-year-old Harry Potter has been __1__ an ordinary life, constantly abused by his surly and cold uncle and aunt, Vernon and Petunia Dursley and bullied by their spoiled son Dudley.
His life changes on the day of his eleventh birthday when he receives a __2__ of acceptance into a Hogwarts School of Witchcraft and Wizardry, delivered by a half-giant named Rubeus Hagrid after 
previous letters had been destroyed by Vernon and Petunia. Hagrid explains Harry's hidden past as the wizard son of James and Lily Potter, who are a wizard and witch respectively, and how they were
murdered by the most __3__ and powerful dark wizard in history, Lord Voldemort, which resulted in the one-year-old Harry being sent to live with his aunt and uncle. The strangest bit of the murder was 
how Voldemort was unable to __4__ him, but instead had his powers removed and blasted away, sparking Harry's immense fame among the magical community.''',

        '''A month later, Harry leaves the Dursleys' home to catch the __1__ Express from King's Cross railway station's secret __1__ platform, Platform 9,3/4. On the train, he befriends fellow 
first-year __2__ Weasley and Hermione Granger, whose snobbiness and affinity for spells initially causes the two boys to dislike her. There, Harry also makes an enemy of yet another first-year, Draco Malfoy,
who prejudices against Hermione due to her being the daughter of Muggles, a term used by wizards and witches that describe ordinary humans with no __3__ ability.

Arriving at __1__, the first-years are assigned by the __3__ Sorting Hat to houses that best suit their personalities, the four Houses being __4__, __5__, Hufflepuff and Ravenclaw. 
Harry hears from Ron about __5__'s dark reputation which is known to house potential dark witches and wizards, and thus objects to being sorted into __5__ despite the Hat claiming that Harry has potential
to develop under that House. He winds up in __4__ instead with Ron and Hermione while Draco is sorted into __5__, like his whole family before him.''',

        '''A visit to Hagrid's cottage at the foot of the school leads the trio to find a newspaper report stating the attempted robbery of a __1__ vault-a vault that Hagrid had gone to take something while
showing Harry around. A further __2__ from Hagrid allows them to work out that the object kept under that trapdoor is a Philosopher's Stone, which grants its user immortality as long as it is constantly 
used, as well as the ability to turn any metal into pure gold. Harry is also informed by a centaur named __6__ in the forest that a plot to steal the Stone is being orchestrated by none other than Voldemort himself,
who schemes to use it to be restored back to his body and return to power. When the school's headmaster Albus Dumbledore is lured from Hogwarts under false __3__, Harry, Hermione and Ron fear that the theft is 
imminent and descend through the trapdoor themselves.

They encounter a series of obstacles, each of which requires unique skills possessed by one of the three, and one of which requires Ron to sacrifice himself in a life-sized game of wizard's chess. In the final room,
Harry, now alone, finds Quirinus __5__, the Defence Against the Dark Arts teacher, who had been the one working behind the scenes to kill Harry by first jinxing his broom and then letting a troll into the school. 
Snape had been trying to protect Harry instead, who had wronged him. Now, __5__ is partly possessed by Voldemort, whose face has sprouted on the back of __5__'s head that is constantly concealed by his oversized
turban. Voldemort needs Harry's help to get past the final obstacle: the Mirror of Erised, forcing him to stand before the Mirror. It recognises Harry's lack of greed for the Stone and __4__ deposits it in his
pocket. As __5__ attempts to seize the stone and kill Harry, his flesh burns on contact with the boy's skin, and __5__ burns alive.''']

# Number  of guesses to be allowed to the user
GUESSES = 5

# Message to the user
CORRECT = "correct !\n"

# A list of difficulty levels to be passed in as options_list to the WordInList function to check against user funciton
quiz_level = ["easy", "medium", "hard"]

# List of blank_numbers in the test strings to be replaced by valid user answer
blank_numbers = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__"]

# A list for each level contaning the answers for the quiz
answers = [["living", "letter", "evil", "kill"], ["Hogwarts", "Ronald", "magical",
                                                  "Gryffindor", "Slytherin"], ["Gringotts", "indiscretion", "pretences", "surreptitiously", "Quirrell", "Firenze"]]

# Check if a word in options_list is a substring of the word passed in function.


def WordInList(word, options_list):
    for wil in options_list:
        if wil in word:
            return wil
    return None

# Function to Prompt the user to select the difficulty level of the quiz .


def UserLevel():
    user_input = None
    while user_input == None:
        print 'Please select a difficulty level for the quiz by typing it in!\nPossible choices include easy/medium/hard.'
        user_input = WordInList(raw_input(), quiz_level)
        if user_input != None:
            return user_input
        else:
            print "That's not an option!"


# Plays full game of code your own quiz by passing in quiz level selected by the user along with  the list of blank_numbers which are to be replaced with user's valid answers
# and number of guesses allowed to the user


def PlayQuiz(level, blank_numbers, turns):
    quiz_string = quiz[quiz_level.index(level)]
    answer_list = answers[quiz_level.index(level)]
    for blank in (range(len(answer_list))):
        while turns >= 1:
            print "The current paragraph reads as such:\n %s" % (quiz_string)
            user_input = raw_input(
                "\nWhat should be substitued in for " + str(blank_numbers[blank]) + "? ")
            if answer_list[blank] == user_input:
                quiz_string = quiz_string.replace(
                    str(blank_numbers[blank]), user_input)
                print CORRECT
                break
            else:
                turns -= 1
                print "Wrong answer! you have %d trys left!\n" % (turns)
    return quiz_string + "\n\nEnd of quiz!"


# Start the quiz
level = UserLevel()
print "you've chosen " + level + "!" + "\n\n" + "you will get " + str(GUESSES) + " guesses\n"
print PlayQuiz(level, blank_numbers, GUESSES)
