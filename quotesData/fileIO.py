def read_data(in_file, attribution_count, distinct_quote_count):
    with open(in_file, "r") as in_lines:
        # Goes line by line and increments the relevant counters for each attributed person
        for line in in_lines: # each line is a quote bullet point
            line_attribution_count = {} # keeps track of attributions in the current line
            words = line.split(" ")

            # For each word in the current line, if it's a quote attribution, increment the counter
            # corresponding person's count for the current line
            for word in words:
                if word.startswith("-"): # if the word is an attribution
                    name = word[1:] # chop off the '-'
                    line_attribution_count[name] = line_attribution_count.get(word[1:], 0) + 1 # increment for attributed person

            # Update the total file counters with data from the current line
            for name in line_attribution_count:
                attribution_count[name] = attribution_count.get(name, 0) + line_attribution_count[name]
                distinct_quote_count[name] = distinct_quote_count.get(name, 0) + 1

def write_data(out_file, attribution_count, distinct_quote_count):
    with open(out_file, "w") as count_file:
        # For each person who has an attributed quote, write a line to the out file with a comma separated list of the
        # person's name, attribution count, and distinct quote count.
        for name in distinct_quote_count:
            count_file.write(f"{name},{attribution_count[name]},{distinct_quote_count[name]}\n")