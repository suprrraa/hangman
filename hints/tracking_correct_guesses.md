# Hint: Tracking Correct Guesses

You _could_ use a list to store all the correct guesses, but that list by itself
won't be very helpful for displaying the word with correct guesses filled in.
For example, if the secret word is `knight` and the player has guessed `n` and
`t`, you might have kept track of the correct guesses like this:

```python
correct_guesses = ['n', 't']
```

But how would you use that list to display the word with correct guesses filled in?

```shell
_ n _ _ t
```

But remember: lists are **ordered**. What if you stored correct guesses _at
their position in the word_? And if you start with a list of underscores, one
for each letter in the word, you'll be well set up to display unknown letters,
too.

```python
guessed_word = ["_", "n", "_", "_", "t"]
```

And here's a little recipe for creating a list of underscores, one for each
letter in the secret word:

```python
guessed_word = ['_'] * len(secret_word)
```
