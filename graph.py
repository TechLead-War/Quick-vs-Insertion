import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        labels = lines[0].strip().split('\t')
        print("here")
        print(labels)
        data = [[val for val in line.strip().split('\t')] for line in lines[1:]]
        return labels, data

def create_bar_chart(labels, data):
    array_size = [row[0] for row in data]
    bubble_time = [row[1] for row in data]
    insertion_time = [row[2] for row in data]
    quick_time = [row[3] for row in data]

    x = range(len(array_size))
	
	# bar_width = 0.2  # Adjust this value to increase or decrease the margin

    plt.figure(figsize=(10, 6))
    
    plt.bar(x, bubble_time, width=0.2, label='Bubble Sort')
    plt.bar([i + 0.2 for i in x], insertion_time, width=0.2, label='Insertion Sort')
    plt.bar([i + 0.4 for i in x], quick_time, width=0.2, label='Quick Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance')
    plt.xticks([i + 0.8 for i in x], array_size)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filename = 'sorting_runtimes.txt'
    labels, data = read_data(filename)
    create_bar_chart(labels, data)
