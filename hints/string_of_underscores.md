# Printing a string of underscores, one for each letter in the secret word

This works if `secret_word` is a string or a list, but won't help you when
you're ready to start filling in correct guesses:

```python
print('_ ' * len(secret_word))
```

A more flexible approach would be to use a list to store the guessed word.
If you have a list, you can `join` its elements into a string (see below).

```python
guessed_word = ['_'] * len(secret_word)
print(' '.join(guessed_word))
```
