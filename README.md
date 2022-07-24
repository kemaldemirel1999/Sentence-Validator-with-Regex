# Sentence-Validator-with-Regex
validate_sentences.py that will validate sentences in the given input text file. This program should read sentences.txt to get sentences.

Rules:

• In each line, there must be only one sentence. Multiple sentences should not be accepted.

• Every sentence must begin with a capital letter.

• A word should not consist of both numbers and letters, they can be found separately. (Example: “4ever” should not be accepted)

• A sentence cannot end with a comma. At the end of the sentence, exclamation point, ellipsis, question mark and dot can be used. Also, sentences can end with quotes and quotation marks. (Example: This was first said by Shakespeare: "To thine own self be true.")

• Words can start with capital letters or words can be uppercase, but no middle or trailing capital letters. (NFA is acceptable, but NfA is not.)

• Sentences can contain punctuation marks such as quotes, quotation marks, colons; and the quotation marks and quotes must match. There may be sentences between quotation marks and quotes.

• You can assume that there are no contracted words. (Example: She'll-She will)

• You can assume that there will be no spaces before any punctuation mark. (Example: you, me is valid but you , me is not valid.)

• You can assume that there are no extra punctuation marks other than those found in the examples.

Example Input File:

How can you say that to me?

As he looked at his reflection in the mirror, he took a deep breath.

He nodded at himself and, feeling braver, he stepped outside the bathroom. He bumped straight into the extremely tall man, who was waiting by the door.

David said ‘Oh, sorry!’.

The happy pair discussed their future life 2gether and shared sweet words of admiration.

We will not stop you; I promise!

Come here ASAP!

He pushed his chair back and went to the kitchen at 2 pM.

I do not know…

The main character in the movie said: "Play hard. Work harder."
