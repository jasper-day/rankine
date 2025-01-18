
import re

def parse_propeller_performance(filename):
    with open(filename, 'r') as f:
        result = {}
        reg = re.compile("\s*(\d*\.?\d+\s+)+")
        l = f.readline()
        rpm = 0
        while l:
            if re.search('PROP\s+RPM', l):
                rpm = float(re.search("\d+", l).group())
                f.readline()
                titles = f.readline().split()
                units = f.readline().split()
                names = [t + " " + u for t, u in zip(titles, units)]
                if result == {}:
                    result['rpm'] = []
                    for name in names:
                        result[name] = []
            if rpm > 0:
                if len(l.split()) == len(names):
                    vals = map(float, l.split())
                    result['rpm'].append(rpm)
                    for name, val in zip(names, vals):
                        try:
                            result[name].append(val)
                        except KeyError:
                            print(name + "not found in result")
            l = f.readline()
            
        return result

# Example Usage:
# parse_propeller_performance('resources/PER3_12x8.dat')
