import re

POLAR = "VSPAERO_Polar"
NAME = "Results_Name"


def parse_openvsp(filename):
    results = []
    with open(filename) as f:
        result = {}
        while line := f.readline():
            s = line.split(",")
            if s[0] == NAME:
                results.append(result)
                result = {}
            result[s[0].strip()] = [s_.strip() for s_ in s[1:]]
    return results[1:]


def get_result(res, name):
    return [r for r in res if r[NAME] == [name]]

def get_polar(filename):
    res = parse_openvsp(filename)
    return get_result(res, POLAR)[0]

def get_dataframe(result):
    import pandas as pd
    return pd.DataFrame({
        key: map(float, value) for key, value in 
        result.items()
        if key.find("Result") == -1 and 
        key.find("Analysis") == -1 and
        key.find("FC") == -1
        })

def get_names(res):
    return [r[NAME] for r in res]


def f(l):
    return [float(x) for x in l]
