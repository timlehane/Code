#!/usr/bin/env python3
# Wc.py file...
# output the number of lines, words, and characters in each file 'file';
# if multiple files are specified, also output the totals of these values
from sys import argv
format = "%5i %5i %5i %s"
totalLines = 0
totalWords = 0
totalChars = 0
for fileName in argv[ 1 : ] :
    try :
        fileHandle = open( fileName, "r" )
    except FileNotFoundError :
        print( "Wc: %s: No such file or directory" % ( fileName ) )
        continue
    except PermissionError :
        print( "Wc: %s: Permission denied" % ( fileName ) )
        continue
        thisLines = 0
        thisWords = 0
        thisChars = 0
        for line in fileHandle :
            thisLines += 1
            thisWords += len( line.split( ) )
            thisChars += len( line )
            fileHandle.close()
            print( format % ( thisLines, thisWords, thisChars, fileName ) )
            totalLines += thisLines
            totalWords += thisWords
            totalChars += thisChars
            if len( argv ) > 2 :
                print( format % ( totalLines, totalWords, totalChars, "total" ) )

#!/usr/bin/env python3
# Uniq.py inFile [outFile]
# output each line in file 'inFile' which differs from the previous line;
# if 'outFile' is specified, send the output to that file, not the screen
from sys import argv, exit

inFile = argv[ 1 ]
try :
    inHandle = open( inFile, "r" )
except IOError :
    print( "Uniq: %s: No such file or directory" % ( inFile ) )
    exit( )
    outToFile = ( len( argv ) == 3 )
    if outToFile :
        outFile = argv[ 2 ]
        try :
            outHandle = open( outFile, "w" )
        except PermissionError :
            print( "Uniq: %s: Permission denied" % ( outFile ) )
            exit( )
            prevLine = ""
            for thisLine in inHandle :
                if thisLine != prevLine :
                    if outToFile :
                        outHandle.write( thisLine )
                    else :
                        print( thisLine, end = "" )
                        prevLine = thisLine
                        inHandle.close()
                        if outToFile:
                            outHandle.close()

#!/usr/bin/env python3
# Cat.py [-E] [-n] [-s] file...
# output all lines in each file 'file'
# -E : append "$" to the end of each output line
# -n : precede each line with its output line number
# -s : output consecutive blank lines as a single blank line
from sys import argv
markEnd = False
number = False
squeeze = False
for i in range( 1, len( argv ) ) :
    arg = argv[ i ]
    if arg == "-E" :
        markEnd = True
    elif arg == "-n" :
        number = True

    elif arg == "-s" :
        squeeze = True
    else :
        break
        lineNumber = 0
        for fileName in argv[ i : ] :
            try :
                fileHandle = open( fileName, "r" )
            except FileNotFoundError :
                print( "Cat: %s: No such file or directory" % ( fileName ) )
                continue
            except PermissionError :
                print( "Cat: %s: Permission denied" % ( fileName ) )
                continue
                prevBlank = False
                for line in fileHandle :
                    trimLine = line[ : -1 ]
                    thisBlank = ( trimLine == "" )
                    if not ( squeeze and prevBlank and thisBlank ) :
                        lineNumber += 1
                        if number :
                            print( "%6i " % ( lineNumber ), end = "" )
                            if markend :
                                print( trimLine + "$" )
                            else :
                                print( trimLine )
                                prevBlank = thisBlank
                                fileHandle.close()

#!/usr/bin/env python3
# Tail [-number] file
# output the last 10 lines of file 'file'
# -number : output instead the last 'number' lines
# output the entire file if it has fewer than the specified number of lines
from sys import argv, exit
if len( argv ) == 3 :
    lineCount = int( argv[ 1 ][ 1 : ] )
    fileName = argv[ 2 ]
else :
    lineCount = 10
    fileName = argv[ 1 ]
    try :
        fileHandle = open( fileName, "r" )
    except FileNotFoundError :

        print( "Tail: cannot open `%s' for reading: No such file or directory" % \
        ( fileName ) )
        exit( )
    except PermissionError :
        print( "Tail: cannot open `%s' for reading: Permission denied" % \
        ( fileName ) )
        exit( )
        if lineCount == 0 :
            exit( )
            lines = lineCount * [ "" ]
            pos = 0
            for line in fileHandle :
                lines[ pos ] = line
                pos = ( pos + 1 ) % lineCount
                fileHandle.close()
                for line in lines[ pos : ] + lines[ : pos ] :
                    print( line, end = "" )

#!/usr/bin/env python3
# Grep [-n] [-v] target file...
# output all lines in each file 'file' which contain the string 'target'
# -n : precede each line by its line number in its file
# -v : output instead lines which do not contain 'target'
from sys import argv
number = False
negate = False
for i in range( 1, len( argv ) ) :
    arg = argv[ i ]
    if arg == "-n" :
        number = True
    elif arg == "-v" :
        negate = True
    else :
        break
        target = argv[ i ]
        multiFiles = ( i + 1 < len( argv ) - 1 )
        for fileName in argv[ i + 1 : ] :
            try :
                fileHandle = open( fileName, "r" )

            except FileNotFoundError :
                print( "Grep: %s: No such file or directory" % ( fileName ) )
                continue
            except PermissionError :
                print( "Grep: %s: Permission denied" % ( fileName ) )
                continue
                lineNumber = 0
                for line in fileHandle :
                    lineNumber += 1
                    if ( not negate and target in line ) or \
                    ( negate and target not in line ) :
                    if multiFiles :
                        print( "%s:" % ( fileName ), end = "" )
                        if number :
                            print( "%i:" % ( lineNumber ), end = "" )
                            print( line, end = "" )
                            fileHandle.close()

#!/usr/bin/env python3
# Factor [number]...
# output each non-negative integer 'number' followed by its prime factors;
# if none are specified on the command line, read them from standard input
from sys import argv

def WriteFactors( sn ) :
    # Output the non-negative integer represented by string 'sn',
    # followed by its prime factors
    n = int( sn )
    print( "%i:" % ( n ), end = "" )
    d = 2
    while n > 1 :
        if n % d == 0 :
            print( " %i" % ( d ), end = "" )
            n = n // d
        else :
            d += 1
            print( )

            if len( argv ) > 1 :
                for sn in argv[ 1 : ] :
                    WriteFactors( sn )

                else :
                    while True :
                        try :
                            inputNums = input( )
                        except EOFError :
                            break
                            nums = inputNums.split()
                            for sn in nums:
                                WriteFactors( sn )
