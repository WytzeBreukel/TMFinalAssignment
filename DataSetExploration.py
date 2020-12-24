import csv
file_paths = ["twitter-2016train-A.tsv","twitter-2016test-A.tsv","twitter-2016devtest-A.tsv","twitter-2016dev-A.tsv","twitter-2015train-A.tsv","twitter-2015test-A.tsv","twitter-2014test-A.tsv","twitter-2014sarcasm-A.tsv","twitter-2013train-A.tsv","twitter-2013test-A.tsv","twitter-2013dev-A.tsv"]


def print_result(file_path,count_lines, count_positive, count_neutral, count_negative, average_tweet_length):
    #print(f"For file {file_path} \n Total lines {count_lines} \n Count positive {count_positive} \n Count neutral {count_neutral} \n Count negative {count_negative} \n The average tweet length is {average_tweet_length}" )
    print(f"{file_path} & {count_lines} & {count_positive} & {count_neutral} & {count_negative} & {average_tweet_length:0.2f} \\\\")


def explore_data_set(file_path):
    count_lines = 0
    count_positive = 0
    count_negative = 0
    count_neutral = 0
    total_tweet_length = 0
    with open(file_path) as csv_file:
        rows = csv.reader(csv_file, delimiter='\t')
        for row in rows:
            count_lines += 1
            sentiment = row[1]
            if sentiment == 'positive':
                count_positive += 1
            elif sentiment == 'neutral':
                count_neutral += 1
            elif sentiment == 'negative':
                count_negative += 1

            total_tweet_length += len(row[2])

    average_tweet_length = total_tweet_length/count_lines
    return count_lines,count_positive, count_neutral, count_negative, average_tweet_length


def main():
    total_lines = 0
    total_positive = 0
    total_neutral = 0
    total_negative = 0
    sum_of_average_tweet_length = 0
    for file_path in file_paths:
        count_lines,count_positive, count_neutral, count_negative, average_tweet_length = explore_data_set(file_path)
        print_result(file_path, count_lines, count_positive, count_neutral, count_negative, average_tweet_length)
        total_lines += count_lines
        total_positive += count_positive
        total_neutral += count_neutral
        total_negative += count_negative
        sum_of_average_tweet_length += average_tweet_length
    total_average_tweet_length = sum_of_average_tweet_length/len(file_paths)
    print_result("combined", total_lines, total_positive, total_neutral, total_negative,total_average_tweet_length)


if __name__ == '__main__':
    main()

