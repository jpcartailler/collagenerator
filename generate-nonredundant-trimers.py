import pprint

chains = range(1, 7, 1)
trimers_alt1 = list()    # Declare as a dict
trimers_alt2 = list()    # Declare as a dict
trimers_alt3 = list()    # Declare as a dict
trimers_distinct = list()   # non-redundant set
trimers_redundant = list()    # Declare as a dict

count = 0

for a in chains:

    chain_a = a

    for b in chains:

        chain_b = b

        for c in chains:
            count += 1
            chain_c = c

            # generate base trimer
            trimer = str(chain_a) + "-" + str(chain_b) + "-" + str(chain_c)
            trimers_alt1.append(trimer)

            # test to see if it exists in alternative redundant set
            # if it does NOT, then store it
            if trimer not in trimers_redundant:
                trimers_distinct.append(trimer)

            # now, generate both alternative (but equivalent) search trimers
            trimer = str(chain_b) + "-" + str(chain_c) + "-" + str(chain_a)
            trimers_alt2.append(trimer)
            trimers_redundant.append(trimer)

            trimer = str(chain_c) + "-" + str(chain_a) + "-" + str(chain_b)
            trimers_alt3.append(trimer)
            trimers_redundant.append(trimer)


print "Generated " + str(len(trimers_distinct)) + " trimers (trimers_distinct)"
print "Generated " + str(len(trimers_redundant)) + " trimers (trimers_redundant)"
print "Generated " + str(len(trimers_alt1)) + " trimers (trimers_alt1)"
print "Generated " + str(len(trimers_alt2)) + " trimers (trimers_alt2)"
print "Generated " + str(len(trimers_alt3)) + " trimers (trimers_alt3)"
print "List of distinct trimers:"
pprint.pprint(trimers_distinct)
