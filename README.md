# rx-calc

> a reactive subset of Python for doing napkin math

Inspired by Hillel Wayne's [Six Programming Languages I'd Like to See](https://buttondown.email/hillelwayne/archive/six-programming-languages-id-like-to-see/).

## Install

```bash
git clone https://github.com/supersonichub1/rx-calc
cd rx-calc
poetry install
# OR
pip install reactivex
```

## How to Use 
```
$ python -m rx_calc
> # This is the Python you know and love...
> 4 ** 3
64
> a = 5
5
> b = a + 5
10
> a = 4
4
> b
10
> # just with a reactive twist!
> a_and_b: a * b               
40
> a = 6 * 8
Variable 'a_and_b' is now: 480
48
> b = 4 * 9
Variable 'a_and_b' is now: 1728
36
> # Don't worry, other datatypes haven't been left out!
> subject = "world"
world
> classic: "Hello, " + subject + "!"
Hello, world!
> subject = "Kyle"
Variable 'classic' is now: Hello, Kyle!
Kyle
> # Type .exit to leave once you're done.
> .exit
```

## TODO

* Support a whole lot more Python nodes
	* ~unary ops~
	* function calls 
	* sequences
	* ternary conditions
	* formatted strings
* ~Nicer error handling~
* ~Use `readline` instead of `input`~
	* ~History!~
	* ~Go backwards in input!~
	* ~Autocomplete~
* Make certain variables (`inf`) constant
* Figure out how to expose Python standard library
	* most builtins
	* `math`
	* list-based versions of `itertools`, `filter`, `map`
	* `functools.reduce`
	* `datetime`
* reactive functions?
