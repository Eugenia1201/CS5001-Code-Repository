" testing arbitrary argument lists "


def average(*values, average_type="mean"):
    """ Return the average of the values

    Args:
        average_type (string, optional): "mean" or "median".
            Defaults to "mean".
    """

    if average_type == "median":
        result = sorted(values)[len(values)//2]
    elif average_type == "mean":
        result = sum(values) / len(values)
    else:
        result = None

    return result


print(f"Mean of [1,5,2,2,2] is \
{average(1, 5, 2, 2, 2, average_type='mean')}")
print(f"Median of [1,5,2,2,2] is \
{average(1, 5, 2, 2, 2, average_type='median')}")
