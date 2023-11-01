<br>

# Python Examples

Small python programs.

<br>

## Shell aliases

To save time, I have added some aliases to my .zshrc file.

```
#PYTHON3 ALIASES
alias piu='pip3 install --upgrade pip'
alias prr='pur -r requirements.txt'
alias dep='pip3 install -r requirements.txt'
alias pra='python3 app.py'
```

<br>

## AI Code Generation

Large Language Models (LLMs) are only effective for me because I don't trust their output.

I always test the code that they generate!

However, given that Python3 is a mature language that is fairly popular in academia and industry, there is a suprising amount of training data for them to work with.

Once you have generated the code that you want in Python3, manually making the changes required to turn it into valid Mojo code is not so hard.

<br>

## Learning Python3 with LLMs

This prompt template is good for learning Python idioms.

```
What is the idiomatic way to [do the thing you want to do]
in Python3?
```

<br>

## Function Generation With LLMs

This prompt template is good for generating Python functions.

```
Write a [name] function in Python3 that takes
[name the parameters and their types] and returns
a [type] such that [describe what the function does].
Then show me the code.
```

<br>
