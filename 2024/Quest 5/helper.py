class DoesNotMatchException(Exception):
    """The subtracting dictionary contains a key not contained in the original"""

class Freq(dict):
    def __add__(self, other):
        new_dict = {}
        self_keys, other_keys = set(self.keys()), set(other.keys())
        just_self = self_keys-other_keys
        just_other = other_keys-self_keys
        both = self_keys.intersection(other_keys)
        for key in just_self:
            new_dict[key] = self[key]
        for key in just_other:
            new_dict[key] = other[key]
        for key in both:
            new_dict[key] = self[key]+other[key]
        return new_dict
    
    def __sub__(self, other):
        new_dict = self.copy()
        self_keys, other_keys = self.keys(), other.keys()
        for key in other_keys:
            if key not in self_keys:
                raise DoesNotMatchException
            new_dict[key] -= other[key]
        return new_dict
    
    def __mul__(self, num):
        new_dict = self.copy()
        for key in self.keys():
            new_dict[key] = self[key]*num
        return new_dict
        
dict_one = Freq()
dict_two = Freq()
dict_one["1"] = 1
dict_two["2"] = 1
print(dict_one+dict_two)