# oList
##### A Python 'Object List'. It's basically your standard python list that additionally lets you attach data to it that doesn't affect the actual list items itself.<br>
##### Treat the oList as you would a normal list:<br>
```python
my_list = oList([-10,3,4,-11,7,14])
my_list.sort()
for list_item in my_list:
    print(str(list_item))
```
## oList Methods:
``` python
# Import the oList class
from oList import oList

oList.attach('data') # can be of any type
oList.get_attachments() # returns a list or the object itself if the attachments are only 1
oList.as_dict(_attachments=True) # returns a dict, access values being index, _attachment=True will add attachment data to the dict
oList.as_tuple() # returns tuple
```
## Example Usage:
``` python
# Import the oList class
from oList import oList

intel_list = oList([
    'i5-9600k',
    'i9-10910',
    'i9-10900K',
]).attach({
    'carrier': 'Intel',
    'description': 'A nice little list of some intel Cpus.'
})

ryzen_list = oList([
    'Ryzen 3 1200',
    'Ryzen 5 1400',
    'Ryzen 5 3600x'
]).attach({
    'carrier': 'AMD',
    'description': 'A nice little list of some Ryzen Cpus.'
})

cpu_list = oList([intel_list, ryzen_list]).attach('List of Intel and Ryzen Cpus')

# .... later on in the program ....

print("--- " + cpu_list.get_attachments() + " ---\n")

for cpus in cpu_list:
    print(cpus.get_attachments())
    for cpu in cpus:
        print(cpus.get_attachments()['carrier'] + ' - ' + cpu)
    print('')


# OUTPUT:
# --- List of Intel and Ryzen Cpus ---
#
# {'carrier': 'Intel', 'description': 'A nice little list of some intel Cpus.'}
# Intel - i5-9600k
# Intel - i9-10910
# Intel - i9-10900K
#
# {'carrier': 'AMD', 'description': 'A nice little list of some Ryzen Cpus.'}
# AMD - Ryzen 3 1200
# AMD - Ryzen 5 1400
# AMD - Ryzen 5 3600x
```
