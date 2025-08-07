# character-name-extractor

This Python program attempts to identify potential **character names** from a plain text story (`story.txt`) by applying a set of rules related to capitalization and punctuation.

## Concept:
Many character names in stories begin with capital letters but are not at the start of sentences. This script uses that heuristic to isolate likely character names.

##  How it works:
- Loads `story.txt` and splits it into a list of words
- Identifies capitalized words that do **not**:
  - Follow a sentence-ending punctuation mark (`.`, `!`, `?`, `,"`)
  - Appear at the beginning of the story
  - Equal the standalone word `'I'`
- Appends matching words to a list of potential characters

##  Sample Output: 
- ['Charlie', 'Thomas', 'Maria', 'Xavier']
- 
## Try It:
- Replace the contents of story.txt with your own story and run the script to see what names it finds!
