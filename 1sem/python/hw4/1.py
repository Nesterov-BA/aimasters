import random


def BatchGenerator(list_of_sequences, batch_size, shuffle=False):
    if shuffle:
        for seq in list_of_sequences:
            random.shuffle(seq)
    for i in range(0, len(list_of_sequences[0]), batch_size):
        batch = []
        for seq in list_of_sequences:
            batch.append(seq[i:i + batch_size])
        yield batch


def batch(sequence, size):
    batch_list = []
    length = len(sequence)
    for i in range(0, length, size):
        batch_list.append(sequence[i:i + size])
    return batch_list


bg = BatchGenerator(
    list_of_sequences=[
        [1, 2, 3, 5, 1, 'a'],
        [0, 0, 1, 1, 0, 1]
    ], batch_size=2, shuffle=False
)

for elem in bg:
    print(elem)
