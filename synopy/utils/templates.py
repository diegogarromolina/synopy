
ERRORS = {
    1 : "The group {} has more than five digits.",
    2 : "The group {} has less than five digits.",
    3 : "The group {} for {} is not found.",
    4 : "The indicator {} for {} is not in {}.",
    5 : "The indicator {} for {} is not a digit.",
}

class Group_Indicator:
    
    def __init__(self, indicator: str, name: str):
        self.name = name
        self._set_indicator_value(indicator)
    
    def _set_indicator_value(self, indicator: str):
        if indicator.isdigit():
            self.value = int(indicator)
        else:
            self.value = indicator
    
    def verify_indicator(self, value=1):
        if self.value != value:
            return False
        return True

class Table_Indicator:
    
    valid = True
    
    def __init__(self, indicator: str, name: str, table: dict):
        self.name = name
        self.table = table
        self.objective = table[-1]
        self._set_indicator_value(indicator)
    
    def _set_indicator_value(self, indicator: str):
        if indicator == "/":
            self.indicator = indicator
        elif indicator.isdigit():
            self.indicator = int(indicator)
        else:
            self.indicator = indicator
    
    def verify_indicator(self):
        if self.indicator in list(self.table.keys()):
            return self.valid
        self.valid = False
        return self.valid

    def __str__(self):
        if self.valid:
            return self.table[self.indicator]
        return 'Indicator {} not valid.'.format(self.name)

class Value_Indicator:
    
    valid = True
    
    def __init__(self, indicator: str, name: str, objective: str):
        self.name = name
        self.objective = objective
        self._set_indicator_value(indicator)
    
    def _set_indicator_value(self, indicator: str):
        if indicator.isdigit():
            self.indicator = int(indicator)
        else:
            self.indicator = indicator
    
    def verify_indicator(self):
        if isinstance(self.indicator, int):
            return self.valid
        self.valid = False
        return self.valid
    
    def __str__(self):
        if self.valid:
            return self.indicator
        return 'Indicator {} not valid.'.format(self.name)

class Group:
    
    _errors = []
    _group_objective = ''
    group_indicator = None
    found = True
    
    def __init__(self, group: str, name: str):
        self.group = group
        self.name = name
        self.length = len(group)
        if self.length > 5:
            self._errors.append(ERRORS[1].format(self.name))
        elif self.length < 5:
            self._errors.append(ERRORS[2].format(self.name))
        else:
            pass
    
    def _extract_indicator(self, start, end):
        if end >= 4:
            return self.group[start:]
        else:
            return self.group[start:end]
    
    def _show_characteristics(self):
        return ""
    
    def verify_group_indicator(self, value=1):
        if self.group_indicator.verify_indicator(value=value):
            self.found = False
            self._errors.append(ERRORS[3].format(self.name, self._group_objective))
      
    def verify_table_indicator(self, indicator):
        if not indicator.verify_indicator():
            self._errors.append(ERRORS[4].format(indicator.name, indicator.objective, indicator.table[-2]))

    def verify_value_indicator(self, indicator):
        if not indicator.verify_indicator():
            self._errors.append(ERRORS[5].format(indicator.name, indicator.objective))
    
    def _save_indicators(self, *args):
        self._indicators = []
        for ind in args:
            self._indicators.append(ind)
    
    def get_indicator(self, indicator_name: str):
        for ind in self._indicators:
            if ind.name == indicator_name:
                return ind.indicator
        raise ValueError("No indicators found with name {}".format(indicator_name))
    
    def errors(self):
        return self._errors
    
    def __str__(self):
        return "Group name: {}.".format(self.name)

class Section:
    
    errors = []
    
    def __init__(self, section: list):
        self.section = section
        self.length = len(section)
    
    def copy_group_errors(self, group):
        for error in group.errors():
            self.errors.append(error)
        