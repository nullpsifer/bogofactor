# bogofactor
This implements a factoring algorithm using random trial division and Wilson's theorem for primality testing.

# Installation
Clone the git repo and then run
```
python setup.py install
```

# Example
```python
>>> from bogofactor import bogofactor
>>> bogofactor(16449767)
[4093, 4019]
```
