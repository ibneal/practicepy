def FirstFactorial(num):

    if num == 0:
        return 1
    else:
        return num * FirstFactorial(num)

# keep this function call here


print FirstFactorial(5)
