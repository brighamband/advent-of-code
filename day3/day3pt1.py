def most_freq(lst):
    return max(set(lst), key=lst.count)


def least_freq(lst):
    return min(set(lst), key=lst.count)


def binaryToDecimal(n):
    return int(n, 2)


def calc_bin_rates(nums):
    BINARY_STR_LEN = len(nums[0])

    bin_gamma_rate = ""
    bin_epsilon_rate = ""

    for i in range(BINARY_STR_LEN):
        col = [num[i] for num in nums]
        bin_gamma_rate += most_freq(col)
        bin_epsilon_rate += least_freq(col)

    return bin_gamma_rate, bin_epsilon_rate


def calc_dec_rates(bin_gamma_rate, bin_epsilon_rate):
    dec_gamma_rate = binaryToDecimal(bin_gamma_rate)
    dec_epsilon_rate = binaryToDecimal(bin_epsilon_rate)

    return dec_gamma_rate, dec_epsilon_rate


def input_txt_to_list():
    file = open("in.txt", "r")
    # Put all file contents into string, then splits into array items on new lines
    nums = file.read().splitlines()
    file.close()
    return nums


def main():
    nums = input_txt_to_list()

    bin_gamma_rate, bin_epsilon_rate = calc_bin_rates(nums)
    dec_gamma_rate, dec_epsilon_rate = calc_dec_rates(bin_gamma_rate, bin_epsilon_rate)

    print("Gamma rate is", bin_gamma_rate, "or", dec_gamma_rate, "in decimal.")
    print("Epsilon rate is", bin_epsilon_rate, "or", dec_epsilon_rate, "in decimal.")

    power_consumption = dec_gamma_rate * dec_epsilon_rate
    print(
        "Power consumption is",
        power_consumption,
        " ( gamma * epsilon,",
        dec_gamma_rate,
        "*",
        dec_epsilon_rate,
        ")",
    )


if __name__ == "__main__":
    main()
