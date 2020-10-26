switch={
    "a":lambda a:'00'+str(a),
    "b":lambda a:x*3,
    "c":lambda a:x**x,
    }
'''try:
   switch["c"](6)
except KeyError as e:
    pass'''

#switch["c"] (6)


print(switch["a"](6))

