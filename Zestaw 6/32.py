def rek(T, k, sum1=0, moc1=0, sum2=0, moc2=0, i=0):
    print(sum1, sum2, moc1 + moc2)
    if sum1 == sum2 and moc1 + moc2 == k:
        return True

    if i >= len(T):
        return False

    return rek(T, k, sum1 + T[i], moc1 + 1, sum2, moc2, i+1) or rek(T, k, sum1, moc1, sum2 + T[i], moc2 + 1, i+1)


T = [2, 3, 5]
print(rek(T,3))