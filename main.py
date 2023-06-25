def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males=int(input("Number of males:"))
    females=int(input("Number of females:"))
    total=males+females
    m_perc=males/total*100
    f_perc=females/total*100
    print("The total number of students: \t\t{}".format(total))
    print("The number of males and females \t{} \t{}".format(males,females))
    print("The percentage of males and females \t{:.2f}% \t{:.2f}%".format(m_perc,f_perc))
    """
    
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
