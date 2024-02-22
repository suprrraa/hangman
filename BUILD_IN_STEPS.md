# Hangman in <Some Number> Easy Steps

Hangman is much more complex than anything we've built so far. As always, when
faced with complexity, we'll try to _simplify_. Let's build one component at a
time.

There's nothing stopping you from breaking the problem down into different
components or building them in a different order. This is just one way of
tackling the problem.

## Step 1: Prompt for a secret word

Ask the first user to enter a secret word for the other player to guess. Store
that word in a sensibly-named variable. We'll surely need to refer back to it.

If you're not sure how to ask for input and store it in a variable, look back to
some of the code you've already written. In particular, look for places where
you used the `input` function.

## Step 2: Set up your record keeping

What information do you need to keep track of?

At minimum, you'll need to keep track of which letters have been guessed. Does it
make sense to track correct and incorrect guesses in the same place and in the
same way? What data structure(s) would work best?

Think about what you'll need to do with this information? Here's a few
considerations to get you started:

- How will you check if a letter has already been guessed?
- How will you tell the player where a correct guess is located in the word?
- How will you know when the game is over? Can the same information tell you
  if the player has won or lost?

Create and initialize variables to keep track of the state of the game.

As you run into problems or needs you didn't anticipate, there's a good chance
you'll change your mind about what to track and how best to track it. Such is
life for a programmer.

## Step 3: Start building the initial game board

When the game starts and after each guess, we need to display the current state
of the game. We'll add more elements to our game board later, but let's start by
thinking about how to display the secret word with any correctly guessed letters
filled in and a list of guessed letters.

When the game begins, there are no guessed letters and thus no correct guesses.
In that case, we want to display an underscore for each letter in the secret word.
For example, if the secret word is `knight` (6 letters long), write code that will
print 6 space-separated underscores, like this:

```
_ _ _ _ _ _
Letters guessed:
```

How you'll it depends on how you've chosen to store game state.

Need a hint? Here are a few [code snippets](/hints/string_of_underscores.md)
to help you image what's possible.

## Step 4: Ask the user to guess a letter and update the game state

With a secret word stored and a basic game board printed to the screen, we're
ready to play. The steps we're about to code will eventually need to be
repeated, but for now, let's get and process only a single guess.

Ask you the second player to guess a letter.

We've reached a fork in the road. The guessed letter is either in the word or
it's not. Exactly what you'll do depends on how your tracking game state. Use
the updated game state to print an updated game board:

- `if` the guess is correct, replace the appropriate blank with the guessed
  letter. For example, if the guess was `i` and the secret word is `knight`, the
  game board should now look like this: `_ _ i _ _ _`.
- `else` print the basic game board (still all underscores), and print the
  (incorrectly?) guessed letter (for now, just a single letter).

## Step 5: Refactor: create single-purpose functions
