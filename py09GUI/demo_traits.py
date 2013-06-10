#!/usr/bin/env python
# all_traits_features.py 

from enthought.traits.api import Delegate, HasTraits, Instance, Int, Str
import enthought.traits.ui

class Parent(HasTraits):

    # INITIALIZATION: last_name' is initialized to '':
    last_name = Str('')


class Child(HasTraits):
    age = Int

    # VALIDATION: 'father' must be a Parent instance:
    father = Instance(Parent)

    # DELEGATION: 'last_name' is delegated to father's 'last_name':
    last_name = Delegate('father')

    # NOTIFICATION: This method is called when 'age' changes:
    def _age_changed(self, old, new): 
        print 'Age changed from %s to %s ' % (old, new)

# Set up the example:
joe = Parent()
joe.last_name = 'Johnson'
moe = Child()
moe.father = joe
    
# DELEGATION in action:
#print "Moe's last name is %s" % moe.last_name

# NOTIFICATION in action:
#moe.age = 10

# VISUALIZATION: Displays a UI for editing moe's 
# attributes (if a supported GUI toolkit is installed)
#moe.configure_traits()