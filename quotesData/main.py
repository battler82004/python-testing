from fileIO import read_data, write_data

APO_IN_FILE = "apo/apoQuotes.txt"
APO_OUT_FILE = "apo/apoQuoteCounts.txt"
PSU_IN_FILE = "psu/psuQuotes.txt"
PSU_OUT_FILE = "psu/psuQuoteCounts.txt"

def main():
    # Attributed count shows the total number of times that a person has a quote in the file.
    # The distinct quote count shows the number of distinct quote bullets that the person
    # appears in. For example, a line of:
    #   "Hello." -A "World!" -B "Hello." -A
    # gives A an attribution count of 2 but a distinct quote count of 1.

    apo_attribution_count = {}
    apo_distinct_quote_count = {}
    psu_attribution_count = {}
    psu_distinct_quote_count = {}

    # APO
    read_data(APO_IN_FILE, apo_attribution_count, apo_distinct_quote_count)
    write_data(APO_OUT_FILE, apo_attribution_count, apo_distinct_quote_count)

    # PSU
    read_data(PSU_IN_FILE, psu_attribution_count, psu_distinct_quote_count)
    write_data(PSU_OUT_FILE, psu_attribution_count, psu_distinct_quote_count)

if __name__ == "__main__":
    main()