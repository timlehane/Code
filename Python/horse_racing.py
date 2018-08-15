# CS-1117 : 2016-2017 : Assignment #15 : Processing Race Results
"""

Consider a race in which the score of each entrant is the
place in which they finish, and the score of a team is the
sum of the scores of its first three finishers. Any
finishers from a team after the third do not contribute to
that team’s score; teams with fewer than three finishers
are eliminated.
The team with the lowest overall score places first, that
with the next lowest score places second, and so forth.
Registration data for all entrants is stored in a file,
with each line consisting of the racer number, personal
name, and team name for that entrant;

Write a Python program
which will first read in this data file, and then read in
from the keyboard, one per line, the racer numbers of
entrants in the order in which they finish. Invalid race
numbers should trigger an error message, but otherwise be
skipped. The number 0 signals the end of the keyboard input.
As soon as the third member of any team finishes, the
program should output the team score, its name, and the
names of its three scoring members in their finishing
order;

The program should finally output a table containing, for
each team with three or more finishers, the team place, its
score, its name, and the names of its scoring members,
sorted in increasing order of team place, where teams on
equal scores are given the same place;

"""
MAX_SCORERS = 3 # number of team members who contribute to its score

def ReadEntries( fileName ) :
    # Read the file 'fileName', in which each line is of the form
    # number name team
    # with each 'number' being unique, and return a dictionary with items
    # number : ( name, team )
    # or the empty dictionary if 'fileName' cannot be read
    try :
        fileHandle = open( fileName, "r" )
    except IOError :
        print( "*** ReadEntries : cannot read file '%s'" % ( fileName ) )
        return { }
        entries = { }
        for line in fileHandle :
            number, name, team = line.split( )
            entries[ number ] = ( name, team )
            fileHandle.close()
            return entries

            def Join( strings ) :
                # The result of concatenating all items in the list-of-strings 'strings',
                # with ", " inserted between each pair of adjacent items
                return ", ".join( strings )



def GenerateResults( entries ) :
    # Take the dictionary 'entries', whose items have the form
    # number : ( name, team )
    # and then input, from the keyboard, a sequence of finisher numbers
    # ( terminated by 0 ); for each such number, find the corresponding 'name'
    # and 'team' from 'entries', and construct, and ultimately return,
    # a dictionary with items
    # team : ( [ finishers ], score )
    # where 'finishers' are the first 'MAX_SCORERS' 'name's from 'team' to finish
    # and 'score' is the sum of their scores, where the score of each 'name' is
    # the sequential order in which their 'number' finished; also, as soon as
    # 'MAX_SCORERS' members of any 'team' finish, output its 'score', 'team',
    # and 'finishers'
    results = { }
    finished = set( )
    place = 0
    print( )
    print( "Enter race numbers, one per line, in finishing order;" +
    " enter 0 to stop:" )
    print( )
    while True :
        number = input( "> " )
        if number == "0" :
            break
            if number not in entries :
                print( "*** %s is not a valid race number" % ( number ) )
            elif number in finished :
                print( "*** %s has already finished" % ( number ) )
            else :
                finished |= { number }
                place += 1
                name, team = entries[ number ]
                if team in results :
                    finishers, score = results[ team ]
                    if len( finishers ) < MAX_SCORERS :
                        finishers += [ name ]
                        score += place
                        results[ team ] = ( finishers, score )
                        if len( finishers ) == MAX_SCORERS :

                            print( "SCORE = %3i TEAM = %-5s : %s" %
                            ( score, team, Join( finishers ) ) )
                        else :
                            results[ team ] = ( [ name ], place )
                            return results



def PrintTeamResults( results ) :
    # Take the dictionary 'results', whose items have the form
    # team : ( [ finishers ], score )
    # and output each 'team' and its 'finishers', in increasing 'score' order;
    # also output the place of each 'team', which the position of its 'score'
    # in the increasing sequence of 'score's; however, produce no output
    # for any 'team' which has fewer than 'MaxScorers' members in 'finishers'
    scorers = { }
    for team in results :
        finishers, score = results[ team ]
        if len( finishers ) == MAX_SCORERS :
            if score in scorers :
                scorers[ score ] += [ ( team, finishers ) ]
            else :
                scorers[ score ] = [ ( team, finishers ) ]
                print( "PLACE SCORE TEAM SCORING MEMBERS" )
                place = 1
                for score in sorted( scorers ) :
                    for ( team, finishers ) in sorted( scorers[ score ] ) :
                        print( " %2i %3i %-5s %s" %
                        ( place, score, team, Join( finishers ) ) )
                        place += len( scorers[ score ] )

                        def RaceResults( fileName ) :
                            # Process the race results whose entries are stored in 'fileName'
                            entries = ReadEntries( fileName )
                            if entries == { } :
                                return

                                results = GenerateResults( entries )
                                PrintTeamResults( results )
