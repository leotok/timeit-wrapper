# Timeit wrapper
An alternate way of using the python 'timeit' module

Keep all the algorithms you want to check inside the same folder as `timer.py` and run `python timer.py`!
You can pass the number of loops as a parameter or it will use the default (1000 loops).

### Ex:

Directory tree: <br>
  - ../unique_character_string/ <br>
    - array_sorting_algorithm.py <br>
    - bitmap_algorithm.py <br>
    - set_algorithm.py <br>
    - timer.py

`$ python timer.py 10000`

```
array_sorting_algorithm.py loops:  10000
0.303525924683

bitmap_algorithm.py loops:  10000
0.491348981857

set_algorithm.py loops:  10000
0.127987146378
```
