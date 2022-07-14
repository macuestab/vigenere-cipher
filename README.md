# Vigenere Cipher

The Vigenère Cipher was invented by an Italian cryptologist named Giovan Battista Bellaso in the 16th century, but named after another cryptologist from the 16th century, Blaise de Vigenère.

The Vigenère Cipher is a polyalphabetic substitution cipher. What this means is that opposed to having a single shift that is applied to every letter, the Vigenère Cipher has a different shift for each individual letter. The value of the shift for each letter is determined by a given keyword.

Consider the message

    barry is the spy

If we want to code this message, first we choose a keyword. For this example, we'll use the keyword

    dog

Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. So if we want to code the message "barry is the spy" our _keyword phrase_ is "dogdo gd ogd ogd". Now we are ready to start coding our message. We shift the each letter of our message by the place value of the corresponding letter in the keyword phrase, assuming that "a" has a place value of 0, "b" has a place value of 1, and so forth. Remember, we zero-index because this is Python we're talking about!

                  message:       b  a  r  r  y    i  s   t  h  e   s  p  y

           keyword phrase:       d  o  g  d  o    g  d   o  g  d   o  g  d

    resulting place value:       4  14 15 12 16   24 11  21 25 22  22 17 5

So we shift "b", which has an index of 1, by the index of "d", which is 3. This gives us an place value of 4, which is "e". Then continue the trend: we shift "a" by the place value of "o", 14, and get "o" again, we shift "r" by the place value of "g", 15, and get "x", shift the next "r" by 12 places and "u", and so forth. Once we complete all the shifts we end up with our coded message:

     eoxum ov hnh gvb

As you can imagine, this is a lot harder to crack without knowing the keyword!
