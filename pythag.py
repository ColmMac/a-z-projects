finding = input("Are you trying to find the hyp, opp or adj?")
if finding.lower() == "hyp":
    opp = float(input("Opp:"))
    adj = float(input("Adj:"))
    squared = adj * adj + opp * opp
    hyp = squared ** 0.5
    print("The hypotenuse is " + str(hyp))
if finding.lower() == "opp":
    hyp = float(input("Hyp:"))
    adj = float(input("Adj:"))
    squared = hyp * hyp - adj * adj
    opp = squared ** 0.5
    print("The opposition is " + str(opp))
if finding.lower() == "adj":
    hyp = float(input("Hyp:"))
    opp = float(input("Opp:"))
    squared = hyp * hyp - opp * opp
    adj = squared ** 0.5
    print("The adjacent is " + str(adj))