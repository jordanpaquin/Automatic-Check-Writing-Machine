import argparse
import inflect

# Initialize Argument Parser
parser = argparse.ArgumentParser(description='Take in a dollar amount and convert it into a phonetic representation..')
parser.add_argument('dollarAmount', help='enter a dollar amount in format $1,234.56')
args = parser.parse_args()

dollarValue = args.dollarAmount

# Divide String into the two parts of its Phonetic Representation
dollars, cents = dollarValue.split('.',1)

# Initializes Inflect
p = inflect.engine()

wordPhrase = p.number_to_words(dollars)

# Removes 'ands' in resulting inflect string and cases with too many spaces
wordPhrase = wordPhrase.replace('thousand and ', 'thousand ')
wordPhrase = wordPhrase.replace(' and ', '')
wordPhrase = wordPhrase.replace('hundred', 'hundred ')
wordPhrase = wordPhrase.replace(',', '')

#Prints Resulting Phonetic Representation
if (len(cents) == 1):
  print(wordPhrase + ' and ' + cents + '0/100 dollars.')
else:
    print(wordPhrase + ' and ' + cents + '/100 dollars.')
