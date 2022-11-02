## Report

### Argparse

```
action=('store_true'),
```

In this case the user only needs to enter the optional argument. Initially it was stored as False but by entering the optional argument without value it is stored as True. This makes it possible to use it in an if-statement without an additional parameter.

```
metavar='buy, sell, inventory, revenue, profit',
```

The metavar keep the -h/ help function tidy. It lines op the help-visualisation by adding text or just an empty string.

```
nargs='?'
```

When trying to use an optional argument _without_ a positional argument the user normaly would get an error. By setting the nargs to a **single value wich is optional** this problem is solved. The problem occurred when trying to use _--advance_time_ without positional argument

### Inventory and PySimpleGui (Tkinter)

The commandline interface is usefull but has some limitations. You always run in to presenting variables with a random nummer of characters. When creating a box around the inventory things start shifting for every other product you are trying to visualize.
You end up with complicated functions like this:

```
def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)
```

By using PySimpleGui it creates a better and predicable output to the user. Presenting it any way you like.
Along the project it seemed usefull to give the user extra information. For example when you buy something there is no response written in the command line no other than maybe an error message. This could be solved by sending gui-messages like

```
python super.py buy --product_name orange --price 1 --expiration_date 2020-01-30
```

> **'appel has been succesfully registered as sold'**

```
python super.py sell --product_name airplane --price 1
```

> **'airplane is not in stock'**

### CSV files

Not knowing to much about CSV the first option was to use **csv.DictReader**. Further on is **csv.reader** seamed more usefull because of the list-output wich is easy iterable. Eventhough the DictReader output can be flattened this is one step faster.

### Advance time

I know myself!, always forget to change the date back to the original date. So for a selling or buying operation I arranged a check function to see if the current date is used. If not a message shows how many days you have to reset the date to be .. up-to-date.
